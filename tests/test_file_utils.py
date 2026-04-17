from __future__ import annotations

import unittest

from pdf_toolkit.models import ToolError
from pdf_toolkit.utils.file_utils import ensure_files_exist, ensure_pdf_files


class FileValidationTests(unittest.TestCase):
    def test_empty_input_list_reports_user_facing_error(self) -> None:
        with self.assertRaisesRegex(ToolError, "choose at least one input file"):
            ensure_files_exist([])

    def test_empty_pdf_input_list_reports_user_facing_error(self) -> None:
        with self.assertRaisesRegex(ToolError, "choose at least one input file"):
            ensure_pdf_files([])


if __name__ == "__main__":
    unittest.main()
