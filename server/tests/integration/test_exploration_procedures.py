"""
Integration tests for db/procedures/exploration.sql (#633). Replaces raw SQL previously inline in
server/services/coordinate_generator.py, server/services/coordinate_validator.py, and
server/services/exploration_service.py.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@pytest.fixture
async def room_pair(session_factory: async_sessionmaker[AsyncSession]):
    """One zone/subzone with two rooms linked by a 'north' exit, both positioned on the map.
    Yields (zone_stable_id, subzone_stable_id, source_room_id, source_stable_id, target_room_id,
    target_stable_id)."""
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    subzone_id = uuid.uuid4()
    source_id = uuid.uuid4()
    target_id = uuid.uuid4()
    zone_stable_id = f"test_zone_{suffix}"
    subzone_stable_id = f"test_subzone_{suffix}"
    source_stable_id = f"{zone_stable_id}_{subzone_stable_id}_room_source"
    target_stable_id = f"{zone_stable_id}_{subzone_stable_id}_room_target"

    async with session_factory() as session:
        await session.execute(
            text("INSERT INTO zones (id, stable_id, name) VALUES (:id, :stable_id, 'Test Zone')"),
            {"id": zone_id, "stable_id": zone_stable_id},
        )
        await session.execute(
            text("INSERT INTO subzones (id, zone_id, stable_id, name) VALUES (:id, :zone_id, :stable_id, 'Test Sub')"),
            {"id": subzone_id, "zone_id": zone_id, "stable_id": subzone_stable_id},
        )
        await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description, map_x, map_y) "
                "VALUES (:id, :subzone_id, :stable_id, 'Source', 'A room.', 0, 0)"
            ),
            {"id": source_id, "subzone_id": subzone_id, "stable_id": source_stable_id},
        )
        await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description, map_x, map_y) "
                "VALUES (:id, :subzone_id, :stable_id, 'Target', 'A room.', 0, -1)"
            ),
            {"id": target_id, "subzone_id": subzone_id, "stable_id": target_stable_id},
        )
        await session.execute(
            text(
                "INSERT INTO room_links (id, from_room_id, to_room_id, direction) "
                "VALUES (:id, :from_id, :to_id, 'north')"
            ),
            {"id": uuid.uuid4(), "from_id": source_id, "to_id": target_id},
        )
        await session.commit()

    yield zone_stable_id, subzone_stable_id, source_id, source_stable_id, target_id, target_stable_id


@pytest.mark.asyncio
async def test_get_rooms_for_coordinate_generation_matches_pattern(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
) -> None:
    zone_stable_id, _subzone, _source_id, source_stable_id, _target_id, target_stable_id = room_pair
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT id, stable_id, name, attributes, map_x, map_y, map_origin_zone, "
                        "map_symbol, map_style, zone_stable_id, subzone_stable_id "
                        "FROM get_rooms_for_coordinate_generation(:pattern)"
                    ),
                    {"pattern": zone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        found_stable_ids = {row["stable_id"] for row in rows}
        assert {source_stable_id, target_stable_id} <= found_stable_ids


@pytest.mark.asyncio
async def test_get_room_exits_for_coordinate_generation_returns_the_link(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
) -> None:
    _zone, _subzone, source_id, source_stable_id, target_id, target_stable_id = room_pair
    async with session_factory() as session:
        rows = (
            (
                await session.execute(
                    text(
                        "SELECT from_stable_id, to_stable_id, direction "
                        "FROM get_room_exits_for_coordinate_generation(:room_uuids)"
                    ),
                    {"room_uuids": [source_id, target_id]},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        assert rows[0]["from_stable_id"] == source_stable_id
        assert rows[0]["to_stable_id"] == target_stable_id
        assert rows[0]["direction"] == "north"


@pytest.mark.asyncio
async def test_count_coordinated_rooms_counts_positioned_rooms(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
) -> None:
    zone_stable_id, *_rest = room_pair
    async with session_factory() as session:
        count = (
            await session.execute(text("SELECT count_coordinated_rooms(:pattern)"), {"pattern": zone_stable_id})
        ).scalar()
        assert count == 2


@pytest.mark.asyncio
async def test_get_coordinate_conflicts_pairs_same_coordinate_rooms(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
) -> None:
    """A third room at the source room's exact coordinates conflicts with it -- one row per pair."""
    zone_stable_id, subzone_stable_id, source_id, source_stable_id, _target_id, _target_stable_id = room_pair
    conflicting_stable_id = f"{zone_stable_id}_{subzone_stable_id}_room_conflict"
    async with session_factory() as session:
        subzone_id = (
            await session.execute(text("SELECT subzone_id FROM rooms WHERE id = :id"), {"id": source_id})
        ).scalar()
        await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description, map_x, map_y) "
                "VALUES (:id, :subzone_id, :stable_id, 'Conflict', 'A room.', 0, 0)"
            ),
            {"id": uuid.uuid4(), "subzone_id": subzone_id, "stable_id": conflicting_stable_id},
        )
        await session.commit()

        rows = (
            (
                await session.execute(
                    text(
                        "SELECT room1_id, room1_name, room2_id, room2_name, map_x, map_y "
                        "FROM get_coordinate_conflicts(:pattern)"
                    ),
                    {"pattern": zone_stable_id},
                )
            )
            .mappings()
            .all()
        )
        assert len(rows) == 1
        pair = {rows[0]["room1_id"], rows[0]["room2_id"]}
        assert pair == {source_stable_id, conflicting_stable_id}


