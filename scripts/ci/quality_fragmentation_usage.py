#!/usr/bin/env python3
"""Import-usage helpers for fragmentation guard."""

from __future__ import annotations

import re
from pathlib import Path


def imported_by_count(target_path: str, code_texts: list[tuple[str, str]]) -> int:
    stem = Path(target_path).stem
    pattern = re.compile(rf"\b{re.escape(stem)}\b")
    return sum(1 for source_path, text in code_texts if source_path != target_path and pattern.search(text))


def is_single_use_small_file(path: str, file_nloc: int, code_texts: list[tuple[str, str]]) -> bool:
    return imported_by_count(path, code_texts) <= 1 and file_nloc < 100
