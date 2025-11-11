"""Runtime validation tests for inventory schema enforcement."""

from __future__ import annotations

import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

import pytest

from server.exceptions import DatabaseError
from server.models.player import Player
from server.persistence import PersistenceLayer


def initialize_database(db_path: Path, user_id: str = "inventory-validation-user") -> None:
    schema_sql = Path("server/sql/schema.sql").read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(schema_sql)
        conn.execute(
            """
            INSERT OR REPLACE INTO users (
                id, email, username, hashed_password, is_active, is_superuser, is_verified
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                "inventory_validation@example.com",
                "inventory_validation_user",
                "hashed-password",
                1,
                0,
                1,
            ),
        )
        conn.commit()


def build_player(player_id: str, user_id: str) -> Player:
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="InventoryValidator",
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    now = datetime.now(UTC).replace(tzinfo=None)
    player.created_at = now  # type: ignore[assignment]
    player.last_active = now  # type: ignore[assignment]
    return player


def test_save_player_with_oversized_inventory_rejected(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    db_path = tmp_path / "oversized_inventory.db"
    user_id = "oversized-user"
    initialize_database(db_path, user_id=user_id)

    persistence = PersistenceLayer(db_path=str(db_path))
    player = build_player("oversized-player", user_id)

    invalid_inventory = [
        {"item_id": f"token_{idx}", "item_name": f"Token {idx}", "slot_type": "backpack", "quantity": 1}
        for idx in range(25)
    ]
    player.set_inventory(invalid_inventory)

    with pytest.raises(DatabaseError) as excinfo:
        persistence.save_player(player)

    assert "Inventory validation failed" in str(excinfo.value)


def test_save_player_with_invalid_equipped_payload_rejected(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    db_path = tmp_path / "invalid_equipped.db"
    user_id = "equipped-user"
    initialize_database(db_path, user_id=user_id)

    persistence = PersistenceLayer(db_path=str(db_path))
    player = build_player("equipped-player", user_id)

    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_id": "crown_of_tindalos",
                "item_name": "Crown of Tindalos",
                "slot_type": "head",
                "quantity": 2,
            }
        }
    )

    with pytest.raises(DatabaseError) as excinfo:
        persistence.save_player(player)

    assert "Inventory validation failed" in str(excinfo.value)


def test_loading_player_with_corrupt_inventory_raises(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    db_path = tmp_path / "corrupt_inventory.db"
    user_id = "corrupt-user"
    initialize_database(db_path, user_id=user_id)

    persistence = PersistenceLayer(db_path=str(db_path))
    player = build_player("corrupt-player", user_id)
    player.set_inventory([])
    persistence.save_player(player)

    oversized_payload = [
        {"item_id": f"specimen_{idx}", "item_name": f"Specimen {idx}", "slot_type": "backpack", "quantity": 1}
        for idx in range(30)
    ]
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            UPDATE player_inventories
            SET inventory_json = ?
            WHERE player_id = ?
            """,
            (json.dumps(oversized_payload), "corrupt-player"),
        )
        conn.commit()

    with pytest.raises(DatabaseError) as excinfo:
        persistence.get_player("corrupt-player")

    assert "Invalid inventory payload detected in storage" in str(excinfo.value)
