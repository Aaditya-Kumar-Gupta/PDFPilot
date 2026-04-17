from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    password = context.options.get("password", "")
    if not password:
        raise ToolError("Please provide a password.")
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    context.progress(100, "Encryption applied")
    return ToolResult(True, "PDF protected with password.", [context.output_path])
