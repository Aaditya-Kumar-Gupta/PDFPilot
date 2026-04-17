from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QFormLayout, QFrame, QLineEdit, QVBoxLayout, QWidget

from pdf_toolkit.models import OptionField
from pdf_toolkit.ui.components.file_picker_row import FilePickerRow


class SettingsPanel(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("settingsPanel")
        self._field_widgets: dict[str, QWidget] = {}

        root = QVBoxLayout(self)
        root.setContentsMargins(4, 4, 4, 4)
        root.setSpacing(12)

        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self.form_layout.setFormAlignment(Qt.AlignmentFlag.AlignTop)
        self.form_layout.setHorizontalSpacing(16)
        self.form_layout.setVerticalSpacing(14)
        host = QWidget()
        host.setLayout(self.form_layout)
        root.addWidget(host)

    def set_fields(self, fields: list[OptionField]) -> None:
        while self.form_layout.rowCount():
            self.form_layout.removeRow(0)
        self._field_widgets.clear()
        for field in fields:
            widget: QWidget
            if field.field_type == "choice":
                combo = QComboBox()
                combo.addItems(field.choices)
                if field.default:
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
                widget = QLineEdit(str(field.default))
            if field.field_type != "hidden":
                label_text = f"{field.label}{' *' if field.required else ''}"
                self.form_layout.addRow(label_text, widget)
            self._field_widgets[field.key] = widget

    def values(self) -> dict:
        values: dict[str, object] = {}
        for key, widget in self._field_widgets.items():
            if isinstance(widget, QLineEdit):
                values[key] = widget.text().strip()
            elif isinstance(widget, QComboBox):
                values[key] = widget.currentText()
            elif isinstance(widget, FilePickerRow):
                values[key] = widget.value()
        return values

    def widget_for(self, key: str) -> QWidget | None:
        return self._field_widgets.get(key)

    def has_visible_fields(self) -> bool:
        return self.form_layout.rowCount() > 0
