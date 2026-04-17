from __future__ import annotations

from pathlib import Path

import fitz
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout

from pdf_toolkit.utils.preview import create_thumbnail


class PageOrganizerDialog(QDialog):
    def __init__(self, pdf_path: Path, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Organize PDF Pages")
        self.resize(920, 560)
        self._pdf_path = pdf_path
        self._rotations: dict[str, int] = {}

        layout = QVBoxLayout(self)
        description = QLabel("Drag pages to reorder them. Use the rotate button for the selected page.")
        description.setWordWrap(True)
        layout.addWidget(description)

        self.list_widget = QListWidget()
        self.list_widget.setViewMode(QListWidget.ViewMode.IconMode)
        self.list_widget.setDragDropMode(QListWidget.DragDropMode.InternalMove)
        self.list_widget.setResizeMode(QListWidget.ResizeMode.Adjust)
        preview = create_thumbnail(pdf_path)
        if preview:
            self.list_widget.setIconSize(preview.size())
        self.list_widget.setSpacing(12)
        layout.addWidget(self.list_widget, 1)

        button_row = QHBoxLayout()
        rotate_button = QPushButton("Rotate Selected 90 deg")
        rotate_button.clicked.connect(self.rotate_selected)
        button_row.addWidget(rotate_button)
        button_row.addStretch(1)
        cancel_button = QPushButton("Cancel")
        cancel_button.setProperty("secondary", True)
        cancel_button.clicked.connect(self.reject)
        save_button = QPushButton("Use This Order")
        save_button.clicked.connect(self.accept)
        button_row.addWidget(cancel_button)
        button_row.addWidget(save_button)
        layout.addLayout(button_row)

        self._populate()

    def _populate(self) -> None:
        document = fitz.open(self._pdf_path)
        try:
            for index in range(len(document)):
                item = QListWidgetItem(f"Page {index + 1}")
                item.setData(Qt.ItemDataRole.UserRole, index + 1)
                thumb = create_thumbnail(self._pdf_path, index, width=140)
                if thumb:
                    item.setIcon(QIcon(thumb))
                self.list_widget.addItem(item)
        finally:
            document.close()

    def rotate_selected(self) -> None:
        item = self.list_widget.currentItem()
        if item is None:
            return
        page_number = str(item.data(Qt.ItemDataRole.UserRole))
        current = self._rotations.get(page_number, 0)
        self._rotations[page_number] = (current + 90) % 360
        item.setText(f"Page {page_number} ({self._rotations[page_number]} deg)")

    def results(self) -> tuple[str, dict[str, int]]:
        order = []
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            order.append(str(item.data(Qt.ItemDataRole.UserRole)))
        return ", ".join(order), self._rotations
