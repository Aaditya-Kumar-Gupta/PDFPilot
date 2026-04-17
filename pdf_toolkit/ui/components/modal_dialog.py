from __future__ import annotations

from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout


class ModalDialog(QDialog):
    def __init__(self, title: str, body: str, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)
        layout = QVBoxLayout(self)
        label = QLabel(body)
        label.setWordWrap(True)
        layout.addWidget(label)
