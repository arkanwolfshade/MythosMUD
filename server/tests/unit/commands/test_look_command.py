"""Unit tests for look_command entry point and routing helpers."""

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


def test_get_app_and_persistence_from_container():
    """Reads async_persistence from app container."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state.container.async_persistence = MagicMock()
    app, persistence = _get_app_and_persistence(request)
    assert app is request.app
    assert persistence is request.app.state.container.async_persistence


def test_get_app_and_persistence_state_fallback():
    """Falls back to app.state.persistence when container missing."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state.container = None
    request.app.state.persistence = MagicMock()
    _, persistence = _get_app_and_persistence(request)
    assert persistence is request.app.state.persistence


@pytest.mark.asyncio
async def test_validate_look_prerequisites_no_persistence():
    """Validation fails when persistence is missing."""
    result = await _validate_look_prerequisites(None, {"username": "alice"}, "alice")
    assert result is None


@pytest.mark.asyncio
async def test_validate_look_prerequisites_room_missing():
    """Validation fails when room cannot be loaded."""
    persistence = MagicMock()
    player = MagicMock()
    player.current_room_id = "missing-room"
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.get_room_by_id.return_value = None

    result = await _validate_look_prerequisites(persistence, {"username": "alice"}, "alice")
    assert result is None


def test_get_room_drops_from_room_manager():
    """Room drops cloned from room manager list."""
    app = MagicMock()
    room_manager = MagicMock()
    room_manager.list_room_drops.return_value = [{"item_name": "lantern"}]
    app.state.container.connection_manager.room_manager = room_manager

    with patch("server.commands.look_command.clone_room_drops", side_effect=lambda drops: drops):
        drops = _get_room_drops(app, 42, "alice")

    assert drops == [{"item_name": "lantern"}]


def test_get_room_drops_no_connection_manager():
    """Returns empty list when connection manager is absent."""
    app = MagicMock()
    app.state.container = None
    app.state.connection_manager = None
    assert _get_room_drops(app, 1, "alice") == []


@pytest.mark.asyncio
async def test_setup_look_command_success():
    """Setup returns app, persistence, player, room, and drops."""
    request = MagicMock()
    request.app = MagicMock()
    persistence = MagicMock()
    player = MagicMock()
    player.current_room_id = "room-1"
    room = MagicMock()
    room.id = "room-1"
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.get_room_by_id.return_value = room
    request.app.state.container.async_persistence = persistence

    with patch("server.commands.look_command._get_room_drops", return_value=[]):
        result = await _setup_look_command(request, {"username": "alice"}, "alice")

    assert result is not None
    assert result[2] is player
    assert result[3] is room


@pytest.mark.asyncio
async def test_handle_look_command_setup_failure():
    """handle_look_command returns default message when setup fails."""
    request = MagicMock()
    with patch("server.commands.look_command._setup_look_command", new=AsyncMock(return_value=None)):
        result = await handle_look_command({}, {"username": "alice"}, request, None, "alice")
    assert result["result"] == "You see nothing special."


@pytest.mark.asyncio
async def test_handle_look_command_routes_to_room_look():
    """handle_look_command delegates to room look by default."""
    request = MagicMock()
    app = MagicMock()
    persistence = MagicMock()
    player = MagicMock()
    room = MagicMock()
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
async def test_try_direction_look_delegates():
    """_try_direction_look calls direction handler when direction set."""
    with patch(
        "server.commands.look_command._handle_direction_look",
        new=AsyncMock(return_value={"result": "You see a door to the north."}),
    ) as mock_direction:
        result = await _try_direction_look("north", MagicMock(), MagicMock(), "alice")

    mock_direction.assert_awaited_once()
    assert "north" in result["result"]


@pytest.mark.asyncio
async def test_handle_look_command_explicit_player_target():
    """handle_look_command routes explicit player targets."""
    request = MagicMock()
    app = MagicMock()
    persistence = MagicMock()
    player = MagicMock()
    room = MagicMock()
    room.id = "room-1"

    with patch(
        "server.commands.look_command._setup_look_command",
        new=AsyncMock(return_value=(app, persistence, player, room, [])),
    ):
        with patch(
            "server.commands.look_command._handle_player_look",
            new=AsyncMock(return_value={"result": "You see Armitage."}),
        ) as mock_player_look:
            result = await handle_look_command(
                {"target": "Armitage", "target_type": "player"},
                {"username": "alice"},
                request,
                None,
                "alice",
            )

    mock_player_look.assert_awaited_once()
    assert "Armitage" in result["result"]


@pytest.mark.asyncio
async def test_handle_look_command_implicit_target_not_found():
    """handle_look_command returns not-found for unknown implicit target."""
    request = MagicMock()
    app = MagicMock()
    persistence = MagicMock()
    player = MagicMock()
    room = MagicMock()
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

    assert "don't see" in result["result"]


@pytest.mark.asyncio
async def test_validate_look_prerequisites_player_not_found():
    """Validation fails when player record is missing."""
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await _validate_look_prerequisites(persistence, {"username": "ghost"}, "ghost")
    assert result is None


def test_get_room_drops_list_failure():
    """Room drop listing errors are swallowed and return empty list."""
    app = MagicMock()
    room_manager = MagicMock()
    room_manager.list_room_drops.side_effect = ValueError("bad room")
    app.state.container.connection_manager.room_manager = room_manager
    assert _get_room_drops(app, 1, "alice") == []
