#!/usr/bin/env python3
"""
Verify canonical E2E users exist in mythos_e2e before Playwright login checks.

Exits 0 when ArkanWolfshade and Ithaqua are present; exits 1 with stderr detail otherwise.
Uses DATABASE_URL and POSTGRES_SEARCH_PATH from the environment (same as seed_e2e_users.py).
"""

from __future__ import annotations

import os
import sys

import asyncpg
from anyio import run

_REQUIRED_USERNAMES = ("ArkanWolfshade", "Ithaqua")


async def _verify() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")
    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"

    conn = await asyncpg.connect(url, server_settings={"search_path": search_path})
    try:
        missing: list[str] = []
        for username in _REQUIRED_USERNAMES:
            row = await conn.fetchrow(
                "SELECT id, is_active FROM users WHERE LOWER(username) = LOWER($1)",
                username,
            )
            if not row:
                missing.append(username)
                continue
            if not row["is_active"]:
                print(f"[ERROR] User {username} exists but is_active=false", file=sys.stderr)
                sys.exit(1)
        if missing:
            print(
                f"[ERROR] Missing E2E users in schema {search_path}: {', '.join(missing)}. "
                "Run: uv run python scripts/seed_e2e_users.py (with .env.e2e_test loaded).",
                file=sys.stderr,
            )
            sys.exit(1)
    finally:
        await conn.close()


def main() -> None:
    """Entry point."""
    run(_verify)


if __name__ == "__main__":
    main()
