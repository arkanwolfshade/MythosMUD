#!/usr/bin/env python3
"""
HADS Validator - Human-AI Document Standard v1.0.0
Vendored from https://github.com/catcam/hads (validate.py).

Pinned source commit: dcfe582df90c8a276690fd05ebe4819d4ba12c36

Usage:
    python scripts/hads/validate.py <file.md>
    python scripts/hads/validate.py <file.md> --verbose
    python scripts/hads/validate.py --manifest docs/hads.manifest

Exit codes:
    0 - valid HADS document (all files when using --manifest)
    1 - missing required element (title, version, manifest)
    2 - malformed block tag
    3 - [BUG] block missing required fields
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import TypedDict

# -- Constants ------------------------------------------------------------------

VALID_TAGS = {"[SPEC]", "[NOTE]", "[BUG]", "[?]"}
BLOCK_TAG_PATTERN: re.Pattern[str] = re.compile(r"^\*\*(\[(?:SPEC|NOTE|BUG|\?)\])\*\*$")
LOOSE_TAG_PATTERN: re.Pattern[str] = re.compile(r"\[(?:SPEC|NOTE|BUG|\?)\]")
VERSION_PATTERN: re.Pattern[str] = re.compile(r"\*\*Version\s+\d+\.\d+\.\d+\*\*")
MANIFEST_KEYWORDS: list[str] = ["[SPEC]", "[BUG]", "reading instruction", "ai reading"]


class BugBlock(TypedDict):
    line: int
    content: list[str]


# -- Helpers --------------------------------------------------------------------


def load(path: str) -> list[str]:
    try:
        return Path(path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"ERROR: File is not valid UTF-8: {path}")
        sys.exit(1)


def find_h1(lines: list[str]) -> int | None:
    """Return line index of first H1, or None."""
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            return i
    return None


def find_version(lines: list[str]) -> int | None:
    """Return line index of version declaration, or None."""
    for i, line in enumerate(lines[:20]):  # version should be near top
        if VERSION_PATTERN.search(line):
            return i
    return None


def find_manifest(lines: list[str]) -> int | None:
    """Return line index where AI manifest starts, or None."""
    for i, line in enumerate(lines):
        lower = line.lower()
        if any(kw in lower for kw in MANIFEST_KEYWORDS):
            return i
    return None


def find_first_content_section(lines: list[str]) -> int | None:
    """Return line index of first H2 that is NOT the manifest."""
    in_manifest = False
    for i, line in enumerate(lines):
        if line.startswith("## "):
            lower = line.lower()
            if "ai reading" in lower or "reading instruction" in lower:
                in_manifest = True
                continue
            if in_manifest:
                in_manifest = False
            return i
    return None


def find_bug_blocks(lines: list[str]) -> list[BugBlock]:
    """Return list of BUG blocks with their content."""
    bugs: list[BugBlock] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = BLOCK_TAG_PATTERN.match(line)
        if m and m.group(1) == "[BUG]":
            block: BugBlock = {"line": i + 1, "content": []}
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if BLOCK_TAG_PATTERN.match(next_line) or next_line.startswith("## ") or next_line.startswith("### "):
                    break
                block["content"].append(lines[j])
                j += 1
            bugs.append(block)
            i = j
        else:
            i += 1
    return bugs


def check_loose_tags(lines: list[str]) -> list[tuple[int, str]]:
    """Find tag-like patterns that are not properly formatted."""
    issues: list[tuple[int, str]] = []
    in_fence = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if BLOCK_TAG_PATTERN.match(stripped):
            continue
        stripped_check = stripped.lstrip("*").strip()
        matches: list[str] = LOOSE_TAG_PATTERN.findall(stripped_check)
        for match in matches:
            if "`" + match + "`" in line:
                continue
            if not stripped_check.startswith(match):
                continue
            if stripped.startswith("**" + match):
                continue
            issues.append((i + 1, f"Possible unformatted tag '{match}' - should be **{match}**"))
    return issues


def check_bug_content(bug: BugBlock) -> list[str]:
    """Check that a [BUG] block contains required fields."""
    content = " ".join(bug["content"]).lower()
    missing: list[str] = []
    if "symptom" not in content and "symptom:" not in content:
        missing.append("symptom")
    if "fix" not in content:
        missing.append("fix")
    return missing


# -- Main validation ------------------------------------------------------------


def _check_required_structure(lines: list[str], errors: list[str], passed: list[str]) -> None:
    """Validate H1, version, and AI manifest placement."""
    h1_line = find_h1(lines)
    if h1_line is None:
        errors.append("MISSING H1 title - document must begin with a '# Title' heading")
    else:
        passed.append(f"H1 title found (line {h1_line + 1}): {lines[h1_line][:60]}")

    ver_line = find_version(lines)
    if ver_line is None:
        errors.append("MISSING version - add '**Version X.Y.Z**' near the top of the document")
    else:
        passed.append(f"Version found (line {ver_line + 1}): {lines[ver_line].strip()[:60]}")

    manifest_line = find_manifest(lines)
    if manifest_line is None:
        errors.append("MISSING AI manifest - add an 'AI READING INSTRUCTION' section before content")
        return
    passed.append(f"AI manifest found (line {manifest_line + 1})")
    content_line = find_first_content_section(lines)
    if content_line is not None and manifest_line > content_line:
        errors.append(
            f"AI manifest (line {manifest_line + 1}) appears AFTER first content section "
            + f"(line {content_line + 1}) - manifest must come first"
        )


def _check_bugs(lines: list[str], errors: list[str], passed: list[str]) -> None:
    """Validate [BUG] blocks have required fields."""
    for bug in find_bug_blocks(lines):
        missing = check_bug_content(bug)
        if missing:
            errors.append(f"[BUG] block at line {bug['line']} is missing required field(s): " + ", ".join(missing))
        else:
            passed.append(f"[BUG] block at line {bug['line']} - OK")


def _print_validation_report(
    path: str,
    errors: list[str],
    warnings: list[str],
    passed: list[str],
    verbose: bool,
) -> None:
    """Print HADS validation results to stdout."""
    print(f"\nHADS Validator - {path}")
    print("-" * 60)

    if verbose and passed:
        print("\nPassed checks:")
        for p in passed:
            print(f"  {p}")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  {w}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
        print(f"\nResult: INVALID ({len(errors)} error(s))\n")
        return

    print("\nResult: VALID HADS document")
    if warnings:
        print(f"        {len(warnings)} warning(s) - review recommended")
    print()


def _exit_code_for_errors(errors: list[str]) -> int:
    """Map first error message to HADS exit code."""
    if not errors:
        return 0
    first = errors[0]
    if "MISSING" in first:
        return 1
    if "unformatted tag" in first or "nesting" in first:
        return 2
    if "[BUG]" in first:
        return 3
    return 1


def validate(path: str, verbose: bool = False) -> int:
    lines = load(path)
    errors: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    _check_required_structure(lines, errors, passed)
    _check_bugs(lines, errors, passed)
    warnings.extend(f"Line {line_num}: {msg}" for line_num, msg in check_loose_tags(lines))
    _print_validation_report(path, errors, warnings, passed, verbose)
    return _exit_code_for_errors(errors)


def parse_manifest(manifest_path: Path) -> list[Path]:
    """Return non-comment, non-empty paths from a HADS manifest file."""
    root = Path.cwd()
    paths: list[Path] = []
    for raw in manifest_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        paths.append((root / line).resolve())
    return paths


def validate_manifest(manifest_path: Path, verbose: bool = False) -> int:
    if not manifest_path.is_file():
        print(f"ERROR: Manifest not found: {manifest_path}")
        return 1
    paths = parse_manifest(manifest_path)
    if not paths:
        print(f"HADS Validator - manifest {manifest_path} has no active paths (OK)")
        return 0
    worst = 0
    failures = 0
    for path in paths:
        if not path.is_file():
            print(f"\nERROR: Manifest path missing: {path}")
            failures += 1
            worst = max(worst, 1)
            continue
        code = validate(str(path), verbose=verbose)
        if code != 0:
            failures += 1
            worst = max(worst, code)
    print(f"\nManifest summary: {len(paths)} path(s), {failures} failure(s)")
    return worst


# -- Entry point ----------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    args = [a for a in sys.argv[1:] if a not in ("--verbose", "-v")]

    if not args:
        print(__doc__)
        sys.exit(0)

    if args[0] == "--manifest":
        if len(args) < 2:
            print("ERROR: --manifest requires a path")
            sys.exit(1)
        sys.exit(validate_manifest(Path(args[1]), verbose=verbose))

    sys.exit(validate(args[0], verbose=verbose))
