from __future__ import annotations

import argparse
import json
import shutil
import sys
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import fitz
from pypdf import PdfReader

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from pdf_toolkit.models import MissingDependencyError, ToolContext, ToolError, ToolResult
from pdf_toolkit.tools import (
    annotate_pdf,
    compare_pdf,
    compress_pdf,
    crop_pdf,
    image_to_pdf,
    merge_pdf,
    office_to_pdf,
    organize_pdf,
    page_numbers,
    pdf_to_excel,
    pdf_to_jpg,
    pdf_to_pdfa,
    pdf_to_powerpoint,
    pdf_to_word,
    protect_pdf,
    redact_pdf,
    remove_pages,
    repair_pdf,
    rotate_pdf,
    scan_to_pdf,
    sign_pdf,
    split_pdf,
    unlock_pdf,
    watermark,
)
from pdf_toolkit.utils.dependencies import tesseract_status
from pdf_toolkit.utils.renderer import resolve_office_renderer


@dataclass(frozen=True)
class Case:
    name: str
    run: Callable[[Path], dict]


def _context(
    input_files: list[Path],
    output_path: Path,
    options: dict | None = None,
    *,
    cancelled: bool = False,
) -> ToolContext:
    return ToolContext(
        input_files=input_files,
        output_path=output_path,
        options=options or {},
        progress=lambda *_: None,
        is_cancelled=lambda: cancelled,
    )


def _assert_readable_pdf(path: Path) -> dict:
    reader = PdfReader(str(path))
    return {"kind": "pdf", "pages": len(reader.pages), "bytes": path.stat().st_size}


def _assert_encrypted_pdf(path: Path) -> dict:
    reader = PdfReader(str(path))
    if not reader.is_encrypted:
        raise AssertionError(f"Expected encrypted PDF: {path}")
    return {"kind": "pdf", "encrypted": True, "bytes": path.stat().st_size}


def _assert_readable_with_fitz(path: Path) -> dict:
    with fitz.open(path) as document:
        return {"kind": "pdf", "pages": len(document), "bytes": path.stat().st_size}


def _assert_exists(path: Path, kind: str) -> dict:
    if not path.exists():
        raise AssertionError(f"Expected output was not created: {path}")
    if path.stat().st_size <= 0:
        raise AssertionError(f"Expected output is empty: {path}")
    return {"kind": kind, "bytes": path.stat().st_size}


def _first_text_phrase(pdf_path: Path) -> str:
    with fitz.open(pdf_path) as document:
        for page in document:
            words = [word for word in page.get_text("text").split() if len(word) >= 4]
            if words:
                return words[0]
    return "PDFPilot"


def _run_tool(
    runner: Callable[[ToolContext], ToolResult],
    input_files: list[Path],
    output_path: Path,
    options: dict | None = None,
) -> ToolResult:
    result = runner(_context(input_files, output_path, options))
    if not result.success:
        raise AssertionError(result.message)
    if not result.output_files:
        raise AssertionError("Tool returned no output files.")
    for output_file in result.output_files:
        if not output_file.exists() or output_file.stat().st_size <= 0:
            raise AssertionError(f"Tool returned missing or empty output: {output_file}")
    return result


def _prepare_office_fixtures(work_dir: Path) -> dict[str, Path]:
    fixtures = REPO_ROOT / "runtime_tests" / "manual_verify"
    office_dir = work_dir / "office_sources"
    office_dir.mkdir(parents=True, exist_ok=True)

    paths: dict[str, Path] = {}
    candidates = {
        "Word": fixtures / "sample1.docx",
        "PowerPoint": fixtures / "sample1.pptx",
        "Excel": fixtures / "sample1.xlsx",
    }
    for source_type, source in candidates.items():
        target = office_dir / source.name
        shutil.copy2(source, target)
        paths[source_type] = target

    csv_path = office_dir / "sample.csv"
    csv_path.write_text("Region,Sales\nNorth,42\nSouth,11\n", encoding="utf-8")
    paths["CSV"] = csv_path
    return paths


