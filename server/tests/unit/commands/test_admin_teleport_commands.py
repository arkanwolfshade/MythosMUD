"""Unit tests for admin teleport/goto command handlers."""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import UUID

import pytest

from server.commands.admin_teleport_commands import (
    handle_confirm_goto_command,
    handle_confirm_teleport_command,
    handle_goto_command,
    handle_teleport_command,
)

TARGET_PLAYER_ID = UUID("11111111-1111-1111-1111-111111111111")


def _request_with_services(player_service=None, connection_manager=None, persistence=None):
    app = MagicMock()
    app.state.player_service = player_service
    app.state.connection_manager = connection_manager
    app.state.persistence = persistence
    return MagicMock(app=app)


@pytest.mark.asyncio
async def test_handle_goto_missing_target():
    current = MagicMock(current_room_id="room-a")
    with patch(
        "server.commands.admin_teleport_commands.validate_goto_context",
        new_callable=AsyncMock,
        return_value=(current, None),
    ):
        result = await handle_goto_command({}, {}, _request_with_services(), None, "Admin")
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_goto_context_error():
    with patch(
        "server.commands.admin_teleport_commands.validate_goto_context",
        new_callable=AsyncMock,
        return_value=(None, {"result": "denied"}),
    ):
        result = await handle_goto_command({"target_player": "Bob"}, {}, _request_with_services(), None, "Admin")
    assert result["result"] == "denied"


@pytest.mark.asyncio
async def test_handle_goto_same_room():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-a")
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_goto_target",
            new_callable=AsyncMock,
            return_value=(target, None),
        ),
    ):
        result = await handle_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), MagicMock()),
            None,
            "Admin",
        )
    assert "already in the same location" in result["result"]


@pytest.mark.asyncio
async def test_handle_goto_success():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_goto_target",
            new_callable=AsyncMock,
            return_value=(target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_goto_teleport",
            new_callable=AsyncMock,
            return_value={"result": "You teleport to Bob's location."},
        ),
    ):
        result = await handle_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), MagicMock()),
            None,
            "Admin",
        )
    assert "teleport" in result["result"]


@pytest.mark.asyncio
async def test_handle_goto_exception_logs_failure():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_goto_target",
            new_callable=AsyncMock,
            return_value=(target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_goto_teleport",
            new_callable=AsyncMock,
            side_effect=ValueError("boom"),
        ),
        patch("server.commands.admin_teleport_commands.log_goto_failure") as log_fail,
    ):
        result = await handle_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), MagicMock()),
            None,
            "Admin",
        )
    log_fail.assert_called_once()
    assert "Failed to teleport" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_goto_missing_target():
    current = MagicMock(current_room_id="room-a")
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_goto_context",
        new_callable=AsyncMock,
        return_value=(current, None),
    ):
        result = await handle_confirm_goto_command({}, {}, _request_with_services(), None, "Admin")
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_goto_no_connection_manager():
    current = MagicMock(current_room_id="room-a")
    app = MagicMock()
    app.state.player_service = MagicMock()
    app.state.connection_manager = None
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_goto_context",
        new_callable=AsyncMock,
        return_value=(current, None),
    ):
        result = await handle_confirm_goto_command(
            {"target_player": "Bob"},
            {},
            MagicMock(app=app),
            None,
            "Admin",
        )
    assert "Connection manager" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_goto_success():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    conn = MagicMock()
    svc = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_goto",
            new_callable=AsyncMock,
            return_value=({"player_id": "1"}, target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_confirm_goto",
            new_callable=AsyncMock,
            return_value={"result": "You have successfully teleported to Bob's location."},
        ),
    ):
        result = await handle_confirm_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(svc, conn),
            None,
            "Admin",
        )
    assert "successfully teleported" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_service_unavailable(mock_resolve):
    mock_resolve.return_value = {"result": "Teleport unavailable."}
    result = await handle_teleport_command({}, {}, MagicMock(), None, "Admin")
    assert result["result"] == "Teleport unavailable."


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_missing_target(mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock())
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with patch(
        "server.commands.admin_teleport_commands.validate_admin_permission",
        new_callable=AsyncMock,
        return_value=True,
    ):
        result = await handle_teleport_command({}, {}, MagicMock(), None, "Admin")
    assert "Usage" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_not_admin(mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock())
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with patch(
        "server.commands.admin_teleport_commands.validate_admin_permission",
        new_callable=AsyncMock,
        return_value=False,
    ):
        result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(), None, "Admin")
    assert "permission" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.validate_admin_permission", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.resolve_target_player", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.resolve_teleport_direction")
