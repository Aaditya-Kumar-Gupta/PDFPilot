from __future__ import annotations

import os
import itertools
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

from pdf_toolkit.utils import dependencies


TEST_OUTPUTS = Path(__file__).resolve().parents[1] / "runtime_tests" / "_test_outputs"


def _fresh_output_dir() -> Path:
    TEST_OUTPUTS.mkdir(parents=True, exist_ok=True)
    for index in itertools.count(1):
        candidate = TEST_OUTPUTS / f"deps_run_{index}"
        if not candidate.exists():
            candidate.mkdir()
            return candidate
    raise RuntimeError("Unable to allocate dependency test output directory.")


class _FakeSettings:
    def __init__(self, tesseract_override: str = "") -> None:
        self.tesseract_override = tesseract_override


class _FakeSettingsManager:
    def __init__(self, tesseract_override: str = "") -> None:
        self._settings = _FakeSettings(tesseract_override)

    def load(self) -> _FakeSettings:
        return self._settings


class TesseractDependencyTests(unittest.TestCase):
    def test_accepts_directory_override(self) -> None:
        temp_dir = _fresh_output_dir()
        try:
            install_dir = temp_dir
            executable = install_dir / "tesseract.exe"
            executable.write_text("stub", encoding="utf-8")
            manager = _FakeSettingsManager(str(install_dir))

            with patch("pdf_toolkit.utils.dependencies.get_settings_manager", return_value=manager):
                resolved = dependencies.resolve_tesseract_path()
                status = dependencies.tesseract_status()
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

        self.assertEqual(resolved, executable)
        self.assertTrue(status.available)
        self.assertEqual(status.details, str(executable))

    def test_auto_detects_common_windows_install_path(self) -> None:
        temp_dir = _fresh_output_dir()
        try:
            local_app_data = temp_dir
            executable = local_app_data / "Programs" / "Tesseract-OCR" / "tesseract.exe"
            executable.parent.mkdir(parents=True, exist_ok=True)
            executable.write_text("stub", encoding="utf-8")
            manager = _FakeSettingsManager("")

            with patch("pdf_toolkit.utils.dependencies.get_settings_manager", return_value=manager):
                with patch.object(shutil, "which", return_value=None):
                    with patch.dict(os.environ, {"LOCALAPPDATA": str(local_app_data)}, clear=False):
                        resolved = dependencies.resolve_tesseract_path()
                        status = dependencies.tesseract_status()
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

        self.assertEqual(resolved, executable)
        self.assertTrue(status.available)
        self.assertEqual(status.summary, "Tesseract OCR auto-detected")
        self.assertEqual(status.details, str(executable))

    def test_store_release_reports_not_bundled_message(self) -> None:
        manager = _FakeSettingsManager("")
        with patch("pdf_toolkit.utils.dependencies.get_settings_manager", return_value=manager):
            with patch.object(shutil, "which", return_value=None):
                with patch("pdf_toolkit.utils.dependencies._common_tesseract_locations", return_value=[]):
                    with patch.dict(os.environ, {"PDFPILOT_RELEASE_FLAVOR": "store"}, clear=False):
                        status = dependencies.tesseract_status()

        self.assertFalse(status.available)
        self.assertEqual(status.summary, "Tesseract OCR not bundled in Store build")


if __name__ == "__main__":
    unittest.main()