def _cases(fixtures: Path) -> list[Case]:
    sample1 = fixtures / "sample1.pdf"
    sample2 = fixtures / "sample2.pdf"
    image1 = fixtures / "sample1.png"
    image2 = fixtures / "sample2.png"

    return [
        Case("merge_pdf", lambda out: _assert_readable_pdf(_run_tool(merge_pdf.run, [sample1, sample2], out / "merged.pdf").output_files[0])),
        Case("split_pdf", lambda out: _assert_readable_pdf(_run_tool(split_pdf.run, [sample1], out / "split.pdf", {"pages": "1"}).output_files[0])),
        Case("remove_pages", lambda out: _assert_readable_pdf(_run_tool(remove_pages.run, [sample1], out / "removed.pdf", {"pages": "2"}).output_files[0])),
        Case(
            "organize_pdf",
            lambda out: _assert_readable_pdf(
                _run_tool(organize_pdf.run, [sample1], out / "organized.pdf", {"page_order": "2,1", "rotate_pages": {"1": 90}}).output_files[0]
            ),
        ),
        Case("rotate_pdf", lambda out: _assert_readable_pdf(_run_tool(rotate_pdf.run, [sample1], out / "rotated.pdf", {"pages": "1", "angle": "90"}).output_files[0])),
        Case("compress_pdf", lambda out: _assert_readable_with_fitz(_run_tool(compress_pdf.run, [sample1], out / "compressed.pdf", {"preset": "Balanced"}).output_files[0])),
        Case("repair_pdf", lambda out: _assert_readable_with_fitz(_run_tool(repair_pdf.run, [sample1], out / "repaired.pdf").output_files[0])),
        Case("image_to_pdf", lambda out: _assert_readable_pdf(_run_tool(image_to_pdf.run, [image1, image2], out / "images.pdf").output_files[0])),
        Case("scan_to_pdf", lambda out: _assert_readable_pdf(_run_tool(scan_to_pdf.run, [image1, image2], out / "scan.pdf").output_files[0])),
        Case("pdf_to_jpg", lambda out: {"files": [_assert_exists(path, "jpg") for path in _run_tool(pdf_to_jpg.run, [sample1], out / "jpg", {"dpi": "120"}).output_files]}),
        Case("pdf_to_word", lambda out: _assert_exists(_run_tool(pdf_to_word.run, [sample1], out / "word.docx").output_files[0], "docx")),
        Case("pdf_to_powerpoint", lambda out: _assert_exists(_run_tool(pdf_to_powerpoint.run, [sample1], out / "slides.pptx").output_files[0], "pptx")),
        Case("pdf_to_excel", lambda out: _assert_exists(_run_tool(pdf_to_excel.run, [sample1], out / "book.xlsx").output_files[0], "xlsx")),
        Case("pdf_to_pdfa", lambda out: _assert_readable_with_fitz(_run_tool(pdf_to_pdfa.run, [sample1], out / "pdfa.pdf").output_files[0])),
        Case("page_numbers", lambda out: _assert_readable_pdf(_run_tool(page_numbers.run, [sample1], out / "numbered.pdf", {"position": "Bottom Right"}).output_files[0])),
        Case("watermark", lambda out: _assert_readable_pdf(_run_tool(watermark.run, [sample1], out / "watermark.pdf", {"text": "RELEASE TEST"}).output_files[0])),
        Case("annotate_pdf", lambda out: _assert_readable_pdf(_run_tool(annotate_pdf.run, [sample1], out / "annotated.pdf", {"pages": "1", "text": "Release test"}).output_files[0])),
        Case("crop_pdf", lambda out: _assert_readable_pdf(_run_tool(crop_pdf.run, [sample1], out / "cropped.pdf", {"margin": "12"}).output_files[0])),
        Case("protect_pdf", lambda out: _assert_encrypted_pdf(_run_tool(protect_pdf.run, [sample1], out / "protected.pdf", {"password": "release-pass"}).output_files[0])),
        Case(
            "unlock_pdf",
            lambda out: _assert_readable_pdf(
                _run_tool(
                    unlock_pdf.run,
                    [_run_tool(protect_pdf.run, [sample1], out / "unlock_source.pdf", {"password": "release-pass"}).output_files[0]],
                    out / "unlocked.pdf",
                    {"password": "release-pass"},
                ).output_files[0]
            ),
        ),
        Case("sign_pdf", lambda out: _assert_readable_with_fitz(_run_tool(sign_pdf.run, [sample1], out / "signed.pdf", {"signature_image": str(image1)}).output_files[0])),
        Case("compare_pdf", lambda out: _assert_exists(_run_tool(compare_pdf.run, [sample1, sample2], out / "compare.pdf").output_files[0], "txt")),
        Case("redact_pdf", lambda out: _assert_readable_with_fitz(_run_tool(redact_pdf.run, [sample1], out / "redacted.pdf", {"text": _first_text_phrase(sample1)}).output_files[0])),
    ]


