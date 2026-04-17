from __future__ import annotations

from PySide6.QtCore import QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, Qt
from PySide6.QtWidgets import QFrame, QLabel, QSizePolicy, QToolButton, QVBoxLayout, QWidget

from pdf_toolkit.ui.components.motion import animate_in


class CollapsibleSection(QFrame):
    def __init__(self, title: str, description: str = "", expanded: bool = True, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("collapsibleSection")
        self._expanded = expanded

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 16, 18, 16)
        root.setSpacing(12)

        self.toggle_button = QToolButton()
        self.toggle_button.setObjectName("sectionToggle")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.ArrowType.DownArrow if expanded else Qt.ArrowType.RightArrow)
        self.toggle_button.setText(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(expanded)
        self.toggle_button.clicked.connect(self.toggle)
        root.addWidget(self.toggle_button)

        self.description_label = QLabel(description)
        self.description_label.setObjectName("sectionDescription")
        self.description_label.setProperty("role", "subtitle")
        self.description_label.setWordWrap(True)
        self.description_label.setVisible(bool(description))
        root.addWidget(self.description_label)

        self.content = QWidget()
        self.content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(12)
        root.addWidget(self.content)

        self.content.setMaximumHeight(16777215 if expanded else 0)
        self.content.setVisible(expanded)

    def set_description(self, description: str) -> None:
        self.description_label.setText(description)
        self.description_label.setVisible(bool(description))

    def add_widget(self, widget: QWidget, stretch: int = 0) -> None:
        self.content_layout.addWidget(widget, stretch)

    def add_layout(self, layout) -> None:
        self.content_layout.addLayout(layout)

    def set_expanded(self, expanded: bool, *, animate: bool = True) -> None:
        if self._expanded == expanded and animate:
            return
        self._expanded = expanded
        self.toggle_button.setChecked(expanded)
        self.toggle_button.setArrowType(Qt.ArrowType.DownArrow if expanded else Qt.ArrowType.RightArrow)
        self.content.setVisible(True)
        hint_height = self.content.layout().sizeHint().height()
        target_height = max(hint_height, 220)

        height_anim = QPropertyAnimation(self.content, b"maximumHeight", self)
        height_anim.setDuration(220)
        height_anim.setStartValue(self.content.maximumHeight())
        height_anim.setEndValue(target_height if expanded else 0)
        height_anim.setEasingCurve(QEasingCurve.Type.OutCubic if expanded else QEasingCurve.Type.InOutCubic)

        group = QParallelAnimationGroup(self)
        group.addAnimation(height_anim)
        if animate and expanded:
            animate_in(self.content, duration=220, offset=10)
        if expanded:
            group.finished.connect(lambda: self.content.setMaximumHeight(16777215))
        if not expanded:
            group.finished.connect(lambda: self.content.setVisible(False))
        self._section_group = group  # type: ignore[attr-defined]
        if animate:
            group.start()
        else:
            self.content.setMaximumHeight(16777215 if expanded else 0)
            self.content.setVisible(expanded)

    def toggle(self) -> None:
        self.set_expanded(not self._expanded)
