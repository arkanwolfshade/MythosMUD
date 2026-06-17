#!/usr/bin/env python3
"""PR quality/fragmentation guardrails for MythosMUD."""

from __future__ import annotations

import sys
from collections.abc import Mapping
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.ci.quality_fragmentation_ai_guardrails import check_ai_guardrails, scan_changed_files
from scripts.ci.quality_fragmentation_core import (
    REPO_ROOT,
    ChangedFile,
    GuardContext,
    build_context,
    collect_repo_texts,
    is_code_file,
    is_safe_git_ref,
    parse_args,
    run_cmd,
)
from scripts.ci.quality_fragmentation_lizard import (
    NLOC_MAX,
    check_lizard_limits,
    file_nloc_failures,
    parse_lizard_output,
)
from scripts.ci.quality_fragmentation_trends import (
    added_file_stats,
    append_fragmentation_failures,
    append_fragmentation_warnings,
    trend_averages,
)

# Backward-compatible aliases for unit tests that load this module directly.
_parse_lizard_output = parse_lizard_output
_scan_changed_files = scan_changed_files

__all__ = [
    "ChangedFile",
    "GuardContext",
    "REPO_ROOT",
    "collect_repo_texts",
    "is_safe_git_ref",
    "_parse_lizard_output",
    "_scan_changed_files",
    "check_fragmentation_trends",
    "emit_results",
    "main",
]


def check_fragmentation_trends(
    ctx: GuardContext, base_lengths: list[float], head_lengths: list[float], file_nlocs: list[int]
) -> tuple[list[str], list[str], Mapping[str, object]]:
    failures: list[str] = []
    warnings: list[str] = []
    base_files = run_cmd(["git", "ls-tree", "-r", "--name-only", ctx.base]).splitlines()
    statuses = [changed.status for changed in ctx.changed_code]
    files_added, files_added_pct = added_file_stats(statuses, base_files, is_code_file)
    avg_base_fn, avg_head_fn, avg_file_nloc = trend_averages(base_lengths, head_lengths, file_nlocs)
    append_fragmentation_failures(failures, files_added_pct, avg_base_fn, avg_head_fn)
    append_fragmentation_warnings(warnings, files_added, avg_base_fn, avg_head_fn, avg_file_nloc, NLOC_MAX)

    metrics = {
        "files_added": files_added,
        "files_added_pct": round(files_added_pct, 2),
        "avg_function_length_base": round(avg_base_fn, 2),
        "avg_function_length_head": round(avg_head_fn, 2),
        "avg_file_length": round(avg_file_nloc, 2),
    }
    return failures, warnings, metrics


def emit_results(summary: dict[str, object], failures: list[str], warnings: list[str]) -> int:
    # Avoid logging full summary payloads to keep potentially sensitive paths/details out of plaintext logs.
    print(f"Quality guard summary: hard_fail_reasons={len(failures)}, warnings={len(warnings)}, metrics={len(summary)}")
    for warning in warnings:
        print(f"[WARNING] {warning}")
        print(f"::warning::{warning}")
    for failure in failures:
        print(f"[ERROR] {failure}")
        print(f"::error::{failure}")
    return 1 if failures else 0


def main() -> int:
    base, head, files, fast_mode = parse_args()
    if not base or not head:
        print("No base/head SHA supplied. Skipping quality fragmentation guard.")
        return 0
    ctx = build_context(base, head, files if files else None)
    lizard_failures, base_lengths, head_lengths, file_nlocs = check_lizard_limits(ctx)
    trend_failures, trend_warnings, trend_metrics = check_fragmentation_trends(
        ctx, base_lengths, head_lengths, file_nlocs
    )
    ai_failures, ai_warnings, ai_metrics = check_ai_guardrails(ctx, fast_mode=fast_mode)
    all_failures = lizard_failures + trend_failures + ai_failures + file_nloc_failures(ctx, file_nlocs)
    all_warnings = trend_warnings + ai_warnings
    summary = {
        **trend_metrics,
        **ai_metrics,
        "hard_fail_reasons": all_failures,
        "warnings": all_warnings,
    }
    return emit_results(summary, all_failures, all_warnings)


if __name__ == "__main__":
    raise SystemExit(main())
