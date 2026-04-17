from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFileDialog, QHBoxLayout, QLineEdit, QWidget

from pdf_toolkit.ui.components.buttons import SecondaryButton


class FilePickerRow(QWidget):
    changed = Signal(str)

    def __init__(self, placeholder: str, directory: bool = False, save_file: bool = False, parent=None) -> None:
        super().__init__(parent)
        self.directory = directory
        self.save_file = save_file
        self.browse_title = "Choose folder" if directory else "Choose file"
        self.browse_start_dir = ""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)
        self.line_edit.setObjectName("filePickerLineEdit")
        self.line_edit.textChanged.connect(self.changed.emit)
        layout.addWidget(self.line_edit, 1)

        browse_button = SecondaryButton("Browse")
        browse_button.clicked.connect(self._browse)
        layout.addWidget(browse_button)

    def _browse(self) -> None:
        if self.directory:
            value = QFileDialog.getExistingDirectory(self, self.browse_title, self.browse_start_dir)
        elif self.save_file:
            value, _ = QFileDialog.getSaveFileName(self, self.browse_title, self.browse_start_dir)
        else:
            value, _ = QFileDialog.getOpenFileName(self, self.browse_title, self.browse_start_dir)
        if value:
            self.line_edit.setText(value)

    def value(self) -> str:
        return self.line_edit.text().strip()
