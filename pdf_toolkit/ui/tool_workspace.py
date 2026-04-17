from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog, QFrame, QHBoxLayout, QLabel, QMessageBox, QScrollArea, QSplitter, QVBoxLayout, QWidget

from pdf_toolkit.models import ToolDefinition
from pdf_toolkit.settings import SettingsManager
from pdf_toolkit.ui.components.buttons import PrimaryButton, SecondaryButton
from pdf_toolkit.ui.components.collapsible_section import CollapsibleSection
from pdf_toolkit.ui.components.file_drop_zone import FileDropZone
from pdf_toolkit.ui.components.file_picker_row import FilePickerRow
from pdf_toolkit.ui.components.file_preview_list import FilePreviewList
from pdf_toolkit.ui.components.preview_panel import PreviewPanel
from pdf_toolkit.ui.components.settings_panel import SettingsPanel
from pdf_toolkit.ui.page_organizer import PageOrganizerDialog
from pdf_toolkit.utils.file_utils import unique_output_path


OUTPUT_SUFFIXES = {
    "compare_pdf": ".txt",
    "pdf_to_word": ".docx",
    "pdf_to_powerpoint": ".pptx",
    "pdf_to_excel": ".xlsx",
}

INPUT_FILTERS = {
    "office_to_pdf": ("Office files (*.doc *.docx *.ppt *.pptx *.xls *.xlsx *.xlsm *.xltx *.xltm *.csv *.tsv *.ods *.fods)", {".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".xlsm", ".xltx", ".xltm", ".csv", ".tsv", ".ods", ".fods"}),
    "scan_to_pdf": ("Image files (*.jpg *.jpeg *.png *.bmp)", {".jpg", ".jpeg", ".png", ".bmp"}),
    "image_to_pdf": ("Image files (*.jpg *.jpeg *.png *.bmp)", {".jpg", ".jpeg", ".png", ".bmp"}),
}


class ToolWorkspace(QFrame):
    run_requested = Signal(object, list, object, dict)
    preview_requested = Signal(object)
    close_requested = Signal()

    def __init__(self, settings_manager: SettingsManager, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("workspacePanel")
        self.settings_manager = settings_manager
        self.current_tool: ToolDefinition | None = None
        self._embedded_mode = True

        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(18)

        header_row = QHBoxLayout()
        self.back_button = SecondaryButton("Back to library")
        self.back_button.clicked.connect(self.close_requested.emit)
        header_row.addWidget(self.back_button, 0, Qt.AlignmentFlag.AlignLeft)
        header_row.addStretch(1)
        root.addLayout(header_row)

        eyebrow = QLabel("Selected workflow")
        eyebrow.setProperty("role", "eyebrow")
        root.addWidget(eyebrow)

        self.heading = QLabel("Choose a tool")
        self.heading.setProperty("role", "title")
        root.addWidget(self.heading)

        self.description = QLabel("Select a tool from the dashboard to start an offline workflow.")
        self.description.setProperty("role", "subtitle")
        self.description.setWordWrap(True)
        root.addWidget(self.description)

        content_splitter = QSplitter(Qt.Orientation.Horizontal)
        content_splitter.setChildrenCollapsible(False)
        root.addWidget(content_splitter, 1)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(14)

        self.drop_zone = FileDropZone()
        self.drop_zone.clicked.connect(self.browse_files)
        self.drop_zone.files_dropped.connect(self.add_files)
        self.files_section = CollapsibleSection("Files", "Add and reorder the documents you want to process.")
        self.files_section.add_widget(self.drop_zone)

        list_header = QHBoxLayout()
        files_label = QLabel("Queue")
        files_label.setProperty("role", "sectionTitle")
        list_header.addWidget(files_label)
        list_header.addStretch(1)
        self.organize_button = SecondaryButton("Page organizer")
        self.organize_button.clicked.connect(self.open_organizer)
        self.organize_button.hide()
        list_header.addWidget(self.organize_button)
        self.files_section.add_layout(list_header)

        self.file_list = FilePreviewList()
        self.file_list.selection_changed.connect(self._handle_selection_change)
        self.files_section.add_widget(self.file_list, 1)

        file_actions = QHBoxLayout()
        add_button = SecondaryButton("Add files")
        add_button.clicked.connect(self.browse_files)
        file_actions.addWidget(add_button)
        remove_button = SecondaryButton("Remove selected")
        remove_button.clicked.connect(self.file_list.remove_selected)
        file_actions.addWidget(remove_button)
        clear_button = SecondaryButton("Clear")
        clear_button.clicked.connect(self.file_list.clear_files)
        file_actions.addWidget(clear_button)
        file_actions.addStretch(1)
        self.files_section.add_layout(file_actions)
        left_layout.addWidget(self.files_section, 1)

        self.settings_panel = SettingsPanel()
        self.settings_section = CollapsibleSection("Settings", "Adjust only the options required for this tool.")
        self.settings_section.add_widget(self.settings_panel)
        left_layout.addWidget(self.settings_section)

        output_host = QFrame()
        output_host.setObjectName("surface")
        output_layout = QVBoxLayout(output_host)
        output_layout.setContentsMargins(16, 16, 16, 16)
        output_layout.setSpacing(12)
        output_title = QLabel("Output")
        output_title.setProperty("role", "sectionTitle")
        output_layout.addWidget(output_title)
        self.output_picker = FilePickerRow("Choose output file or folder", save_file=True)
        self.output_picker.browse_title = "Choose output file or folder"
        output_layout.addWidget(self.output_picker)
        self.output_section = CollapsibleSection("Output", "Confirm where the processed files should be saved.")
        self.output_section.add_widget(output_host)
        left_layout.addWidget(self.output_section)

        action_row = QHBoxLayout()
        self.open_output_button = SecondaryButton("Open output file")
        self.open_output_button.setEnabled(False)
        self.open_output_button.clicked.connect(self.open_output_file)
        action_row.addWidget(self.open_output_button)
        action_row.addStretch(1)
        self.run_button = PrimaryButton("Run tool")
        self.run_button.clicked.connect(self._emit_run)
        action_row.addWidget(self.run_button)
        self.output_section.add_layout(action_row)

        left_scroll = QScrollArea()
        left_scroll.setWidgetResizable(True)
        left_scroll.setFrameShape(QFrame.Shape.NoFrame)
        left_scroll.setMinimumWidth(520)
        left_scroll.setWidget(left_panel)
        content_splitter.addWidget(left_scroll)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(14)
        self.preview_panel = PreviewPanel()
        self.preview_section = CollapsibleSection("Preview", "Check the selected file or the latest output without leaving the app.")
        self.preview_section.add_widget(self.preview_panel, 1)
        right_layout.addWidget(self.preview_section, 1)
        self.right_scroll = QScrollArea()
        self.right_scroll.setWidgetResizable(True)
        self.right_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.right_scroll.setMinimumWidth(420)
        self.right_scroll.setWidget(right_panel)
        content_splitter.addWidget(self.right_scroll)
        content_splitter.setSizes([640, 560])

        self.set_embedded_mode(True)

    def set_embedded_mode(self, embedded: bool) -> None:
        self._embedded_mode = embedded
        self.back_button.setVisible(embedded)

    def set_tool(self, definition: ToolDefinition) -> None:
        self.current_tool = definition
        self.heading.setText(definition.title)
        staged_text = " This workflow is staged for a future milestone." if definition.staged else ""
        dependency_text = ""
        if definition.requires_dependency:
            dependency = definition.requires_dependency()
            if not dependency.available:
                dependency_text = f" Setup required: {dependency.summary}. {dependency.details}".strip()
        self.description.setText(definition.description + staged_text + dependency_text)
        self.organize_button.setVisible(definition.tool_id == "organize_pdf")
        self.output_picker.directory = definition.accepts_output_dir
        self.output_picker.save_file = not definition.accepts_output_dir
        self.output_picker.browse_start_dir = self._last_output_dir()
        self.settings_panel.set_fields(definition.option_fields)
        has_settings = self.settings_panel.has_visible_fields()
        self.settings_section.setVisible(has_settings)
        self.settings_section.set_description("Adjust only the options required for this tool." if has_settings else "")
        self.run_button.setText(f"Run {definition.title}")
        self.set_last_output(None)
        self.output_picker.line_edit.clear()
        self.apply_suggested_output()

    def browse_files(self) -> None:
        start_dir = self._last_input_dir()
        if self.current_tool is None:
            files, _ = QFileDialog.getOpenFileNames(self, "Choose input files", start_dir)
        else:
            file_filter = self._file_dialog_filter(self.current_tool)
            files, _ = QFileDialog.getOpenFileNames(self, "Choose input files", start_dir, file_filter)
        if files:
            self._remember_input_dir(Path(files[0]).parent)
            self.add_files([Path(path) for path in files])

    def add_files(self, paths: list[Path]) -> None:
        if self.current_tool is not None:
            allowed_suffixes = self._allowed_suffixes(self.current_tool)
            invalid = [path.name for path in paths if path.suffix.lower() not in allowed_suffixes]
            if invalid:
                expected = self._expected_label(self.current_tool)
                QMessageBox.warning(
                    self,
                    "PDFPilot",
                    f"{self.current_tool.title} only accepts {expected}.\n\nInvalid files: {', '.join(invalid)}",
                )
                paths = [path for path in paths if path.suffix.lower() in allowed_suffixes]
            if not paths:
                return
        self.file_list.add_paths(paths)
        if paths:
            self._remember_input_dir(paths[0].parent)
            for path in paths:
                self.settings_manager.add_recent_file(path)
            self.preview_panel.set_file(paths[0])
            self.preview_requested.emit(paths[0])
            self.apply_suggested_output()

    def selected_paths(self) -> list[Path]:
        return self.file_list.paths()

    def option_values(self) -> dict:
        return self.settings_panel.values()

    def apply_suggested_output(self, force: bool = False) -> None:
        if self.current_tool is None:
            return
        existing_output = self.output_picker.value()
        if existing_output and not force:
            return
        inputs = self.selected_paths()
        if not inputs:
            if force:
                QMessageBox.information(self, "PDFPilot", "Add at least one input file to generate a suggested output path.")
            return
        first = inputs[0]
        settings = self.settings_manager.load()
        base_dir = Path(settings.default_output_dir) if settings.default_output_dir else first.parent
        if self.current_tool.accepts_output_dir:
            output = base_dir
        else:
            suffix = OUTPUT_SUFFIXES.get(self.current_tool.tool_id, ".pdf")
            output = unique_output_path(base_dir / f"{first.stem}_{self.current_tool.tool_id}{suffix}")
        self.output_picker.line_edit.setText(str(output))
        self.output_section.set_expanded(True)

    def open_organizer(self) -> None:
        inputs = self.selected_paths()
        if not inputs:
            QMessageBox.warning(self, "PDFPilot", "Choose a PDF first.")
            return
        dialog = PageOrganizerDialog(inputs[0], self)
        if dialog.exec():
            page_order, rotate_map = dialog.results()
            order_widget = self.settings_panel.widget_for("page_order")
            rotate_widget = self.settings_panel.widget_for("rotate_pages")
            if hasattr(order_widget, "setText"):
                order_widget.setText(page_order)
            if hasattr(rotate_widget, "setText"):
                rotate_widget.setText(str(rotate_map))

    def _handle_selection_change(self, path: Path | None) -> None:
        self.preview_panel.set_file(path)
        self.preview_requested.emit(path)

    def _emit_run(self) -> None:
        if self.current_tool is None:
            QMessageBox.warning(self, "PDFPilot", "Choose a tool first.")
            return
        output_value = self.output_picker.value()
        if not output_value:
            QMessageBox.warning(self, "PDFPilot", "Choose an output file or folder.")
            return
        output_path = Path(output_value)
        self._remember_output_dir(output_path if self.current_tool.accepts_output_dir else output_path.parent)
        self.run_requested.emit(self.current_tool, self.selected_paths(), output_path, self.option_values())

    def _allowed_suffixes(self, definition: ToolDefinition) -> set[str]:
        if definition.tool_id in INPUT_FILTERS:
            return INPUT_FILTERS[definition.tool_id][1]
        if definition.tool_id == "compare_pdf":
            return {".pdf"}
        return {".pdf"}

    def _file_dialog_filter(self, definition: ToolDefinition) -> str:
        if definition.tool_id in INPUT_FILTERS:
            return INPUT_FILTERS[definition.tool_id][0]
        return "PDF files (*.pdf)"

    def _expected_label(self, definition: ToolDefinition) -> str:
        if definition.tool_id in {"office_to_pdf"}:
            return "Word, PowerPoint, or spreadsheet files"
        if definition.tool_id in {"scan_to_pdf", "image_to_pdf"}:
            return "image files"
        return "PDF files"

    def refresh_settings(self) -> None:
        self.output_picker.browse_start_dir = self._last_output_dir()
        if not self.output_picker.value():
            self.apply_suggested_output()

    def set_last_output(self, path: Path | None) -> None:
        self._last_output = path
        self.open_output_button.setEnabled(path is not None)

    def open_output_file(self) -> None:
        if self._last_output is None:
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self._last_output)))

    def _last_input_dir(self) -> str:
        settings = self.settings_manager.load()
        if settings.remember_last_used_paths and settings.last_input_dir:
            return settings.last_input_dir
        return ""

    def _last_output_dir(self) -> str:
        settings = self.settings_manager.load()
        if settings.remember_last_used_paths and settings.last_output_dir:
            return settings.last_output_dir
        if settings.default_output_dir:
            return settings.default_output_dir
        inputs = self.selected_paths()
        return str(inputs[0].parent) if inputs else ""

    def _remember_input_dir(self, directory: Path) -> None:
        settings = self.settings_manager.load()
        if settings.remember_last_used_paths:
            self.settings_manager.update(last_input_dir=str(directory))

    def _remember_output_dir(self, directory: Path) -> None:
        settings = self.settings_manager.load()
        if settings.remember_last_used_paths:
            self.settings_manager.update(last_output_dir=str(directory))
