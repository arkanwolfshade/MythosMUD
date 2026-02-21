#!/usr/bin/env python3
"""Apply quest subsystem migrations to a database (e.g. mythos_dev).

Runs the same DDL/DML as server/alembic/versions/2026_02_19_*.
Uses DATABASE_URL (default: mythos_dev). Safe to run multiple times (IF NOT EXISTS / ON CONFLICT DO NOTHING).
"""

from __future__ import annotations

import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv()

TUTORIAL_ROOM_ID = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"


def main() -> None:
    """Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial), then exit."""
    url = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Cthulhu1@localhost:5432/mythos_dev",
    ).replace("postgresql+asyncpg://", "postgresql://")
    parsed = urlparse(url)
    dbname = (parsed.path or "/mythos_dev").lstrip("/") or "mythos_dev"

    conn = psycopg2.connect(
        host=parsed.hostname or "localhost",
        port=parsed.port or 5432,
        user=parsed.username or "postgres",
        password=parsed.password,
        database=dbname,
    )
    cur = conn.cursor()

    # DDL: quest_definitions, quest_instances, quest_offers
    cur.execute("""
        CREATE TABLE IF NOT EXISTS quest_definitions (
            id TEXT NOT NULL PRIMARY KEY,
            definition JSONB NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)
    cur.execute(
        "COMMENT ON TABLE quest_definitions IS %s",
        (
            "Quest templates; definition JSONB holds name, title, goals, rewards, "
            "triggers, requires_all/requires_any, auto_complete, turn_in_entities.",
        ),
    )

    cur.execute("""
        CREATE TABLE IF NOT EXISTS quest_instances (
            id UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
            player_id UUID NOT NULL REFERENCES players (player_id) ON DELETE CASCADE,
            quest_id TEXT NOT NULL REFERENCES quest_definitions (id) ON DELETE CASCADE,
            state TEXT NOT NULL CHECK (state IN ('active', 'completed', 'abandoned')),
            progress JSONB NOT NULL DEFAULT '{}',
            accepted_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            completed_at TIMESTAMPTZ,
            UNIQUE (player_id, quest_id)
        )
    """)
    cur.execute(
        "COMMENT ON TABLE quest_instances IS %s",
        ("Per-character quest state; one row per character per quest (active/completed/abandoned).",),
    )
    cur.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_player_id ON quest_instances (player_id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_quest_id ON quest_instances (quest_id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_quest_instances_state ON quest_instances (state)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS quest_offers (
            quest_id TEXT NOT NULL REFERENCES quest_definitions (id) ON DELETE CASCADE,
            offer_entity_type TEXT NOT NULL,
            offer_entity_id TEXT NOT NULL,
            PRIMARY KEY (quest_id, offer_entity_type, offer_entity_id)
        )
    """)
    cur.execute(
        "COMMENT ON TABLE quest_offers IS %s",
        ("Links quests to NPCs or rooms that offer them; offer_entity_type in (npc, room).",),
    )
    cur.execute(
        "CREATE INDEX IF NOT EXISTS idx_quest_offers_entity ON quest_offers (offer_entity_type, offer_entity_id)"
    )

    # Seed: leave_the_tutorial
    exit_target = f"exit_{TUTORIAL_ROOM_ID}"
    definition_json = (
        '{"name": "leave_the_tutorial", "title": "Leave the tutorial", '
        '"description": "Find your way out of the tutorial room.", '
        f'"goals": [{{"type": "complete_activity", "target": "{exit_target}"}}], '
        '"rewards": [{"type": "xp", "amount": 10}], '
        f'"triggers": [{{"type": "room", "entity_id": "{TUTORIAL_ROOM_ID}"}}], '
        '"requires_all": [], "requires_any": [], "auto_complete": true, "turn_in_entities": []}'
    )
    cur.execute(
        """
        INSERT INTO quest_definitions (id, definition, created_at, updated_at)
        VALUES ('leave_the_tutorial', %s::jsonb, NOW(), NOW())
        ON CONFLICT (id) DO NOTHING
        """,
        (definition_json,),
    )
    cur.execute(
        """
        INSERT INTO quest_offers (quest_id, offer_entity_type, offer_entity_id)
        VALUES ('leave_the_tutorial', 'room', %s)
        ON CONFLICT (quest_id, offer_entity_type, offer_entity_id) DO NOTHING
        """,
        (TUTORIAL_ROOM_ID,),
    )

    conn.commit()
    cur.close()
    conn.close()
    print(f"[OK] Quest migrations applied to {dbname}: quest_definitions, quest_instances, quest_offers + seed.")


if __name__ == "__main__":
    main()
