"""
Integration tests for the room-editor write procedures (db/procedures/rooms.sql).

Covers update_room_properties, create_room_link, update_room_link, and delete_room_link
against the real test database (mythos_unit or mythos_e2e). These are the write procedures
behind #627's room/exit editor endpoints -- the read procedures already have coverage in
test_procedures_return_shape.py, but nothing previously executed a write procedure's body,
including the one that shipped before this issue (update_room_map_position).
"""

import json
import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

_UPDATE_ROOM_PROPERTIES_SQL = text(
    "SELECT updated, resolved_environment FROM update_room_properties"
    + "(:room_id, :name, :description, :environment, :set_environment)"
)


async def _call_update_room_properties(
    session: AsyncSession,
    room_id: str,
    name: str | None,
    description: str | None,
    environment: str | None,
    set_environment: bool,
) -> tuple[bool, str | None]:
    """Call update_room_properties() and return (updated, resolved_environment) with real types
    (the raw Row's attribute access is untyped -- see #663's RETURNS TABLE change)."""
    result = await session.execute(
        _UPDATE_ROOM_PROPERTIES_SQL,
        {
            "room_id": room_id,
            "name": name,
            "description": description,
            "environment": environment,
            "set_environment": set_environment,
        },
    )
    return cast(tuple[bool, str | None], cast(object, result.one()))


