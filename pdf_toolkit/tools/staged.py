from __future__ import annotations

from pdf_toolkit.models import ToolContext, ToolResult
from pdf_toolkit.tools.base import staged_feature


def make_staged_runner(name: str):
    def _runner(context: ToolContext) -> ToolResult:
        return staged_feature(context, name)

    return _runner
