from __future__ import annotations

import math
from io import BytesIO
from pathlib import Path

import fitz
from PIL import Image
from pypdf import PdfReader, PdfWriter

from pdf_toolkit.models import ToolError


def parse_page_ranges(raw_value: str, total_pages: int) -> list[int]:
    if not raw_value.strip():
        return list(range(total_pages))

    pages: set[int] = set()
    for chunk in raw_value.split(","):
        token = chunk.strip()
        if not token:
            continue
        if "-" in token:
            start_raw, end_raw = token.split("-", 1)
            start = max(1, int(start_raw))
            end = min(total_pages, int(end_raw))
            pages.update(range(start - 1, end))
        else:
            page = int(token)
            if 1 <= page <= total_pages:
                pages.add(page - 1)
    result = sorted(pages)
    if not result:
        raise ToolError("No valid page selection was provided.")
    return result


def build_pdf_writer(reader: PdfReader, selected_pages: list[int]) -> PdfWriter:
    writer = PdfWriter()
    for page_index in selected_pages:
        writer.add_page(reader.pages[page_index])
    return writer


def save_writer(writer: PdfWriter, output_path: Path) -> None:
    with output_path.open("wb") as handle:
        writer.write(handle)


def optimize_pdf_with_quality(input_path: Path, output_path: Path, image_quality: int = 65, scale: float = 0.8) -> None:
    document = fitz.open(input_path)
    try:
        for page in document:
            for image_info in page.get_images(full=True):
                xref = image_info[0]
                base_image = document.extract_image(xref)
                image = Image.open(BytesIO(base_image["image"]))
                if image.mode not in ("RGB", "L"):
                    image = image.convert("RGB")
                new_size = (
                    max(1, math.floor(image.width * scale)),
                    max(1, math.floor(image.height * scale)),
                )
                image = image.resize(new_size)
                buffer = BytesIO()
                image.save(buffer, format="JPEG", optimize=True, quality=image_quality)
                document.update_stream(xref, buffer.getvalue())
        document.save(output_path, garbage=3, deflate=True)
    finally:
        document.close()
