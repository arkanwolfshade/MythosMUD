"""Unit tests for teleport helper functions."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.teleport_helpers import (
    broadcast_teleport_updates,
    build_teleport_message,
    execute_confirm_teleport,
    log_teleport_success,
    resolve_target_player,
    resolve_target_player_for_teleport,
    resolve_teleport_direction,
    resolve_teleport_services,
    update_player_room_location,
    update_teleport_location,
    validate_confirm_teleport_context,
)


@pytest.mark.asyncio
async def test_resolve_teleport_services_no_app():
    """Returns error when app context is missing."""
    result = await resolve_teleport_services(None, "admin")
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_resolve_teleport_services_no_player_service():
    """Returns error when player service is missing."""
    app = MagicMock()
    app.state.player_service = None
    result = await resolve_teleport_services(app, "admin")
    assert "Player service" in result["result"]


@pytest.mark.asyncio
async def test_resolve_teleport_services_success():
    """Returns service tuple when all dependencies exist."""
    app = MagicMock()
    app.state.player_service = MagicMock()
    app.state.connection_manager = MagicMock()
    app.state.persistence = MagicMock()
    result = await resolve_teleport_services(app, "admin")
    assert isinstance(result, tuple)
    assert len(result) == 4


def test_resolve_teleport_direction_no_direction():
    """No direction keeps player in current room."""
    player = MagicMock()
    player.current_room_id = "room-a"
    room_id, room_name = resolve_teleport_direction(None, MagicMock(), player, "admin")
    assert room_id == "room-a"
    assert room_name is None


def test_resolve_teleport_direction_invalid_exit():
    """Invalid direction returns error dict."""
    player = MagicMock()
    player.current_room_id = "room-a"
    persistence = MagicMock()
    room = MagicMock()
    room.exits = {}
    persistence.get_room_by_id.return_value = room
    result = resolve_teleport_direction("north", persistence, player, "admin")
    assert "no exit" in result["result"]


def test_resolve_teleport_direction_valid_exit():
    """Valid direction resolves target room id and name."""
    player = MagicMock()
    player.current_room_id = "room-a"
    persistence = MagicMock()
    admin_room = MagicMock()
    admin_room.exits = {"east": "room-b"}
    target_room = MagicMock()
    target_room.name = "East Wing"
    persistence.get_room_by_id.side_effect = lambda room_id: admin_room if room_id == "room-a" else target_room

    room_id, room_name = resolve_teleport_direction("east", persistence, player, "admin")
    assert room_id == "room-b"
    assert room_name == "East Wing"


@pytest.mark.asyncio
async def test_resolve_target_player_not_online():
    """Returns error when target is not online."""
    with patch(
        "server.commands.teleport_helpers.get_online_player_by_display_name",
        new=AsyncMock(return_value=None),
    ):
        result = await resolve_target_player(MagicMock(), MagicMock(), "Bob", MagicMock(), None)
    assert "not online" in result["result"]


@pytest.mark.asyncio
async def test_resolve_target_player_already_here():
    """Returns error when target is already in admin room."""
    current = MagicMock()
    current.current_room_id = "room-a"
    target = MagicMock()
    target.current_room_id = "room-a"
    player_service = AsyncMock()
    player_service.get_player_by_name = AsyncMock(return_value=target)

    with patch(
        "server.commands.teleport_helpers.get_online_player_by_display_name",
        new=AsyncMock(return_value={"player_id": "1"}),
    ):
        result = await resolve_target_player(player_service, MagicMock(), "Bob", current, None)

    assert "already in your location" in result["result"]


@pytest.mark.asyncio
async def test_update_teleport_location_failure():
    """Returns error when database update fails."""
    player_service = AsyncMock()
    player_service.update_player_location = AsyncMock(return_value=False)
    target = MagicMock()
    target.current_room_id = "room-a"
    result = await update_teleport_location(
        player_service, target, "Bob", "room-b", {"player_id": "1"}, MagicMock(), MagicMock()
    )
    assert "Failed to teleport" in result["result"]


@pytest.mark.asyncio
async def test_update_teleport_location_success():
    """Updates online player record and room occupancy on success."""
    player_service = AsyncMock()
    player_service.update_player_location = AsyncMock(return_value=True)
    target = MagicMock()
    target.current_room_id = "room-a"
    target.player_id = "player-1"
    connection_manager = MagicMock()
    connection_manager.online_players = {"player-1": {"current_room_id": "room-a"}}
    connection_manager.room_manager = MagicMock()

    with patch("server.commands.teleport_helpers.update_player_room_location", new=AsyncMock()) as mock_update:
        result = await update_teleport_location(
            player_service,
            target,
            "Bob",
            "room-b",
            {"player_id": "player-1"},
            connection_manager,
            MagicMock(),
        )

    assert result == "room-a"
    mock_update.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_room_location_with_persistence():
    """Room manager and persistence updated for source and destination."""
    connection_manager = MagicMock()
    connection_manager.room_manager = MagicMock()
    source_room = MagicMock()
    dest_room = MagicMock()
    persistence = MagicMock()
    persistence.get_room_by_id.side_effect = lambda room_id: source_room if room_id == "a" else dest_room

    await update_player_room_location(connection_manager, "p1", "a", "b", persistence)

    connection_manager.room_manager.remove_room_occupant.assert_called_once()
    connection_manager.room_manager.add_room_occupant.assert_called_once()
    source_room.player_left.assert_called_once_with("p1")
    dest_room.player_entered.assert_called_once_with("p1")


def test_build_teleport_message_with_direction():
    """Directional teleport message names the direction."""
    assert "north" in build_teleport_message("Bob", "north")


def test_build_teleport_message_to_admin():
    """Non-directional teleport message references admin location."""
    assert "your location" in build_teleport_message("Bob", None)


def test_log_teleport_success():
    """log_teleport_success writes admin action without raising."""
    with patch("server.commands.teleport_helpers.get_admin_actions_logger") as mock_logger_factory:
        mock_logger = MagicMock()
        mock_logger_factory.return_value = mock_logger
        log_teleport_success("Admin", "Bob", "north", "room-b", "room-a", "room-a")
    mock_logger.log_teleport_action.assert_called_once()


@pytest.mark.asyncio
async def test_validate_confirm_teleport_context_not_admin():
    """Non-admin players cannot confirm teleport."""
    app = MagicMock()
    player_service = AsyncMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock())
    app.state.player_service = player_service

    with patch("server.commands.admin_permission_utils.validate_admin_permission", new=AsyncMock(return_value=False)):
        player, error = await validate_confirm_teleport_context(app, player_service, "Bob")

    assert player is None
    assert "permission" in error["result"]


@pytest.mark.asyncio
async def test_resolve_target_player_for_teleport_success():
    """Returns target info and player when online and in database."""
    player_service = AsyncMock()
    target_player = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=target_player)
    info = {"player_id": "1"}

    with patch(
        "server.commands.teleport_helpers.get_online_player_by_display_name",
        new=AsyncMock(return_value=info),
    ):
        resolved_info, resolved_player, error = await resolve_target_player_for_teleport(
            "Bob", MagicMock(), player_service
        )

    assert error is None
    assert resolved_info is info
    assert resolved_player is target_player


@pytest.mark.asyncio
async def test_broadcast_teleport_updates():
    """Broadcast helpers invoked with opposite direction for arrivals."""
    connection_manager = MagicMock()
    with patch("server.commands.teleport_helpers.broadcast_teleport_effects", new=AsyncMock()) as mock_broadcast:
        with patch("server.commands.teleport_helpers.notify_player_of_teleport", new=AsyncMock()) as mock_notify:
            await broadcast_teleport_updates(
                connection_manager,
                {"player_id": "1"},
                "room-b",
                "Bob",
                "Admin",
                "north",
                "North Hall",
                "room-a",
            )

    mock_broadcast.assert_awaited_once()
    mock_notify.assert_awaited_once()


@pytest.mark.asyncio
async def test_execute_confirm_teleport_success():
    """execute_confirm_teleport moves target to admin room and logs action."""
    player_service = AsyncMock()
    player_service.update_player_location = AsyncMock(return_value=True)
    target_player = MagicMock()
    target_player.current_room_id = "room-a"
    current_player = MagicMock()
    current_player.current_room_id = "room-b"
    target_info = {"player_id": "target-1"}
    connection_manager = MagicMock()
    connection_manager.room_manager = MagicMock()

    with patch("server.commands.teleport_helpers.update_player_room_location", new=AsyncMock()):
        with patch("server.commands.teleport_helpers.broadcast_teleport_effects", new=AsyncMock()):
            with patch("server.commands.teleport_helpers.notify_player_of_teleport", new=AsyncMock()):
                with patch("server.commands.teleport_helpers.get_admin_actions_logger") as mock_logger_factory:
                    mock_logger_factory.return_value.log_teleport_action = MagicMock()
                    result = await execute_confirm_teleport(
                        "Bob",
                        target_player,
                        target_info,
                        current_player,
                        player_service,
                        connection_manager,
                        "Admin",
                        MagicMock(),
                    )

    assert "Successfully teleported" in result["result"]
