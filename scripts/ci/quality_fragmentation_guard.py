#!/usr/bin/env python3
"""PR quality/fragmentation guardrails for MythosMUD."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict, TypeGuard, cast

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.ci.quality_fragmentation_graph import compute_python_cross_file_depth
from scripts.ci.quality_fragmentation_trends import (
    added_file_stats,
    append_fragmentation_failures,
    append_fragmentation_warnings,
    append_rule_b_failure,
    append_rule_c_warning,
    trend_averages,
)
from scripts.ci.quality_fragmentation_usage import imported_by_count, is_single_use_small_file
from scripts.utils.safe_subprocess import safe_run

REPO_ROOT = Path(__file__).resolve().parents[2]
CODE_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx"}
TEST_PATH_MARKERS = ("/tests/", "\\tests\\", "test_", "_test.")
CCN_MAX = 10
NLOC_MAX = 55
PARAMS_MAX = 6
FILE_NLOC_MAX = 550
GIT_REF_PATTERN = re.compile(r"^(?:[0-9a-fA-F]{7,40}|[A-Za-z0-9][A-Za-z0-9._/-]{0,199})$")


@dataclass
class ChangedFile:
    status: str
    old_path: str | None
    path: str


@dataclass
class GuardContext:
    base: str
    head: str
    changed_files: list[ChangedFile]
    changed_code: list[ChangedFile]
    changed_tests: bool


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


def run_cmd(command: list[str], *, check: bool = True) -> str:
    if command and command[0] == "git":
        command = [_git_executable(), *command[1:]]
    result = safe_run(command, capture_output=True, text=True, check=False, cwd=REPO_ROOT)
    if check and result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def git_show_file(rev: str, path: str) -> str | None:
    if not is_safe_git_ref(rev):
        return None
    result = safe_run(
        [_git_executable(), "show", f"{rev}:{path}"],
        capture_output=True,
        text=True,
        check=False,
        cwd=REPO_ROOT,
    )
    return result.stdout if result.returncode == 0 else None


def _git_executable() -> str:
    # Use command name with safe_run so PATH resolution is handled by the OS.
    # Absolute paths outside repo root are intentionally rejected by safe_subprocess validation.
    return "git"


def is_code_file(path: str) -> bool:
    return Path(path).suffix.lower() in CODE_EXTENSIONS


def parse_changed_files(base: str, head: str) -> list[ChangedFile]:
    rows = run_cmd(["git", "diff", "--name-status", f"{base}...{head}"]).splitlines()
    changed: list[ChangedFile] = []
    for row in rows:
        parts = row.split("\t")
        if not parts or len(parts) < 2:
            continue
        if parts[0].startswith("R") and len(parts) >= 3:
            changed.append(ChangedFile(status="R", old_path=parts[1], path=parts[2]))
            continue
        changed.append(ChangedFile(status=parts[0][0], old_path=None, path=parts[1]))
    return changed


def parse_args() -> tuple[str, str, list[str], bool]:
    parser = argparse.ArgumentParser(description="Enforce CI quality/fragmentation rules for PRs.")
    _ = parser.add_argument("--base", default="", help="Base commit SHA")
    _ = parser.add_argument("--head", default="", help="Head commit SHA")
    _ = parser.add_argument("--files", nargs="*", default=None, help="Optional explicit list of changed files")
    _ = parser.add_argument(
        "--fast", action="store_true", help="Fast local mode (skips expensive whole-repo usage scans)"
    )
    parsed = parser.parse_args()
    base = cast(str, getattr(parsed, "base", ""))
    head = cast(str, getattr(parsed, "head", ""))
    raw_files = cast(list[str] | None, getattr(parsed, "files", None))
    files = [path.strip() for path in (raw_files or []) if path.strip()]
    fast = bool(cast(bool, getattr(parsed, "fast", False)))
    base_ref = base.strip()
    head_ref = head.strip()
    if base_ref and not is_safe_git_ref(base_ref):
        parser.error("Invalid --base git ref format.")
    if head_ref and not is_safe_git_ref(head_ref):
        parser.error("Invalid --head git ref format.")
    return base_ref, head_ref, files, fast


def is_safe_git_ref(value: str) -> bool:
    """Return True when git ref/sha format is safe for subprocess git usage."""
    if not GIT_REF_PATTERN.fullmatch(value):
        return False
    return ".." not in value


def build_context(base: str, head: str, files: list[str] | None = None) -> GuardContext:
    if files:
        changed_files = [ChangedFile(status="M", old_path=None, path=path) for path in files]
    else:
        changed_files = parse_changed_files(base, head)
    changed_code = [changed for changed in changed_files if is_code_file(changed.path)]
    changed_tests = any(
        any(marker in changed.path.lower() for marker in TEST_PATH_MARKERS) for changed in changed_files
    )
    return GuardContext(base, head, changed_files, changed_code, changed_tests)


def _parse_lizard_output(output: str) -> list[LizardFunctionRow]:
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
        return _parse_lizard_output(output)
    except (OSError, UnicodeDecodeError, ValueError):
        return []
    finally:
        Path(temp_path).unlink(missing_ok=True)


def nloc_for_text(path: str, text: str) -> int:
    ext = Path(path).suffix.lower()
    nloc = 0
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ext == ".py" and line.startswith("#"):
            continue
        if ext in {".ts", ".tsx", ".js", ".jsx"} and line.startswith("//"):
            continue
        nloc += 1
    return nloc


def avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def collect_repo_texts(extension: str) -> tuple[list[tuple[str, str]], int]:
    texts: list[tuple[str, str]] = []
    read_errors = 0
    for file_path in REPO_ROOT.rglob(f"*{extension}"):
        if ".git" in file_path.parts or "node_modules" in file_path.parts:
            continue
        try:
            rel = str(file_path.relative_to(REPO_ROOT))
            texts.append((rel, file_path.read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError, ValueError):
            read_errors += 1
            continue
    return texts, read_errors


def check_ai_guardrails(
    ctx: GuardContext, *, fast_mode: bool = False
) -> tuple[list[str], list[str], Mapping[str, object]]:
    failures: list[str] = []
    warnings, python_texts, code_texts = _guardrail_scan_inputs(fast_mode)
    module_exports, new_lengths, tiny_single_use, single_use_small = _scan_changed_files(
        ctx.changed_code, python_texts, code_texts, failures, fast_mode=fast_mode
    )
    new_files_count = sum(1 for changed in ctx.changed_code if changed.status == "A")
    avg_new_file = avg(new_lengths)
    append_rule_b_failure(failures, new_files_count, avg_new_file)
    depth = compute_python_cross_file_depth(REPO_ROOT, [c.path for c in ctx.changed_code if c.path.endswith(".py")])
    append_rule_c_warning(warnings, depth)
    if fast_mode:
        warnings.append("Fast mode: skipped whole-repo single-use analysis for Rule A and Rule E.")

    metrics = {
        "new_files_count": new_files_count,
        "avg_new_file_length": round(avg_new_file, 2),
        "single_use_small_files": single_use_small,
        "single_use_tiny_functions": tiny_single_use,
        "max_cross_file_call_depth": depth,
        "module_public_exports": module_exports,
    }
    return failures, warnings, metrics


def _guardrail_scan_inputs(fast_mode: bool) -> tuple[list[str], list[tuple[str, str]], list[tuple[str, str]]]:
    warnings: list[str] = []
    if fast_mode:
        return warnings, [], []
    python_texts, py_read_errors = collect_repo_texts(".py")
    code_texts, code_read_errors = _collect_code_texts()
    total_read_errors = py_read_errors + code_read_errors
    if total_read_errors:
        warnings.append(f"Repository scan skipped unreadable files: count={total_read_errors}.")
    return warnings, python_texts, code_texts


def _scan_changed_files(
    changed_code: list[ChangedFile],
    python_texts: list[tuple[str, str]],
    code_texts: list[tuple[str, str]],
    failures: list[str],
    *,
    fast_mode: bool = False,
) -> tuple[dict[str, int], list[float], int, int]:
    module_exports: dict[str, int] = {}
    new_lengths: list[float] = []
    tiny_single_use = 0
    single_use_small = 0
    for changed in changed_code:
        path = REPO_ROOT / changed.path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if changed.status == "A":
            if not fast_mode and not _is_test_file_path(changed.path):
                _check_single_use_file(changed.path, text, code_texts, failures)
            new_lengths.append(float(nloc_for_text(changed.path, text)))
            if not fast_mode and not _is_test_file_path(changed.path):
                single_use_small += int(_is_single_use_small_file(changed.path, text, code_texts))
        exports, tiny = _check_exports_and_tiny_functions(
            changed.path,
            text,
            python_texts,
            failures,
            is_new_file=changed.status == "A",
            fast_mode=fast_mode,
        )
        module_exports[changed.path] = exports
        tiny_single_use += tiny
    return module_exports, new_lengths, tiny_single_use, single_use_small


def _collect_code_texts() -> tuple[list[tuple[str, str]], int]:
    items: list[tuple[str, str]] = []
    read_errors = 0
    for extension in CODE_EXTENSIONS:
        ext_items, ext_read_errors = collect_repo_texts(extension)
        items.extend(ext_items)
        read_errors += ext_read_errors
    return items, read_errors


def _check_single_use_file(path: str, text: str, code_texts: list[tuple[str, str]], failures: list[str]) -> None:
    file_nloc = nloc_for_text(path, text)
    imported_by = imported_by_count(path, code_texts)
    if imported_by <= 1 and file_nloc < 100:
        failures.append(f"{path} appears single-use and small ({file_nloc} NLOC, imported_by={imported_by}).")


def _is_single_use_small_file(path: str, text: str, code_texts: list[tuple[str, str]]) -> bool:
    return is_single_use_small_file(path, nloc_for_text(path, text), code_texts)


def _check_exports_and_tiny_functions(
    path: str,
    text: str,
    python_texts: list[tuple[str, str]],
    failures: list[str],
    *,
    is_new_file: bool,
    fast_mode: bool = False,
) -> tuple[int, int]:
    ext = Path(path).suffix.lower()
    is_test_file = _is_test_file_path(path)
    if ext in {".ts", ".tsx", ".js", ".jsx"}:
        count = len(re.findall(r"^\s*export\s+.*\b(function|const|class|type|interface|enum)\b", text, re.MULTILINE))
        if is_new_file and not is_test_file and count > 7 and "group:" not in text.lower():
            failures.append(f"{path} exports {count} public symbols without clear grouping marker.")
        return count, 0
    if ext != ".py":
        return 0, 0
    return _python_export_and_tiny(path, text, python_texts, failures, is_new_file=is_new_file, fast_mode=fast_mode)


def _python_export_and_tiny(
    path: str,
    text: str,
    python_texts: list[tuple[str, str]],
    failures: list[str],
    *,
    is_new_file: bool,
    fast_mode: bool = False,
) -> tuple[int, int]:
    try:
        tree = ast.parse(text)
    except Exception:
        return 0, 0
    public_defs, tiny_violations = _collect_python_public_defs_and_tiny(
        path, tree, text, python_texts, failures, fast_mode=fast_mode
    )
    if is_new_file and not _is_test_file_path(path) and len(public_defs) > 7 and "group:" not in text.lower():
        failures.append(f"{path} exports {len(public_defs)} public functions without clear grouping marker.")
    return len(public_defs), tiny_violations


def _collect_python_public_defs_and_tiny(
    path: str,
    tree: ast.Module,
    text: str,
    python_texts: list[tuple[str, str]],
    failures: list[str],
    *,
    fast_mode: bool = False,
) -> tuple[list[ast.FunctionDef | ast.AsyncFunctionDef], int]:
    public_defs: list[ast.FunctionDef | ast.AsyncFunctionDef] = []
    tiny_violations = 0
    lines = text.splitlines()
    for node in tree.body:
        if not _is_public_function_stmt(node):
            continue
        public_defs.append(node)
        if _is_test_file_path(path):
            continue
        if fast_mode or not _is_tiny_single_use(node, lines, python_texts):
            continue
        tiny_violations += 1
        failures.append(f"{path}:{node.lineno} tiny single-use function '{node.name}' without justification.")
    return public_defs, tiny_violations


def _is_test_file_path(path: str) -> bool:
    normalized = path.replace("\\", "/").lower()
    name = Path(path).name.lower()
    return (
        "/tests/" in normalized
        or "/__tests__/" in normalized
        or name.startswith("test_")
        or name.endswith("_test.py")
        or ".test." in name
        or ".spec." in name
    )


def _is_public_function_stmt(node: ast.stmt) -> TypeGuard[ast.FunctionDef | ast.AsyncFunctionDef]:
    return isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef) and not node.name.startswith("_")


def _is_tiny_single_use(node: ast.AST, lines: list[str], python_texts: list[tuple[str, str]]) -> bool:
    if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
        raise TypeError(f"Expected FunctionDef or AsyncFunctionDef, got {type(node).__name__}")
    nloc = max(1, (node.end_lineno or node.lineno) - node.lineno + 1)
    if nloc >= 5:
        return False
    line = lines[node.lineno - 1] if node.lineno - 1 < len(lines) else ""
    if "lizard: allow" in line:
        return False
    pattern = re.compile(rf"\b{re.escape(node.name)}\s*\(")
    usage = sum(len(pattern.findall(text)) for _, text in python_texts)
    return usage <= 2


def emit_results(summary: dict[str, object], failures: list[str], warnings: list[str]) -> int:
    # Avoid logging full summary payloads to keep potentially sensitive paths/details out of plaintext logs.
    print(f"Quality guard summary: hard_fail_reasons={len(failures)}, warnings={len(warnings)}, metrics={len(summary)}")
    if warnings:
        print("::warning::Quality guard reported warnings. See local run output for details.")
    if failures:
        print("::error::Quality guard reported failures. See local run output for details.")
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
    all_failures = lizard_failures + trend_failures + ai_failures + _file_nloc_failures(ctx, file_nlocs)
    all_warnings = trend_warnings + ai_warnings
    summary = {
        **trend_metrics,
        **ai_metrics,
        "hard_fail_reasons": all_failures,
        "warnings": all_warnings,
    }
    return emit_results(summary, all_failures, all_warnings)


def _file_nloc_failures(ctx: GuardContext, file_nlocs: list[int]) -> list[str]:
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


if __name__ == "__main__":
    raise SystemExit(main())
