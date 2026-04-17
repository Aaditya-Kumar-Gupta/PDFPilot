from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable


ProgressCallback = Callable[[int, str], None]


@dataclass(slots=True)
class OptionField:
    key: str
    label: str
    field_type: str = "text"
    default: Any = ""
    help_text: str = ""
    placeholder: str = ""
    choices: list[str] = field(default_factory=list)
    required: bool = False


@dataclass(slots=True)
class DependencyStatus:
    available: bool
    summary: str
    details: str = ""


@dataclass(slots=True)
class ToolContext:
    input_files: list[Path]
    output_path: Path
    options: dict[str, Any]
    progress: ProgressCallback
    is_cancelled: Callable[[], bool]


@dataclass(slots=True)
class ToolResult:
    success: bool
    message: str
    output_files: list[Path] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ToolDefinition:
    tool_id: str
    category: str
    title: str
    description: str
    icon_name: str
    executor: Callable[[ToolContext], ToolResult]
    option_fields: list[OptionField] = field(default_factory=list)
    allows_multiple_inputs: bool = True
    accepts_output_dir: bool = False
    staged: bool = False
    supports_preview: bool = True
    requires_dependency: Callable[[], DependencyStatus] | None = None
    keywords: list[str] = field(default_factory=list)
    workflow_steps: list[str] = field(
        default_factory=lambda: ["Upload files", "Configure settings", "Run process"]
    )
    badge: str = ""
    workspace_mode: str = "standard"


class ToolError(RuntimeError):
    """Raised when a tool cannot complete because of invalid inputs or runtime errors."""


class MissingDependencyError(ToolError):
    """Raised when an optional offline dependency is not available."""
