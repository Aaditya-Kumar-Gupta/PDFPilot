from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from PySide6.QtCore import QSettings

from pdf_toolkit.utils.paths import settings_file_path


MAX_RECENT_FILES = 10


@dataclass(slots=True)
class AppSettings:
    theme: str = "auto"
    default_output_dir: str = ""
    remember_last_used_paths: bool = True
    libreoffice_override: str = ""
    tesseract_override: str = ""
    remember_recent_files: bool = True
    recent_files: list[str] = field(default_factory=list)
    last_input_dir: str = ""
    last_output_dir: str = ""


class SettingsManager:
    def __init__(self) -> None:
        self._qsettings = QSettings(str(settings_file_path()), QSettings.Format.IniFormat)

    def load(self) -> AppSettings:
        return AppSettings(
            theme=self._read_str("appearance.theme", "auto"),
            default_output_dir=self._read_str("defaults.output_dir", ""),
            remember_last_used_paths=self._read_bool("defaults.remember_last_used_paths", True),
            libreoffice_override=self._read_str("dependencies.libreoffice_override", ""),
            tesseract_override=self._read_str("dependencies.tesseract_override", ""),
            remember_recent_files=self._read_bool("privacy.remember_recent_files", True),
            recent_files=self._read_list("privacy.recent_files"),
            last_input_dir=self._read_str("history.last_input_dir", ""),
            last_output_dir=self._read_str("history.last_output_dir", ""),
        )

    def save(self, settings: AppSettings) -> None:
        self._qsettings.setValue("appearance.theme", settings.theme)
        self._qsettings.setValue("defaults.output_dir", settings.default_output_dir)
        self._qsettings.setValue("defaults.remember_last_used_paths", settings.remember_last_used_paths)
        self._qsettings.setValue("dependencies.libreoffice_override", settings.libreoffice_override)
        self._qsettings.setValue("dependencies.tesseract_override", settings.tesseract_override)
        self._qsettings.setValue("privacy.remember_recent_files", settings.remember_recent_files)
        self._qsettings.setValue("privacy.recent_files", settings.recent_files[:MAX_RECENT_FILES])
        self._qsettings.setValue("history.last_input_dir", settings.last_input_dir)
        self._qsettings.setValue("history.last_output_dir", settings.last_output_dir)
        self._qsettings.sync()

    def update(self, **changes) -> AppSettings:
        settings = self.load()
        for key, value in changes.items():
            setattr(settings, key, value)
        self.save(settings)
        return settings

    def add_recent_file(self, path: str | Path) -> AppSettings:
        settings = self.load()
        if not settings.remember_recent_files:
            return settings
        value = str(Path(path))
        recent = [item for item in settings.recent_files if item != value]
        recent.insert(0, value)
        settings.recent_files = recent[:MAX_RECENT_FILES]
        self.save(settings)
        return settings

    def clear_recent_files(self) -> AppSettings:
        settings = self.load()
        settings.recent_files = []
        self.save(settings)
        return settings

    def clear_last_used_paths(self) -> AppSettings:
        settings = self.load()
        settings.last_input_dir = ""
        settings.last_output_dir = ""
        self.save(settings)
        return settings

    def _read_str(self, key: str, default: str) -> str:
        value = self._qsettings.value(key, default)
        return str(value or default)

    def _read_bool(self, key: str, default: bool) -> bool:
        value = self._qsettings.value(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return bool(value)

    def _read_list(self, key: str) -> list[str]:
        value = self._qsettings.value(key, [])
        if isinstance(value, str):
            return [value] if value else []
        if isinstance(value, (list, tuple)):
            return [str(item) for item in value if str(item).strip()]
        return []


_SETTINGS_MANAGER: SettingsManager | None = None


def get_settings_manager() -> SettingsManager:
    global _SETTINGS_MANAGER
    if _SETTINGS_MANAGER is None:
        _SETTINGS_MANAGER = SettingsManager()
    return _SETTINGS_MANAGER
