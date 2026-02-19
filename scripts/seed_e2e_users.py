#!/usr/bin/env python3
"""
Seed the TestAdmin E2E auth user so character-creation E2E tests can log in.

Creates TestAdmin in the `users` table with password Cthulhu1 (Argon2-hashed) if missing.
Does NOT create or modify ArkanWolfshade or Ithaqua (canonical accounts must exist separately).
Safe to run multiple times: skips if TestAdmin already exists.
Use the same DATABASE_URL as the server for E2E (e.g. from .env.e2e_test or default mythos_e2e).

Run from project root: uv run python scripts/seed_e2e_users.py
"""

import os
import sys
import uuid
from datetime import UTC, datetime

from anyio import run

# Project root is parent of scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# Only TestAdmin: used by character-creation E2E tests. ArkanWolfshade and Ithaqua are NOT created here.
E2E_USERS = [
    ("TestAdmin", True, True),  # Superuser, for character-creation E2E only
]
E2E_PASSWORD = "Cthulhu1"


async def _seed_e2e_users() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    import asyncpg

    from server.auth.argon2_utils import hash_password

    hashed = hash_password(E2E_PASSWORD)
    now = datetime.now(UTC).replace(tzinfo=None)

    conn = await asyncpg.connect(url)
    try:
        for username, is_superuser, is_admin in E2E_USERS:
            existing = await conn.fetchrow("SELECT id FROM users WHERE LOWER(username) = LOWER($1)", username)
            if existing:
                continue
            user_id = uuid.uuid4()
            email = f"{username}@wolfshade.org"
            await conn.execute(
                """
                INSERT INTO users (
                    id, email, hashed_password, username, display_name,
                    is_active, is_superuser, is_verified, is_admin,
                    created_at, updated_at
                ) VALUES ($1, $2, $3, $4, $5, true, $6, true, $7, $8, $8)
                """,
                user_id,
                email,
                hashed,
                username,
                username,
                is_superuser,
                is_admin,
                now,
            )
            print(f"Created user: {username}")
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run E2E user seed via anyio."""
    run(_seed_e2e_users)


if __name__ == "__main__":
    main()
