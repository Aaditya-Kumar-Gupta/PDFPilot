from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QProgressBar, QVBoxLayout

from pdf_toolkit.ui.components.buttons import DangerButton


class JobStatusPanel(QFrame):
    cancel_requested = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("jobStatusPanel")
        self._last_output: Path | None = None

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        title = QLabel("Run status")
        title.setProperty("role", "sectionTitle")
        layout.addWidget(title)

        self.status = QLabel("Ready")
        self.status.setProperty("role", "subtitle")
        layout.addWidget(self.status)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        layout.addWidget(self.progress)

        actions = QHBoxLayout()
        cancel_button = DangerButton("Cancel run")
        cancel_button.clicked.connect(self.cancel_requested.emit)
        actions.addWidget(cancel_button)
        actions.addStretch(1)
        layout.addLayout(actions)

    def append_log(self, message: str) -> None:
        return

    def set_last_output(self, path: Path | None) -> None:
        self._last_output = path

    def reset(self) -> None:
        self._last_output = None
        self.status.setText("Ready")
        self.progress.setValue(0)
