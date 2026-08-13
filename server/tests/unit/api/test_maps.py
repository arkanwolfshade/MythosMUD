# pyright: reportPrivateUsage=false
# Tests intentionally exercise maps.py helpers; those names are module-private by convention.
"""Unit tests for server.api.maps helpers (exploration filter, room id, coordinate prep)."""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import QueryParams

from server.api.map_helpers import MapZoneContext
from server.api.maps import (
    _apply_exploration_filter_if_needed,
    _ensure_coordinates_generated,
    _filter_explored_rooms,
    _get_current_room_id,
    _get_minimap_player_and_room_id,
    _get_player_and_exploration_service,
    _handle_ascii_map_error,
    _needs_coordinate_generation,
    _prepare_ascii_map_context,
)
from server.exceptions import DatabaseError, LoggedHTTPException
from server.game.room_service import RoomService
from server.models.user import User
from server.services.exploration_service import ExplorationService

_MapRoom = dict[str, object]
_MapRooms = list[_MapRoom]


@pytest.fixture
def mock_request() -> MagicMock:
    req = MagicMock(spec=Request)
    req.query_params = QueryParams()
    return req


@pytest.fixture
def mock_user_and_player() -> tuple[MagicMock, MagicMock, uuid.UUID]:
    user = MagicMock(spec=User)
    user.is_superuser = False
    user.is_admin = False
    player = MagicMock()
    player_id = uuid.uuid4()
    player.player_id = player_id
    return user, player, player_id


def _two_rooms() -> _MapRooms:
    return [
        {"id": "r1", "exits": cast(dict[str, object], {})},
        {"id": "r2", "exits": cast(dict[str, object], {})},
    ]


async def _ensure_coords_stub(ctx: object) -> _MapRooms:
    rooms = getattr(ctx, "rooms", None)
    return cast(_MapRooms, rooms if rooms is not None else [])


@pytest.mark.asyncio
async def test_filter_explored_rooms_calls_room_service() -> None:
    player_id = uuid.uuid4()
    two_rooms = _two_rooms()
    explored_only: _MapRooms = [two_rooms[0]]
    mock_room_service = MagicMock(spec=RoomService)
    filter_mock: AsyncMock = AsyncMock(return_value=explored_only)
    mock_room_service.filter_rooms_by_exploration = filter_mock

    result = await _filter_explored_rooms(
        two_rooms,
        player_id,
        MagicMock(spec=ExplorationService),
        AsyncMock(spec=AsyncSession),
        mock_room_service,
    )

    assert result == explored_only
    filter_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_prepare_ascii_map_context_applies_exploration_filter(
    mock_request: MagicMock,
    mock_user_and_player: tuple[MagicMock, MagicMock, uuid.UUID],
) -> None:
    user, player, player_id = mock_user_and_player
    two_rooms = _two_rooms()
    explored_only: _MapRooms = [two_rooms[0]]
    zone_context = MapZoneContext(plane="p", zone="zone_a", sub_zone=None)

    mock_room_service = MagicMock(spec=RoomService)
    filter_mock: AsyncMock = AsyncMock(return_value=explored_only)
    mock_room_service.filter_rooms_by_exploration = filter_mock

    with (
        patch("server.api.maps.load_rooms_with_coordinates", new_callable=AsyncMock) as load_mock,
        patch("server.api.maps._get_current_room_id", new_callable=AsyncMock) as gr,
        patch("server.api.maps._get_player_and_exploration_service", new_callable=AsyncMock) as gp,
        patch("server.api.maps._ensure_coordinates_generated", new_callable=AsyncMock) as ensure,
    ):
        load_mock.return_value = two_rooms
        gr.return_value = "r1"
        gp.return_value = (player, player_id, MagicMock(spec=ExplorationService))
        ensure.side_effect = _ensure_coords_stub

        rooms_out, cur_id = await _prepare_ascii_map_context(
            mock_request,
            zone_context,
            user,
            AsyncMock(spec=AsyncSession),
            MagicMock(),
            MagicMock(spec=ExplorationService),
            mock_room_service,
        )

    assert rooms_out == explored_only
    assert cur_id == "r1"
    filter_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_current_room_id_from_query_param(mock_request: MagicMock) -> None:
    mock_request.query_params = QueryParams("current_room_id=room_from_q")
    persistence = MagicMock()
    gpid: AsyncMock = AsyncMock()
    persistence.get_player_by_user_id = gpid
    out = await _get_current_room_id(mock_request, MagicMock(spec=User), persistence)
    assert out == "room_from_q"
    gpid.assert_not_called()


@pytest.mark.asyncio
async def test_get_current_room_id_from_player(mock_request: MagicMock) -> None:
    mock_request.query_params = QueryParams()
    cu = MagicMock(spec=User)
    cu.id = uuid.uuid4()
    pl = MagicMock()
    pl.current_room_id = "room_from_p"
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=pl)
    out = await _get_current_room_id(mock_request, cu, persistence)
    assert out == "room_from_p"


