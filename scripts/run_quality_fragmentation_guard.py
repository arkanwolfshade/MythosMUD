#!/usr/bin/env python3
"""
Run quality fragmentation guard with local git SHA detection.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.utils.safe_subprocess import safe_run

REPO_ROOT = Path(__file__).resolve().parents[1]
# Windows CreateProcess limit is ~32k chars; stay well under.
_WIN_CMDLINE_SOFT_LIMIT = 24_000


def _git_executable() -> str:
    # Use command name with safe_run so PATH resolution is handled by the OS.
    # Absolute paths outside repo root are intentionally rejected by safe_subprocess validation.
    return "git"


def _run_git(args: list[str]) -> str | None:
    git_path = _git_executable()
    result = safe_run(
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
    result = safe_run(
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
        result = safe_run(
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


def _is_graphify_path(path: str) -> bool:
    """Generated graphify trees are not product code; skip guard/lint argv bloat."""
    normalized = path.replace("\\", "/")
    return (
        normalized.startswith("graphify-out/")
        or "/graphify-out/" in f"/{normalized}"
        or "/graphify/" in f"/{normalized}"
    )


def _resolved_changed_files(cli_files: list[str], base_sha: str, head_sha: str) -> list[str]:
    if cli_files:
        candidates = cli_files
    else:
        local = _local_changed_files()
        candidates = local if local else _changed_files_between(base_sha, head_sha)
    return [path for path in candidates if not _is_graphify_path(path)]


def _argv_char_len(args: list[str]) -> int:
    return sum(len(arg) + 1 for arg in args)


def _build_guard_command(base_sha: str, head_sha: str, changed_files: list[str]) -> tuple[list[str], Path | None]:
    command = [
        # Use PATH resolution so safe_subprocess validation accepts the executable.
        # pre-commit often supplies an interpreter path outside repo root.
        "python",
        "scripts/ci/quality_fragmentation_guard.py",
        "--base",
        base_sha,
        "--head",
        head_sha,
    ]
    with_files = [*command, "--files", *changed_files]
    if _argv_char_len(with_files) <= _WIN_CMDLINE_SOFT_LIMIT:
        return with_files, None

    # Large local dirty trees (e.g. graphify-out) blow Windows CreateProcess (WinError 206).
    # ponytail: tempfile list; stream stdin if we ever need zero disk I/O.
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".txt",
        prefix="qfg-files-",
        dir=REPO_ROOT,
        delete=False,
    )
    with handle as tmp:
        tmp.write("\n".join(changed_files))
        tmp.write("\n")
        list_path = Path(tmp.name)
    return [*command, "--files-from", str(list_path)], list_path


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

    command, list_path = _build_guard_command(base_sha, head_sha, changed_files)
    try:
        result = safe_run(command, cwd=REPO_ROOT, check=False)
        return result.returncode
    finally:
        if list_path is not None:
            list_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
