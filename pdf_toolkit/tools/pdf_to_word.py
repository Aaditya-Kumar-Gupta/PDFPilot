from __future__ import annotations

from pdf_toolkit.models import ToolContext, ToolError, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files, resolve_output_path


def run(context: ToolContext) -> ToolResult:
    try:
        from pdf2docx import Converter
    except ImportError as exc:
        raise ToolError("PDF to Word requires pdf2docx. Install dependencies from requirements.txt.") from exc

    ensure_pdf_files(context.input_files)
    input_file = context.input_files[0]
    output_path = resolve_output_path(context.output_path, input_file, "pdf_to_word", ".docx")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    converter = Converter(str(input_file))
    try:
        context.progress(10, "Analyzing PDF layout for Word conversion")
        converter.convert(str(output_path))
        context.progress(100, "Converted PDF to Word")
    except Exception as exc:
        raise ToolError(f"Word conversion failed: {exc}") from exc
    finally:
        converter.close()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return ToolResult(True, "Word export completed.", [output_path], {"fallback_mode": "structured-docx"})
