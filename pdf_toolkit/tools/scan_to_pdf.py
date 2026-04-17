from __future__ import annotations

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.tools.image_to_pdf import run as image_to_pdf_run


def run(context: ToolContext) -> ToolResult:
    result = image_to_pdf_run(context)
    result.message = "Images converted to PDF. Scanner-device integration can be added through the same import pipeline later."
    return result
