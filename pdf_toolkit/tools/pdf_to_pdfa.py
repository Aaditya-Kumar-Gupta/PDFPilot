from __future__ import annotations

import fitz

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files, resolve_output_path


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    input_file = context.input_files[0]
    output_path = resolve_output_path(context.output_path, input_file, "pdf_to_pdfa", ".pdf")

    source = fitz.open(input_file)
    target = fitz.open()
    try:
        if source.needs_pass or source.is_encrypted:
            raise ToolError("PDF to PDF/A cannot process encrypted PDFs. Unlock the PDF first.")
        target.insert_pdf(source)
        metadata = source.metadata or {}
        metadata.update(
            {
                "producer": "PDFPilot archival-oriented rewrite",
                "creator": "PDFPilot",
                "subject": metadata.get("subject") or "Best-effort archival PDF export",
                "keywords": metadata.get("keywords") or "archival, pdfa, best-effort",
            }
        )
        target.set_metadata(metadata)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        target.save(output_path, garbage=4, deflate=True, clean=True)
    finally:
        source.close()
        target.close()
    return ToolResult(
        True,
        "Archival-oriented PDF export completed.",
        [output_path],
        {"fallback_mode": "normalized-rewrite"},
    )
