"""
Integration tests for the room environment inheritance cascade (#663).

rooms.environment (promoted from the attributes JSONB blob, matching zones.environment /
subzones.environment) resolves via COALESCE(room, subzone, zone, 'outdoors') in SQL --
get_rooms_with_exits() and update_room_properties() both compute it, rather than in Python, so
the inheritance rule stays defined once.
"""

import re
import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.world import ROOM_ENVIRONMENTS

# The three CHECK constraints that must all enumerate the same environment values
# (server.models.world.ROOM_ENVIRONMENTS) -- #663 promoted rooms.environment to a typed column
# with its own constraint, matching its zone/subzone siblings; this guards them from drifting
# apart again.
ENVIRONMENT_CHECK_CONSTRAINTS = ("chk_zones_environment", "chk_subzones_environment", "chk_rooms_environment")

_UPDATE_ROOM_PROPERTIES_SQL = text(
    "SELECT updated, resolved_environment FROM update_room_properties(:room_id, NULL, NULL, NULL, FALSE)"
)


def _enum_values_from_check_definition(check_def: str) -> set[str]:
    """Extract the quoted string literals out of a CHECK constraint's pg_get_constraintdef() text."""
    return set(re.findall(r"'([a-z_]+)'", check_def))


@pytest.fixture
async def cascade_room(session_factory: async_sessionmaker[AsyncSession]):
    """Zone (environment='underwater') -> subzone (environment='indoors') -> room (NULL).

    Yields the room's stable_id. Cleaned up the same way test_room_write_procedures.py's
    room_pair fixture is -- zones/subzones/rooms are excluded from the autouse db_cleanup
    fixture, so this tears itself down explicitly.
    """
    suffix = uuid.uuid4().hex[:8]
    zone_id = uuid.uuid4()
    subzone_id = uuid.uuid4()
    room_id = uuid.uuid4()
    room_stable_id = f"test_zone_{suffix}_subzone_{suffix}_room_cascade_{suffix}"

    async with session_factory() as session:
        _ = await session.execute(
            text("INSERT INTO zones (id, stable_id, name, environment) VALUES (:id, :stable_id, :name, :env)"),
            {"id": zone_id, "stable_id": f"test_zone_{suffix}", "name": "Test Zone", "env": "underwater"},
        )
        _ = await session.execute(
            text(
                "INSERT INTO subzones (id, zone_id, stable_id, name, environment) VALUES (:id, :zone_id, :stable_id, :name, :env)"
            ),
            {
                "id": subzone_id,
                "zone_id": zone_id,
                "stable_id": f"test_subzone_{suffix}",
                "name": "Test Subzone",
                "env": "indoors",
            },
        )
        _ = await session.execute(
            text(
                "INSERT INTO rooms (id, subzone_id, stable_id, name, description) VALUES (:id, :subzone_id, :stable_id, :name, :description)"
            ),
            {
                "id": room_id,
                "subzone_id": subzone_id,
                "stable_id": room_stable_id,
                "name": "Cascade Room",
                "description": "A room used for environment-cascade tests.",
            },
        )
        await session.commit()

    yield room_stable_id

    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM zones WHERE id = :id"), {"id": zone_id})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.integration
async def test_get_rooms_with_exits_resolves_from_subzone_when_room_unset(
    session_factory: async_sessionmaker[AsyncSession], cascade_room: str
) -> None:
    """A room with no environment of its own inherits its subzone's, not its zone's."""
    async with session_factory() as session:
        row = (
            (
                await session.execute(
                    text("SELECT room_environment, resolved_environment FROM get_rooms_with_exits() WHERE stable_id = :id"),
                    {"id": cascade_room},
                )
            )
            .mappings()
            .one()
        )
    assert row["room_environment"] is None
    assert row["resolved_environment"] == "indoors"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_update_room_properties_resolves_from_zone_when_room_and_subzone_unset(
    session_factory: async_sessionmaker[AsyncSession], cascade_room: str
) -> None:
    """Clearing a subzone's environment falls through to its zone's."""
    async with session_factory() as session:
        _ = await session.execute(
            text("UPDATE subzones SET environment = NULL WHERE id = (SELECT subzone_id FROM rooms WHERE stable_id = :id)"),
            {"id": cascade_room},
        )
        await session.commit()

        result = await session.execute(_UPDATE_ROOM_PROPERTIES_SQL, {"room_id": cascade_room})
        updated, resolved_environment = cast(tuple[bool, str | None], cast(object, result.one()))
    assert updated is True
    assert resolved_environment == "underwater"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_environment_check_constraints_share_the_same_enum(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """chk_zones_environment, chk_subzones_environment, and chk_rooms_environment must always
    enumerate the same values -- server.models.world.ROOM_ENVIRONMENTS. If rooms.environment's
    constraint (added typed in #663) drifts from its zone/subzone siblings, the inheritance
    cascade could accept a room-level value the zone/subzone levels reject, or vice versa."""
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT conname, pg_get_constraintdef(oid) AS def FROM pg_constraint WHERE conname = ANY(:names)"),
            {"names": list(ENVIRONMENT_CHECK_CONSTRAINTS)},
        )
        rows = result.mappings().all()

    found = {cast(str, row["conname"]): _enum_values_from_check_definition(cast(str, row["def"])) for row in rows}
    missing = set(ENVIRONMENT_CHECK_CONSTRAINTS) - found.keys()
    assert not missing, f"Missing CHECK constraint(s): {missing}"
    for name, values in found.items():
        assert values == set(ROOM_ENVIRONMENTS), f"{name} enumerates {values}, expected {set(ROOM_ENVIRONMENTS)}"
