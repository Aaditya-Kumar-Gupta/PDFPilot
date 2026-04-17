from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QFrame


class SearchBar(QFrame):
    text_changed = Signal(str)

    def __init__(self, placeholder: str = "Search tools, actions, or workflows", parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("searchSurface")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 8, 14, 8)
        layout.setSpacing(10)

        icon = QLabel("Find")
        icon.setProperty("role", "eyebrow")
        layout.addWidget(icon)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)
        self.line_edit.setClearButtonEnabled(True)
        self.line_edit.setObjectName("searchLineEdit")
        self.line_edit.textChanged.connect(self.text_changed.emit)
        layout.addWidget(self.line_edit, 1)

    def setText(self, value: str) -> None:  # noqa: N802
        self.line_edit.setText(value)

    def text(self) -> str:
        return self.line_edit.text()

    def setFocus(self) -> None:  # noqa: N802
        self.line_edit.setFocus()