@pytest.mark.asyncio
async def test_get_current_room_id_none_when_persistence_errors(mock_request: MagicMock) -> None:
    mock_request.query_params = QueryParams()
    cu = MagicMock(spec=User)
    cu.id = uuid.uuid4()
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(side_effect=DatabaseError("db err"))
    out = await _get_current_room_id(mock_request, cu, persistence)
    assert out is None


@pytest.mark.asyncio
async def test_get_player_and_exploration_returns_none_when_no_player() -> None:
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=None)
    cu = MagicMock(spec=User)
    cu.is_admin = False
    cu.is_superuser = False
    cu.id = uuid.uuid4()
    triple = await _get_player_and_exploration_service(cu, persistence, MagicMock(spec=ExplorationService))
    p: MagicMock | None
    pid: uuid.UUID | None
    es: ExplorationService | None
    p, pid, es = cast(
        tuple[MagicMock | None, uuid.UUID | None, ExplorationService | None],
        triple,
    )
    assert p is None
    assert pid is None
    assert es is None


@pytest.mark.asyncio
async def test_apply_exploration_filter_if_needed_skips_for_superuser() -> None:
    user = MagicMock(spec=User)
    user.is_superuser = True
    rooms = _two_rooms()
    mock_rs = MagicMock(spec=RoomService)
    filter_mock: AsyncMock = AsyncMock()
    mock_rs.filter_rooms_by_exploration = filter_mock
    out = await _apply_exploration_filter_if_needed(
        rooms,
        user,
        MagicMock(),
        uuid.uuid4(),
        MagicMock(spec=ExplorationService),
        AsyncMock(spec=AsyncSession),
        mock_rs,
    )
    assert out == rooms
    filter_mock.assert_not_awaited()


@pytest.mark.asyncio
async def test_apply_exploration_filter_if_needed_calls_for_normal_user() -> None:
    user = MagicMock(spec=User)
    user.is_superuser = False
    user.is_admin = False
    rooms = _two_rooms()
    filtered: _MapRooms = [rooms[0]]
    mock_rs = MagicMock(spec=RoomService)
    filter_mock: AsyncMock = AsyncMock(return_value=filtered)
    mock_rs.filter_rooms_by_exploration = filter_mock
    out = await _apply_exploration_filter_if_needed(
        rooms,
        user,
        MagicMock(),
        uuid.uuid4(),
        MagicMock(spec=ExplorationService),
        AsyncMock(spec=AsyncSession),
        mock_rs,
    )
    assert out == filtered
    filter_mock.assert_awaited_once()


def test_needs_coordinate_generation_true_when_missing() -> None:
    rooms: _MapRooms = [{"id": "a", "map_x": None, "map_y": None}]
    assert _needs_coordinate_generation(rooms) is True


def test_needs_coordinate_generation_false_when_present() -> None:
    rooms: _MapRooms = [{"id": "a", "map_x": 1, "map_y": 2}]
    assert _needs_coordinate_generation(rooms) is False


def test_handle_ascii_map_error_raises_logged_http() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _handle_ascii_map_error(RuntimeError("boom"), "p", "z", None)
    assert ei.value.status_code == 500


@pytest.mark.asyncio
async def test_get_minimap_player_and_room_id_requires_auth(mock_request: MagicMock) -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        await _get_minimap_player_and_room_id(mock_request, None, MagicMock())
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_get_minimap_player_and_room_id_success(mock_request: MagicMock) -> None:
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    player = MagicMock()
    player.current_room_id = "room_from_db"
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=player)
    player_out, room_id = await _get_minimap_player_and_room_id(mock_request, user, persistence)
    assert player_out is player
    assert room_id == "room_from_db"


@pytest.mark.asyncio
async def test_ensure_coordinates_generated_when_missing(
    mock_user_and_player: tuple[MagicMock, MagicMock, uuid.UUID],
) -> None:
    user, player, player_id = mock_user_and_player
    rooms: _MapRooms = [{"id": "a", "map_x": None, "map_y": None}]
    zone_ctx = MapZoneContext(plane="p", zone="z", sub_zone=None)
    reloaded: _MapRooms = [{"id": "a", "map_x": 1, "map_y": 2}]
    generator = MagicMock()
    generator.generate_coordinates_for_zone = AsyncMock()
    with (
        patch("server.api.maps.CoordinateGenerator", return_value=generator),
        patch("server.api.maps.load_rooms_with_coordinates", new_callable=AsyncMock, return_value=reloaded),
        patch("server.api.maps._apply_exploration_filter_if_needed", new_callable=AsyncMock, return_value=reloaded),
    ):
        out = await _ensure_coordinates_generated(
            AsyncMock(spec=AsyncSession),
            zone_ctx,
            rooms,
            player,
            player_id,
            MagicMock(spec=ExplorationService),
            user,
            MagicMock(spec=RoomService),
        )
    assert out == reloaded
    generator.generate_coordinates_for_zone.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_ascii_map_renders_html(mock_request: MagicMock) -> None:
    rooms: _MapRooms = [{"id": "a", "map_x": 1, "map_y": 2, "exits": {}}]
    with (
        patch("server.api.maps._prepare_ascii_map_context", new_callable=AsyncMock, return_value=(rooms, "a")),
        patch("server.api.maps.AsciiMapRenderer") as renderer_cls,
    ):
        renderer_cls.return_value.render_map.return_value = "<pre>map</pre>"
        from server.api.maps import get_ascii_map

        response = await get_ascii_map(
            mock_request,
            plane="p",
            zone="z",
            sub_zone=None,
            viewport_x=0,
            viewport_y=0,
            viewport_width=80,
            viewport_height=24,
            current_user=None,
            session=AsyncMock(spec=AsyncSession),
            persistence=MagicMock(),
            exploration_service=MagicMock(spec=ExplorationService),
            room_service=MagicMock(spec=RoomService),
        )
    assert "map" in response.map_html


