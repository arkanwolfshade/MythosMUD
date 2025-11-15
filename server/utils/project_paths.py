"""Project path resolution helpers used across runtime code and tooling."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

_ENVIRONMENT_ALIASES = {
    "production": "local",
}


@lru_cache(maxsize=1)
def get_project_root() -> Path:
    """Return the repository root (directory containing pyproject.toml)."""

    current = Path(__file__).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists():
            return candidate
    # Fallback: assume we're two levels under the repo root (server/utils/)
    return current.parent.parent


def normalize_environment(environment: str | None) -> str:
    """Normalize logging environment names to their canonical directory names."""

    env = (environment or os.getenv("LOGGING_ENVIRONMENT") or "local").strip().lower()
    if not env:
        env = "local"
    return _ENVIRONMENT_ALIASES.get(env, env)


def get_environment_data_dir(environment: str | None = None) -> Path:
    """Compute the base data directory for the provided environment."""

    env = normalize_environment(environment)
    return get_project_root() / "data" / env


def get_calendar_paths_for_environment(environment: str | None = None) -> tuple[Path, Path]:
    """Return (holidays_file, schedules_dir) for the requested environment."""

    data_dir = get_environment_data_dir(environment) / "calendar"
    holidays_file = data_dir / "holidays.json"
    schedules_dir = data_dir / "schedules"
    return holidays_file, schedules_dir
