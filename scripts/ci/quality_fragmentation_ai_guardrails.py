#!/usr/bin/env python3
"""AI guardrail checks for quality fragmentation guard."""

from __future__ import annotations

import ast
import re
import sys
import warnings
from collections.abc import Mapping
from pathlib import Path
from typing import TypeGuard

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.ci.quality_fragmentation_core import (
    CODE_EXTENSIONS,
    REPO_ROOT,
    ChangedFile,
    GuardContext,
    collect_repo_texts,
    nloc_for_text,
)
from scripts.ci.quality_fragmentation_graph import compute_python_cross_file_depth
from scripts.ci.quality_fragmentation_trends import append_rule_b_failure, append_rule_c_warning
from scripts.ci.quality_fragmentation_usage import imported_by_count, is_single_use_small_file


def check_ai_guardrails(
    ctx: GuardContext, *, fast_mode: bool = False
) -> tuple[list[str], list[str], Mapping[str, object]]:
    failures: list[str] = []
    warnings_out, python_texts, code_texts = _guardrail_scan_inputs(fast_mode)
    module_exports, new_lengths, tiny_single_use, single_use_small = scan_changed_files(
        ctx.changed_code, python_texts, code_texts, failures, fast_mode=fast_mode
    )
    new_files_count = sum(1 for changed in ctx.changed_code if changed.status == "A")
    avg_new_file = sum(new_lengths) / len(new_lengths) if new_lengths else 0.0
    append_rule_b_failure(failures, new_files_count, avg_new_file)
    depth = compute_python_cross_file_depth(REPO_ROOT, [c.path for c in ctx.changed_code if c.path.endswith(".py")])
    append_rule_c_warning(warnings_out, depth)
    if fast_mode:
        warnings_out.append("Fast mode: skipped whole-repo single-use analysis for Rule A and Rule E.")

    metrics = {
        "new_files_count": new_files_count,
        "avg_new_file_length": round(avg_new_file, 2),
        "single_use_small_files": single_use_small,
        "single_use_tiny_functions": tiny_single_use,
        "max_cross_file_call_depth": depth,
        "module_public_exports": module_exports,
    }
    return failures, warnings_out, metrics


def _guardrail_scan_inputs(fast_mode: bool) -> tuple[list[str], list[tuple[str, str]], list[tuple[str, str]]]:
    warnings_out: list[str] = []
    if fast_mode:
        return warnings_out, [], []
    python_texts, py_read_errors = collect_repo_texts(".py")
    code_texts, code_read_errors = _collect_code_texts()
    total_read_errors = py_read_errors + code_read_errors
    if total_read_errors:
        warnings_out.append(f"Repository scan skipped unreadable files: count={total_read_errors}.")
    return warnings_out, python_texts, code_texts


