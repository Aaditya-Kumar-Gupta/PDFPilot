from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class NotificationToast(QFrame):
    def __init__(self, message: str, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("toast")
        self.setMaximumWidth(360)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        title = QLabel("Update")
        title.setProperty("role", "eyebrow")
        layout.addWidget(title)
        label = QLabel(message)
        label.setWordWrap(True)
        layout.addWidget(label)
        QTimer.singleShot(2800, self.deleteLater)
