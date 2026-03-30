#!/usr/bin/env python3
"""Gate coverage artifacts before Codacy upload: minimum aggregate line rates and non-empty reports.

Aligns with .coveragerc fail_under (Python) and client Vitest coverage thresholds (JavaScript).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import cast

from defusedxml import ElementTree as etree

# Defaults match repo policy: pyproject [tool.coverage.report] fail_under = 63;
# client vite.vitestOptions coverage thresholds lines = 70.
DEFAULT_MIN_PYTHON_LINE_RATE = 0.63
DEFAULT_MIN_LCOV_LINE_RATE = 0.70


def cobertura_root_line_rate(coverage_xml: Path) -> float:
    """Return root line-rate from Cobertura XML (0.0--1.0)."""
    if not coverage_xml.is_file():
        msg = f"coverage XML not found: {coverage_xml}"
        raise FileNotFoundError(msg)
    tree = etree.parse(str(coverage_xml))
    root = tree.getroot()
    if root is None:
        msg = "Malformed Cobertura XML: missing root element"
        raise ValueError(msg)
    rate_raw = root.get("line-rate")
    if rate_raw is None:
        msg = "Cobertura XML missing root line-rate attribute"
        raise ValueError(msg)
    return float(rate_raw)


def cobertura_has_server_sources(coverage_xml: Path) -> bool:
    """True if report lists at least one class under server/ (relative paths)."""
    tree = etree.parse(str(coverage_xml))
    root = tree.getroot()
    if root is None:
        return False
    for el in root.iter():
        if el.tag.endswith("class") or el.tag == "class":
            fn = el.get("filename") or ""
            if fn.startswith("server/") or fn.startswith("server\\"):
                return True
    return False


def lcov_aggregate_hits(lcov_path: Path) -> tuple[int, int]:
    """Sum LH (lines hit) and LF (lines found) across all LCOV records."""
    if not lcov_path.is_file():
        msg = f"LCOV file not found: {lcov_path}"
        raise FileNotFoundError(msg)
    text = lcov_path.read_text(encoding="utf-8", errors="replace")
    total_lh = 0
    total_lf = 0
    for line in text.splitlines():
        if line.startswith("LH:"):
            total_lh += int(line.partition(":")[2].strip())
        elif line.startswith("LF:"):
            total_lf += int(line.partition(":")[2].strip())
    return total_lh, total_lf


def validate_python_gate(coverage_xml: Path, min_line_rate: float) -> None:
    """Fail fast if Python Cobertura aggregate or server scope is insufficient."""
    rate = cobertura_root_line_rate(coverage_xml)
    if rate + 1e-9 < min_line_rate:
        msg = (
            f"Python aggregate line coverage {rate:.4f} is below gate {min_line_rate:.4f} "
            f"({coverage_xml})"
        )
        raise ValueError(msg)
    if not cobertura_has_server_sources(coverage_xml):
        msg = f"No server/ classes found in Cobertura report ({coverage_xml}); refusing Codacy upload"
        raise ValueError(msg)
    print(
        f"[PASS] Python Cobertura gate: line-rate={rate:.4f} (min {min_line_rate:.4f}), server/ sources present"
    )


def validate_lcov_gate(lcov_path: Path, min_line_rate: float) -> None:
    """Fail fast if LCOV aggregate line rate is below minimum."""
    lh, lf = lcov_aggregate_hits(lcov_path)
    if lf <= 0:
        msg = f"LCOV has no instrumented lines (LF=0): {lcov_path}"
        raise ValueError(msg)
    rate = lh / lf
    if rate + 1e-9 < min_line_rate:
        msg = (
            f"Client LCOV aggregate line coverage {rate:.4f} is below gate {min_line_rate:.4f} "
            f"({lh}/{lf} lines, {lcov_path})"
        )
        raise ValueError(msg)
    print(
        f"[PASS] Client LCOV gate: line-rate={rate:.4f} (min {min_line_rate:.4f}), lines hit {lh} / found {lf}"
    )


def main() -> None:
    doc = __doc__ or "Codacy coverage gate"
    parser = argparse.ArgumentParser(description=doc.split("\n", maxsplit=1)[0].strip())
    _ = parser.add_argument(
        "--python",
        type=Path,
        metavar="PATH",
        help="Path to coverage.xml (Cobertura)",
    )
    _ = parser.add_argument(
        "--min-python-line-rate",
        type=float,
        default=DEFAULT_MIN_PYTHON_LINE_RATE,
        help=f"Minimum root line-rate for Cobertura (default {DEFAULT_MIN_PYTHON_LINE_RATE})",
    )
    _ = parser.add_argument(
        "--lcov",
        type=Path,
        metavar="PATH",
        help="Path to lcov.info for the client",
    )
    _ = parser.add_argument(
        "--min-lcov-line-rate",
        type=float,
        default=DEFAULT_MIN_LCOV_LINE_RATE,
        help=f"Minimum aggregate LH/LF for LCOV (default {DEFAULT_MIN_LCOV_LINE_RATE})",
    )
    ns = parser.parse_args()
    py_path: Path | None = cast(Path | None, getattr(ns, "python", None))
    min_py: float = cast(float, getattr(ns, "min_python_line_rate", DEFAULT_MIN_PYTHON_LINE_RATE))
    lcov_path: Path | None = cast(Path | None, getattr(ns, "lcov", None))
    min_lcov: float = cast(float, getattr(ns, "min_lcov_line_rate", DEFAULT_MIN_LCOV_LINE_RATE))
    if py_path is None and lcov_path is None:
        parser.error("at least one of --python or --lcov is required")
    if py_path is not None:
        validate_python_gate(py_path.resolve(), min_py)
    if lcov_path is not None:
        validate_lcov_gate(lcov_path.resolve(), min_lcov)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
