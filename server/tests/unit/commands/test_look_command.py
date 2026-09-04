"""Unit tests for look_command entry point and routing helpers."""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally call look_command private helpers.

from __future__ import annotations

from collections.abc import Mapping
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_command import (
    _get_app_and_persistence,
    _get_room_drops,
    _setup_look_command,
    _try_direction_look,
    _validate_look_prerequisites,
    handle_look_command,
)
from server.realtime.request_context import create_websocket_request_context


def test_get_app_and_persistence_from_container() -> None:
    """Reads async_persistence from app container."""
    persistence: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.async_persistence = persistence
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    request: MagicMock = MagicMock()
    request.app = app

    got_app, got_persistence = _get_app_and_persistence(request)
    assert got_app is app
    assert got_persistence is persistence


def test_get_app_and_persistence_state_fallback() -> None:
    """Falls back to app.state.persistence when container missing."""
    persistence: MagicMock = MagicMock()
    state: MagicMock = MagicMock()
    state.container = None
    state.persistence = persistence
    app: MagicMock = MagicMock()
    app.state = state
    request: MagicMock = MagicMock()
    request.app = app

    _, got_persistence = _get_app_and_persistence(request)
    assert got_persistence is persistence


@pytest.mark.asyncio
async def test_validate_look_prerequisites_no_persistence() -> None:
    """Validation fails when persistence is missing."""
    result = await _validate_look_prerequisites(None, {"username": "alice"}, "alice")
    assert result is None


@pytest.mark.asyncio
async def test_validate_look_prerequisites_room_missing() -> None:
    """Validation fails when room cannot be loaded."""
    player: MagicMock = MagicMock()
    player.current_room_id = "missing-room"
    get_player_by_name: AsyncMock = AsyncMock(return_value=player)
    get_room_by_id: MagicMock = MagicMock(return_value=None)
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = get_player_by_name
    persistence.get_room_by_id = get_room_by_id

    result = await _validate_look_prerequisites(persistence, {"username": "alice"}, "alice")
    assert result is None


def test_get_room_drops_from_room_manager() -> None:
    """Room drops cloned from room manager list."""
    room_drops: list[dict[str, object]] = [{"item_name": "lantern"}]
    list_room_drops: MagicMock = MagicMock(return_value=room_drops)
    room_manager: MagicMock = MagicMock()
    room_manager.list_room_drops = list_room_drops
    connection_manager: MagicMock = MagicMock()
    connection_manager.room_manager = room_manager
    container: MagicMock = MagicMock()
    container.connection_manager = connection_manager
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state

    def _identity(drops: list[dict[str, object]]) -> list[dict[str, object]]:
        return drops

    with patch("server.commands.look_command.clone_room_drops", side_effect=_identity):
        drops = _get_room_drops(app, 42, "alice")

    assert drops == [{"item_name": "lantern"}]


def test_get_room_drops_no_connection_manager() -> None:
    """Returns empty list when connection manager is absent."""
    state: MagicMock = MagicMock()
    state.container = None
    state.connection_manager = None
    app: MagicMock = MagicMock()
    app.state = state
    assert _get_room_drops(app, 1, "alice") == []


@pytest.mark.asyncio
async def test_setup_look_command_success() -> None:
    """Setup returns app, persistence, player, room, and drops."""
    player: MagicMock = MagicMock()
    player.current_room_id = "room-1"
    room: MagicMock = MagicMock()
    room.id = "room-1"
    get_player_by_name: AsyncMock = AsyncMock(return_value=player)
    get_room_by_id: MagicMock = MagicMock(return_value=room)
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = get_player_by_name
    persistence.get_room_by_id = get_room_by_id

    container: MagicMock = MagicMock()
    container.async_persistence = persistence
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    request: MagicMock = MagicMock()
    request.app = app

    with patch("server.commands.look_command._get_room_drops", return_value=[]):
        result = await _setup_look_command(request, {"username": "alice"}, "alice")

    assert result is not None
    assert result[2] is player
    assert result[3] is room


@pytest.mark.asyncio
async def test_handle_look_command_setup_failure() -> None:
    """handle_look_command returns default message when setup fails."""
    request: MagicMock = MagicMock()
    with patch("server.commands.look_command._setup_look_command", new=AsyncMock(return_value=None)):
        result = await handle_look_command({}, {"username": "alice"}, request, None, "alice")
    assert result["result"] == "You see nothing special."


@pytest.mark.asyncio
async def test_handle_look_command_routes_to_room_look() -> None:
    """handle_look_command delegates to room look by default."""
    request: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    persistence: MagicMock = MagicMock()
    player: MagicMock = MagicMock()
    room: MagicMock = MagicMock()
    room.id = "room-1"

    with patch(
        "server.commands.look_command._setup_look_command",
        new=AsyncMock(return_value=(app, persistence, player, room, [])),
    ):
        with patch(
            "server.commands.look_command._handle_room_look",
            new=AsyncMock(return_value={"result": "A dusty hall."}),
        ) as mock_room_look:
            result = await handle_look_command({}, {"username": "alice"}, request, None, "alice")

    mock_room_look.assert_awaited_once()
    assert result["result"] == "A dusty hall."


