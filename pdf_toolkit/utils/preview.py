from __future__ import annotations

from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap


def create_thumbnail(path: Path, page_number: int = 0, width: int = 180) -> QPixmap | None:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        document = fitz.open(path)
        try:
            page = document.load_page(page_number)
            zoom = width / page.rect.width
            pixmap = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
            image = Image.open(BytesIO(pixmap.tobytes("png")))
            return QPixmap.fromImage(ImageQt.ImageQt(image))
        except Exception:
            return None
        finally:
            document.close()
    if suffix in {".jpg", ".jpeg", ".png", ".bmp"}:
        image = Image.open(path)
        image.thumbnail((width, width))
        return QPixmap.fromImage(ImageQt.ImageQt(image))
    return None
