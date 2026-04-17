from __future__ import annotations

from io import BytesIO

from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files
from pdf_toolkit.utils.pdf_helpers import parse_page_ranges


def _annotation_overlay(width: float, height: float, text: str) -> BytesIO:
    packet = BytesIO()
    page_canvas = canvas.Canvas(packet, pagesize=(width, height))
    page_canvas.setFillColorRGB(0.95, 0.78, 0.19)
    page_canvas.roundRect(32, height - 96, width - 64, 44, 8, fill=1, stroke=0)
    page_canvas.setFillColorRGB(0.07, 0.08, 0.11)
    page_canvas.setFont("Helvetica", 12)
    page_canvas.drawString(44, height - 70, text)
    page_canvas.save()
    packet.seek(0)
    return packet


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    note = context.options.get("text", "Reviewed offline")
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    pages = set(parse_page_ranges(context.options.get("pages", ""), len(reader.pages)))
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        if index - 1 in pages:
            overlay_pdf = PdfReader(_annotation_overlay(float(page.mediabox.width), float(page.mediabox.height), note))
            page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
        context.progress(int(index / total * 100), f"Processed page {index}")
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    return ToolResult(True, "Annotation overlay added.", [context.output_path])
