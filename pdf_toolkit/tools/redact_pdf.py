from __future__ import annotations

import fitz

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    phrase = str(context.options.get("text", "")).strip()
    if not phrase:
        raise ToolError("Provide the exact text to redact.")
    document = fitz.open(context.input_files[0])
    try:
        total_hits = 0
        for page in document:
            matches = page.search_for(phrase)
            for rect in matches:
                page.add_redact_annot(rect, fill=(0, 0, 0))
            if matches:
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
            total_hits += len(matches)
        document.save(context.output_path)
    finally:
        document.close()
    context.progress(100, "Redactions applied")
    return ToolResult(True, f"Redacted {total_hits} matching text items.", [context.output_path], {"matches": total_hits})
