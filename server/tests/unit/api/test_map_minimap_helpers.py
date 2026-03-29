"""
Unit tests for map_minimap pure helpers.

Guards against regressions in minimap fallback coordinates and
ensuring current room is in the room list (append with fallback coords).
"""

# pyright: reportPrivateUsage=false
# AI: Tests intentionally cover map_minimap private helpers; production API stays encapsulated.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.map_helpers import MapZoneContext
from server.api.map_minimap import (
    _append_room_with_fallback_coords_if_needed,
    _apply_minimap_fallback_coordinates,
    _ensure_current_room_in_minimap_rooms,
    _resolve_current_room_for_minimap,
    generate_minimap_html,
)
from server.game.room_service import RoomService

# Room payloads mirror map_minimap list[dict[str, Any]] without importing Any.
_MinimapRoom = dict[str, object]
_MinimapRooms = list[_MinimapRoom]


class TestAppendRoomWithFallbackCoordsIfNeeded:
    """Tests for _append_room_with_fallback_coords_if_needed."""

    def test_appends_room_unchanged_when_has_coords(self) -> None:
        """Room with map_x/map_y is appended as-is."""
        rooms: _MinimapRooms = []
        room: _MinimapRoom = {"id": "r1", "stable_id": "r1", "map_x": 5.0, "map_y": 10.0}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 5.0
        assert rooms[0]["map_y"] == 10.0

    def test_appends_copy_with_fallback_0_0_when_coords_missing(self) -> None:
        """Room with missing coords is appended with fallback (0, 0); original unchanged."""
        rooms: _MinimapRooms = []
        room: _MinimapRoom = {"id": "r1", "stable_id": "r1", "map_x": None, "map_y": None}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0
        assert room["map_x"] is None  # original unchanged

    def test_appends_fallback_when_only_one_coord_missing(self) -> None:
        """If either map_x or map_y is missing, appended room gets fallback (0, 0)."""
        rooms: _MinimapRooms = []
        room: _MinimapRoom = {"id": "r1", "map_x": 1.0, "map_y": None}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0


class TestApplyMinimapFallbackCoordinates:
    """Tests for _apply_minimap_fallback_coordinates (mutates rooms in place)."""

    def test_admin_gets_grid_layout_for_rooms_without_coords(self) -> None:
        """Admin sees all rooms without coords laid out in a grid (fallback applied)."""
        rooms: _MinimapRooms = [
            {"id": "r0", "map_x": None, "map_y": None},
            {"id": "r1", "map_x": None, "map_y": None},
            {"id": "r2", "map_x": None, "map_y": None},
        ]
        _apply_minimap_fallback_coordinates(rooms, current_room_id=None, is_admin=True, fallback_grid_width=2)
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0
        assert rooms[1]["map_x"] == 1.0
        assert rooms[1]["map_y"] == 0.0
        assert rooms[2]["map_x"] == 0.0
        assert rooms[2]["map_y"] == 1.0

    def test_fallback_grid_wraps_by_fallback_grid_width(self) -> None:
        """Fallback grid assigns coords so rooms wrap at fallback_grid_width (e.g. width=3)."""
        rooms: _MinimapRooms = [
            {"id": "r0", "map_x": None, "map_y": None},
            {"id": "r1", "map_x": None, "map_y": None},
            {"id": "r2", "map_x": None, "map_y": None},
            {"id": "r3", "map_x": None, "map_y": None},
            {"id": "r4", "map_x": None, "map_y": None},
        ]
        _apply_minimap_fallback_coordinates(rooms, current_room_id=None, is_admin=True, fallback_grid_width=3)
        assert rooms[0]["map_x"] == 0.0 and rooms[0]["map_y"] == 0.0
        assert rooms[1]["map_x"] == 1.0 and rooms[1]["map_y"] == 0.0
        assert rooms[2]["map_x"] == 2.0 and rooms[2]["map_y"] == 0.0
        assert rooms[3]["map_x"] == 0.0 and rooms[3]["map_y"] == 1.0
        assert rooms[4]["map_x"] == 1.0 and rooms[4]["map_y"] == 1.0

    def test_non_admin_gets_fallback_only_for_current_room(self) -> None:
        """Non-admin gets fallback coords only for the current room; others stay None."""
        rooms: _MinimapRooms = [
            {"id": "r0", "map_x": 1.0, "map_y": 1.0},
            {"id": "current", "map_x": None, "map_y": None},
            {"id": "r2", "map_x": None, "map_y": None},
        ]
        _apply_minimap_fallback_coordinates(rooms, current_room_id="current", is_admin=False)
        assert rooms[0]["map_x"] == 1.0
        assert rooms[0]["map_y"] == 1.0
        assert rooms[1]["map_x"] == 0.0
        assert rooms[1]["map_y"] == 0.0
        assert rooms[2]["map_x"] is None  # unchanged
        assert rooms[2]["map_y"] is None

    def test_non_admin_uses_stable_id_for_current_room_match(self) -> None:
        """Current room is matched by stable_id and receives fallback coords."""
        rooms: _MinimapRooms = [{"id": "sid_123", "stable_id": "sid_123", "map_x": None, "map_y": None}]
        _apply_minimap_fallback_coordinates(rooms, current_room_id="sid_123", is_admin=False)
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0


