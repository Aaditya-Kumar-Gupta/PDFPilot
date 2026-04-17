from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files
from pdf_toolkit.utils.pdf_helpers import parse_page_ranges


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    pages = set(parse_page_ranges(context.options.get("pages", ""), len(reader.pages)))
    angle = int(context.options.get("angle", 90))
    for index, page in enumerate(reader.pages):
        if index in pages:
            page = page.rotate(angle)
        writer.add_page(page)
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    context.progress(100, "Selected pages rotated")
    return ToolResult(True, "Rotation applied.", [context.output_path])
