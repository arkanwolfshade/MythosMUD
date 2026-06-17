#!/usr/bin/env python3
"""Lizard complexity checks for quality fragmentation guard."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
from typing import TypedDict, cast

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.ci.quality_fragmentation_core import (
    REPO_ROOT,
    ChangedFile,
    GuardContext,
    git_show_file,
    nloc_for_text,
    run_cmd,
)

CCN_MAX = 10
NLOC_MAX = 55
PARAMS_MAX = 6
FILE_NLOC_MAX = 550


class LizardFunctionRow(TypedDict):
    name: str
    nloc: int
    ccn: int
    params: int
    start_line: int


def _to_str(value: object, default: str) -> str:
    return value if isinstance(value, str) else default


def _to_int(value: object, default: int) -> int:
    return value if isinstance(value, int) else default


def parse_lizard_output(output: str) -> list[LizardFunctionRow]:
    if not output.strip():
        return []
    parsed_obj = cast(object, json.loads(output))
    return [_map_function_node_to_row(fn_map) for fn_map in _iter_lizard_function_maps(parsed_obj)]


def _map_function_node_to_row(fn_map: dict[str, object]) -> LizardFunctionRow:
    return {
        "name": _to_str(fn_map.get("name"), "<unknown>"),
        "nloc": _to_int(fn_map.get("nloc"), 0),
        "ccn": _to_int(fn_map.get("cyclomatic_complexity"), 0),
        "params": _to_int(fn_map.get("parameter_count"), 0),
        "start_line": _to_int(fn_map.get("start_line"), 0),
    }


def _iter_lizard_function_maps(parsed_obj: object) -> list[dict[str, object]]:
    entries = _lizard_entries(parsed_obj)
    function_maps: list[dict[str, object]] = []
    for entry_obj in entries:
        if not isinstance(entry_obj, dict):
            continue
        function_list_obj = cast(dict[str, object], entry_obj).get("function_list", [])
        if not isinstance(function_list_obj, list):
            continue
        for fn_obj in cast(list[object], function_list_obj):
            if isinstance(fn_obj, dict):
                function_maps.append(cast(dict[str, object], fn_obj))
    return function_maps


def _lizard_entries(parsed_obj: object) -> list[object]:
    if isinstance(parsed_obj, list):
        return cast(list[object], parsed_obj)
    if isinstance(parsed_obj, dict):
        raw_files = cast(dict[str, object], parsed_obj).get("files", [])
        if isinstance(raw_files, list):
            return cast(list[object], raw_files)
    return []


def run_lizard_on_content(path: str, content: str) -> list[LizardFunctionRow]:
    suffix = Path(path).suffix or ".txt"
    with tempfile.NamedTemporaryFile("w", suffix=suffix, encoding="utf-8", delete=False) as temp_file:
        _ = temp_file.write(content)
        temp_path = temp_file.name
    try:
        output = run_cmd(["lizard", "-j", temp_path], check=False)
        return parse_lizard_output(output)
    except (OSError, UnicodeDecodeError, ValueError):
        return []
    finally:
        Path(temp_path).unlink(missing_ok=True)


def has_lizard_override(file_path: str, start_line: int) -> bool:
    absolute = REPO_ROOT / file_path
    if not absolute.exists() or start_line <= 0:
        return False
    lines = absolute.read_text(encoding="utf-8").splitlines()
    return start_line <= len(lines) and "lizard: allow" in lines[start_line - 1]


def check_lizard_limits(ctx: GuardContext) -> tuple[list[str], list[float], list[float], list[int]]:
    failures: list[str] = []
    base_lengths: list[float] = []
    head_lengths: list[float] = []
    file_nlocs: list[int] = []
    override_used = False

    for changed in ctx.changed_code:
        _process_head_lizard(changed, ctx.head, failures, head_lengths, file_nlocs)
        override_used = override_used or _has_override_in_file(changed, ctx.head)
        _process_base_lizard(changed, ctx.base, base_lengths)

    if override_used and not ctx.changed_tests:
        failures.append("Lizard override(s) used but no test files were changed in this PR.")
    return failures, base_lengths, head_lengths, file_nlocs


def _check_head_rows(changed: ChangedFile, rows: list[LizardFunctionRow], failures: list[str]) -> None:
    for row in rows:
        if not _row_exceeds(row):
            continue
        if has_lizard_override(changed.path, row["start_line"]):
            continue
        failures.append(f"{changed.path}:{row['start_line']} {row['name']} exceeds limits ({_row_reason(row)}).")


def _process_head_lizard(
    changed: ChangedFile,
    head_sha: str,
    failures: list[str],
    head_lengths: list[float],
    file_nlocs: list[int],
) -> None:
    head_content = git_show_file(head_sha, changed.path)
    if head_content is None:
        return
    file_nlocs.append(nloc_for_text(changed.path, head_content))
    rows = run_lizard_on_content(changed.path, head_content)
    head_lengths.extend(float(row["nloc"]) for row in rows)
    _check_head_rows(changed, rows, failures)


def _has_override_in_file(changed: ChangedFile, head_sha: str) -> bool:
    head_content = git_show_file(head_sha, changed.path)
    if head_content is None:
        return False
    rows = run_lizard_on_content(changed.path, head_content)
    return any(has_lizard_override(changed.path, row["start_line"]) for row in rows)


def _process_base_lizard(changed: ChangedFile, base_sha: str, base_lengths: list[float]) -> None:
    if changed.status == "A":
        return
    base_path = changed.old_path if (changed.status == "R" and changed.old_path) else changed.path
    base_content = git_show_file(base_sha, base_path)
    if base_content is None:
        return
    rows = run_lizard_on_content(base_path, base_content)
    base_lengths.extend(float(row["nloc"]) for row in rows)


def _row_exceeds(row: LizardFunctionRow) -> bool:
    return row["ccn"] > CCN_MAX or row["nloc"] > NLOC_MAX or row["params"] > PARAMS_MAX


def _row_reason(row: LizardFunctionRow) -> str:
    parts: list[str] = []
    if row["ccn"] > CCN_MAX:
        parts.append(f"ccn={row['ccn']}")
    if row["nloc"] > NLOC_MAX:
        parts.append(f"nloc={row['nloc']}")
    if row["params"] > PARAMS_MAX:
        parts.append(f"params={row['params']}")
    return ", ".join(parts)


def file_nloc_failures(ctx: GuardContext, file_nlocs: list[int]) -> list[str]:
    failures: list[str] = []
    for changed, nloc in zip(ctx.changed_code, file_nlocs, strict=False):
        if changed.status != "A" or nloc <= FILE_NLOC_MAX:
            continue
        if _has_file_nloc_override(changed.path):
            continue
        failures.append(f"{changed.path} exceeds file NLOC threshold ({nloc} > {FILE_NLOC_MAX}).")
    return failures


def _has_file_nloc_override(path: str) -> bool:
    abs_path = REPO_ROOT / path
    if not abs_path.exists():
        return False
    try:
        text = abs_path.read_text(encoding="utf-8")
    except Exception:
        return False
    return "lizard: allow file_nloc" in text.lower()
