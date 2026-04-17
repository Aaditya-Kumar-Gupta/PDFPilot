from __future__ import annotations

from pathlib import Path

import fitz

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    source = fitz.open(context.input_files[0])
    output_dir = context.output_path if context.output_path.is_dir() else context.output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    try:
        total = len(source)
        dpi = int(context.options.get("dpi", 150) or 150)
        for index, page in enumerate(source, start=1):
            pixmap = page.get_pixmap(dpi=dpi, alpha=False)
            target = output_dir / f"{context.input_files[0].stem}_page_{index}.jpg"
            pixmap.save(target)
            created.append(target)
            context.progress(int(index / total * 100), f"Exported page {index}")
    finally:
        source.close()
    return ToolResult(True, "Pages exported as JPG.", created)
