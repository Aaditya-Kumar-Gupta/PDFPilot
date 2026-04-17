from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout

from pdf_toolkit.ui.components.job_status import JobStatusPanel


class RunStatusDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Run status")
        self.setModal(False)
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.resize(460, 220)
        self.setMinimumSize(420, 200)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        self.job_status = JobStatusPanel(self)
        layout.addWidget(self.job_status)

    def show_centered(self) -> None:
        self.adjustSize()
        self.show()
        parent = self.parentWidget()
        if parent is not None:
            geometry = self.frameGeometry()
            geometry.moveCenter(parent.frameGeometry().center())
            self.move(geometry.topLeft())
