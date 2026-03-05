"""
Integration tests that call PostgreSQL procedures/functions directly and verify return shape.

These tests ensure procedures applied by scripts/apply_procedures.ps1 exist and return
the column structure expected by Python repositories and services. They run against
the test database (mythos_unit or mythos_e2e) with procedures already applied.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

# Expected column names from db/procedures (used by Python mappers)
GET_ROOMS_WITH_EXITS_COLUMNS = {
    "room_uuid",
    "stable_id",
    "name",
    "description",
    "attributes",
    "subzone_stable_id",
    "zone_stable_id",
    "plane",
    "zone",
    "exits",
}

GET_PLAYER_BY_ID_COLUMNS = {
    "player_id",
    "user_id",
    "name",
    "inventory",
    "current_room_id",
    "experience_points",
    "level",
    "stats",
    "is_deleted",
}

GET_NPC_SYSTEM_STATISTICS_COLUMNS = {
    "total_npc_definitions",
    "npc_definitions_by_type",
    "total_spawn_rules",
}

ADD_EFFECT_PARAMS = {
    "effect_type": "login_warded",
    "category": "entry_ward",
    "duration": 100,
    "applied_at_tick": 0,
    "intensity": 1,
    "source": "game_entry",
    "visibility_level": "visible",
}


@pytest.mark.asyncio
async def test_get_rooms_with_exits_return_shape(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """Call get_rooms_with_exits() and verify result columns match procedure definition."""
    async with session_factory() as session:
        result = await session.execute(
            text(
                """
                SELECT
                    room_uuid,
                    stable_id,
                    name,
                    description,
                    attributes,
                    subzone_stable_id,
                    zone_stable_id,
                    plane,
                    zone,
                    exits
                FROM get_rooms_with_exits()
                """
            )
        )
        rows = result.mappings().all()
    # May be empty if no rooms; we only assert shape
    if rows:
        first = rows[0]
        keys = set(first.keys())
        assert GET_ROOMS_WITH_EXITS_COLUMNS.issubset(keys), (
            f"get_rooms_with_exits() must return columns {GET_ROOMS_WITH_EXITS_COLUMNS}; got {keys}"
        )
    # If empty, at least the call succeeded (procedure exists and returns TABLE)


@pytest.mark.asyncio
async def test_get_player_by_id_return_shape_and_not_found(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """Call get_player_by_id() with non-existent UUID; verify return shape when empty."""
    async with session_factory() as session:
        result = await session.execute(
            text(
                """
                SELECT
                    player_id,
                    user_id,
                    name,
                    inventory,
                    status_effects,
                    current_room_id,
                    respawn_room_id,
                    experience_points,
                    level,
                    is_admin,
                    profession_id,
                    created_at,
                    last_active,
                    stats,
                    is_deleted,
                    deleted_at,
                    tutorial_instance_id,
                    inventory_json,
                    equipped_json
                FROM get_player_by_id(:id)
                """
            ),
            {"id": uuid.uuid4()},
        )
        rows = result.mappings().all()
    assert len(rows) == 0
    # If we had a player row, we would assert GET_PLAYER_BY_ID_COLUMNS.issubset(rows[0].keys())


@pytest.mark.asyncio
async def test_get_npc_system_statistics_return_shape(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """Call get_npc_system_statistics() and verify result columns."""
    async with session_factory() as session:
        result = await session.execute(
            text(
                """
                SELECT
                    total_npc_definitions,
                    npc_definitions_by_type,
                    total_spawn_rules
                FROM get_npc_system_statistics()
                """
            )
        )
        rows = result.mappings().all()
    assert len(rows) >= 1, "get_npc_system_statistics() must return at least one row"
    first = rows[0]
    keys = set(first.keys())
    assert GET_NPC_SYSTEM_STATISTICS_COLUMNS.issubset(keys), (
        f"get_npc_system_statistics() must return columns {GET_NPC_SYSTEM_STATISTICS_COLUMNS}; got {keys}"
    )
    assert isinstance(first.get("total_npc_definitions"), int | None)
    assert isinstance(first.get("total_spawn_rules"), int | None)


@pytest.mark.asyncio
@pytest.mark.serial
async def test_add_player_effect_generates_id(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """
    Call add_player_effect() and verify it returns a non-null UUID.

    This guards against schema regressions where player_effects.id lacks a default,
    which would cause a NOT NULL violation when inserting via the procedure.
    """
    async with session_factory() as session:
        # Use an existing player_id from seed data to satisfy FK constraint.
        player_result = await session.execute(text("SELECT player_id FROM players LIMIT 1"))
        player_id = player_result.scalar()
        assert player_id is not None, "Seed data must include at least one player for add_player_effect test"

        result = await session.execute(
            text(
                "SELECT add_player_effect("
                ":player_id, :effect_type, :category, :duration, :applied_at_tick,"
                " :intensity, :source, :visibility_level)"
            ),
            {"player_id": player_id, **ADD_EFFECT_PARAMS},
        )
        effect_id = result.scalar()

    assert effect_id is not None
