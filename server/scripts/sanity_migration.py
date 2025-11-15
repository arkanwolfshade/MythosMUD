"""Schema migration for the MythosMUD sanity system tables."""

from __future__ import annotations

import argparse
import sqlite3
from collections.abc import Iterable
from pathlib import Path

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

PLAYER_SANITY_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS player_sanity (
    player_id TEXT PRIMARY KEY REFERENCES players(player_id) ON DELETE CASCADE,
    current_san INTEGER NOT NULL DEFAULT 100 CHECK (current_san BETWEEN -100 AND 100),
    current_tier TEXT NOT NULL DEFAULT 'lucid' CHECK (
        current_tier IN ('lucid','uneasy','fractured','deranged','catatonic')
    ),
    liabilities TEXT NOT NULL DEFAULT '[]',
    last_updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    catatonia_entered_at DATETIME NULL
)
"""

PLAYER_SANITY_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_player_sanity_tier ON player_sanity(current_tier)
"""

SANITY_ADJUSTMENT_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sanity_adjustment_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    delta INTEGER NOT NULL,
    reason_code TEXT NOT NULL,
    metadata TEXT NOT NULL DEFAULT '{}',
    location_id TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

SANITY_ADJUSTMENT_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_sanity_adjustment_player_created
ON sanity_adjustment_log(player_id, created_at)
"""

SANITY_EXPOSURE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sanity_exposure_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    entity_archetype TEXT NOT NULL,
    encounter_count INTEGER NOT NULL DEFAULT 0,
    last_encounter_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(player_id, entity_archetype)
)
"""

SANITY_COOLDOWNS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sanity_cooldowns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    action_code TEXT NOT NULL,
    cooldown_expires_at DATETIME NOT NULL,
    UNIQUE(player_id, action_code)
)
"""

PLAYER_SANITY_BACKFILL_SQL = """
INSERT OR IGNORE INTO player_sanity (player_id)
SELECT player_id FROM players
"""


def migrate_sanity_system(database_path: str | Path) -> None:
    """
    Apply sanity schema migration to a SQLite database.

    The ritual crafts the new sanity tables and backfills player_sanity rows
    for pre-existing investigators without disturbing prior adjustments.
    """

    db_path = Path(database_path)
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    logger.info("Starting sanity migration", database=str(db_path))

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        try:
            cursor.execute("BEGIN")

            cursor.execute(PLAYER_SANITY_TABLE_SQL)
            cursor.execute(PLAYER_SANITY_INDEX_SQL)

            cursor.execute(SANITY_ADJUSTMENT_TABLE_SQL)
            cursor.execute(SANITY_ADJUSTMENT_INDEX_SQL)

            cursor.execute(SANITY_EXPOSURE_TABLE_SQL)
            cursor.execute(SANITY_COOLDOWNS_TABLE_SQL)

            cursor.execute(PLAYER_SANITY_BACKFILL_SQL)

            conn.commit()
        except sqlite3.DatabaseError as exc:
            conn.rollback()
            logger.error("Sanity migration failed", database=str(db_path), error=str(exc))
            raise
        finally:
            cursor.close()

    logger.info("Sanity migration completed", database=str(db_path))


def migrate_multiple(databases: Iterable[str | Path]) -> None:
    """Run the sanity migration across multiple database files."""
    for path in databases:
        try:
            migrate_sanity_system(path)
        except FileNotFoundError as exc:
            logger.error("Skipping sanity migration; database missing", database=str(path), error=str(exc))


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the sanity migration runner."""
    parser = argparse.ArgumentParser(description="Add sanity tracking tables and seed baseline player_sanity rows.")
    parser.add_argument(
        "databases",
        nargs="+",
        help="SQLite database files to migrate.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    migrate_multiple(args.databases)