def _office_cases(office_sources: dict[str, Path]) -> list[Case]:
    return [
        Case("office_to_pdf_word", lambda out: _office_assert(out, office_sources["Word"], "Word")),
        Case("office_to_pdf_powerpoint", lambda out: _office_assert(out, office_sources["PowerPoint"], "PowerPoint")),
        Case("office_to_pdf_excel", lambda out: _office_assert(out, office_sources["Excel"], "Excel")),
        Case("office_to_pdf_csv", lambda out: _office_assert(out, office_sources["CSV"], "Excel")),
    ]


def _office_assert(out: Path, source: Path, source_type: str) -> dict:
    result = _run_tool(office_to_pdf.run, [source], out / f"{source.stem}.pdf", {"source_type": source_type})
    details = _assert_readable_with_fitz(result.output_files[0])
    details["render_mode"] = result.metadata.get("render_mode", "")
    return details


def _expected_failure_cases(fixtures: Path) -> list[Case]:
    sample1 = fixtures / "sample1.pdf"
    return [
        Case("invalid_empty_selection", lambda out: _expect_tool_error(split_pdf.run, [], out / "empty.pdf", {}, "input")),
        Case("invalid_page_range", lambda out: _expect_tool_error(split_pdf.run, [sample1], out / "bad_range.pdf", {"pages": "999"}, "page")),
        Case(
            "invalid_wrong_password",
            lambda out: _expect_tool_error(
                unlock_pdf.run,
                [_run_tool(protect_pdf.run, [sample1], out / "wrong_password_source.pdf", {"password": "right-pass"}).output_files[0]],
                out / "wrong_password.pdf",
                {"password": "wrong-pass"},
                "password",
            ),
        ),
        Case("cancelled_operation", lambda out: _expect_cancelled(merge_pdf.run, [sample1, sample1], out / "cancelled.pdf")),
        Case(
            "encrypted_pdfa_rejected",
            lambda out: _expect_tool_error(
                pdf_to_pdfa.run,
                [_run_tool(protect_pdf.run, [sample1], out / "encrypted_pdfa_source.pdf", {"password": "secret"}).output_files[0]],
                out / "encrypted_pdfa.pdf",
                {},
                "encrypted",
            ),
        ),
    ]


def _expect_tool_error(
    runner: Callable[[ToolContext], ToolResult],
    input_files: list[Path],
    output_path: Path,
    options: dict,
    expected_text: str,
) -> dict:
    try:
        runner(_context(input_files, output_path, options))
    except (MissingDependencyError, ToolError, FileNotFoundError, ValueError) as exc:
        message = str(exc)
        if expected_text.lower() not in message.lower():
            raise AssertionError(f"Expected '{expected_text}' in error message, got: {message}") from exc
        return {"expected_error": message}
    raise AssertionError("Expected tool to fail, but it succeeded.")


