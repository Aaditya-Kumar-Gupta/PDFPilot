from __future__ import annotations

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files, resolve_output_path
from pdf_toolkit.utils.pdf_extract import extract_pages, render_page_png_stream


def run(context: ToolContext) -> ToolResult:
    try:
        from openpyxl.drawing.image import Image as ExcelImage
        from openpyxl import Workbook
    except ImportError as exc:
        raise ToolError("PDF to Excel requires openpyxl. Install dependencies from requirements.txt.") from exc

    ensure_pdf_files(context.input_files)
    input_file = context.input_files[0]
    output_path = resolve_output_path(context.output_path, input_file, "pdf_to_excel", ".xlsx")
    pages = extract_pages(input_file)
    workbook = Workbook()
    first_sheet = workbook.active

    total = max(1, len(pages))
    for index, page in enumerate(pages, start=1):
        sheet = first_sheet if index == 1 else workbook.create_sheet()
        sheet.title = f"Page {page.page_number}"
        sheet.sheet_view.showGridLines = False
        sheet["A1"] = "Layout-preserving page preview"
        preview = ExcelImage(render_page_png_stream(input_file, page.page_number, dpi=200))
        preview.anchor = "A3"
        sheet.add_image(preview)
        sheet.column_dimensions["A"].width = max(60, round(page.width / 8))
        for row_index in range(3, 80):
            sheet.row_dimensions[row_index].height = 24
        context.progress(int(index / total * 100), f"Prepared Excel sheet for page {page.page_number}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_path)
    return ToolResult(True, "Excel export completed with layout-preserving page previews.", [output_path], {"fallback_mode": "page-image"})
