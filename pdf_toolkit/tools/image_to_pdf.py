from __future__ import annotations

from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from PIL import Image

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.utils.file_utils import ensure_image_files


def run(context: ToolContext) -> ToolResult:
    ensure_image_files(context.input_files)
    pdf = canvas.Canvas(str(context.output_path))
    total = len(context.input_files)
    for index, path in enumerate(context.input_files, start=1):
        image = Image.open(path)
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")
        width, height = image.size
        pdf.setPageSize((width, height))
        pdf.drawImage(ImageReader(image), 0, 0, width=width, height=height, preserveAspectRatio=True)
        pdf.showPage()
        context.progress(int(index / total * 100), f"Added image {index} of {total}")
    pdf.save()
    return ToolResult(True, "PDF created from images.", [context.output_path])