def _expect_cancelled(runner: Callable[[ToolContext], ToolResult], input_files: list[Path], output_path: Path) -> dict:
    try:
        runner(_context(input_files, output_path, {}, cancelled=True))
    except ToolError as exc:
        message = str(exc)
        if "cancel" not in message.lower():
            raise AssertionError(f"Expected cancellation error, got: {message}") from exc
        return {"expected_error": message}
    raise AssertionError("Expected cancelled operation to fail, but it succeeded.")


def _run_cases(cases: list[Case], output_root: Path) -> list[dict]:
    results: list[dict] = []
    for case in cases:
        case_output = output_root / case.name
        case_output.mkdir(parents=True, exist_ok=True)
        started = datetime.now(timezone.utc)
        try:
            details = case.run(case_output)
            status = "passed"
            error = ""
            trace = ""
        except Exception as exc:  # noqa: BLE001 - release report should preserve all failures
            details = {}
            status = "failed"
            error = str(exc)
            trace = traceback.format_exc()
        finished = datetime.now(timezone.utc)
        results.append(
            {
                "name": case.name,
                "status": status,
                "started_utc": started.isoformat(),
                "finished_utc": finished.isoformat(),
                "details": details,
                "error": error,
                "trace": trace,
            }
        )
    return results


def _write_markdown(report_path: Path, payload: dict) -> None:
    lines = [
        "# PDFPilot Functional Smoke Report",
        "",
        f"- Created UTC: {payload['created_utc']}",
        f"- Fixture root: `{payload['fixture_root']}`",
        f"- Output root: `{payload['output_root']}`",
        f"- Office renderer: {payload['office_renderer']['mode']} ({payload['office_renderer']['details']})",
        f"- Tesseract: {payload['tesseract']['summary']} ({payload['tesseract']['details']})",
        f"- Status: {payload['status']}",
        "",
        "## Cases",
        "",
        "| Case | Status | Notes |",
        "| --- | --- | --- |",
    ]
    for result in payload["cases"]:
        note = result["error"] or result["details"].get("kind") or result["details"].get("expected_error", "")
        lines.append(f"| {result['name']} | {result['status']} | {str(note).replace('|', '/')} |")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PDFPilot release functional smoke tests.")
    parser.add_argument("--output-root", type=Path, default=REPO_ROOT / "releases" / "validation" / "functional")
    parser.add_argument("--fixture-root", type=Path, default=REPO_ROOT / "runtime_tests")
    parser.add_argument("--json-report", type=Path, default=None)
    parser.add_argument("--markdown-report", type=Path, default=None)
    args = parser.parse_args()

    output_root = args.output_root.resolve()
    fixture_root = args.fixture_root.resolve()
    shutil.rmtree(output_root, ignore_errors=True)
    output_root.mkdir(parents=True, exist_ok=True)

    office_sources = _prepare_office_fixtures(output_root)
    cases = _cases(fixture_root) + _office_cases(office_sources) + _expected_failure_cases(fixture_root)
    case_results = _run_cases(cases, output_root / "cases")
    failed = [result for result in case_results if result["status"] != "passed"]
    renderer = resolve_office_renderer()
    tesseract = tesseract_status()

    payload = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "failed" if failed else "passed",
        "fixture_root": str(fixture_root),
        "output_root": str(output_root),
        "office_renderer": {
            "available": renderer.available,
            "mode": renderer.mode,
            "soffice_path": str(renderer.soffice_path) if renderer.soffice_path else "",
            "details": renderer.details,
        },
        "tesseract": {
            "available": tesseract.available,
            "summary": tesseract.summary,
            "details": tesseract.details,
        },
        "cases": case_results,
    }

    json_report = args.json_report or output_root / "functional-smoke.json"
    markdown_report = args.markdown_report or output_root / "functional-smoke.md"
    json_report.parent.mkdir(parents=True, exist_ok=True)
    json_report.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_markdown(markdown_report, payload)

    print(f"Functional smoke report: {markdown_report}")
    if failed:
        print(f"{len(failed)} functional smoke case(s) failed.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
