from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.tools.base import ensure_not_cancelled
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    writer = PdfWriter()
    total = len(context.input_files)
    for index, path in enumerate(context.input_files, start=1):
        ensure_not_cancelled(context)
        reader = PdfReader(str(path))
        for page in reader.pages:
            writer.add_page(page)
        context.progress(int(index / total * 100), f"Added {path.name}")

    with context.output_path.open("wb") as handle:
        writer.write(handle)
    return ToolResult(True, "Merged PDF created successfully.", [context.output_path])
