"""Runtime validation tests for inventory schema enforcement."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from typing import Protocol, cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.exceptions import DatabaseError
from server.models.base import Base
from server.models.player import Player
from server.models.user import User
from server.persistence import PersistenceLayer


class InventorySaveLogRecord(Protocol):
    # Human researchers: this protocol documents the structured context emitted when inventory validation fails on save.
    # Machine aides: adhere to these attribute expectations to maintain type safety across log assertions.
    player_id: str
    player_name: str


class InventoryLoadLogRecord(Protocol):
    # Mortal archivists: this log record shape captures load-time validation failures.
    # Algorithmic custodians: keep these fields intact to appease mypy while we scrutinize the logs.
    player_id: str


@pytest.fixture
async def async_session_factory():
    """Create an async session factory for database setup."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def initialize_database(session: AsyncSession, user_id: str | None = None) -> str:
    """Create required schema and seed data in PostgreSQL.

    Returns:
        The UUID of the created user (as string)
    """
    import uuid

    # Generate a proper UUID for user_id if not provided
    if user_id is None:
        user_uuid = uuid.uuid4()
    else:
        # If user_id is provided, try to use it as UUID, or generate new one
        try:
            user_uuid = uuid.UUID(user_id)
        except (ValueError, AttributeError):
            # If it's not a valid UUID, generate a new one
            user_uuid = uuid.uuid4()

    unique_suffix = str(user_uuid)[:8]

    # Create user with unique email and username
    user = User(
        id=str(user_uuid),
        email=f"inventory_validation_{unique_suffix}@example.com",
        username=f"inventory_validation_user_{unique_suffix}",
        display_name=f"inventory_validation_user_{unique_suffix}",
        hashed_password="hashed-password",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    session.add(user)
    await session.commit()
    return str(user_uuid)


def build_player(player_id: str, user_id: str, name: str | None = None) -> Player:
    """Create a Player instance with timestamps normalized for persistence tests."""
    import json
    import uuid

    # Use unique name based on player_id if not provided
    # Player.name has unique constraint, so we need to ensure uniqueness
    if name is None:
        # Use a combination of player_id and a short UUID to ensure uniqueness
        unique_part = player_id.replace("-", "")[-12:] if len(player_id) > 12 else player_id
        name = f"InventoryValidator-{unique_part}-{str(uuid.uuid4())[:8]}"

    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=name,
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        status_effects=json.dumps([]),  # Ensure status_effects is set (not null)
        experience_points=0,  # Ensure experience_points is set (not null)
        level=1,  # Ensure level is set (not null)
        is_admin=0,  # Ensure is_admin is set (not null)
        profession_id=0,  # Ensure profession_id is set (not null)
    )
    now = datetime.now(UTC).replace(tzinfo=None)
    player.created_at = now  # type: ignore[assignment]
    player.last_active = now  # type: ignore[assignment]
    return player


