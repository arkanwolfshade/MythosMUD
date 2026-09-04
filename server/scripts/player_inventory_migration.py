"""Create and backfill the player_inventories table."""

from __future__ import annotations

import argparse
import sqlite3
from collections.abc import Iterable
from pathlib import Path
from typing import cast

from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS player_inventories (
    player_id TEXT PRIMARY KEY REFERENCES players(player_id) ON DELETE CASCADE,
    inventory_json TEXT NOT NULL DEFAULT '[]',
    equipped_json TEXT NOT NULL DEFAULT '{}',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

BACKFILL_SQL = """
INSERT OR IGNORE INTO player_inventories (player_id, inventory_json, equipped_json)
SELECT player_id, '[]', '{}' FROM players
"""


def migrate_player_inventories(database_path: str | Path) -> int:
    """
    Ensure the player_inventories table exists and is populated for existing players.

    Returns:
        Number of inventory records inserted during this migration run.
    """
    db_path = Path(database_path)
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    logger.info("Migrating player_inventories table", database=str(db_path))

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(CREATE_TABLE_SQL)
        before = conn.execute("SELECT COUNT(*) FROM player_inventories").fetchone()[0]

        conn.execute(BACKFILL_SQL)
        conn.commit()

        after = conn.execute("SELECT COUNT(*) FROM player_inventories").fetchone()[0]

    after_count: int = cast(int, after)
    before_count: int = cast(int, before)
    inserted: int = after_count - before_count
    logger.info(
        "player_inventories migration completed",
        database=str(db_path),
        inserted=inserted,
        total=after_count,
    )
    return inserted


def migrate_multiple(databases: Iterable[str | Path]) -> None:
    """Run the migration across multiple database paths."""
    for path in databases:
        try:
            migrate_player_inventories(path)
        except FileNotFoundError as exc:
            logger.error("Skipping database; file not found", database=str(path), error=str(exc))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add and backfill the player_inventories table.")
    parser.add_argument(
        "databases",
        nargs="+",
        help="SQLite database files to migrate.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    migrate_multiple(arguments.databases)
