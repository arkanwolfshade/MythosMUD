#!/usr/bin/env python3
"""Run Make stages sequentially; fail loudly and stop on the first bad stage.

Used by composite Makefile targets (all, codacy-tools, test, test-coverage).
Fail conditions: non-zero exit, or a Python traceback/callstack in stage output.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BANNER = "=" * 72
TRACEBACK_MARKER = "Traceback (most recent call last):"


def keep_going_requested(makeflags: str | None = None) -> bool:
    """Return True when Make was invoked with -k / --keep-going."""
    flags = makeflags if makeflags is not None else os.environ.get("MAKEFLAGS", "")
    if not flags.strip():
        return False
    if "--keep-going" in flags:
        return True
    # GNU Make packs single-letter options in the first MAKEFLAGS word (e.g. "kw").
    first = flags.split(None, 1)[0]
    if first.startswith("-"):
        return "-k" in flags.split()
    return "k" in first


def stage_failed_from_output(output: str, returncode: int) -> str | None:
    """Return a short failure reason, or None if the stage is OK."""
    if returncode != 0:
        return f"non-zero exit ({returncode})"
    if TRACEBACK_MARKER in output:
        return "traceback/callstack detected in output"
    return None


def _print_fail(stage: str, reason: str, remaining: list[str], exit_code: int | None) -> None:
    print(BANNER, file=sys.stderr)
    print(f"FAIL-FAST: stage '{stage}' failed - {reason}", file=sys.stderr)
    if exit_code is not None:
        print(f"exit code: {exit_code}", file=sys.stderr)
    if remaining:
        print(f"skipped stages: {' '.join(remaining)}", file=sys.stderr)
    else:
        print("skipped stages: (none)", file=sys.stderr)
    print(BANNER, file=sys.stderr)


def run_stage(make_cmd: str, stage: str) -> tuple[int, str]:
    """Run `make <stage>`, stream output, return (exit_code, captured_output)."""
    # Trust MAKE / --make from the parent Makefile; do not shell=True.
    proc = subprocess.Popen(
        [make_cmd, stage],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    chunks: list[str] = []
    assert proc.stdout is not None
    for line in proc.stdout:
        sys.stdout.write(line)
        sys.stdout.flush()
        chunks.append(line)
    code = proc.wait()
    return code, "".join(chunks)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--make",
        default=os.environ.get("MAKE") or "make",
        help="Make executable (default: $MAKE or 'make')",
    )
    parser.add_argument("stages", nargs="+", help="Make targets to run in order")
    args = parser.parse_args(argv)

    if keep_going_requested():
        print(
            f"{BANNER}\nFAIL-FAST: refuse make -k / --keep-going for multi-stage runs\n{BANNER}",
            file=sys.stderr,
        )
        return 2

    stages: list[str] = args.stages
    for index, stage in enumerate(stages):
        print(BANNER)
        print(f"STAGE [{index + 1}/{len(stages)}]: {stage}")
        print(BANNER)
        code, output = run_stage(args.make, stage)
        reason = stage_failed_from_output(output, code)
        if reason is not None:
            _print_fail(stage, reason, stages[index + 1 :], code)
            return code if code > 0 else 1

    print(BANNER)
    print(f"OK: all {len(stages)} stages passed")
    print(BANNER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
