#!/usr/bin/env python3
"""Query NPC room assignments from database."""
import os
import sys
from pathlib import Path

# Add server to path
sys.path.insert(0, str(Path(__file__).parent / "server"))

from sqlalchemy import create_engine, text

# Get database URL from environment or use default
database_url = os.getenv("DATABASE_URL") or os.getenv("DATABASE_NPC_URL") or "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_dev"

# Convert asyncpg URL to psycopg2 for sync queries
if "+asyncpg" in database_url:
    database_url = database_url.replace("+asyncpg", "+psycopg2")

engine = create_engine(database_url)

with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT name, room_id, sub_zone_id, npc_type
        FROM npc_definitions
        WHERE room_id IS NOT NULL
        ORDER BY room_id, name
    """))
    rows = result.fetchall()

    print(f"{'NPC Name':<30} | {'Room ID':<50} | {'Sub Zone':<30} | {'Type'}")
    print("-" * 120)
    for row in rows:
        name, room_id, sub_zone_id, npc_type = row
        print(f"{name:<30} | {room_id:<50} | {sub_zone_id:<30} | {npc_type}")
