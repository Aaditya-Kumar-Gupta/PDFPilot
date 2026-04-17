from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPalette
from PySide6.QtWidgets import QApplication

LIGHT_TOKENS = {
    "background": "#f3f6fb",
    "panel": "#ffffff",
    "card": "#f8faff",
    "accent": "#2f6df6",
    "success": "#0f9d58",
    "warning": "#dd8a00",
    "danger": "#d93025",
    "text": "#142033",
    "muted": "#5d6c86",
}

DARK_TOKENS = {
    "background": "#101722",
    "panel": "#162130",
    "card": "#1b293b",
    "accent": "#74a2ff",
    "success": "#37c871",
    "warning": "#f4b042",
    "danger": "#ff7b72",
    "text": "#e9f0ff",
    "muted": "#a7b5cc",
}


def _best_font_family() -> str:
    families = {family.lower(): family for family in QFontDatabase.families()}
    for candidate in ("Roboto", "Segoe UI Variable", "Segoe UI", "Inter"):
        if candidate.lower() in families:
            return families[candidate.lower()]
    return "Sans Serif"


def _theme_path() -> Path:
    return Path(__file__).resolve().parent / "styles" / "dark_theme.qss"


def _effective_mode(app: QApplication, theme: str) -> str:
    selected = (theme or "auto").strip().lower()
    if selected in {"light", "dark"}:
        return selected
    color_scheme = app.styleHints().colorScheme()
    return "dark" if color_scheme == Qt.ColorScheme.Dark else "light"


def _build_palette(tokens: dict[str, str], dark: bool) -> QPalette:
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(tokens["background"]))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(tokens["text"]))
    palette.setColor(QPalette.ColorRole.Base, QColor(tokens["panel"]))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(tokens["card"]))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(tokens["panel"]))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(tokens["text"]))
    palette.setColor(QPalette.ColorRole.Text, QColor(tokens["text"]))
    palette.setColor(QPalette.ColorRole.Button, QColor(tokens["panel"]))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(tokens["text"]))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(tokens["danger"]))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(tokens["accent"]))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#FFFFFF" if not dark else "#09111f"))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(tokens["muted"]))
    return palette


def _stylesheet_for(mode: str) -> str:
    stylesheet = _theme_path().read_text(encoding="utf-8")
    if mode != "dark":
        return stylesheet
    replacements = {
        "#142033": DARK_TOKENS["text"],
        "#2f6df6": DARK_TOKENS["accent"],
        "#f3f6fb": DARK_TOKENS["background"],
        "#ffffff": DARK_TOKENS["panel"],
        "#f8faff": DARK_TOKENS["card"],
        "#eef3fd": "#152233",
        "#d7deea": "#2b3b52",
        "#eaf1ff": "#21324b",
        "#f7faff": "#182436",
        "#cbd7f2": "#3a516d",
        "#edf4ff": "#20304a",
        "#ccd6e5": "#32465f",
        "#f4f8ff": "#20314b",
        "#e8eef8": "#24354d",
        "#255fe0": "#5d8ef5",
        "#fff2f1": "#3a2224",
        "#8f261e": "#ffb4ad",
        "#f0c7c2": "#694145",
        "#e7eefb": "#223147",
        "#dbe6ff": "#243654",
        "#11357f": "#d5e3ff",
        "#d0d8e6": "#32465f",
        "#cfd9ea": "#41597a",
        "#e2e8f3": "#2b3b52",
        "#31538f": "#8eb5ff",
        "#5f6b7b": DARK_TOKENS["muted"],
        "#eef3ff": "#22324b",
        "#d6e2ff": "#35517a",
        "#e9f7ef": "#1a3025",
        "#bfe4cf": "#2f6d49",
        "#0f6b3c": "#7fe0a9",
        "#ecf1f8": "#182436",
    }
    for old, new in replacements.items():
        stylesheet = stylesheet.replace(old, new)
    return stylesheet


def apply_app_theme(app: QApplication, theme: str = "auto") -> str:
    mode = _effective_mode(app, theme)
    tokens = DARK_TOKENS if mode == "dark" else LIGHT_TOKENS
    app.setPalette(_build_palette(tokens, dark=mode == "dark"))
    app.setFont(QFont(_best_font_family(), 10))
    app.setStyleSheet(_stylesheet_for(mode))
    app.setProperty("themeMode", mode)
    return mode
