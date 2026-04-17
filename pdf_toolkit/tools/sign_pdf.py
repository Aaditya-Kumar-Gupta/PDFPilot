from __future__ import annotations

from pathlib import Path

import fitz

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_files_exist, ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    signature_path = context.options.get("signature_image", "")
    if not signature_path:
        raise ToolError("Choose a signature image to stamp into the PDF.")
    signature = Path(signature_path)
    ensure_files_exist([signature])

    document = fitz.open(context.input_files[0])
    try:
        page = document[-1]
        rect = fitz.Rect(page.rect.width - 180, page.rect.height - 100, page.rect.width - 30, page.rect.height - 30)
        page.insert_image(rect, filename=str(signature))
        document.save(context.output_path)
    finally:
        document.close()
    context.progress(100, "Signature image stamped")
    return ToolResult(True, "Signature image added to PDF.", [context.output_path])
