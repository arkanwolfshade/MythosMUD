#!/usr/bin/env python3
"""
Seed canonical E2E auth users and player rows for a fresh mythos_e2e database.

Creates if missing:
  - ArkanWolfshade / Cthulhu1 (user is_admin, character is_admin for /commands)
  - Ithaqua / Cthulhu1 (regular user and character)

Both seeded characters use DEFAULT_RESPAWN_ROOM (server.constants.spawn_defaults) for placement.

Player rows use CALL upsert_player (db/procedures/players.sql) so player_inventories stays consistent.

Safe to run multiple times: skips existing users by username; skips player if character name exists.

Run from project root: uv run python scripts/seed_e2e_users.py
Use the same DATABASE_URL and POSTGRES_SEARCH_PATH as the E2E server (e.g. .env.e2e_test).
"""

from __future__ import annotations

import json
import os
import sys
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast

import asyncpg
from anyio import run

# pyright: reportUnnecessaryTypeIgnoreComment=false
# Reason: reportMissingImports ignores below help editors whose workspace root is not this repo.  # noqa: I001

# Project root is parent of scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# First-party imports follow sys.path above. Per-line pyright: ignore[reportMissingImports] if workspace root
# is not this repo (runtime still resolves). noqa: E402, I001 for import order after path setup.
from server.auth.argon2_utils import hash_password as _hash_password_impl  # noqa: E402, I001  # pylint: disable=wrong-import-position  # pyright: ignore[reportMissingImports, reportUnknownVariableType]
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM as _default_respawn_room  # noqa: E402, I001  # pylint: disable=wrong-import-position  # pyright: ignore[reportMissingImports, reportUnknownVariableType]

# Strict Pyright may still infer Unknown for symbols imported here; cast to the real types.
hash_password: Callable[[str], str] = cast(Callable[[str], str], _hash_password_impl)
# Reason: import may be Unknown in some roots; cast pins str. Ignore if checker already knows str (redundant cast).
DEFAULT_RESPAWN_ROOM: str = cast(str, _default_respawn_room)  # pyright: ignore[reportUnnecessaryCast]

E2E_PASSWORD = "Cthulhu1"

# Stats aligned with mythos_e2e players.stats default + fields used by gameplay/teardown.
DEFAULT_STATS: dict[str, int | str] = {
    "strength": 50,
    "dexterity": 50,
    "constitution": 50,
    "size": 50,
    "intelligence": 50,
    "power": 50,
    "education": 50,
    "charisma": 50,
    "luck": 50,
    "lucidity": 100,
    "occult": 0,
    "corruption": 0,
    "current_dp": 20,
    "max_dp": 20,
    "magic_points": 10,
    "max_magic_points": 10,
    "max_lucidity": 100,
    "position": "standing",
}


@dataclass(frozen=True)
class E2eUserSpec:
    """One row in users plus optional default character for login E2E."""

    username: str
    email: str
    is_superuser: bool
    is_admin: bool
    seed_player: bool
    player_is_admin: int


E2E_USER_SPECS: tuple[E2eUserSpec, ...] = (
    E2eUserSpec(
        username="ArkanWolfshade",
        email="arkanwolfshade@test.local",
        is_superuser=False,
        is_admin=True,
        seed_player=True,
        player_is_admin=1,
    ),
    E2eUserSpec(
        username="Ithaqua",
        email="ithaqua@test.local",
        is_superuser=False,
        is_admin=False,
        seed_player=True,
        player_is_admin=0,
    ),
)

UPSERT_PLAYER_SQL = """
CALL upsert_player(
    $1::uuid, $2::uuid, $3::varchar(50), $4::text, $5::text,
    $6::varchar(255), $7::varchar(100), $8::int, $9::int, $10::int,
    $11::bigint, $12::timestamptz, $13::timestamptz, $14::jsonb,
    $15::boolean, $16::timestamptz, $17::varchar(255), $18::text, $19::text
)
"""


async def _ensure_player_for_user(
    conn: asyncpg.Connection,
    *,
    user_id: uuid.UUID,
    character_name: str,
    player_is_admin: int,
    now: datetime,
) -> None:
    existing_char = await conn.fetchrow("SELECT player_id FROM players WHERE name = $1", character_name)
    if existing_char:
        return

    player_id = uuid.uuid4()
    stats_json = json.dumps(DEFAULT_STATS)
    _ = await conn.execute(
        UPSERT_PLAYER_SQL,
        player_id,
        user_id,
        character_name,
        "[]",
        "[]",
        DEFAULT_RESPAWN_ROOM,
        DEFAULT_RESPAWN_ROOM,
        0,
        1,
        player_is_admin,
        None,
        now,
        now,
        stats_json,
        False,
        None,
        None,
        "[]",
        "{}",
    )
    print(f"Created player character: {character_name} (user {user_id})")


async def _seed_e2e_users() -> None:
    database_url = os.environ.get("DATABASE_URL", "").strip()
    if not database_url:
        database_url = "postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e"
    url = database_url.replace("postgresql+asyncpg://", "postgresql://")

    search_path = os.environ.get("POSTGRES_SEARCH_PATH", "").strip() or "mythos_e2e"
    server_settings: dict[str, str] = {"search_path": search_path}

    hashed = hash_password(E2E_PASSWORD)
    now = datetime.now(UTC)

    conn = await asyncpg.connect(url, server_settings=server_settings)
    try:
        for spec in E2E_USER_SPECS:
            row = await conn.fetchrow(
                "SELECT id FROM users WHERE LOWER(username) = LOWER($1)",
                spec.username,
            )
            if row:
                user_id = cast(uuid.UUID, row["id"])
            else:
                user_id = uuid.uuid4()
                _ = await conn.execute(
                    """
                    INSERT INTO users (
                        id, email, hashed_password, username, display_name,
                        is_active, is_superuser, is_verified, is_admin,
                        created_at, updated_at
                    ) VALUES ($1, $2, $3, $4, $5, true, $6, true, $7, $8, $8)
                    """,
                    user_id,
                    spec.email,
                    hashed,
                    spec.username,
                    spec.username,
                    spec.is_superuser,
                    spec.is_admin,
                    now,
                )
                print(f"Created user: {spec.username}")

            if spec.seed_player:
                await _ensure_player_for_user(
                    conn,
                    user_id=user_id,
                    character_name=spec.username,
                    player_is_admin=spec.player_is_admin,
                    now=now,
                )
    finally:
        await conn.close()


def main() -> None:
    """Entry point: run E2E user seed via anyio."""
    run(_seed_e2e_users)


if __name__ == "__main__":
    main()
