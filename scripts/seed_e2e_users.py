#!/usr/bin/env python3
"""
Seed canonical E2E auth users and player rows for a fresh mythos_e2e database.

Creates if missing:
  - ArkanWolfshade / Cthulhu1 (user is_admin, character is_admin for /commands)
  - Ithaqua / Cthulhu1 (regular user and character)
  - TestAdmin / Cthulhu1 (superuser; no default character — character-creation E2E only)

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
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast

import asyncpg
from anyio import run

# Project root is parent of scripts/
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# First-party import must follow sys.path insert when running as scripts/*.py (no package context).
from server.auth.argon2_utils import hash_password  # noqa: E402  # pylint: disable=wrong-import-position

E2E_PASSWORD = "Cthulhu1"

START_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"

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
    E2eUserSpec(
        username="TestAdmin",
        email="testadmin@test.local",
        is_superuser=True,
        is_admin=True,
        seed_player=False,
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
        START_ROOM,
        START_ROOM,
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
