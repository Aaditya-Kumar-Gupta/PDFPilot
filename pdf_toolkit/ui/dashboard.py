from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QScrollArea, QVBoxLayout, QWidget

from pdf_toolkit.models import ToolDefinition
from pdf_toolkit.ui.components.motion import animate_opacity
from pdf_toolkit.ui.components.responsive_grid import ResponsiveGrid
from pdf_toolkit.ui.components.search_bar import SearchBar
from pdf_toolkit.ui.components.tool_card import ToolCard


class DashboardPanel(QFrame):
    tool_selected = Signal(str)
    search_changed = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("dashboardPanel")
        self._definitions: list[ToolDefinition] = []
        self._cards: list[ToolCard] = []
        self._active_tool_id: str | None = None
        self._available_tool_count = 0

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        eyebrow = QLabel("Offline PDF workspace")
        eyebrow.setProperty("role", "eyebrow")
        root.addWidget(eyebrow)

        self.title = QLabel("Dashboard")
        self.title.setProperty("role", "title")
        root.addWidget(self.title)

        self.search_bar = SearchBar()
        self.search_bar.text_changed.connect(self.search_changed.emit)
        root.addWidget(self.search_bar)

        section_row = QHBoxLayout()
        section_title = QLabel("Tool library")
        section_title.setProperty("role", "sectionTitle")
        section_row.addWidget(section_title)
        section_row.addStretch(1)
        self.context_label = QLabel("All workflows")
        self.context_label.setProperty("role", "subtitle")
        section_row.addWidget(self.context_label)
        root.addLayout(section_row)

        self.grid = ResponsiveGrid()
        scroll_host = QWidget()
        scroll_layout = QVBoxLayout(scroll_host)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.addWidget(self.grid)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(scroll_host)
        root.addWidget(scroll, 1)
        self.grid_host = scroll_host

    def bind_definitions(self, definitions: list[ToolDefinition]) -> None:
        self._definitions = definitions
        self._available_tool_count = sum(
            1
            for item in definitions
            if not item.staged and (item.requires_dependency is None or item.requires_dependency().available)
        )

    def set_cards(self, definitions: list[ToolDefinition], context_label: str) -> None:
        self.title.setText(context_label)
        matches_label = "workflow" if len(definitions) == 1 else "workflows"
        available_label = "tool" if self._available_tool_count == 1 else "tools"
        if context_label == "Dashboard":
            summary = f"{len(definitions)} {matches_label} ready to run"
        else:
            summary = f"{len(definitions)} {matches_label} in this library section"
        if self._available_tool_count:
            summary = f"{summary} | {self._available_tool_count} offline-ready {available_label}"
        self.context_label.setText(summary)
        self._cards = []
        for definition in definitions:
            dependency_status = definition.requires_dependency() if definition.requires_dependency else None
            dependency_available = dependency_status is None or dependency_status.available
            card_enabled = not definition.staged
            card = ToolCard(definition, enabled=card_enabled)
            card.clicked.connect(self.tool_selected.emit)
            card.set_selected(definition.tool_id == self._active_tool_id)
            self._cards.append(card)
        self.grid.set_cards(self._cards)
        animate_opacity(self.grid_host, start=0.45, end=1.0, duration=180)

    def set_active_tool(self, tool_id: str | None) -> None:
        self._active_tool_id = tool_id
        for card in self._cards:
            card.set_selected(card.definition.tool_id == tool_id)