@pytest.mark.asyncio
async def test_get_ascii_minimap_requires_auth(mock_request: MagicMock) -> None:
    from server.api.maps import get_ascii_minimap

    with pytest.raises(LoggedHTTPException) as ei:
        await get_ascii_minimap(
            mock_request,
            plane="p",
            zone="z",
            sub_zone=None,
            current_user=None,
            session=AsyncMock(spec=AsyncSession),
            persistence=MagicMock(),
            exploration_service=MagicMock(spec=ExplorationService),
            room_service=MagicMock(spec=RoomService),
        )
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_get_ascii_minimap_success(mock_request: MagicMock) -> None:
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    user.is_admin = False
    user.is_superuser = False
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "room_a"
    persistence = MagicMock()
    persistence.get_player_by_user_id = AsyncMock(return_value=player)
    with patch("server.api.maps.generate_minimap_html", new_callable=AsyncMock, return_value="<pre>mini</pre>"):
        from server.api.maps import get_ascii_minimap

        response = await get_ascii_minimap(
            mock_request,
            plane="p",
            zone="z",
            sub_zone=None,
            size=5,
            current_user=user,
            session=AsyncMock(spec=AsyncSession),
            persistence=persistence,
            exploration_service=MagicMock(spec=ExplorationService),
            room_service=MagicMock(spec=RoomService),
        )
    assert "mini" in response.map_html


@pytest.mark.asyncio
async def test_recalculate_coordinates_admin(mock_request: MagicMock) -> None:
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    generator = MagicMock()
    generator.generate_coordinates_for_zone = AsyncMock(return_value={"coordinates": [{"x": 1}]})
    validator = MagicMock()
    validator.validate_coordinates = AsyncMock(return_value={"conflicts": [], "conflict_count": 0, "valid": True})
    with (
        patch("server.api.maps.get_admin_auth_service", return_value=auth),
        patch("server.api.maps.CoordinateGenerator", return_value=generator),
        patch("server.api.maps.CoordinateValidator", return_value=validator),
    ):
        from server.api.maps import recalculate_coordinates

        response = await recalculate_coordinates(
            mock_request,
            plane="p",
            zone="z",
            sub_zone=None,
            current_user=user,
            session=AsyncMock(spec=AsyncSession),
        )
    assert response.coordinates_generated == 1


@pytest.mark.asyncio
async def test_recalculate_coordinates_requires_auth(mock_request: MagicMock) -> None:
    from server.api.maps import recalculate_coordinates

    with pytest.raises(LoggedHTTPException) as ei:
        await recalculate_coordinates(
            mock_request,
            plane="p",
            zone="z",
            sub_zone=None,
            current_user=None,
            session=AsyncMock(spec=AsyncSession),
        )
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_set_map_origin_requires_auth(mock_request: MagicMock) -> None:
    from server.api.maps import SetOriginRequest, set_map_origin

    with pytest.raises(LoggedHTTPException) as ei:
        await set_map_origin(
            "room-a",
            SetOriginRequest(plane="p", zone="z", sub_zone=None),
            mock_request,
            current_user=None,
            session=AsyncMock(spec=AsyncSession),
        )
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_set_map_origin_success(mock_request: MagicMock) -> None:
    user = MagicMock(spec=User)
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    session = AsyncMock(spec=AsyncSession)
    session.execute = AsyncMock(side_effect=[MagicMock(scalar=lambda: True), MagicMock()])
    session.commit = AsyncMock()
    generator = MagicMock()
    generator.generate_coordinates_for_zone = AsyncMock(return_value={"coordinates": [{"x": 1}, {"x": 2}]})
    validator = MagicMock()
    validator.validate_coordinates = AsyncMock(return_value={"conflicts": [], "conflict_count": 0, "valid": True})
    with (
        patch("server.api.maps.get_admin_auth_service", return_value=auth),
        patch("server.api.maps.CoordinateGenerator", return_value=generator),
        patch("server.api.maps.CoordinateValidator", return_value=validator),
    ):
        from server.api.maps import SetOriginRequest, set_map_origin

        response = await set_map_origin(
            "room-a",
            SetOriginRequest(plane="p", zone="z", sub_zone="sz"),
            mock_request,
            current_user=user,
            session=session,
        )
    assert response.room_id == "room-a"
    assert response.coordinates_generated == 2
