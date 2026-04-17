from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    order_raw = str(context.options.get("page_order", "")).strip()
    source = context.input_files[0]
    reader = PdfReader(str(source))
    total_pages = len(reader.pages)
    if not order_raw:
        raise ToolError("No page order was supplied. Use the page organizer to arrange pages.")

    page_order = [int(item.strip()) - 1 for item in order_raw.split(",") if item.strip()]
    if sorted(page_order) != list(range(total_pages)):
        raise ToolError("Page order must include each page exactly once.")

    rotate_map = context.options.get("rotate_pages", {})
    writer = PdfWriter()
    for page_index in page_order:
        page = reader.pages[page_index]
        rotation = int(rotate_map.get(str(page_index + 1), 0))
        if rotation:
            page = page.rotate(rotation)
        writer.add_page(page)

    with context.output_path.open("wb") as handle:
        writer.write(handle)

    context.progress(100, "Page organization saved")
    return ToolResult(True, "PDF reorganized successfully.", [context.output_path])
