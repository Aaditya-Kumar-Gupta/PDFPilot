from __future__ import annotations

from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):
    def __init__(self, text: str, parent=None) -> None:
        super().__init__(text, parent)
        self.setProperty("variant", "primary")
        self.setMinimumHeight(42)


class SecondaryButton(QPushButton):
    def __init__(self, text: str, parent=None) -> None:
        super().__init__(text, parent)
        self.setProperty("variant", "secondary")
        self.setMinimumHeight(42)


class DangerButton(QPushButton):
    def __init__(self, text: str, parent=None) -> None:
        super().__init__(text, parent)
        self.setProperty("variant", "danger")
        self.setMinimumHeight(42)