@pytest.fixture
async def room_pair(session_factory: async_sessionmaker[AsyncSession]):
    """Create a zone, subzone, and two rooms (source, target) with unique stable_ids.

    Yields (source_stable_id, target_stable_id). zones/subzones/rooms/room_links are excluded
    from the autouse db_cleanup fixture (world topology is preserved across tests), so this
    fixture tears itself down explicitly -- otherwise every run leaks a zone/subzone/2 rooms
    forever (#784 follow-up: this exact leak pattern in a sibling fixture left a row that
    failed startup validation and blocked the whole E2E stack).
    """
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    subzone_id = uuid.uuid4()
    source_id = uuid.uuid4()
    target_id = uuid.uuid4()
    source_stable_id = f"test_zone_{suffix}_subzone_{suffix}_room_source_{suffix}"
    target_stable_id = f"test_zone_{suffix}_subzone_{suffix}_room_target_{suffix}"

    async with session_factory() as session:
        await session.execute(
            text("INSERT INTO zones (id, stable_id, name) VALUES (:id, :stable_id, :name)"),
            {"id": zone_id, "stable_id": f"test_zone_{suffix}", "name": "Test Zone"},
        )
        await session.execute(
            text("INSERT INTO subzones (id, zone_id, stable_id, name) VALUES (:id, :zone_id, :stable_id, :name)"),
            {"id": subzone_id, "zone_id": zone_id, "stable_id": f"test_subzone_{suffix}", "name": "Test Subzone"},
        )
        await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description) "
                "VALUES (:id, :subzone_id, :stable_id, :name, :description)"
            ),
            {
                "id": source_id,
                "subzone_id": subzone_id,
                "stable_id": source_stable_id,
                "name": "Source Room",
                "description": "A room used for write-procedure tests.",
            },
        )
        await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description) "
                "VALUES (:id, :subzone_id, :stable_id, :name, :description)"
            ),
            {
                "id": target_id,
                "subzone_id": subzone_id,
                "stable_id": target_stable_id,
                "name": "Target Room",
                "description": "A room used for write-procedure tests.",
            },
        )
        await session.commit()

    yield source_stable_id, target_stable_id

    async with session_factory() as session:
        # Tests in this file exercise create_room_link/update_room_link/delete_room_link against
        # these two rooms, so room_links rows may exist beyond the ones this fixture created.
        # to_room_id is ON DELETE RESTRICT (not CASCADE), so any surviving link would block the
        # zone delete below unless cleared first.
        _ = await session.execute(
            text(
                "DELETE FROM room_links WHERE from_room_id IN (:source_id, :target_id) OR to_room_id IN (:source_id, :target_id)"
            ),
            {"source_id": source_id, "target_id": target_id},
        )
        _ = await session.execute(text("DELETE FROM zones WHERE id = :id"), {"id": zone_id})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_properties_writes_and_reads_back(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """update_room_properties() updates name/description/environment and can be read back."""
    source_id, _target_id = room_pair
    async with session_factory() as session:
        updated, resolved_environment = await _call_update_room_properties(
            session, source_id, "Renamed Room", "New description.", "arena", True
        )
        assert updated is True
        assert resolved_environment == "arena"
        await session.commit()

        row = (
            (
                await session.execute(
                    text("SELECT name, description, environment FROM rooms WHERE stable_id = :id"),
                    {"id": source_id},
                )
            )
            .mappings()
            .one()
        )
        assert row["name"] == "Renamed Room"
        assert row["description"] == "New description."
        assert row["environment"] == "arena"

        # #663: environment lives in the column now, never in the JSONB blob.
        has_jsonb_key = (
            await session.execute(
                text("SELECT attributes ? 'environment' FROM rooms WHERE stable_id = :id"),
                {"id": source_id},
            )
        ).scalar()
        assert has_jsonb_key is False


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_properties_clears_environment_to_null(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """update_room_properties() with p_set_environment=TRUE and NULL clears the environment
    (reverting the room to inheriting from its subzone/zone -- #663)."""
    source_id, _target_id = room_pair
    async with session_factory() as session:
        _ = await _call_update_room_properties(session, source_id, None, None, "arena", True)
        await session.commit()

        updated, resolved_environment = await _call_update_room_properties(session, source_id, None, None, None, True)
        assert updated is True
        # room_pair's rooms have no subzone/zone environment set, so clearing the room's own
        # value falls all the way through the cascade to the 'outdoors' default.
        assert resolved_environment == "outdoors"
        await session.commit()

        environment = (
            await session.execute(
                text("SELECT environment FROM rooms WHERE stable_id = :id"),
                {"id": source_id},
            )
        ).scalar()
        assert environment is None


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_properties_leaves_environment_alone_when_not_set(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """p_set_environment=FALSE leaves rooms.environment untouched, regardless of p_environment."""
    source_id, _target_id = room_pair
    async with session_factory() as session:
        _ = await _call_update_room_properties(session, source_id, None, None, "arena", True)
        await session.commit()

        _ = await _call_update_room_properties(session, source_id, "Only Name Changed", None, None, False)
        await session.commit()

        row = (
            (
                await session.execute(
                    text("SELECT name, environment FROM rooms WHERE stable_id = :id"),
                    {"id": source_id},
                )
            )
            .mappings()
            .one()
        )
        assert row["name"] == "Only Name Changed"
        assert row["environment"] == "arena"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_properties_unknown_room_returns_false(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """update_room_properties() on a nonexistent stable_id returns FALSE, no exception."""
    async with session_factory() as session:
        updated, resolved_environment = await _call_update_room_properties(
            session, "does_not_exist", "x", None, None, False
        )
        assert updated is False
        assert resolved_environment is None


@pytest.mark.asyncio
@pytest.mark.integration
async def test_create_room_link_writes_a_single_row(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """create_room_link() writes exactly one room_links row for the given direction."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT create_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "to_id": target_id, "attrs": json.dumps({"description": "A dark corridor."})},
        )
        assert bool(result.scalar()) is True
        await session.commit()

        rows = (
            (
                await session.execute(
                    text(
                        "SELECT rl.direction, r2.stable_id AS to_stable_id, rl.attributes "
                        "FROM room_links rl JOIN rooms r1 ON rl.from_room_id = r1.id "
                        "JOIN rooms r2 ON rl.to_room_id = r2.id WHERE r1.stable_id = :from_id"
                    ),
                    {"from_id": source_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        assert rows[0]["direction"] == "north"
        assert rows[0]["to_stable_id"] == target_id
        assert rows[0]["attributes"]["description"] == "A dark corridor."

        # No reverse link was synthesized -- bidirectionality in this schema is two explicit rows.
        reverse = (
            await session.execute(
                text(
                    "SELECT COUNT(*) FROM room_links rl JOIN rooms r1 ON rl.from_room_id = r1.id WHERE r1.stable_id = :from_id"
                ),
                {"from_id": target_id},
            )
        ).scalar()
        assert reverse == 0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_create_room_link_duplicate_direction_raises_integrity_error(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """A second create_room_link() for the same (from_room, direction) hits the UNIQUE constraint."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        await session.execute(
            text("SELECT create_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "to_id": target_id, "attrs": "{}"},
        )
        await session.commit()

        with pytest.raises(IntegrityError):
            await session.execute(
                text("SELECT create_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
                {"from_id": source_id, "to_id": target_id, "attrs": "{}"},
            )
        await session.rollback()


@pytest.mark.asyncio
@pytest.mark.integration
async def test_create_room_link_unknown_room_returns_false(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """create_room_link() returns FALSE (no row written) when either stable_id doesn't resolve."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        missing_target = await session.execute(
            text("SELECT create_room_link(:from_id, 'north', 'does_not_exist', CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "attrs": "{}"},
        )
        assert bool(missing_target.scalar()) is False

        missing_source = await session.execute(
            text("SELECT create_room_link('does_not_exist', 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"to_id": target_id, "attrs": "{}"},
        )
        assert bool(missing_source.scalar()) is False


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_link_changes_target_and_attributes(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """update_room_link() can retarget an exit and/or replace its attributes."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        await session.execute(
            text("SELECT create_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "to_id": target_id, "attrs": "{}"},
        )
        await session.commit()

        # Retarget to the source room itself (self_reference) and set new attributes.
        result = await session.execute(
            text("SELECT update_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "to_id": source_id, "attrs": json.dumps({"flags": ["self_reference"]})},
        )
        assert bool(result.scalar()) is True
        await session.commit()

        row = (
            (
                await session.execute(
                    text(
                        "SELECT r2.stable_id AS to_stable_id, rl.attributes FROM room_links rl "
                        "JOIN rooms r1 ON rl.from_room_id = r1.id JOIN rooms r2 ON rl.to_room_id = r2.id "
                        "WHERE r1.stable_id = :from_id AND rl.direction = 'north'"
                    ),
                    {"from_id": source_id},
                )
            )
            .mappings()
            .one()
        )
        assert row["to_stable_id"] == source_id
        assert row["attributes"]["flags"] == ["self_reference"]


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_link_missing_exit_returns_false(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """update_room_link() on a direction with no existing exit returns FALSE."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT update_room_link(:from_id, 'south', :to_id, NULL)"),
            {"from_id": source_id, "to_id": target_id},
        )
        assert bool(result.scalar()) is False


@pytest.mark.asyncio
@pytest.mark.integration
async def test_delete_room_link_removes_the_row(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """delete_room_link() removes exactly the named exit and returns TRUE."""
    source_id, target_id = room_pair
    async with session_factory() as session:
        await session.execute(
            text("SELECT create_room_link(:from_id, 'north', :to_id, CAST(:attrs AS jsonb))"),
            {"from_id": source_id, "to_id": target_id, "attrs": "{}"},
        )
        await session.commit()

        result = await session.execute(text("SELECT delete_room_link(:from_id, 'north')"), {"from_id": source_id})
        assert bool(result.scalar()) is True
        await session.commit()

        remaining = (
            await session.execute(
                text(
                    "SELECT COUNT(*) FROM room_links rl JOIN rooms r1 ON rl.from_room_id = r1.id WHERE r1.stable_id = :from_id"
                ),
                {"from_id": source_id},
            )
        ).scalar()
        assert remaining == 0


@pytest.mark.asyncio
@pytest.mark.integration
async def test_delete_room_link_missing_exit_returns_false(
    session_factory: async_sessionmaker[AsyncSession], room_pair: tuple[str, str]
) -> None:
    """delete_room_link() on a direction with no exit returns FALSE."""
    source_id, _target_id = room_pair
    async with session_factory() as session:
        result = await session.execute(text("SELECT delete_room_link(:from_id, 'south')"), {"from_id": source_id})
        assert bool(result.scalar()) is False