@pytest.mark.asyncio
async def test_save_player_with_oversized_inventory_rejected(
    async_session_factory,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    """Test that saving a player with oversized inventory is rejected."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    import uuid

    unique_suffix = str(uuid.uuid4())[:8]

    async with async_session_factory() as session:
        user_id = await initialize_database(session)

    persistence = PersistenceLayer(db_path=database_url)
    player = build_player(f"oversized-player-{unique_suffix}", user_id)

    invalid_inventory = []
    for idx in range(25):
        invalid_inventory.append(
            {
                "item_instance_id": f"instance-token_{idx}",
                "prototype_id": f"token_{idx}",
                "item_id": f"token_{idx}",
                "item_name": f"Token {idx}",
                "slot_type": "backpack",
                "quantity": 1,
            }
        )
    player.set_inventory(invalid_inventory)

    capsys.readouterr()

    with caplog.at_level(logging.ERROR, logger="server.persistence"):
        with pytest.raises(DatabaseError) as excinfo:
            persistence.save_player(player)

    player_name = cast(str, player.name)
    player_id_str = str(player.player_id)  # Convert to str for type checking
    assert "Inventory validation failed" in str(excinfo.value)
    error_logs = [
        record for record in caplog.records if record.message == "Inventory payload validation failed during save"
    ]
    combined_output = (caplog.text or "") + capsys.readouterr().out
    if error_logs:
        log_record = cast(InventorySaveLogRecord, error_logs[0])
        assert log_record.player_id == player_id_str
        assert log_record.player_name == player_name
    else:
        assert "Inventory payload validation failed during save" in combined_output
        assert player_id_str in combined_output
        assert player_name in combined_output
    caplog.clear()


@pytest.mark.asyncio
async def test_save_player_with_invalid_equipped_payload_rejected(
    async_session_factory,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    """Test that saving a player with invalid equipped payload is rejected."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    import uuid

    unique_suffix = str(uuid.uuid4())[:8]

    async with async_session_factory() as session:
        user_id = await initialize_database(session)

    persistence = PersistenceLayer(db_path=database_url)
    player = build_player(f"equipped-player-{unique_suffix}", user_id)

    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_instance_id": "instance-crown_of_tindalos",
                "prototype_id": "crown_of_tindalos",
                "item_id": "crown_of_tindalos",
                "item_name": "Crown of Tindalos",
                "slot_type": "head",
                "quantity": 2,
            }
        }
    )

    capsys.readouterr()

    with caplog.at_level(logging.ERROR, logger="server.persistence"):
        with pytest.raises(DatabaseError) as excinfo:
            persistence.save_player(player)

    player_name = cast(str, player.name)
    assert "Inventory validation failed" in str(excinfo.value)
    error_logs = [
        record for record in caplog.records if record.message == "Inventory payload validation failed during save"
    ]
    combined_output = (caplog.text or "") + capsys.readouterr().out
    if error_logs:
        log_record = cast(InventorySaveLogRecord, error_logs[0])
        assert log_record.player_id == "equipped-player"
        assert log_record.player_name == player_name
    else:
        assert "Inventory payload validation failed during save" in combined_output
        assert "equipped-player" in combined_output
        assert player_name in combined_output
    caplog.clear()


@pytest.mark.asyncio
async def test_loading_player_with_corrupt_inventory_raises(
    async_session_factory,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    """Test that loading a player with corrupt inventory raises an error."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    import uuid

    unique_suffix = str(uuid.uuid4())[:8]
    player_id = f"corrupt-player-{unique_suffix}"

    async with async_session_factory() as session:
        user_id = await initialize_database(session)

    persistence = PersistenceLayer(db_path=database_url)
    player = build_player(player_id, user_id)
    player.set_inventory([])
    persistence.save_player(player)

    oversized_payload = []
    for idx in range(30):
        oversized_payload.append(
            {
                "item_instance_id": f"instance-specimen_{idx}",
                "prototype_id": f"specimen_{idx}",
                "item_id": f"specimen_{idx}",
                "item_name": f"Specimen {idx}",
                "slot_type": "backpack",
                "quantity": 1,
            }
        )

    # Update the database directly using PostgreSQL async session
    async with async_session_factory() as session:
        await session.execute(
            text(
                """
                UPDATE player_inventories
                SET inventory_json = :inventory_json
                WHERE player_id = :player_id
                """
            ),
            {"inventory_json": json.dumps(oversized_payload), "player_id": player_id},
        )
        await session.commit()

    capsys.readouterr()

    with caplog.at_level(logging.ERROR, logger="server.persistence"):
        with pytest.raises(DatabaseError) as excinfo:
            # Convert string player_id to UUID for type safety
            persistence.get_player(uuid.UUID(player_id))

    assert "Invalid inventory payload detected in storage" in str(excinfo.value)
    load_logs = [record for record in caplog.records if record.message == "Stored inventory payload failed validation"]
    combined_output = (caplog.text or "") + capsys.readouterr().out
    if load_logs:
        load_log = cast(InventoryLoadLogRecord, load_logs[0])
        assert load_log.player_id == "corrupt-player"
    else:
        assert "Stored inventory payload failed validation" in combined_output
        assert "corrupt-player" in combined_output
