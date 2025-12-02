"""Schema migration for the MythosMUD lucidity system tables."""

from __future__ import annotations

import argparse
import sqlite3
from collections.abc import Iterable
from pathlib import Path

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

PLAYER_lucidity_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS player_lucidity (
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

PLAYER_lucidity_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_player_lucidity_tier ON player_lucidity(current_tier)
"""

lucidity_ADJUSTMENT_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS lucidity_adjustment_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    delta INTEGER NOT NULL,
    reason_code TEXT NOT NULL,
    metadata TEXT NOT NULL DEFAULT '{}',
    location_id TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

lucidity_ADJUSTMENT_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_lucidity_adjustment_player_created
ON lucidity_adjustment_log(player_id, created_at)
"""

lucidity_EXPOSURE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS lucidity_exposure_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    entity_archetype TEXT NOT NULL,
    encounter_count INTEGER NOT NULL DEFAULT 0,
    last_encounter_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(player_id, entity_archetype)
)
"""

lucidity_COOLDOWNS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS lucidity_cooldowns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id TEXT NOT NULL REFERENCES players(player_id) ON DELETE CASCADE,
    action_code TEXT NOT NULL,
    cooldown_expires_at DATETIME NOT NULL,
    UNIQUE(player_id, action_code)
)
"""

PLAYER_lucidity_BACKFILL_SQL = """
INSERT OR IGNORE INTO player_lucidity (player_id)
SELECT player_id FROM players
"""


def migrate_lucidity_system(database_path: str | Path) -> None:
    """
    Apply lucidity schema migration to a SQLite database.

    The ritual crafts the new lucidity tables and backfills player_lucidity rows
    for pre-existing investigators without disturbing prior adjustments.
    """

    db_path = Path(database_path)
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    logger.info("Starting lucidity migration", database=str(db_path))

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        try:
            cursor.execute("BEGIN")

            cursor.execute(PLAYER_lucidity_TABLE_SQL)
            cursor.execute(PLAYER_lucidity_INDEX_SQL)

            cursor.execute(lucidity_ADJUSTMENT_TABLE_SQL)
            cursor.execute(lucidity_ADJUSTMENT_INDEX_SQL)

            cursor.execute(lucidity_EXPOSURE_TABLE_SQL)
            cursor.execute(lucidity_COOLDOWNS_TABLE_SQL)

            cursor.execute(PLAYER_lucidity_BACKFILL_SQL)

            conn.commit()
        except sqlite3.DatabaseError as exc:
            conn.rollback()
            logger.error("lucidity migration failed", database=str(db_path), error=str(exc))
            raise
        finally:
            cursor.close()

    logger.info("lucidity migration completed", database=str(db_path))


def migrate_multiple(databases: Iterable[str | Path]) -> None:
    """Run the lucidity migration across multiple database files."""
    for path in databases:
        try:
            migrate_lucidity_system(path)
        except FileNotFoundError as exc:
            logger.error("Skipping lucidity migration; database missing", database=str(path), error=str(exc))


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the lucidity migration runner."""
    parser = argparse.ArgumentParser(description="Add lucidity tracking tables and seed baseline player_lucidity rows.")
    parser.add_argument(
        "databases",
        nargs="+",
        help="SQLite database files to migrate.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    migrate_multiple(args.databases)
