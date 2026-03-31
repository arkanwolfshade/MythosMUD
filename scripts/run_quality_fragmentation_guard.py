#!/usr/bin/env python3
"""
Run quality fragmentation guard with local git SHA detection.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _git_executable() -> str:
    return shutil.which("git") or "git"


def _run_git(args: list[str]) -> str | None:
    git_path = _git_executable()
    # nosec B603: args are fixed git subcommands composed by this script.
    result = subprocess.run(
        [git_path, *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def _resolve_base_sha() -> str | None:
    return _run_git(["merge-base", "origin/main", "HEAD"]) or _run_git(["rev-parse", "HEAD~1"])


def _changed_files_between(base_sha: str, head_sha: str) -> list[str]:
    git_path = _git_executable()
    # nosec B603: git ref inputs are resolved from local git commands in this module.
    result = subprocess.run(
        [git_path, "diff", "--name-only", f"{base_sha}...{head_sha}"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def _local_changed_files() -> list[str]:
    changed: set[str] = set()
    git_path = _git_executable()
    for args in (["diff", "--name-only", "--cached"], ["diff", "--name-only", "HEAD"]):
        # nosec B603: args are fixed and not user-provided.
        result = subprocess.run(
            [git_path, *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            continue
        for line in result.stdout.splitlines():
            path = line.strip()
            if path:
                changed.add(path)
    return sorted(changed)


def _resolved_changed_files(cli_files: list[str], base_sha: str, head_sha: str) -> list[str]:
    if cli_files:
        return cli_files
    local = _local_changed_files()
    if local:
        return local
    return _changed_files_between(base_sha, head_sha)


def _build_guard_command(base_sha: str, head_sha: str, changed_files: list[str]) -> list[str]:
    command = [
        sys.executable,
        "scripts/ci/quality_fragmentation_guard.py",
        "--base",
        base_sha,
        "--head",
        head_sha,
    ]
    command.extend(["--files", *changed_files])
    command.append("--fast")
    return command


def main() -> int:
    cli_files = [path for path in sys.argv[1:] if path and not path.startswith("-")]
    base_sha = _resolve_base_sha()
    head_sha = _run_git(["rev-parse", "HEAD"])

    if not base_sha or not head_sha:
        print("Skipping quality fragmentation guard: unable to determine git base/head.")
        return 0

    changed_files = _resolved_changed_files(cli_files, base_sha, head_sha)

    if not changed_files:
        print("No changed files detected for quality fragmentation guard; skipping.")
        return 0

    command = _build_guard_command(base_sha, head_sha, changed_files)
    # nosec B603: command uses sys.executable and a repository-local script path.
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
