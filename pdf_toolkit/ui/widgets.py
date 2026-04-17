from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from pdf_toolkit.models import ToolDefinition
from pdf_toolkit.utils.paths import assets_dir
from pdf_toolkit.utils.preview import create_thumbnail


def load_icon(icon_name: str) -> QIcon:
    icon_path = assets_dir() / "icons" / f"{icon_name}.svg"
    return QIcon(str(icon_path))


class ToolCard(QFrame):
    clicked = Signal(str)

    def __init__(self, definition: ToolDefinition, status_text: str) -> None:
        super().__init__()
        self.definition = definition
        self.setObjectName("toolCard")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(
            """
            QFrame#toolCard {
                background: #16202b;
                border: 1px solid #263345;
                border-radius: 18px;
            }
            QFrame#toolCard:hover {
                border-color: #0ea5e9;
                background: #1a2634;
            }
            """
        )
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(8)

        icon_label = QLabel()
        icon_label.setPixmap(load_icon(definition.icon_name).pixmap(40, 40))
        layout.addWidget(icon_label)

        title = QLabel(definition.title)
        title.setStyleSheet("font-size: 13pt; font-weight: 700;")
        layout.addWidget(title)

        description = QLabel(definition.description)
        description.setWordWrap(True)
        description.setStyleSheet("color: #cbd5e1;")
        layout.addWidget(description, 1)

        badge = QLabel(status_text)
        badge.setStyleSheet(
            "background: #0f1722; border: 1px solid #334155; border-radius: 10px; padding: 6px 10px; color: #93c5fd;"
        )
        layout.addWidget(badge)

    def mousePressEvent(self, event) -> None:  # noqa: N802
        self.clicked.emit(self.definition.tool_id)
        super().mousePressEvent(event)


class PreviewPanel(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("background: #131c26; border: 1px solid #263345; border-radius: 18px;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        heading = QLabel("File Preview")
        heading.setStyleSheet("font-size: 12pt; font-weight: 700;")
        layout.addWidget(heading)

        self.thumbnail = QLabel("Drop a file or choose a tool to preview.")
        self.thumbnail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumbnail.setMinimumHeight(220)
        self.thumbnail.setStyleSheet("background: #0f1722; border-radius: 14px; border: 1px dashed #334155;")
        layout.addWidget(self.thumbnail)

        self.meta = QTextEdit()
        self.meta.setReadOnly(True)
        layout.addWidget(self.meta, 1)

    def set_file(self, path: Path | None) -> None:
        if path is None:
            self.thumbnail.setText("No file selected.")
            self.thumbnail.setPixmap(QPixmap())
            self.meta.setText("")
            return
        pixmap = create_thumbnail(path)
        if pixmap:
            self.thumbnail.setText("")
            self.thumbnail.setPixmap(pixmap)
            self.thumbnail.setScaledContents(False)
        else:
            self.thumbnail.setPixmap(QPixmap())
            self.thumbnail.setText(path.name)
        details = [
            f"Name: {path.name}",
            f"Path: {path}",
            f"Size: {path.stat().st_size / 1024:.1f} KB" if path.exists() else "Size: unavailable",
        ]
        self.meta.setText("\n".join(details))


class JobPanel(QFrame):
    cancel_requested = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background: #131c26; border: 1px solid #263345; border-radius: 18px;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        heading = QLabel("Jobs")
        heading.setStyleSheet("font-size: 12pt; font-weight: 700;")
        layout.addWidget(heading)

        self.status = QLabel("Idle")
        layout.addWidget(self.status)

        from PySide6.QtWidgets import QProgressBar  # local import keeps this module tidy

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        layout.addWidget(self.progress)

        button_row = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel Active Job")
        self.cancel_button.setProperty("warning", True)
        self.cancel_button.clicked.connect(self.cancel_requested.emit)
        button_row.addWidget(self.cancel_button)
        layout.addLayout(button_row)

        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        layout.addWidget(self.log_view, 1)

    def append_log(self, message: str) -> None:
        self.log_view.append(message)


class DropFileList(QListWidget):
    files_dropped = Signal(list)
    selection_changed = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.setAcceptDrops(True)
        self.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.itemSelectionChanged.connect(self._emit_selected_path)

    def dragEnterEvent(self, event) -> None:  # noqa: N802
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event) -> None:  # noqa: N802
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event) -> None:  # noqa: N802
        paths = [Path(url.toLocalFile()) for url in event.mimeData().urls() if url.isLocalFile()]
        if paths:
            self.files_dropped.emit(paths)
            event.acceptProposedAction()

    def add_paths(self, paths: list[Path]) -> None:
        existing = {self.item(index).data(Qt.ItemDataRole.UserRole) for index in range(self.count())}
        for path in paths:
            resolved = str(path)
            if resolved in existing:
                continue
            item = QListWidgetItem(path.name)
            item.setData(Qt.ItemDataRole.UserRole, resolved)
            self.addItem(item)

    def paths(self) -> list[Path]:
        return [Path(self.item(index).data(Qt.ItemDataRole.UserRole)) for index in range(self.count())]

    def _emit_selected_path(self) -> None:
        selected = self.selectedItems()
        self.selection_changed.emit(Path(selected[0].data(Qt.ItemDataRole.UserRole)) if selected else None)


class FilePickerRow(QWidget):
    changed = Signal(str)

    def __init__(self, label_text: str, directory: bool = False, save_file: bool = False) -> None:
        super().__init__()
        self.directory = directory
        self.save_file = save_file
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(label_text)
        self.line_edit.textChanged.connect(self.changed.emit)
        button = QPushButton("Browse")
        button.setProperty("secondary", True)
        button.clicked.connect(self._browse)
        layout.addWidget(self.line_edit, 1)
        layout.addWidget(button)

    def _browse(self) -> None:
        if self.directory:
            value = QFileDialog.getExistingDirectory(self, "Choose folder")
        elif self.save_file:
            value, _ = QFileDialog.getSaveFileName(self, "Choose output file")
        else:
            value, _ = QFileDialog.getOpenFileName(self, "Choose file")
        if value:
            self.line_edit.setText(value)

    def value(self) -> str:
        return self.line_edit.text().strip()


class CardGrid(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QGridLayout(self)
        self.layout.setSpacing(14)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def set_cards(self, cards: list[QWidget]) -> None:
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
        columns = 3
        for index, card in enumerate(cards):
            row = index // columns
            column = index % columns
            self.layout.addWidget(card, row, column)
