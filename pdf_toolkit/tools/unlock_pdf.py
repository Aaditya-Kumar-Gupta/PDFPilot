from __future__ import annotations

from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    password = context.options.get("password", "")
    reader = PdfReader(str(context.input_files[0]))
    if reader.is_encrypted and reader.decrypt(password) == 0:
        raise ToolError("Incorrect PDF password.")
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    context.progress(100, "Password removed")
    return ToolResult(True, "PDF unlocked successfully.", [context.output_path])
