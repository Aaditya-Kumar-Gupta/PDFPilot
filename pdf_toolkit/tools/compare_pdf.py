from __future__ import annotations

from difflib import unified_diff
from pathlib import Path

import fitz

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def _extract_text(path: Path) -> list[str]:
    document = fitz.open(path)
    try:
        return [page.get_text("text") for page in document]
    finally:
        document.close()


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    if len(context.input_files) != 2:
        raise ToolError("Compare PDF requires exactly two PDF files.")
    left, right = context.input_files
    left_text = _extract_text(left)
    right_text = _extract_text(right)
    diff = "\n".join(unified_diff(left_text, right_text, fromfile=left.name, tofile=right.name, lineterm=""))
    report_path = context.output_path.with_suffix(".txt")
    report_path.write_text(diff or "No textual differences found.", encoding="utf-8")
    context.progress(100, "Comparison report generated")
    return ToolResult(True, "Comparison report created.", [report_path])
