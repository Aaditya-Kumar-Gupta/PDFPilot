from __future__ import annotations

import os
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

from pdf_toolkit.utils import paths


class WritablePathTests(unittest.TestCase):
    def _fresh_root(self, name: str) -> Path:
        root = Path(__file__).resolve().parents[1] / "runtime_tests" / "_test_outputs" / name
        shutil.rmtree(root, ignore_errors=True)
        root.mkdir(parents=True, exist_ok=True)
        return root

    def test_data_dir_override_controls_settings_logs_and_temp(self) -> None:
        root = self._fresh_root("paths_override")
        try:
            override = root / "portable-data"
            with patch.dict(os.environ, {paths.DATA_DIR_ENV: str(override)}, clear=False):
                settings_path = paths.settings_file_path()
                logs_path = paths.log_file_path()
                temp_path = paths.temp_dir()

            self.assertEqual(settings_path, override / "settings.ini")
            self.assertEqual(logs_path, override / "logs" / "pdfpilot.log")
            self.assertEqual(temp_path, override / "temp")
            self.assertTrue(temp_path.exists())
            self.assertTrue(logs_path.parent.exists())
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_local_appdata_is_used_when_no_override_is_present(self) -> None:
        root = self._fresh_root("paths_local_appdata")
        try:
            expected_root = root / paths.ORG_NAME / paths.APP_NAME
            with patch.dict(os.environ, {paths.DATA_DIR_ENV: "", "LOCALAPPDATA": str(root)}, clear=False):
                with patch("pdf_toolkit.utils.paths.QStandardPaths.writableLocation", return_value=""):
                    actual_root = paths.writable_data_root()

            self.assertEqual(actual_root, expected_root)
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
