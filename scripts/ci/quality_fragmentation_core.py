#!/usr/bin/env python3
"""Shared types and git helpers for quality fragmentation guard."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import cast

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.utils.safe_subprocess import safe_run

REPO_ROOT = Path(__file__).resolve().parents[2]
CODE_EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".jsx"}
TEST_PATH_MARKERS = ("/tests/", "\\tests\\", "test_", "_test.")
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


def run_cmd(command: list[str], *, check: bool = True) -> str:
    if command and command[0] == "git":
        command = [_git_executable(), *command[1:]]
    # UTF-8: Windows text=True defaults to cp1252 and fails on lizard/git bytes (e.g. 0x8f).
    result = safe_run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        cwd=REPO_ROOT,
    )
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
        encoding="utf-8",
        errors="replace",
        check=False,
        cwd=REPO_ROOT,
    )
    return result.stdout if result.returncode == 0 else None


def _git_executable() -> str:
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
