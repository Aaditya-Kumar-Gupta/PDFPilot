from __future__ import annotations

from pathlib import Path

import fitz
from PySide6.QtCore import Qt, QUrl, Signal
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSpinBox, QTextEdit, QVBoxLayout

from pdf_toolkit.ui.components.buttons import SecondaryButton
from pdf_toolkit.utils.preview import create_thumbnail


class PreviewPanel(QFrame):
    page_changed = Signal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("previewPanel")
        self._path: Path | None = None
        self._page_count = 1
        self._current_pixmap: QPixmap | None = None

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        header = QHBoxLayout()
        title = QLabel("Preview")
        title.setProperty("role", "sectionTitle")
        header.addWidget(title)
        header.addStretch(1)
        page_label = QLabel("Page")
        page_label.setProperty("role", "subtitle")
        header.addWidget(page_label)
        self.page_spin = QSpinBox()
        self.page_spin.setMinimum(1)
        self.page_spin.setMaximum(1)
        self.page_spin.valueChanged.connect(self._on_page_changed)
        header.addWidget(self.page_spin)
        layout.addLayout(header)

        self.thumbnail = QLabel("Select a file to preview.")
        self.thumbnail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumbnail.setMinimumHeight(320)
        self.thumbnail.setWordWrap(True)
        self.thumbnail.setObjectName("previewCanvas")
        layout.addWidget(self.thumbnail, 1)

        self.open_button = SecondaryButton("Open source folder")
        self.open_button.setEnabled(False)
        self.open_button.clicked.connect(self._open_source_folder)
        layout.addWidget(self.open_button, 0, Qt.AlignmentFlag.AlignLeft)

        self.meta = QTextEdit()
        self.meta.setReadOnly(True)
        self.meta.setMinimumHeight(110)
        layout.addWidget(self.meta)

    def set_file(self, path: Path | None) -> None:
        self._path = path
        self.open_button.setEnabled(path is not None)
        if path is None:
            self._current_pixmap = None
            self.thumbnail.setText("Select a file to preview.")
            self.thumbnail.setPixmap(QPixmap())
            self.meta.setText("")
            self.page_spin.setMaximum(1)
            self.page_spin.setValue(1)
            return
        self._page_count = self._resolve_page_count(path)
        self.page_spin.setMaximum(max(1, self._page_count))
        self.page_spin.setValue(1)
        self._render_preview(path, 0)

    def _resolve_page_count(self, path: Path) -> int:
        if path.suffix.lower() != ".pdf":
            return 1
        try:
            document = fitz.open(path)
            try:
                return max(1, len(document))
            finally:
                document.close()
        except Exception:
            return 1

    def _on_page_changed(self, page_number: int) -> None:
        if self._path is None:
            return
        self._render_preview(self._path, page_number - 1)
        self.page_changed.emit(page_number - 1)

    def _render_preview(self, path: Path, page_index: int) -> None:
        pixmap = create_thumbnail(path, page_index, width=320)
        if pixmap:
            self._current_pixmap = pixmap
            self.thumbnail.setText("")
            self._apply_thumbnail_pixmap()
        else:
            self._current_pixmap = None
            self.thumbnail.setPixmap(QPixmap())
            self.thumbnail.setText(path.name)
        details = [f"Name: {path.name}", f"Path: {path}", f"Pages: {self._page_count}"]
        if path.exists():
            details.append(f"Size: {path.stat().st_size / 1024:.1f} KB")
        self.meta.setText("\n".join(details))

    def _open_source_folder(self) -> None:
        if self._path is None:
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self._path.parent)))

    def resizeEvent(self, event) -> None:  # noqa: N802
        self._apply_thumbnail_pixmap()
        super().resizeEvent(event)

    def _apply_thumbnail_pixmap(self) -> None:
        if self._current_pixmap is None:
            return
        target_size = self.thumbnail.contentsRect().size()
        if target_size.width() <= 0 or target_size.height() <= 0:
            return
        scaled = self._current_pixmap.scaled(
            target_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.thumbnail.setPixmap(scaled)
