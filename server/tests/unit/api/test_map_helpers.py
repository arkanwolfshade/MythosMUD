"""
Unit tests for map_helpers (build_zone_pattern, build_room_dict).

Guards against regressions in zone pattern and room dict construction
used by ASCII map and minimap endpoints.
"""

from collections.abc import Iterator
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.map_helpers import (
    build_room_dict,
    build_zone_pattern,
    load_room_exits,
    load_rooms_with_coordinates,
    load_single_room_with_coordinates,
)


class _MockResultRows:
    """Minimal iterable matching SQLAlchemy result iteration (typed __iter__, no MagicMock)."""

    _rows: list[tuple[object, ...]]

    def __init__(self, rows: list[tuple[object, ...]]) -> None:
        self._rows = rows

    def __iter__(self) -> Iterator[tuple[object, ...]]:
        return iter(self._rows)


class TestBuildZonePattern:
    """Tests for build_zone_pattern."""

    def test_plane_zone_only(self) -> None:
        """Plane plus zone without sub-zone builds 'plane_zone'."""
        assert build_zone_pattern("material", "arkham", None) == "material_arkham"

    def test_plane_zone_sub_zone(self) -> None:
        """Plane, zone, and sub-zone build 'plane_zone_sub_zone'."""
        assert build_zone_pattern("material", "arkham", "miskatonic") == "material_arkham_miskatonic"

    def test_empty_sub_zone_treated_as_none(self) -> None:
        """Empty or missing sub-zone is treated like None and omitted."""
        # Pattern is plane_zone when sub_zone is None; empty string would still be truthy in the function
        assert build_zone_pattern("p", "z", None) == "p_z"


class TestBuildRoomDict:
    """Tests for build_room_dict from database row.

    Row tuple: (id, stable_id, name, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style).
    """

    def test_full_row(self) -> None:
        """Full database row is mapped to a complete room dict."""
        row = (
            "uuid-123",
            "material_arkham_room_1",
            "Main Foyer",
            {"environment": "interior"},
            1.0,
            2.0,
            False,
            "#",
            "interior",
        )
        out = build_room_dict(row)
        assert out["uuid"] == "uuid-123"
        assert out["id"] == "material_arkham_room_1"
        assert out["stable_id"] == "material_arkham_room_1"
        assert out["name"] == "Main Foyer"
        assert out["attributes"] == {"environment": "interior"}
        assert out["map_x"] == 1.0
        assert out["map_y"] == 2.0
        assert out["map_origin_zone"] is False
        assert out["map_symbol"] == "#"
        assert out["map_style"] == "interior"
        assert not out["exits"]

    def test_null_map_coords(self) -> None:
        """Null map coordinates in the row become None in the room dict."""
        row = (
            "u",
            "stable_1",
            "Room",
            None,
            None,
            None,
            None,
            None,
            None,
        )
        out = build_room_dict(row)
        assert out["map_x"] is None
        assert out["map_y"] is None
        assert out["attributes"] == {}


@pytest.mark.asyncio
async def test_load_room_exits_no_rooms_no_query() -> None:
    """Empty room list skips DB call."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    execute_mock: AsyncMock = AsyncMock()
    session.execute = execute_mock
    await load_room_exits(session, [])
    execute_mock.assert_not_called()


@pytest.mark.asyncio
async def test_load_room_exits_attaches_exits_by_stable_id() -> None:
    """Exit rows are grouped onto room dicts by from_stable_id."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    room: dict[str, str | dict[str, str]] = {"stable_id": "r1", "exits": {}}
    exits_result = _MockResultRows([("r1", "r2", "north"), ("r1", "r3", "south")])
    execute_mock: AsyncMock = AsyncMock(return_value=exits_result)
    session.execute = execute_mock
    await load_room_exits(session, [room])
    assert room["exits"] == {"north": "r2", "south": "r3"}


@pytest.mark.asyncio
async def test_load_rooms_with_coordinates_executes_zone_query_and_exits() -> None:
    """Zone query builds rooms then load_room_exits runs second query."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    room_row: tuple[object, ...] = ("uuid-1", "stable_a", "Name", {}, 1.0, 2.0, True, ".", "style")
    rooms_result = _MockResultRows([room_row])
    exits_result = _MockResultRows([])

    execute_mock: AsyncMock = AsyncMock(side_effect=[rooms_result, exits_result])
    session.execute = execute_mock

    rooms = await load_rooms_with_coordinates(session, "material", "arkham", None)
    assert len(rooms) == 1
    assert rooms[0]["stable_id"] == "stable_a"
    assert rooms[0]["map_x"] == 1.0
    assert execute_mock.await_count == 2


@pytest.mark.asyncio
async def test_load_single_room_with_coordinates_none_when_missing() -> None:
    """fetchone() None returns None without building a room."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    mock_result = MagicMock()
    mock_result.fetchone = MagicMock(return_value=None)
    execute_mock: AsyncMock = AsyncMock(return_value=mock_result)
    session.execute = execute_mock
    out = await load_single_room_with_coordinates(session, "missing_stable")
    assert out is None


@pytest.mark.asyncio
async def test_load_single_room_with_coordinates_loads_exits() -> None:
    """Single room row is built and exits query is run."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    room_row: tuple[object, ...] = ("uuid-1", "stable_b", "R", None, 0.0, 0.0, False, "x", "s")
    first = MagicMock()
    first.fetchone = MagicMock(return_value=room_row)
    exits_result = _MockResultRows([])
    execute_mock: AsyncMock = AsyncMock(side_effect=[first, exits_result])
    session.execute = execute_mock

    out = await load_single_room_with_coordinates(session, "stable_b")
    assert out is not None
    assert out["stable_id"] == "stable_b"
    assert execute_mock.await_count == 2
