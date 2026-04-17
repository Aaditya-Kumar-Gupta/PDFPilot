from __future__ import annotations

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from pdf_toolkit.settings import get_settings_manager
from pdf_toolkit.ui.main_window import MainWindow
from pdf_toolkit.ui.theme import apply_app_theme
from pdf_toolkit.utils.logging_config import configure_logging
from pdf_toolkit.utils.paths import APP_NAME, ORG_NAME, assets_dir


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORG_NAME)
    configure_logging()
    app_icon = assets_dir() / "app.ico"
    if app_icon.exists():
        app.setWindowIcon(QIcon(str(app_icon)))
    settings_manager = get_settings_manager()
    apply_app_theme(app, settings_manager.load().theme)
    app.styleHints().colorSchemeChanged.connect(
        lambda _scheme: apply_app_theme(app, settings_manager.load().theme)
        if settings_manager.load().theme == "auto"
        else None
    )

    window = MainWindow(settings_manager)
    window.show()
    return app.exec()
