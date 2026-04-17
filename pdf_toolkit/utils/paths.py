from __future__ import annotations

import os
import sys
from pathlib import Path

from PySide6.QtCore import QStandardPaths


APP_NAME = "PDFPilot"
ORG_NAME = "PDFPilot"
DATA_DIR_ENV = "PDFPILOT_DATA_DIR"


def runtime_root() -> Path:
    if getattr(sys, "frozen", False):
        executable = Path(sys.executable).resolve()
        return executable.parent
    return project_root()


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def writable_data_root() -> Path:
    override = os.environ.get(DATA_DIR_ENV, "").strip()
    if override:
        path = Path(override).expanduser().resolve()
    else:
        qstandard_location = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation)
        if qstandard_location:
            path = Path(qstandard_location)
        else:
            local_app_data = os.environ.get("LOCALAPPDATA", "").strip()
            if local_app_data:
                path = Path(local_app_data) / ORG_NAME / APP_NAME
            else:
                path = Path.home() / "AppData" / "Local" / ORG_NAME / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def settings_file_path() -> Path:
    return writable_data_root() / "settings.ini"


def assets_dir() -> Path:
    root = runtime_root()
    candidates = [
        root / "assets",
        root / "_internal" / "assets",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return project_root() / "assets"


def bundled_renderer_override() -> Path | None:
    raw = os.environ.get("PDFPILOT_RENDERER_DIR", "").strip()
    return Path(raw).expanduser().resolve() if raw else None


def bundled_renderer_dir() -> Path:
    override = bundled_renderer_override()
    if override is not None:
        return override
    return runtime_root() / "vendor" / "libreoffice"


def logs_dir() -> Path:
    path = writable_data_root() / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def log_file_path() -> Path:
    return logs_dir() / "pdfpilot.log"


def temp_dir() -> Path:
    path = writable_data_root() / "temp"
    path.mkdir(parents=True, exist_ok=True)
    return path
