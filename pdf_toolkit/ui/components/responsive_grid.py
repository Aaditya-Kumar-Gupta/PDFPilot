from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QSizePolicy, QWidget


class ResponsiveGrid(QWidget):
    def __init__(self, minimum_card_width: int = 280, parent=None) -> None:
        super().__init__(parent)
        self.minimum_card_width = minimum_card_width
        self._cards: list[QWidget] = []
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setHorizontalSpacing(12)
        self.layout.setVerticalSpacing(12)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def set_cards(self, cards: list[QWidget]) -> None:
        self._cards = cards
        self._reflow()

    def resizeEvent(self, event) -> None:  # noqa: N802
        self._reflow()
        super().resizeEvent(event)

    def _reflow(self) -> None:
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        if not self._cards:
            return
        width = self._available_width()
        columns = self._column_count(width)
        for index, card in enumerate(self._cards):
            self.layout.addWidget(card, index // columns, index % columns)
            card.show()
        for column in range(columns):
            self.layout.setColumnStretch(column, 1)
        for column in range(columns, 6):
            self.layout.setColumnStretch(column, 0)
        self.updateGeometry()

    def _available_width(self) -> int:
        parent = self.parentWidget()
        if parent is not None and parent.width() > self.minimum_card_width:
            return parent.width()
        return max(self.width(), self.minimum_card_width)

    def _column_count(self, width: int) -> int:
        return max(1, min(5, width // self.minimum_card_width))