def scan_changed_files(
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
    call_usage_map = _build_python_call_usage_map(python_texts) if not fast_mode else {}
    for changed in changed_code:
        path = REPO_ROOT / changed.path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if changed.status == "A":
            single_use_small += _process_added_file_checks(
                changed.path, text, code_texts, failures, new_lengths, fast_mode
            )
        exports, tiny = _check_exports_and_tiny_functions(
            changed.path,
            text,
            call_usage_map,
            failures,
            is_new_file=changed.status == "A",
            fast_mode=fast_mode,
        )
        module_exports[changed.path] = exports
        tiny_single_use += tiny
    return module_exports, new_lengths, tiny_single_use, single_use_small


def _process_added_file_checks(
    changed_path: str,
    text: str,
    code_texts: list[tuple[str, str]],
    failures: list[str],
    new_lengths: list[float],
    fast_mode: bool,
) -> int:
    is_test = _is_test_file_path(changed_path)
    if not fast_mode and not is_test:
        _check_single_use_file(changed_path, text, code_texts, failures)
    new_lengths.append(float(nloc_for_text(changed_path, text)))
    if fast_mode or is_test:
        return 0
    return int(_is_single_use_small_file(changed_path, text, code_texts))


def _collect_code_texts() -> tuple[list[tuple[str, str]], int]:
    items: list[tuple[str, str]] = []
    read_errors = 0
    for extension in CODE_EXTENSIONS:
        ext_items, ext_read_errors = collect_repo_texts(extension)
        items.extend(ext_items)
        read_errors += ext_read_errors
    return items, read_errors


def _check_single_use_file(path: str, text: str, code_texts: list[tuple[str, str]], failures: list[str]) -> None:
    if "group:" in text.lower():
        return
    file_nloc = nloc_for_text(path, text)
    imported_by = imported_by_count(path, code_texts)
    if imported_by <= 1 and file_nloc < 100:
        failures.append(f"{path} appears single-use and small ({file_nloc} NLOC, imported_by={imported_by}).")


def _is_single_use_small_file(path: str, text: str, code_texts: list[tuple[str, str]]) -> bool:
    return is_single_use_small_file(path, nloc_for_text(path, text), code_texts)


def _check_exports_and_tiny_functions(
    path: str,
    text: str,
    call_usage_map: dict[str, int],
    failures: list[str],
    *,
    is_new_file: bool,
    fast_mode: bool = False,
) -> tuple[int, int]:
    ext = Path(path).suffix.lower()
    is_test_file = _is_test_file_path(path)
    has_group_marker = "group:" in text.lower()
    if ext in {".ts", ".tsx", ".js", ".jsx"}:
        count = len(re.findall(r"^\s*export\s+.*\b(function|const|class|type|interface|enum)\b", text, re.MULTILINE))
        if is_new_file and not is_test_file and count > 7 and not has_group_marker:
            failures.append(f"{path} exports {count} public symbols without clear grouping marker.")
        return count, 0
    if ext != ".py":
        return 0, 0
    return _python_export_and_tiny(
        path,
        text,
        call_usage_map,
        failures,
        is_new_file=is_new_file,
        has_group_marker=has_group_marker,
        fast_mode=fast_mode,
    )


def _python_export_and_tiny(
    path: str,
    text: str,
    call_usage_map: dict[str, int],
    failures: list[str],
    *,
    is_new_file: bool,
    has_group_marker: bool,
    fast_mode: bool = False,
) -> tuple[int, int]:
    try:
        tree = ast.parse(text)
    except Exception:
        return 0, 0
    public_defs, tiny_violations = _collect_python_public_defs_and_tiny(
        path,
        tree,
        text,
        call_usage_map,
        failures,
        has_group_marker=has_group_marker,
        fast_mode=fast_mode,
    )
    if is_new_file and not _is_test_file_path(path) and len(public_defs) > 7 and not has_group_marker:
        failures.append(f"{path} exports {len(public_defs)} public functions without clear grouping marker.")
    return len(public_defs), tiny_violations


def _collect_python_public_defs_and_tiny(
    path: str,
    tree: ast.Module,
    text: str,
    call_usage_map: dict[str, int],
    failures: list[str],
    *,
    has_group_marker: bool = False,
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
        if has_group_marker:
            continue
        if fast_mode or not _is_tiny_single_use(node, lines, call_usage_map):
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


def _build_python_call_usage_map(python_texts: list[tuple[str, str]]) -> dict[str, int]:
    """Build a repo-wide call usage map from Python AST call sites."""
    usage: dict[str, int] = {}
    for path, text in python_texts:
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=SyntaxWarning)
                tree = ast.parse(text, filename=path)
        except (SyntaxError, ValueError, TypeError):
            continue
        for node in (n for n in ast.walk(tree) if isinstance(n, ast.Call)):
            call_name = _call_target_name(node)
            if call_name is None:
                continue
            usage[call_name] = usage.get(call_name, 0) + 1
    return usage


def _call_target_name(call_node: ast.Call) -> str | None:
    callee = call_node.func
    if isinstance(callee, ast.Name):
        return callee.id
    if isinstance(callee, ast.Attribute):
        return callee.attr
    return None


def _is_tiny_single_use(node: ast.AST, lines: list[str], call_usage_map: dict[str, int]) -> bool:
    if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
        raise TypeError(f"Expected FunctionDef or AsyncFunctionDef, got {type(node).__name__}")
    nloc = max(1, (node.end_lineno or node.lineno) - node.lineno + 1)
    if nloc >= 5:
        return False
    line = lines[node.lineno - 1] if node.lineno - 1 < len(lines) else ""
    if "lizard: allow" in line:
        return False
    usage = call_usage_map.get(node.name, 0)
    return usage == 1
