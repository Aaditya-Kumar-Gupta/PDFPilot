from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import QSize, Qt, Signal, QTimer
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QToolButton, QVBoxLayout

from pdf_toolkit.ui.components.buttons import SecondaryButton
from pdf_toolkit.ui.components.icon_utils import load_icon


@dataclass(slots=True)
class NavigationItem:
    item_id: str
    label: str
    icon_name: str


class SidebarNavigation(QFrame):
    section_changed = Signal(str)
    toggled = Signal(bool)

    def __init__(self, items: list[NavigationItem], parent=None, initial_collapsed: bool = False) -> None:
        super().__init__(parent)
        self.setObjectName("sidebar")
        self._expanded_width = 232
        self._collapsed_width = 96
        self._collapsed = initial_collapsed
        self._buttons: dict[str, QToolButton] = {}
        self._typewriter_text = "Created by Aditya Kumar Gupta"
        self._typewriter_index = 0

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(12)

        top = QHBoxLayout()
        self.brand = QLabel("PDFPilot")
        self.brand.setProperty("role", "sectionTitle")
        top.addWidget(self.brand)
        top.addStretch(1)
        self.toggle_button = SecondaryButton("Hide")
        self.toggle_button.setObjectName("sidebarToggle")
        self.toggle_button.clicked.connect(lambda: self.set_collapsed(not self._collapsed))
        top.addWidget(self.toggle_button)
        layout.addLayout(top)

        self.meta = QLabel("")
        self.meta.setProperty("role", "subtitle")
        self.meta.setWordWrap(True)
        layout.addWidget(self.meta)
        self._typewriter_timer = QTimer(self)
        self._typewriter_timer.setInterval(65)
        self._typewriter_timer.timeout.connect(self._advance_typewriter)
        self._typewriter_timer.start()

        for item in items:
            button = QToolButton()
            button.setObjectName("navButton")
            button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            button.setIcon(load_icon(item.icon_name))
            button.setIconSize(QSize(20, 20))
            button.setText(item.label)
            button.setToolTip(item.label)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            button.setMinimumHeight(42)
            button.clicked.connect(lambda checked=False, item_id=item.item_id: self.section_changed.emit(item_id))
            layout.addWidget(button)
            self._buttons[item.item_id] = button

        layout.addStretch(1)

        self.footer = QLabel("100% offline\nZero telemetry")
        self.footer.setProperty("role", "subtitle")
        layout.addWidget(self.footer)

        self._apply_collapsed_state(self._collapsed)

    def set_active(self, item_id: str) -> None:
        for current_id, button in self._buttons.items():
            button.setProperty("active", current_id == item_id)
            button.style().unpolish(button)
            button.style().polish(button)

    def set_collapsed(self, collapsed: bool) -> None:
        if self._collapsed == collapsed:
            return
        self._collapsed = collapsed
        self._apply_collapsed_state(collapsed)
        self.toggled.emit(collapsed)

    def _apply_collapsed_state(self, collapsed: bool) -> None:
        width = self._collapsed_width if collapsed else self._expanded_width
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        style = Qt.ToolButtonStyle.ToolButtonIconOnly if collapsed else Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        for button in self._buttons.values():
            button.setToolButtonStyle(style)
        self.brand.setVisible(not collapsed)
        self.meta.setVisible(not collapsed)
        self.footer.setVisible(not collapsed)
        self.toggle_button.setText("Show" if collapsed else "Hide")

    def is_collapsed(self) -> bool:
        return self._collapsed

    def _advance_typewriter(self) -> None:
        if self._collapsed:
            return
        if self._typewriter_index >= len(self._typewriter_text):
            self._typewriter_timer.stop()
            return
        self._typewriter_index += 1
        self.meta.setText(self._typewriter_text[: self._typewriter_index])
