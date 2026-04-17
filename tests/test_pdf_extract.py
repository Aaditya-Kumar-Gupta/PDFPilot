from __future__ import annotations

import unittest
from pathlib import Path

from pdf_toolkit.utils.pdf_extract import extract_pages, is_sparse_page


FIXTURES = Path(__file__).resolve().parents[1] / "runtime_tests"


class PdfExtractTests(unittest.TestCase):
    def test_extract_pages_returns_text_in_reading_order(self) -> None:
        pages = extract_pages(FIXTURES / "sample1.pdf")
        self.assertGreaterEqual(len(pages), 1)
        self.assertTrue(pages[0].text_lines)
        self.assertIsInstance(pages[0].text_lines[0], str)

    def test_sparse_detection_flags_image_heavy_pages(self) -> None:
        pages = extract_pages(FIXTURES / "images.pdf")
        self.assertTrue(any(is_sparse_page(page) for page in pages))

    def test_table_extraction_falls_back_to_empty_when_missing(self) -> None:
        pages = extract_pages(FIXTURES / "sample1.pdf")
        self.assertEqual(pages[0].tables, [])


if __name__ == "__main__":
    unittest.main()
