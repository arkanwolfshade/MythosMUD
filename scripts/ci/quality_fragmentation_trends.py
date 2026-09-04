#!/usr/bin/env python3
"""Trend helpers for quality fragmentation guard."""

from __future__ import annotations

from collections.abc import Callable


def added_file_stats(
    changed_code_statuses: list[str], base_files: list[str], is_code_file: Callable[[str], bool]
) -> tuple[int, float]:
    base_code_count = sum(1 for path in base_files if is_code_file(path))
    files_added = sum(1 for status in changed_code_statuses if status == "A")
    files_added_pct = (files_added / base_code_count * 100.0) if base_code_count else 0.0
    return files_added, files_added_pct


def trend_averages(
    base_lengths: list[float], head_lengths: list[float], file_nlocs: list[int]
) -> tuple[float, float, float]:
    avg_base = _avg(base_lengths)
    avg_head = _avg(head_lengths)
    avg_file = _avg([float(value) for value in file_nlocs])
    return avg_base, avg_head, avg_file


def append_fragmentation_failures(
    failures: list[str],
    files_added_pct: float,
    avg_base_fn: float,
    avg_head_fn: float,
) -> None:
    if files_added_pct <= 20.0:
        return
    if avg_head_fn >= avg_base_fn:
        return
    message = (
        f"Over-fragmentation signal: files_added_pct={files_added_pct:.2f}% and "
        f"avg_function_length decreased ({avg_base_fn:.2f} -> {avg_head_fn:.2f})."
    )
    failures.append(message)


def append_fragmentation_warnings(
    warnings: list[str],
    files_added: int,
    avg_base_fn: float,
    avg_head_fn: float,
    avg_file_nloc: float,
    nloc_max: int,
) -> None:
    if files_added <= 0:
        return
    if avg_base_fn <= 0:
        return
    if avg_head_fn >= avg_base_fn:
        return
    if avg_file_nloc >= nloc_max:
        return
    warnings.append("Fragmentation smell: files added while function and file lengths trended down.")


def append_rule_b_failure(failures: list[str], new_files_count: int, avg_new_file: float) -> None:
    if new_files_count > 10 and avg_new_file < 50:
        failures.append(f"Rule B violation: new_files={new_files_count}, avg_new_file_length={avg_new_file:.2f} (<50).")


def append_rule_c_warning(warnings: list[str], depth: int) -> None:
    if depth > 5:
        warnings.append(f"Rule C warning: estimated cross-file call depth is {depth} (>5).")


def _avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