@pytest.mark.asyncio
async def test_get_room_id_by_stable_id_resolves_the_uuid(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
) -> None:
    _zone, _subzone, source_id, source_stable_id, _target_id, _target_stable_id = room_pair
    async with session_factory() as session:
        found = (await session.execute(text("SELECT get_room_id_by_stable_id(:id)"), {"id": source_stable_id})).scalar()
        assert found is not None
        assert uuid.UUID(str(found)) == source_id


@pytest.mark.asyncio
async def test_get_room_id_by_stable_id_unknown_returns_null(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    async with session_factory() as session:
        found = (await session.execute(text("SELECT get_room_id_by_stable_id(:id)"), {"id": "does_not_exist"})).scalar()
        assert found is None


@pytest.fixture
async def player_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create a user and a player row. Yields the player_id."""
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    username = f"explorer_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO users (id, username, display_name, email, hashed_password, is_active) "
                "VALUES (:id, :username, :username, :email, 'hashed', true)"
            ),
            {"id": user_id, "username": username, "email": f"{username}@example.com"},
        )
        await session.execute(
            text("INSERT INTO players (player_id, user_id, name) VALUES (:player_id, :user_id, :name)"),
            {"player_id": player_id, "user_id": user_id, "name": username},
        )
        await session.commit()
    yield player_id


@pytest.mark.asyncio
async def test_mark_room_explored_new_then_existing(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
    player_row: uuid.UUID,
) -> None:
    """First call is newly-inserted (True); second, idempotent call is already-existed (False);
    exactly one row lands either way (#633 judgment call 3)."""
    _zone, _subzone, source_id, _source_stable_id, _target_id, _target_stable_id = room_pair
    async with session_factory() as session:
        first = await session.execute(
            text("SELECT mark_room_explored(:player_id, :room_id)"),
            {"player_id": player_row, "room_id": source_id},
        )
        assert bool(first.scalar()) is True
        await session.commit()

        second = await session.execute(
            text("SELECT mark_room_explored(:player_id, :room_id)"),
            {"player_id": player_row, "room_id": source_id},
        )
        assert bool(second.scalar()) is False
        await session.commit()

        count = (
            await session.execute(
                text("SELECT COUNT(*) FROM player_exploration WHERE player_id = :player_id AND room_id = :room_id"),
                {"player_id": player_row, "room_id": source_id},
            )
        ).scalar()
        assert count == 1


@pytest.mark.asyncio
async def test_get_explored_rooms_and_is_room_explored(
    session_factory: async_sessionmaker[AsyncSession],
    room_pair: tuple[str, str, uuid.UUID, str, uuid.UUID, str],
    player_row: uuid.UUID,
) -> None:
    _zone, _subzone, source_id, _source_stable_id, target_id, _target_stable_id = room_pair
    async with session_factory() as session:
        await session.execute(
            text("SELECT mark_room_explored(:player_id, :room_id)"),
            {"player_id": player_row, "room_id": source_id},
        )
        await session.commit()

        explored = (
            (
                await session.execute(
                    text("SELECT room_id FROM get_explored_rooms(:player_id)"), {"player_id": player_row}
                )
            )
            .scalars()
            .all()
        )
        assert [str(r) for r in explored] == [str(source_id)]

        is_source_explored = (
            await session.execute(
                text("SELECT is_room_explored(:player_id, :room_id)"),
                {"player_id": player_row, "room_id": source_id},
            )
        ).scalar()
        assert bool(is_source_explored) is True

        is_target_explored = (
            await session.execute(
                text("SELECT is_room_explored(:player_id, :room_id)"),
                {"player_id": player_row, "room_id": target_id},
            )
        ).scalar()
        assert bool(is_target_explored) is False
