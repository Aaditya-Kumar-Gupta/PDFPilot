from __future__ import annotations

from io import BytesIO

import fitz
import pytesseract
from PIL import Image

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.tools.base import ensure_not_cancelled, require_dependency
from pdf_toolkit.utils.dependencies import resolve_tesseract_path, tesseract_status
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    dependency = tesseract_status()
    require_dependency(dependency.available, dependency.details or dependency.summary)
    tesseract_path = resolve_tesseract_path()
    if tesseract_path is not None:
        pytesseract.pytesseract.tesseract_cmd = str(tesseract_path)
    ensure_pdf_files(context.input_files)

    source = fitz.open(context.input_files[0])
    target = fitz.open()
    try:
        total = len(source)
        for index, page in enumerate(source, start=1):
            ensure_not_cancelled(context)
            pixmap = page.get_pixmap(dpi=200, alpha=False)
            with Image.open(BytesIO(pixmap.tobytes("png"))) as image:
                pdf_bytes = pytesseract.image_to_pdf_or_hocr(image, extension="pdf")
            ocr_document = fitz.open("pdf", pdf_bytes)
            try:
                target.insert_pdf(ocr_document)
            finally:
                ocr_document.close()
            context.progress(int(index / total * 100), f"OCR processed page {index} of {total}")
        target.save(context.output_path)
    finally:
        source.close()
        target.close()
    return ToolResult(True, "OCR completed successfully.", [context.output_path])
