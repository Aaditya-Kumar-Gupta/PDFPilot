from __future__ import annotations

from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path

import fitz
import pdfplumber


@dataclass(slots=True)
class TextBlock:
    text: str
    x0: float
    y0: float
    x1: float
    y1: float


@dataclass(slots=True)
class PageExtraction:
    page_number: int
    width: float
    height: float
    text_blocks: list[TextBlock] = field(default_factory=list)
    tables: list[list[list[str]]] = field(default_factory=list)

    @property
    def text_content(self) -> str:
        return "\n".join(block.text for block in self.text_blocks if block.text.strip()).strip()

    @property
    def text_lines(self) -> list[str]:
        lines: list[str] = []
        for block in self.text_blocks:
            lines.extend(line.strip() for line in block.text.splitlines() if line.strip())
        return lines


def _clean_tables(raw_tables: list[list[list[str | None]]] | None) -> list[list[list[str]]]:
    cleaned: list[list[list[str]]] = []
    for table in raw_tables or []:
        rows: list[list[str]] = []
        for row in table:
            values = [str(value).strip() if value is not None else "" for value in row]
            if any(values):
                rows.append(values)
        if rows:
            cleaned.append(rows)
    return cleaned


def extract_pages(path: Path) -> list[PageExtraction]:
    extracted: list[PageExtraction] = []
    with fitz.open(path) as document, pdfplumber.open(path) as plumber:
        for index, page in enumerate(document, start=1):
            blocks = []
            for x0, y0, x1, y1, text, *_ in page.get_text("blocks"):
                content = text.strip()
                if not content:
                    continue
                blocks.append(TextBlock(content, float(x0), float(y0), float(x1), float(y1)))
            blocks.sort(key=lambda item: (round(item.y0, 1), round(item.x0, 1)))
            plumber_page = plumber.pages[index - 1]
            tables = _clean_tables(plumber_page.extract_tables())
            extracted.append(
                PageExtraction(
                    page_number=index,
                    width=float(page.rect.width),
                    height=float(page.rect.height),
                    text_blocks=blocks,
                    tables=tables,
                )
            )
    return extracted


def is_sparse_page(page: PageExtraction, min_characters: int = 60, min_blocks: int = 2) -> bool:
    character_count = len("".join(page.text_lines))
    return character_count < min_characters or len(page.text_blocks) < min_blocks


def render_page_png_bytes(path: Path, page_number: int, dpi: int = 144) -> bytes:
    with fitz.open(path) as document:
        page = document[page_number - 1]
        pixmap = page.get_pixmap(dpi=dpi, alpha=False)
        return pixmap.tobytes("png")


def render_page_png_stream(path: Path, page_number: int, dpi: int = 144) -> BytesIO:
    return BytesIO(render_page_png_bytes(path, page_number, dpi=dpi))
