from __future__ import annotations

from pypdf import PdfReader

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files
from pdf_toolkit.utils.pdf_helpers import build_pdf_writer, parse_page_ranges, save_writer


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    source = context.input_files[0]
    reader = PdfReader(str(source))
    pages = parse_page_ranges(context.options.get("pages", ""), len(reader.pages))
    writer = build_pdf_writer(reader, pages)
    save_writer(writer, context.output_path)
    context.progress(100, "Selected pages exported")
    return ToolResult(True, "PDF split completed.", [context.output_path], {"pages": pages})
