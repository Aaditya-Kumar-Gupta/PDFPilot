from __future__ import annotations

import fitz
from pypdf import PdfReader

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    source = context.input_files[0]
    document = fitz.open(source)
    try:
        document.save(context.output_path, garbage=4, deflate=True, clean=True)
    finally:
        document.close()
    PdfReader(str(context.output_path))
    context.progress(100, "Repair attempt finished")
    return ToolResult(True, "Repair attempt completed.", [context.output_path])
