from __future__ import annotations

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files
from pdf_toolkit.utils.pdf_helpers import optimize_pdf_with_quality


QUALITY_MAP = {
    "High quality": (80, 0.95),
    "Balanced": (65, 0.8),
    "Smallest file": (45, 0.65),
}


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    preset = context.options.get("preset", "Balanced")
    quality, scale = QUALITY_MAP.get(preset, QUALITY_MAP["Balanced"])
    optimize_pdf_with_quality(context.input_files[0], context.output_path, quality, scale)
    context.progress(100, f"Compression preset applied: {preset}")
    return ToolResult(True, "Compressed PDF saved.", [context.output_path])
