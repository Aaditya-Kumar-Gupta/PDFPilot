from __future__ import annotations

from PySide6.QtGui import QIcon

from pdf_toolkit.utils.paths import assets_dir


def load_icon(icon_name: str) -> QIcon:
    return QIcon(str(assets_dir() / "icons" / f"{icon_name}.svg"))
