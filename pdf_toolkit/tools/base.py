from __future__ import annotations

from pathlib import Path

from pdf_toolkit.models import MissingDependencyError, ToolContext, ToolError, ToolResult


def staged_feature(context: ToolContext, feature_name: str) -> ToolResult:
    return ToolResult(
        success=False,
        message=f"{feature_name} is planned for a later milestone. The dashboard, registry, and dependency handling are ready for it.",
        output_files=[],
        metadata={"staged": True},
    )


def ensure_not_cancelled(context: ToolContext) -> None:
    if context.is_cancelled():
        raise ToolError("Operation cancelled.")


def single_input(context: ToolContext) -> Path:
    if not context.input_files:
        raise ToolError("Please choose at least one input file.")
    return context.input_files[0]


def require_dependency(available: bool, details: str) -> None:
    if not available:
        raise MissingDependencyError(details)
