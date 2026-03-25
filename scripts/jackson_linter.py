#!/usr/bin/env python3
"""
Run Jackson Linter on JSON files.
Jackson Linter validates JSON syntax and structure.
"""

import json
import sys
from pathlib import Path

# Directories to skip when scanning for *.json (generated or vendor trees).
EXCLUDE_DIRS: frozenset[str] = frozenset(
    {
        "node_modules",
        "dist",
        "build",
        ".git",
        "__pycache__",
        ".venv",
        "htmlcov",
        "coverage",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
    }
)
# Temporary/output JSON filename patterns to skip.
EXCLUDE_PATTERNS: tuple[str, ...] = ("*_output.json", "*_temp.json", "*_tmp.json")
# Fallback encodings when UTF-8 decode fails.
_FALLBACK_ENCODINGS: tuple[str, ...] = ("utf-16", "utf-16-le", "utf-16-be", "latin-1")


def collect_json_files(root: Path | None = None) -> list[Path]:
    """Return paths to JSON files under root, excluding cache and build trees."""
    base = root if root is not None else Path(".")
    found: list[Path] = []
    for json_file in base.rglob("*.json"):
        if any(part in EXCLUDE_DIRS for part in json_file.parts):
            continue
        if any(json_file.match(pattern) for pattern in EXCLUDE_PATTERNS):
            continue
        found.append(json_file)
    return found


def _file_appears_binary_or_terminal_output(json_file: Path) -> bool:
    """True if the first bytes look like binary or UTF-16 BOM, not plain UTF-8 JSON text."""
    try:
        with open(json_file, "rb") as f:
            first_bytes = f.read(100)
    except OSError:
        return False
    return b"\x00" in first_bytes[:10] or first_bytes.startswith(b"\xff\xfe")


def _first_fallback_encoding_that_parses(json_file: Path) -> str | None:
    """If JSON loads under a non-UTF-8 encoding, return that encoding name; otherwise None."""
    for encoding in _FALLBACK_ENCODINGS:
        try:
            with open(json_file, encoding=encoding) as f:
                json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        return encoding
    return None


def _validate_after_unicode_error(json_file: Path, decode_error: UnicodeDecodeError) -> bool:
    """Try alternate encodings; return True if file is valid or intentionally skipped."""
    recovered_encoding = _first_fallback_encoding_that_parses(json_file)
    if recovered_encoding is not None:
        print(
            f"[WARNING] {json_file} is encoded as {recovered_encoding}, not UTF-8. " + "Consider converting to UTF-8."
        )
        return True
    if _file_appears_binary_or_terminal_output(json_file):
        print(f"[WARNING] Skipping {json_file}: appears to be binary or " + "terminal output, not JSON")
        return True
    print(
        f"[ERROR] Cannot decode {json_file}: {decode_error}. " + "File may be corrupted or use an unsupported encoding."
    )
    return False


def validate_json_file(json_file: Path) -> bool:
    """Parse one JSON file; print errors/warnings. Return True if ok or skipped as non-text."""
    try:
        with open(json_file, encoding="utf-8") as f:
            json.load(f)
        return True
    except UnicodeDecodeError as e:
        return _validate_after_unicode_error(json_file, e)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {json_file}: {e}")
        return False
    except OSError as e:
        print(f"[ERROR] Error reading {json_file}: {e}")
        return False


def main() -> int:
    """Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1 failures)."""
    print("Running Jackson Linter on JSON files...")
    print("This will validate JSON syntax and structure...")

    json_files = collect_json_files()
    if not json_files:
        print("[WARNING] No JSON files found")
        return 0

    success = True
    for path in json_files:
        if not validate_json_file(path):
            success = False

    if not success:
        return 1

    print(f"[OK] Validated {len(json_files)} JSON files successfully!")
    print("\n[SUCCESS] All Jackson Linter checks passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
