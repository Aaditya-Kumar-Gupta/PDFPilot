from __future__ import annotations

import ast
from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QMessageBox, QVBoxLayout

from pdf_toolkit.models import ToolContext, ToolDefinition, ToolResult
from pdf_toolkit.settings import SettingsManager
from pdf_toolkit.ui.components.notification import NotificationToast
from pdf_toolkit.ui.components.run_status_dialog import RunStatusDialog
from pdf_toolkit.ui.tool_workspace import ToolWorkspace
from pdf_toolkit.utils.file_utils import unique_output_path
from pdf_toolkit.utils.workers import JobRunner


class ToolPage(QFrame):
    back_requested = Signal()

    def __init__(self, settings_manager: SettingsManager, parent=None) -> None:
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.active_tool: ToolDefinition | None = None

        self.runner = JobRunner()
        self.runner.job_started.connect(self.on_job_started)
        self.runner.job_progress.connect(self.on_job_progress)
        self.runner.job_finished.connect(self.on_job_finished)
        self.runner.job_failed.connect(self.on_job_failed)

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(12)

        self.workspace = ToolWorkspace(settings_manager)
        self.workspace.set_embedded_mode(True)
        self.workspace.run_requested.connect(self.start_tool)
        self.workspace.preview_requested.connect(self.update_preview)
        self.workspace.close_requested.connect(self.back_requested.emit)
        root.addWidget(self.workspace, 1)

        self.toast_host = QVBoxLayout()
        self.toast_host.setSpacing(10)
        self.toast_host.addStretch(1)
        root.addLayout(self.toast_host)

        self.run_status_dialog = RunStatusDialog(self)
        self.run_status_dialog.job_status.cancel_requested.connect(self.runner.cancel_active)

    def set_tool(self, definition: ToolDefinition) -> None:
        self.active_tool = definition
        self.workspace.set_tool(definition)
        self.workspace.refresh_settings()

    def update_preview(self, path: Path | None) -> None:
        self.workspace.preview_panel.set_file(path)

    def start_tool(self, definition: ToolDefinition, input_files: list[Path], output_path: Path, options: dict) -> None:
        if not input_files:
            QMessageBox.warning(self, "PDFPilot", "Please choose one or more input files.")
            return
        if definition.requires_dependency:
            dependency = definition.requires_dependency()
            if not dependency.available and not definition.staged:
                QMessageBox.information(
                    self,
                    definition.title,
                    f"{dependency.summary}\n\n{dependency.details}\n\n"
                    "After setting the path, run the OCR tool again.",
                )
                return
        if "rotate_pages" in options and isinstance(options["rotate_pages"], str) and options["rotate_pages"]:
            try:
                options["rotate_pages"] = ast.literal_eval(options["rotate_pages"])
            except Exception:
                options["rotate_pages"] = {}
        if len(input_files) > 1 and not definition.allows_multiple_inputs and definition.tool_id != "compare_pdf":
            definition = self._build_batch_definition(definition, output_path, options)
            if definition.accepts_output_dir:
                output_path.mkdir(parents=True, exist_ok=True)
        self.run_status_dialog.job_status.reset()
        self.run_status_dialog.job_status.append_log(f"Running: {definition.title}")
        self.run_status_dialog.show_centered()
        self.runner.run_tool(definition, input_files, output_path, options)

    def _build_batch_definition(self, definition: ToolDefinition, output_path: Path, options: dict) -> ToolDefinition:
        output_dir = output_path if definition.accepts_output_dir else output_path.parent

        def batch_executor(context: ToolContext) -> ToolResult:
            created: list[Path] = []
            total = len(context.input_files)
            for index, input_file in enumerate(context.input_files, start=1):
                single_output = output_dir if definition.accepts_output_dir else unique_output_path(
                    output_dir / f"{input_file.stem}_{definition.tool_id}.pdf"
                )
                single_context = ToolContext(
                    input_files=[input_file],
                    output_path=single_output,
                    options=options,
                    progress=lambda _, message, current=index: context.progress(
                        int(current / total * 100), f"[{current}/{total}] {message}"
                    ),
                    is_cancelled=context.is_cancelled,
                )
                result = definition.executor(single_context)
                created.extend(result.output_files)
            return ToolResult(True, f"Batch completed for {total} file(s).", created, {"batch": True})

        return ToolDefinition(
            tool_id=f"{definition.tool_id}_batch",
            category=definition.category,
            title=f"{definition.title} (Batch)",
            description=definition.description,
            icon_name=definition.icon_name,
            executor=batch_executor,
            option_fields=definition.option_fields,
            allows_multiple_inputs=True,
            accepts_output_dir=definition.accepts_output_dir,
            staged=definition.staged,
            supports_preview=definition.supports_preview,
            requires_dependency=definition.requires_dependency,
            keywords=definition.keywords,
            workflow_steps=definition.workflow_steps,
            badge="Batch",
            workspace_mode=definition.workspace_mode,
        )

    def on_job_started(self, name: str) -> None:
        self.run_status_dialog.job_status.status.setText(f"Running {name}")
        self.run_status_dialog.job_status.progress.setValue(0)
        self._show_toast(f"{name} started")

    def on_job_progress(self, value: int, message: str) -> None:
        self.run_status_dialog.job_status.progress.setValue(value)
        self.run_status_dialog.job_status.status.setText(message)
        self.run_status_dialog.job_status.append_log(message)

    def on_job_finished(self, result: ToolResult) -> None:
        self.run_status_dialog.job_status.progress.setValue(100)
        self.run_status_dialog.job_status.status.setText(result.message)
        self.run_status_dialog.job_status.append_log(result.message)
        first_output = result.output_files[0] if result.output_files else None
        self.run_status_dialog.job_status.set_last_output(first_output)
        if first_output:
            self.settings_manager.add_recent_file(first_output)
            self.workspace.preview_panel.set_file(first_output)
        self.workspace.set_last_output(first_output)
        self._show_toast(result.message)
        self.run_status_dialog.close()
        if not result.success and result.metadata.get("staged"):
            QMessageBox.information(self, "Staged Feature", result.message)

    def on_job_failed(self, message: str) -> None:
        self.run_status_dialog.job_status.status.setText("Failed")
        self.run_status_dialog.job_status.append_log(message)
        self.run_status_dialog.close()
        self._show_toast("The active job failed.")
        QMessageBox.critical(self, "PDFPilot", message)

    def _show_toast(self, message: str) -> None:
        toast = NotificationToast(message, self)
        self.toast_host.insertWidget(0, toast)

    def refresh_settings(self) -> None:
        self.workspace.refresh_settings()
