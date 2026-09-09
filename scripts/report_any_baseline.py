#!/usr/bin/env python3
"""Summarise ``.basedpyright/baseline.json`` -- the #784 burn-down chart.

The baseline is the honest debt ledger: every diagnostic recorded here exists in the tree today
and is exempted from the gate until someone fixes it. ``git log .basedpyright/baseline.json``
shows the trend; this script shows where the remaining work actually is.

Four rules are the burn-down commitment. ``reportAny``/``reportExplicitAny`` cover values that
*are* ``Any``; the two parameter rules close the laundering path where deleting an annotation
turns an explicit ``Any`` into an implicit ``Unknown`` and the gate stays green.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

BASELINE_PATH = Path(".basedpyright/baseline.json")

BURN_DOWN_RULES = (
    "reportAny",
    "reportExplicitAny",
    "reportMissingParameterType",
    "reportUnknownParameterType",
)

# How many leading path segments to group by, e.g. "./server/commands/x.py" -> "server/commands".
GROUP_DEPTH = 2
TOP_N = 20


def _load() -> dict[str, list[dict[str, object]]]:
    if not BASELINE_PATH.is_file():
        print(f"No baseline at {BASELINE_PATH}. Run `uv run basedpyright --writebaseline`.", file=sys.stderr)
        raise SystemExit(1)
    raw: object = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        print(f"{BASELINE_PATH}: expected a JSON object at the top level.", file=sys.stderr)
        raise SystemExit(1)
    files: object = raw.get("files", {})
    if not isinstance(files, dict):
        print(f"{BASELINE_PATH}: expected a `files` object.", file=sys.stderr)
        raise SystemExit(1)
    return {str(path): entries for path, entries in files.items() if isinstance(entries, list)}


def _rule_of(entry: dict[str, object]) -> str:
    code = entry.get("code")
    return code if isinstance(code, str) else "<unknown>"


def _group_of(path: str) -> str:
    parts = Path(path.removeprefix("./")).parts
    return "/".join(parts[:GROUP_DEPTH]) if len(parts) > GROUP_DEPTH else str(Path(path.removeprefix("./")).parent)


def main() -> None:
    files = _load()

    total = 0
    by_rule: Counter[str] = Counter()
    by_group: Counter[str] = Counter()
    by_file: Counter[str] = Counter()

    for path, entries in files.items():
        group = _group_of(path)
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            rule = _rule_of(entry)
            total += 1
            by_rule[rule] += 1
            if rule in BURN_DOWN_RULES:
                by_group[group] += 1
                by_file[path.removeprefix("./")] += 1

    burn_down_total = sum(by_rule[rule] for rule in BURN_DOWN_RULES)

    print(f"baselined diagnostics : {total}")
    print(f"burn-down four-rule   : {burn_down_total}")
    print()
    print("--- the four burn-down rules ---")
    for rule in BURN_DOWN_RULES:
        print(f"{by_rule[rule]:7}  {rule}")

    print()
    print(f"--- burn-down findings by directory (depth {GROUP_DEPTH}) ---")
    for group, count in by_group.most_common(TOP_N):
        print(f"{count:7}  {group}")

    print()
    print(f"--- worst {TOP_N} files ---")
    for path, count in by_file.most_common(TOP_N):
        print(f"{count:7}  {path}")

    print()
    print("--- all baselined rules ---")
    for rule, count in by_rule.most_common():
        print(f"{count:7}  {rule}")


if __name__ == "__main__":
    main()
