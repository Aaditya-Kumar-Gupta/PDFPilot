from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files
from pdf_toolkit.utils.pdf_helpers import parse_page_ranges, save_writer


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    source = context.input_files[0]
    reader = PdfReader(str(source))
    to_remove = set(parse_page_ranges(context.options.get("pages", ""), len(reader.pages)))
    writer = PdfWriter()
    for index, page in enumerate(reader.pages):
        if index not in to_remove:
            writer.add_page(page)
    save_writer(writer, context.output_path)
    context.progress(100, "Selected pages removed")
    return ToolResult(True, "Pages removed successfully.", [context.output_path])
