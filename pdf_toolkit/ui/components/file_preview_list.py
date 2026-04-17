from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem

from pdf_toolkit.utils.preview import create_thumbnail


class FilePreviewList(QListWidget):
    files_changed = Signal()
    selection_changed = Signal(object)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("filePreviewList")
        self.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.setDragDropMode(QListWidget.DragDropMode.InternalMove)
        self.itemSelectionChanged.connect(self._emit_selected_path)
        self.model().rowsMoved.connect(lambda *_: self.files_changed.emit())

    def add_paths(self, paths: list[Path]) -> None:
        existing = {self.item(index).data(Qt.ItemDataRole.UserRole) for index in range(self.count())}
        for path in paths:
            resolved = str(path)
            if resolved in existing:
                continue
            item = QListWidgetItem(path.name)
            item.setData(Qt.ItemDataRole.UserRole, resolved)
            thumb = create_thumbnail(path, width=72)
            if thumb:
                item.setIcon(QIcon(thumb))
            item.setToolTip(str(path))
            self.addItem(item)
        self.files_changed.emit()

    def remove_selected(self) -> None:
        for item in self.selectedItems():
            row = self.row(item)
            self.takeItem(row)
        self.files_changed.emit()
        self._emit_selected_path()

    def clear_files(self) -> None:
        self.clear()
        self.files_changed.emit()
        self.selection_changed.emit(None)

    def paths(self) -> list[Path]:
        return [Path(self.item(index).data(Qt.ItemDataRole.UserRole)) for index in range(self.count())]

    def _emit_selected_path(self) -> None:
        selected = self.selectedItems()
        self.selection_changed.emit(Path(selected[0].data(Qt.ItemDataRole.UserRole)) if selected else None)
