from __future__ import annotations

import itertools
import os
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

from pdf_toolkit.utils.renderer import resolve_office_renderer

TEST_OUTPUTS = Path(__file__).resolve().parents[1] / "runtime_tests" / "_test_outputs"


def _fresh_output_dir() -> Path:
    TEST_OUTPUTS.mkdir(parents=True, exist_ok=True)
    for index in itertools.count(1):
        candidate = TEST_OUTPUTS / f"renderer_run_{index}"
        if not candidate.exists():
            candidate.mkdir()
            return candidate
    raise RuntimeError("Unable to allocate renderer test output directory.")


class RendererResolutionTests(unittest.TestCase):
    def test_prefers_bundled_renderer(self) -> None:
        root = _fresh_output_dir()
        try:
            soffice = root / "program" / "soffice.exe"
            soffice.parent.mkdir(parents=True, exist_ok=True)
            soffice.write_text("stub", encoding="utf-8")
            with patch.dict(os.environ, {"PDFPILOT_RENDERER_DIR": str(root), "PDFPILOT_RELEASE_FLAVOR": "desktop"}, clear=False):
                with patch.object(shutil, "which", return_value=None):
                    resolution = resolve_office_renderer()
            self.assertTrue(resolution.available)
            self.assertEqual(resolution.mode, "bundled-libreoffice")
            self.assertEqual(resolution.soffice_path, soffice)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_falls_back_to_system_renderer(self) -> None:
        fake_missing = str((Path.cwd() / "runtime_tests" / "_missing_renderer").resolve())
        with patch.dict(os.environ, {"PDFPILOT_RENDERER_DIR": fake_missing}, clear=False):
            with patch.object(shutil, "which", return_value=r"C:\LibreOffice\program\soffice.exe"):
                resolution = resolve_office_renderer()
        self.assertTrue(resolution.available)
        self.assertEqual(resolution.mode, "system-libreoffice")

    def test_reports_builtin_fallback_when_no_renderer_exists(self) -> None:
        fake_missing = str((Path.cwd() / "runtime_tests" / "_missing_renderer").resolve())
        with patch.dict(os.environ, {"PDFPILOT_RENDERER_DIR": fake_missing}, clear=False):
            with patch.object(shutil, "which", return_value=None):
                resolution = resolve_office_renderer()
        self.assertFalse(resolution.available)
        self.assertEqual(resolution.mode, "builtin-fallback")

    def test_store_release_skips_bundled_renderer(self) -> None:
        root = _fresh_output_dir()
        try:
            soffice = root / "program" / "soffice.exe"
            soffice.parent.mkdir(parents=True, exist_ok=True)
            soffice.write_text("stub", encoding="utf-8")
            with patch.dict(os.environ, {"PDFPILOT_RELEASE_FLAVOR": "store"}, clear=False):
                with patch("pdf_toolkit.utils.renderer.bundled_renderer_dir", return_value=root):
                    with patch.object(shutil, "which", return_value=None):
                        resolution = resolve_office_renderer()
            self.assertFalse(resolution.available)
            self.assertEqual(resolution.mode, "builtin-fallback")
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
