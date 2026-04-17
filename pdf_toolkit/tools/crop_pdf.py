from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    margin = float(context.options.get("margin", 18))
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        left = float(page.mediabox.left) + margin
        bottom = float(page.mediabox.bottom) + margin
        right = float(page.mediabox.right) - margin
        top = float(page.mediabox.top) - margin
        page.cropbox.lower_left = (left, bottom)
        page.cropbox.upper_right = (right, top)
        writer.add_page(page)
        context.progress(int(index / total * 100), f"Cropped page {index}")
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    return ToolResult(True, "Margins cropped.", [context.output_path])
