from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout

from pdf_toolkit.models import ToolDefinition
from pdf_toolkit.ui.components.icon_utils import load_icon


class ToolCard(QFrame):
    clicked = Signal(str)

    def __init__(self, definition: ToolDefinition, enabled: bool = True, parent=None) -> None:
        super().__init__(parent)
        self.definition = definition
        self._selected = False
        self._enabled = enabled
        self.setObjectName("toolCard")
        self.setCursor(Qt.CursorShape.PointingHandCursor if enabled else Qt.CursorShape.ForbiddenCursor)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setMinimumSize(280, 138)
        self.setMaximumHeight(138)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setEnabled(enabled)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 14)
        layout.setSpacing(6)

        top_row = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(load_icon(definition.icon_name).pixmap(24, 24))
        top_row.addWidget(icon_label)
        top_row.addStretch(1)
        layout.addLayout(top_row)

        title = QLabel(definition.title)
        title.setProperty("role", "cardTitle")
        layout.addWidget(title)

        description = QLabel(definition.description)
        description.setWordWrap(True)
        description.setProperty("role", "subtitle")
        layout.addWidget(description, 1)

    def set_selected(self, selected: bool) -> None:
        self._selected = selected and self._enabled
        self.setProperty("selected", selected)
        self.style().unpolish(self)
        self.style().polish(self)

    def mousePressEvent(self, event) -> None:  # noqa: N802
        if self._enabled:
            self.clicked.emit(self.definition.tool_id)
        super().mousePressEvent(event)

    def keyPressEvent(self, event) -> None:  # noqa: N802
        if self._enabled and event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Space):
            self.clicked.emit(self.definition.tool_id)
            event.accept()
            return
        super().keyPressEvent(event)
