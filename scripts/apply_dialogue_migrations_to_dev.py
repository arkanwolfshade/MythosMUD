#!/usr/bin/env python3
"""Apply dialogue_definitions DDL to a database (e.g. mythos_dev).

Safe to run multiple times (IF NOT EXISTS). Uses DATABASE_URL.
"""

from __future__ import annotations

import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def _run_dialogue_ddl(cur: psycopg2.extensions.cursor, schema: str) -> None:
    """Create dialogue_definitions table if missing in the given schema."""
    cur.execute(f"SET search_path TO {schema}, public")
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {schema}.dialogue_definitions (
            id TEXT NOT NULL PRIMARY KEY,
            definition JSONB NOT NULL,
            npc_definition_id BIGINT UNIQUE
                REFERENCES {schema}.npc_definitions (id) ON DELETE SET NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
        """
    )
    cur.execute(
        f"COMMENT ON TABLE {schema}.dialogue_definitions IS %s",
        ("NPC dialogue trees; definition JSONB holds start node id and nodes map (text + options).",),
    )


def main() -> None:
    """Connect via DATABASE_URL and ensure dialogue_definitions exists."""
    url = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Cthulhu1@localhost:5432/mythos_dev",
    ).replace("postgresql+asyncpg://", "postgresql://")
    parsed = urlparse(url)
    dbname = (parsed.path or "/mythos_dev").lstrip("/") or "mythos_dev"
    schema = dbname
    conn = psycopg2.connect(
        host=parsed.hostname or "localhost",
        port=parsed.port or 5432,
        user=parsed.username or "postgres",
        password=parsed.password,
        database=dbname,
    )
    cur = conn.cursor()
    _run_dialogue_ddl(cur, schema)
    conn.commit()
    cur.close()
    conn.close()
    print(f"dialogue_definitions ensured on {dbname}.{schema}")


if __name__ == "__main__":
    main()