@patch("server.commands.admin_teleport_commands.update_teleport_location", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.broadcast_teleport_updates", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.log_teleport_success")
@patch("server.commands.admin_teleport_commands.build_teleport_message", return_value="Teleported Bob.")
async def test_handle_teleport_success(
    mock_message,
    mock_log_success,
    mock_broadcast,
    mock_update,
    mock_direction,
    mock_resolve_target,
    mock_admin,
    mock_resolve_services,
):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock(current_room_id="admin-room"))
    mock_resolve_services.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    mock_admin.return_value = True
    mock_direction.return_value = ("target-room", "Target Room")
    mock_resolve_target.return_value = (MagicMock(current_room_id="old-room"), {"player_id": "1"})
    mock_update.return_value = "old-room"
    result = await handle_teleport_command(
        {"target_player": "Bob", "direction": "north"},
        {},
        MagicMock(app=MagicMock()),
        None,
        "Admin",
    )
    assert result["result"] == "Teleported Bob."
    mock_broadcast.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_outer_exception(mock_resolve):
    mock_resolve.side_effect = ValueError("broken")
    result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(app=MagicMock()), None, "Admin")
    assert "Error processing teleport command" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
@patch("server.commands.admin_teleport_commands.validate_admin_permission", new_callable=AsyncMock)
async def test_handle_teleport_player_not_found(mock_admin, mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=None)
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    mock_admin.return_value = True
    result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(app=MagicMock()), None, "Admin")
    assert result["result"] == "Player not found."


@pytest.mark.asyncio
async def test_handle_confirm_goto_same_room():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-a")
    conn = MagicMock()
    svc = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_goto",
            new_callable=AsyncMock,
            return_value=({"player_id": "1"}, target, None),
        ),
    ):
        result = await handle_confirm_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(svc, conn),
            None,
            "Admin",
        )
    assert "already in the same location" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_goto_exception():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    conn = MagicMock()
    svc = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_goto",
            new_callable=AsyncMock,
            return_value=({"player_id": "1"}, target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_confirm_goto",
            new_callable=AsyncMock,
            side_effect=ValueError("boom"),
        ),
        patch("server.commands.admin_teleport_commands.get_admin_actions_logger") as mock_logger_cls,
    ):
        mock_logger_cls.return_value.log_teleport_action = MagicMock()
        result = await handle_confirm_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(svc, conn),
            None,
            "Admin",
        )
    assert "Failed to teleport" in result["result"]


async def test_handle_teleport_direction_error(mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock(current_room_id="room-a"))
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_admin_permission",
            new_callable=AsyncMock,
            return_value=True,
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_teleport_direction",
            return_value={"result": "No exit north."},
        ),
    ):
        result = await handle_teleport_command(
            {"target_player": "Bob", "direction": "north"},
            {},
            MagicMock(),
            None,
            "Admin",
        )
    assert result["result"] == "No exit north."


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_target_player_error(mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock(current_room_id="room-a"))
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_admin_permission",
            new_callable=AsyncMock,
            return_value=True,
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_teleport_direction",
            return_value=("room-b", "East Wing"),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player",
            new_callable=AsyncMock,
            return_value={"result": "Player Bob not found."},
        ),
    ):
        result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(), None, "Admin")
    assert result["result"] == "Player Bob not found."


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_location_error(mock_resolve):
    player_service = MagicMock()
    player_service.get_player_by_name = AsyncMock(return_value=MagicMock(current_room_id="room-a"))
    target_player = MagicMock(current_room_id="room-c")
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_admin_permission",
            new_callable=AsyncMock,
            return_value=True,
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_teleport_direction",
            return_value=("room-b", "East Wing"),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player",
            new_callable=AsyncMock,
            return_value=(target_player, {"player_id": TARGET_PLAYER_ID}),
        ),
        patch(
            "server.commands.admin_teleport_commands.update_teleport_location",
            new_callable=AsyncMock,
            return_value={"result": "Could not update location."},
        ),
    ):
        result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(), None, "Admin")
    assert result["result"] == "Could not update location."


async def test_handle_teleport_success_with_direction(mock_resolve):
    player_service = MagicMock()
    current_player = MagicMock(current_room_id="room-a")
    target_player = MagicMock(current_room_id="room-c")
    player_service.get_player_by_name = AsyncMock(return_value=current_player)
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_admin_permission",
            new_callable=AsyncMock,
            return_value=True,
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_teleport_direction",
            return_value=("room-b", "North Alcove"),
        ) as mock_direction,
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player",
            new_callable=AsyncMock,
            return_value=(target_player, {"player_id": TARGET_PLAYER_ID}),
        ),
        patch(
            "server.commands.admin_teleport_commands.update_teleport_location",
            new_callable=AsyncMock,
            return_value="room-c",
        ),
        patch(
            "server.commands.admin_teleport_commands.broadcast_teleport_updates",
            new_callable=AsyncMock,
        ),
    ):
        result = await handle_teleport_command(
            {"target_player": "Bob", "direction": "North"},
            {},
            MagicMock(),
            None,
            "Admin",
        )
    mock_direction.assert_called_once()
    assert "north" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_teleport_commands.resolve_teleport_services", new_callable=AsyncMock)