@pytest.mark.asyncio
async def test_try_direction_look_delegates() -> None:
    """_try_direction_look calls direction handler when direction set."""
    with patch(
        "server.commands.look_command._handle_direction_look",
        new=AsyncMock(return_value={"result": "You see a door to the north."}),
    ) as mock_direction:
        result = await _try_direction_look("north", MagicMock(), MagicMock(), "alice")

    mock_direction.assert_awaited_once()
    assert result is not None
    text = result["result"]
    assert isinstance(text, str)
    assert "north" in text


@pytest.mark.asyncio
async def test_handle_look_command_explicit_player_target() -> None:
    """handle_look_command routes explicit player targets."""
    request: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    persistence: MagicMock = MagicMock()
    player: MagicMock = MagicMock()
    room: MagicMock = MagicMock()
    room.id = "room-1"
    command_data: Mapping[str, object] = {"target": "Armitage", "target_type": "player"}

    with patch(
        "server.commands.look_command._setup_look_command",
        new=AsyncMock(return_value=(app, persistence, player, room, [])),
    ):
        with patch(
            "server.commands.look_command._handle_player_look",
            new=AsyncMock(return_value={"result": "You see Armitage."}),
        ) as mock_player_look:
            result = await handle_look_command(
                dict(command_data),
                {"username": "alice"},
                request,
                None,
                "alice",
            )

    mock_player_look.assert_awaited_once()
    text = result["result"]
    assert isinstance(text, str)
    assert "Armitage" in text


@pytest.mark.asyncio
async def test_handle_look_command_implicit_target_not_found() -> None:
    """handle_look_command returns not-found for unknown implicit target."""
    request: MagicMock = MagicMock()
    app: MagicMock = MagicMock()
    persistence: MagicMock = MagicMock()
    player: MagicMock = MagicMock()
    room: MagicMock = MagicMock()
    room.id = "room-1"

    with patch(
        "server.commands.look_command._setup_look_command",
        new=AsyncMock(return_value=(app, persistence, player, room, [])),
    ):
        with patch("server.commands.look_command._try_lookup_player_implicit", new=AsyncMock(return_value=None)):
            with patch("server.commands.look_command._try_lookup_npc_implicit", new=AsyncMock(return_value=None)):
                with patch("server.commands.look_command._try_lookup_item_implicit", new=AsyncMock(return_value=None)):
                    with patch(
                        "server.commands.look_command._try_lookup_container_implicit",
                        new=AsyncMock(return_value=None),
                    ):
                        result = await handle_look_command(
                            {"target": "phantom"},
                            {"username": "alice"},
                            request,
                            None,
                            "alice",
                        )

    text = result["result"]
    assert isinstance(text, str)
    assert "don't see" in text


@pytest.mark.asyncio
async def test_validate_look_prerequisites_player_not_found() -> None:
    """Validation fails when player record is missing."""
    get_player_by_name: AsyncMock = AsyncMock(return_value=None)
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = get_player_by_name
    result = await _validate_look_prerequisites(persistence, {"username": "ghost"}, "ghost")
    assert result is None


def test_get_room_drops_list_failure() -> None:
    """Room drop listing errors are swallowed and return empty list."""
    list_room_drops: MagicMock = MagicMock(side_effect=ValueError("bad room"))
    room_manager: MagicMock = MagicMock()
    room_manager.list_room_drops = list_room_drops
    connection_manager: MagicMock = MagicMock()
    connection_manager.room_manager = room_manager
    container: MagicMock = MagicMock()
    container.connection_manager = connection_manager
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    assert _get_room_drops(app, 1, "alice") == []


@pytest.mark.asyncio
async def test_handle_look_command_accepts_websocket_request_context() -> None:
    """Commands from the game client arrive over WebSocket with a duck-typed request context.

    Narrowing the request to a concrete fastapi.Request drops that context, which silently
    reduces every in-game look to "You see nothing special." Regression guard: this test
    exercises the real setup path instead of patching _setup_look_command.
    """
    player: MagicMock = MagicMock()
    player.current_room_id = "room-1"
    room: MagicMock = MagicMock()
    room.id = "room-1"
    get_player_by_name: AsyncMock = AsyncMock(return_value=player)
    get_room_by_id: MagicMock = MagicMock(return_value=room)
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = get_player_by_name
    persistence.get_room_by_id = get_room_by_id

    container: MagicMock = MagicMock()
    container.async_persistence = persistence
    app_state: MagicMock = MagicMock()
    app_state.container = container
    request = create_websocket_request_context(app_state=app_state, user={"username": "alice"})

    with (
        patch("server.commands.look_command._get_room_drops", return_value=[]),
        patch(
            "server.commands.look_command._handle_room_look",
            new=AsyncMock(return_value={"result": "A dusty hall."}),
        ),
    ):
        result = await handle_look_command({}, {"username": "alice"}, request, None, "alice")

    assert result["result"] == "A dusty hall."
