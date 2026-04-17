from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFileDialog,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QComboBox,
    QVBoxLayout,
    QWidget,
)

from pdf_toolkit.models import OptionField, ToolDefinition
from pdf_toolkit.ui.page_organizer import PageOrganizerDialog
from pdf_toolkit.ui.widgets import DropFileList, FilePickerRow
from pdf_toolkit.utils.file_utils import unique_output_path


OUTPUT_SUFFIXES = {
    "compare_pdf": ".txt",
    "pdf_to_word": ".docx",
    "pdf_to_powerpoint": ".pptx",
    "pdf_to_excel": ".xlsx",
}


class WorkflowPanel(QFrame):
    run_requested = Signal(object, list, object, dict)
    preview_requested = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background: #131c26; border: 1px solid #263345; border-radius: 18px;")
        self.current_tool: ToolDefinition | None = None
        self._field_widgets: dict[str, QWidget] = {}

        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)

        self.heading = QLabel("Select a tool")
        self.heading.setStyleSheet("font-size: 13pt; font-weight: 700;")
        root.addWidget(self.heading)

        self.description = QLabel("Choose a card from the dashboard to configure and run a PDF workflow.")
        self.description.setWordWrap(True)
        root.addWidget(self.description)

        self.input_list = DropFileList()
        self.input_list.files_dropped.connect(self.add_files)
        self.input_list.selection_changed.connect(self.preview_requested.emit)
        root.addWidget(self.input_list, 1)

        file_buttons = QHBoxLayout()
        add_button = QPushButton("Add Files")
        add_button.clicked.connect(self.browse_files)
        clear_button = QPushButton("Clear")
        clear_button.setProperty("secondary", True)
        clear_button.clicked.connect(self.input_list.clear)
        self.organize_button = QPushButton("Open Page Organizer")
        self.organize_button.setProperty("secondary", True)
        self.organize_button.clicked.connect(self.open_organizer)
        self.organize_button.hide()
        file_buttons.addWidget(add_button)
        file_buttons.addWidget(clear_button)
        file_buttons.addWidget(self.organize_button)
        root.addLayout(file_buttons)

        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_host = QWidget()
        form_host.setLayout(self.form_layout)
        root.addWidget(form_host)

        self.output_picker = FilePickerRow("Choose output file or folder", save_file=True)
        root.addWidget(self.output_picker)

        actions = QHBoxLayout()
        actions.addStretch(1)
        self.run_button = QPushButton("Run Tool")
        self.run_button.clicked.connect(self._emit_run)
        actions.addWidget(self.run_button)
        root.addLayout(actions)

    def set_tool(self, definition: ToolDefinition) -> None:
        self.current_tool = definition
        self.heading.setText(definition.title)
        staged_text = " This workflow is staged for a future milestone." if definition.staged else ""
        self.description.setText(definition.description + staged_text)
        self.organize_button.setVisible(definition.tool_id == "organize_pdf")
        self.output_picker.directory = definition.accepts_output_dir
        self.output_picker.save_file = not definition.accepts_output_dir
        self._rebuild_fields(definition.option_fields)
        self.apply_suggested_output()

    def _rebuild_fields(self, fields: list[OptionField]) -> None:
        while self.form_layout.rowCount():
            self.form_layout.removeRow(0)
        self._field_widgets.clear()
        for field in fields:
            widget: QWidget
            if field.field_type == "choice":
                combo = QComboBox()
                combo.addItems(field.choices)
                combo.setCurrentText(str(field.default))
                widget = combo
            elif field.field_type in {"text", "password", "hidden"}:
                line_edit = QLineEdit(str(field.default))
                line_edit.setPlaceholderText(field.placeholder)
                if field.field_type == "password":
                    line_edit.setEchoMode(QLineEdit.EchoMode.Password)
                widget = line_edit
            elif field.field_type == "file":
                widget = FilePickerRow(field.label)
            else:
                line_edit = QLineEdit(str(field.default))
                widget = line_edit
            if field.field_type != "hidden":
                self.form_layout.addRow(field.label, widget)
            self._field_widgets[field.key] = widget

    def browse_files(self) -> None:
        files, _ = QFileDialog.getOpenFileNames(self, "Choose input files")
        if files:
            self.add_files([Path(path) for path in files])

    def add_files(self, paths: list[Path]) -> None:
        self.input_list.add_paths(paths)
        if paths:
            self.preview_requested.emit(paths[0])
            self.apply_suggested_output()

    def selected_paths(self) -> list[Path]:
        return self.input_list.paths()

    def option_values(self) -> dict:
        values: dict[str, object] = {}
        for key, widget in self._field_widgets.items():
            if isinstance(widget, QLineEdit):
                values[key] = widget.text().strip()
            elif isinstance(widget, QComboBox):
                values[key] = widget.currentText()
            elif isinstance(widget, FilePickerRow):
                values[key] = widget.value()
        return values

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
        if self.current_tool.accepts_output_dir:
            output = first.parent
        else:
            suffix = OUTPUT_SUFFIXES.get(self.current_tool.tool_id, ".pdf")
            output = unique_output_path(first.with_name(f"{first.stem}_{self.current_tool.tool_id}{suffix}"))
        self.output_picker.line_edit.setText(str(output))

    def open_organizer(self) -> None:
        inputs = self.selected_paths()
        if not inputs:
            QMessageBox.warning(self, "PDFPilot", "Choose a PDF first.")
            return
        dialog = PageOrganizerDialog(inputs[0], self)
        if dialog.exec():
            page_order, rotate_map = dialog.results()
            order_widget = self._field_widgets.get("page_order")
            rotate_widget = self._field_widgets.get("rotate_pages")
            if isinstance(order_widget, QLineEdit):
                order_widget.setText(page_order)
            if isinstance(rotate_widget, QLineEdit):
                rotate_widget.setText(str(rotate_map))

    def _emit_run(self) -> None:
        if self.current_tool is None:
            QMessageBox.warning(self, "PDFPilot", "Choose a tool from the dashboard first.")
            return
        output_value = self.output_picker.value()
        if not output_value:
            QMessageBox.warning(self, "PDFPilot", "Choose an output file or folder.")
            return
        self.run_requested.emit(self.current_tool, self.selected_paths(), Path(output_value), self.option_values())
