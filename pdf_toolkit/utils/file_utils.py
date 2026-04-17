from __future__ import annotations

from pathlib import Path

from pdf_toolkit.models import ToolError


PDF_SUFFIXES = {".pdf"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp"}
OFFICE_SUFFIXES = {".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"}


def ensure_files_exist(paths: list[Path]) -> None:
    if not paths:
        raise ToolError("Please choose at least one input file.")
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise ToolError(f"Missing input files: {', '.join(missing)}")


def ensure_pdf_files(paths: list[Path]) -> None:
    ensure_files_exist(paths)
    invalid = [path.name for path in paths if path.suffix.lower() not in PDF_SUFFIXES]
    if invalid:
        raise ToolError(f"These files are not PDFs: {', '.join(invalid)}")


def ensure_image_files(paths: list[Path]) -> None:
    ensure_files_exist(paths)
    invalid = [path.name for path in paths if path.suffix.lower() not in IMAGE_SUFFIXES]
    if invalid:
        raise ToolError(f"These files are not supported images: {', '.join(invalid)}")


def unique_output_path(path: Path, suffix: str | None = None) -> Path:
    target = path if suffix is None else path.with_suffix(suffix)
    if not target.exists():
        return target
    stem = target.stem
    extension = target.suffix
    counter = 1
    while True:
        candidate = target.with_name(f"{stem}_{counter}{extension}")
        if not candidate.exists():
            return candidate
        counter += 1


def resolve_output_path(output_path: Path, input_file: Path, tool_id: str, suffix: str) -> Path:
    if output_path.exists() and output_path.is_dir():
        return unique_output_path(output_path / f"{input_file.stem}_{tool_id}{suffix}")
    if output_path.suffix.lower() != suffix.lower():
        return output_path.with_suffix(suffix)
    return output_path