@pytest.mark.asyncio
async def test_resolve_current_room_from_pre_filter_list() -> None:
    """Current room resolved by id match without DB."""
    pre: _MinimapRooms = [{"id": "cur", "stable_id": "cur", "map_x": 1.0, "map_y": 1.0}]
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    execute_mock: AsyncMock = AsyncMock()
    session.execute = execute_mock
    got = await _resolve_current_room_for_minimap(pre, "cur", session)
    assert got == pre[0]
    execute_mock.assert_not_called()


@pytest.mark.asyncio
async def test_resolve_current_room_loads_when_not_in_list() -> None:
    """When not in pre-filter list, load_single_room_with_coordinates is used."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    loaded: _MinimapRoom = {"id": "x", "stable_id": "x", "map_x": 0.0, "map_y": 0.0}
    with patch(
        "server.api.map_minimap.load_single_room_with_coordinates",
        new_callable=AsyncMock,
        return_value=loaded,
    ) as load_one:
        got = await _resolve_current_room_for_minimap([], "x", session)
    assert got == loaded
    load_one.assert_awaited_once_with(session, "x")


@pytest.mark.asyncio
async def test_ensure_current_room_in_minimap_noop_without_id() -> None:
    """No current_room_id leaves rooms unchanged."""
    rooms: _MinimapRooms = [{"id": "a"}]
    await _ensure_current_room_in_minimap_rooms(rooms, [], None, AsyncMock(spec=AsyncSession))
    assert len(rooms) == 1


@pytest.mark.asyncio
async def test_ensure_current_room_in_minimap_noop_when_already_present() -> None:
    """When current room id already in list, no append."""
    rooms: _MinimapRooms = [{"id": "here", "stable_id": "here"}]
    pre: _MinimapRooms = list(rooms)
    await _ensure_current_room_in_minimap_rooms(rooms, pre, "here", AsyncMock(spec=AsyncSession))
    assert len(rooms) == 1


@pytest.mark.asyncio
async def test_ensure_current_room_in_minimap_appends_missing() -> None:
    """Missing current room is resolved and appended with fallback coords if needed."""
    rooms: _MinimapRooms = [{"id": "other"}]
    pre: _MinimapRooms = [
        {"id": "other"},
        {"id": "need", "stable_id": "need", "map_x": None, "map_y": None},
    ]
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    with patch(
        "server.api.map_minimap._resolve_current_room_for_minimap",
        new_callable=AsyncMock,
        return_value=pre[1],
    ):
        await _ensure_current_room_in_minimap_rooms(rooms, pre, "need", session)
    assert len(rooms) == 2
    assert rooms[1]["map_x"] == 0.0
    assert rooms[1]["map_y"] == 0.0


@pytest.mark.asyncio
async def test_generate_minimap_html_admin_path() -> None:
    """Admin path loads rooms, skips exploration filter, renders HTML."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    zone = MapZoneContext("p", "z", None)
    sample: _MinimapRooms = [
        {"id": "r1", "map_x": 0.0, "map_y": 0.0, "exits": cast(dict[str, object], {})},
    ]
    mock_renderer = MagicMock()
    render_map_mock: MagicMock = MagicMock(return_value="<pre>m</pre>")
    mock_renderer.render_map = render_map_mock

    with (
        patch(
            "server.api.map_minimap.load_rooms_with_coordinates",
            new_callable=AsyncMock,
            return_value=sample,
        ),
        patch("server.api.map_minimap.AsciiMapRenderer", return_value=mock_renderer),
    ):
        html = await generate_minimap_html(
            session,
            zone,
            size=3,
            current_room_id="r1",
            is_admin=True,
            player_id=None,
            exploration_service=MagicMock(),
            room_service=MagicMock(spec=RoomService),
        )
    assert html == "<pre>m</pre>"
    render_map_mock.assert_called_once()


@pytest.mark.asyncio
async def test_generate_minimap_html_non_admin_filters_exploration() -> None:
    """Non-admin with player_id applies exploration filter and ensure-current-room."""
    session: AsyncMock = AsyncMock(spec=AsyncSession)
    zone = MapZoneContext("p", "z", None)
    loaded: _MinimapRooms = [{"id": "a", "map_x": 1.0, "map_y": 1.0}]
    filtered: _MinimapRooms = [{"id": "a", "map_x": 1.0, "map_y": 1.0}]
    room_service: MagicMock = MagicMock(spec=RoomService)
    filter_mock: AsyncMock = AsyncMock(return_value=filtered)
    room_service.filter_rooms_by_exploration = filter_mock
    mock_renderer = MagicMock()
    mock_renderer.render_map = MagicMock(return_value="x")

    with (
        patch(
            "server.api.map_minimap.load_rooms_with_coordinates",
            new_callable=AsyncMock,
            return_value=loaded,
        ),
        patch("server.api.map_minimap.AsciiMapRenderer", return_value=mock_renderer),
        patch(
            "server.api.map_minimap._ensure_current_room_in_minimap_rooms",
            new_callable=AsyncMock,
        ) as ensure_mock,
    ):
        pid = uuid.uuid4()
        _ = await generate_minimap_html(
            session,
            zone,
            size=5,
            current_room_id="a",
            is_admin=False,
            player_id=pid,
            exploration_service=MagicMock(),
            room_service=room_service,
        )
    filter_mock.assert_awaited_once()
    ensure_mock.assert_awaited_once()
