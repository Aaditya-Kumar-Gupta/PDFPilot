from __future__ import annotations

from io import BytesIO

from reportlab.lib.colors import Color
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


def _text_overlay(width: float, height: float, watermark_text: str) -> BytesIO:
    packet = BytesIO()
    page_canvas = canvas.Canvas(packet, pagesize=(width, height))
    page_canvas.saveState()
    page_canvas.translate(width / 2, height / 2)
    page_canvas.rotate(45)
    page_canvas.setFillColor(Color(1, 1, 1, alpha=0.18))
    page_canvas.setFont("Helvetica-Bold", 36)
    page_canvas.drawCentredString(0, 0, watermark_text)
    page_canvas.restoreState()
    page_canvas.save()
    packet.seek(0)
    return packet


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    watermark_text = context.options.get("text", "CONFIDENTIAL")
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        overlay_pdf = PdfReader(_text_overlay(float(page.mediabox.width), float(page.mediabox.height), watermark_text))
        page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
        context.progress(int(index / total * 100), f"Watermarked page {index}")
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    return ToolResult(True, "Watermark applied.", [context.output_path])