async def test_handle_teleport_inner_exception(mock_resolve):
    player_service = MagicMock()
    current_player = MagicMock(current_room_id="room-a")
    target_player = MagicMock(current_room_id="room-c")
    player_service.get_player_by_name = AsyncMock(return_value=current_player)
    mock_resolve.return_value = (player_service, MagicMock(), MagicMock(), MagicMock())
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_admin_permission",
            new_callable=AsyncMock,
            return_value=True,
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_teleport_direction",
            return_value=("room-b", "East Wing"),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player",
            new_callable=AsyncMock,
            return_value=(target_player, {"player_id": TARGET_PLAYER_ID}),
        ),
        patch(
            "server.commands.admin_teleport_commands.update_teleport_location",
            new_callable=AsyncMock,
            side_effect=ValueError("db down"),
        ),
        patch("server.commands.admin_teleport_commands.get_admin_actions_logger") as mock_admin_logger,
    ):
        mock_admin_logger.return_value.log_teleport_action = MagicMock()
        result = await handle_teleport_command({"target_player": "Bob"}, {}, MagicMock(), None, "Admin")
    assert "Failed to teleport Bob" in result["result"]


async def test_handle_goto_resolve_target_error():
    current = MagicMock(current_room_id="room-a")
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_goto_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_goto_target",
            new_callable=AsyncMock,
            return_value=(None, {"result": "Target not online."}),
        ),
    ):
        result = await handle_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), MagicMock()),
            None,
            "Admin",
        )
    assert result["result"] == "Target not online."


@pytest.mark.asyncio
async def test_handle_confirm_teleport_context_error():
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
        new_callable=AsyncMock,
        return_value=(None, {"result": "denied"}),
    ):
        result = await handle_confirm_teleport_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(),
            None,
            "Admin",
        )
    assert result["result"] == "denied"


@pytest.mark.asyncio
async def test_handle_confirm_teleport_missing_target():
    current = MagicMock(current_room_id="room-a")
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
        new_callable=AsyncMock,
        return_value=(current, None),
    ):
        result = await handle_confirm_teleport_command({}, {}, _request_with_services(), None, "Admin")
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_teleport_no_connection_manager():
    current = MagicMock(current_room_id="room-a")
    app = MagicMock()
    app.state.player_service = MagicMock()
    app.state.connection_manager = None
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
        new_callable=AsyncMock,
        return_value=(current, None),
    ):
        result = await handle_confirm_teleport_command(
            {"target_player": "Bob"},
            {},
            MagicMock(app=app),
            None,
            "Admin",
        )
    assert "Connection manager" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_teleport_same_room():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-a")
    conn = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_teleport",
            new_callable=AsyncMock,
            return_value=({"player_id": TARGET_PLAYER_ID}, target, None),
        ),
    ):
        result = await handle_confirm_teleport_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), conn),
            None,
            "Admin",
        )
    assert "already in your location" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_teleport_success():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    conn = MagicMock()
    svc = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_teleport",
            new_callable=AsyncMock,
            return_value=({"player_id": TARGET_PLAYER_ID}, target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_confirm_teleport",
            new_callable=AsyncMock,
            return_value={"result": "Bob has been teleported to your location."},
        ),
    ):
        result = await handle_confirm_teleport_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(svc, conn),
            None,
            "Admin",
        )
    assert "teleported" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_teleport_exception():
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    conn = MagicMock()
    with (
        patch(
            "server.commands.admin_teleport_commands.validate_confirm_teleport_context",
            new_callable=AsyncMock,
            return_value=(current, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.resolve_target_player_for_teleport",
            new_callable=AsyncMock,
            return_value=({"player_id": TARGET_PLAYER_ID}, target, None),
        ),
        patch(
            "server.commands.admin_teleport_commands.execute_confirm_teleport",
            new_callable=AsyncMock,
            side_effect=ValueError("boom"),
        ),
        patch("server.commands.admin_teleport_commands.get_admin_actions_logger") as mock_admin_logger,
    ):
        mock_admin_logger.return_value.log_teleport_action = MagicMock()
        result = await handle_confirm_teleport_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(MagicMock(), conn),
            None,
            "Admin",
        )
    assert "Failed to teleport Bob" in result["result"]


@pytest.mark.asyncio
async def test_handle_confirm_goto_context_error():
    with patch(
        "server.commands.admin_teleport_commands.validate_confirm_goto_context",
        new_callable=AsyncMock,
        return_value=(None, {"result": "denied"}),
    ):
        result = await handle_confirm_goto_command(
            {"target_player": "Bob"},
            {},
            _request_with_services(),
            None,
            "Admin",
        )
    assert result["result"] == "denied"
