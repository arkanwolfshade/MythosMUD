#!/usr/bin/env python3
"""Apply the account_sanctions table to one or more databases. Idempotent (IF NOT EXISTS).

The table is now part of the baseline (db/schema.sql, #811); this script remains as a
standalone repair tool for a database that predates that baseline.

Usage: python scripts/apply_account_sanctions_migration.py mythos_dev mythos_e2e
Reads connection details from .env.local / .env.unit_test / .env.e2e_test, matching the schema
name to the target database name (mythos_dev, mythos_unit, mythos_e2e).
"""

from __future__ import annotations

import asyncio
import sys

import asyncpg
from dotenv import dotenv_values

_ENV_FILE_BY_DB = {
    "mythos_dev": ".env.local",
    "mythos_unit": ".env.unit_test",
    "mythos_e2e": ".env.e2e_test",
}

_CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS {schema}.account_sanctions (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES {schema}.users(id) ON DELETE CASCADE,
    sanction_type TEXT NOT NULL CHECK (sanction_type = ANY (ARRAY['kick_cooldown'::text, 'ban'::text])),
    tier TEXT CHECK ((tier IS NULL) OR (tier = ANY (ARRAY['1h'::text, '24h'::text, '7d'::text, 'permanent'::text]))),
    reason TEXT NOT NULL,
    issued_by_player_id UUID REFERENCES {schema}.players(player_id) ON DELETE SET NULL,
    issued_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at TIMESTAMPTZ,
    lifted_at TIMESTAMPTZ,
    lifted_by_player_id UUID REFERENCES {schema}.players(player_id) ON DELETE SET NULL,
    ip_address INET
)
"""

_CREATE_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_account_sanctions_user_active
    ON {schema}.account_sanctions (user_id)
    WHERE (lifted_at IS NULL)
"""

_COMMENT_SQL = (
    "COMMENT ON TABLE {schema}.account_sanctions IS "
    "'Account-level kick cooldowns and bans for admin moderation.'"
)


async def apply_to(db_name: str) -> None:
    env_file = _ENV_FILE_BY_DB[db_name]
    env = dotenv_values(env_file)
    url = (env["DATABASE_URL"] or "").replace("postgresql+asyncpg://", "postgresql://")
    conn = await asyncpg.connect(url, server_settings={"search_path": db_name})
    try:
        await conn.execute(_CREATE_TABLE_SQL.format(schema=db_name))
        await conn.execute(_CREATE_INDEX_SQL.format(schema=db_name))
        await conn.execute(_COMMENT_SQL.format(schema=db_name))
        print(f"{db_name}: account_sanctions table + index present")
    finally:
        await conn.close()


async def main(db_names: list[str]) -> None:
    for db_name in db_names:
        if db_name not in _ENV_FILE_BY_DB:
            print(f"Unknown database {db_name!r}; expected one of {sorted(_ENV_FILE_BY_DB)}")
            sys.exit(1)
        await apply_to(db_name)


if __name__ == "__main__":
    targets = sys.argv[1:] or ["mythos_dev"]
    asyncio.run(main(targets))
