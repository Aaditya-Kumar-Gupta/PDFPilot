from __future__ import annotations

from io import BytesIO

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_pdf_files


POSITION_MAP = {
    "Bottom Right": lambda width, height, margin: (width - margin, margin),
    "Bottom Center": lambda width, height, margin: (width / 2, margin),
    "Top Right": lambda width, height, margin: (width - margin, height - margin),
    "Top Center": lambda width, height, margin: (width / 2, height - margin),
}


def _overlay(width: float, height: float, text: str, position: str) -> BytesIO:
    packet = BytesIO()
    page_canvas = canvas.Canvas(packet, pagesize=(width, height))
    margin = 10 * mm
    x, y = POSITION_MAP[position](width, height, margin)
    page_canvas.setFont("Helvetica", 10)
    page_canvas.drawCentredString(x, y, text)
    page_canvas.save()
    packet.seek(0)
    return packet


def run(context: ToolContext) -> ToolResult:
    ensure_pdf_files(context.input_files)
    position = context.options.get("position", "Bottom Right")
    reader = PdfReader(str(context.input_files[0]))
    writer = PdfWriter()
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        overlay_pdf = PdfReader(_overlay(float(page.mediabox.width), float(page.mediabox.height), str(index), position))
        page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
        context.progress(int(index / total * 100), f"Numbered page {index}")
    with context.output_path.open("wb") as handle:
        writer.write(handle)
    return ToolResult(True, "Page numbers added.", [context.output_path])
