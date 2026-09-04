"""Unit tests for goto command helper functions."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.goto_helpers import (
    execute_confirm_goto,
    execute_goto_teleport,
    log_goto_failure,
    resolve_goto_target,
    resolve_target_player_for_goto,
    validate_confirm_goto_context,
    validate_goto_context,
)


@pytest.mark.asyncio
async def test_validate_goto_context_no_app():
    player, err = await validate_goto_context(None, MagicMock(), MagicMock(), "Admin")
    assert player is None
    assert err is not None


@pytest.mark.asyncio
async def test_validate_goto_context_no_player_service():
    player, err = await validate_goto_context(MagicMock(), None, MagicMock(), "Admin")
    assert player is None
    assert "Player service" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_permission_utils.validate_admin_permission", new_callable=AsyncMock)
async def test_validate_goto_context_not_admin(mock_admin):
    mock_admin.return_value = False
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=MagicMock())
    player, err = await validate_goto_context(MagicMock(), svc, MagicMock(), "Admin")
    assert player is None
    assert "permission" in err["result"]


@pytest.mark.asyncio
async def test_validate_goto_context_player_not_found():
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=None)
    player, err = await validate_goto_context(MagicMock(), svc, MagicMock(), "Missing")
    assert player is None
    assert "not found" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_permission_utils.validate_admin_permission", new_callable=AsyncMock)
async def test_validate_goto_context_no_connection_manager(mock_admin):
    mock_admin.return_value = True
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=MagicMock())
    player, err = await validate_goto_context(MagicMock(), svc, None, "Admin")
    assert player is None
    assert "Connection manager" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_permission_utils.validate_admin_permission", new_callable=AsyncMock)
async def test_validate_goto_context_success(mock_admin):
    mock_admin.return_value = True
    current = MagicMock()
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=current)
    player, err = await validate_goto_context(MagicMock(), svc, MagicMock(), "Admin")
    assert player is current
    assert err is None


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_goto_target_offline(mock_online):
    mock_online.return_value = None
    target, err = await resolve_goto_target("Bob", MagicMock(), MagicMock())
    assert target is None
    assert "not online" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_goto_target_success(mock_online):
    mock_online.return_value = {"player_id": "1"}
    target_player = MagicMock()
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=target_player)
    target, err = await resolve_goto_target("Bob", svc, MagicMock())
    assert target is target_player
    assert err is None


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.notify_player_of_teleport", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.broadcast_teleport_effects", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.update_player_room_location", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.get_admin_actions_logger")
async def test_execute_goto_teleport_success(mock_logger_cls, mock_update, mock_broadcast, mock_notify):
    admin_logger = MagicMock()
    mock_logger_cls.return_value = admin_logger
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    svc = MagicMock()
    svc.update_player_location = AsyncMock(return_value=True)
    conn = MagicMock()
    conn.get_online_player_by_display_name.return_value = {"player_id": "uuid-1", "room_id": "room-a"}

    result = await execute_goto_teleport(svc, conn, current, target, "Bob", "Admin")

    assert "teleport" in result["result"]
    mock_broadcast.assert_awaited_once()
    mock_notify.assert_awaited_once()
    admin_logger.log_teleport_action.assert_called_once()


@pytest.mark.asyncio
async def test_execute_goto_teleport_db_failure():
    svc = MagicMock()
    svc.update_player_location = AsyncMock(return_value=False)
    result = await execute_goto_teleport(
        svc, MagicMock(), MagicMock(current_room_id="a"), MagicMock(current_room_id="b"), "Bob", "Admin"
    )
    assert "database update failed" in result["result"]


@patch("server.commands.goto_helpers.get_admin_actions_logger")
@patch("server.commands.goto_helpers.logger")
def test_log_goto_failure(mock_logger, mock_admin_cls):
    admin_logger = MagicMock()
    mock_admin_cls.return_value = admin_logger
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    log_goto_failure("Admin", "Bob", current, target, RuntimeError("boom"))
    admin_logger.log_teleport_action.assert_called_once()
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
@patch("server.commands.admin_permission_utils.validate_admin_permission", new_callable=AsyncMock)
async def test_validate_confirm_goto_context_success(mock_admin):
    mock_admin.return_value = True
    current = MagicMock()
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=current)
    player, err = await validate_confirm_goto_context(MagicMock(), svc, "Admin")
    assert player is current
    assert err is None


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_target_player_for_goto(mock_online):
    mock_online.return_value = {"player_id": "1"}
    target_player = MagicMock()
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=target_player)
    info, player, err = await resolve_target_player_for_goto("Bob", MagicMock(), svc)
    assert info == {"player_id": "1"}
    assert player is target_player
    assert err is None


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.broadcast_teleport_effects", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.update_player_room_location", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.get_admin_actions_logger")
async def test_execute_confirm_goto(mock_admin_cls, mock_update, mock_broadcast):
    admin_logger = MagicMock()
    mock_admin_cls.return_value = admin_logger
    current = MagicMock(current_room_id="room-a")
    target = MagicMock(current_room_id="room-b")
    svc = MagicMock()
    svc.update_player_location = AsyncMock(return_value=True)
    conn = MagicMock()
    conn.get_online_player_by_display_name.return_value = {"player_id": "uuid-1"}

    result = await execute_confirm_goto("Admin", current, "Bob", target, svc, conn)

    assert "successfully teleported" in result["result"]
    mock_broadcast.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_goto_target_not_in_database(mock_online):
    mock_online.return_value = {"player_id": "1"}
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=None)
    target, err = await resolve_goto_target("Bob", svc, MagicMock())
    assert target is None
    assert "not found in database" in err["result"]


@pytest.mark.asyncio
async def test_validate_confirm_goto_context_no_app():
    player, err = await validate_confirm_goto_context(None, MagicMock(), "Admin")
    assert player is None
    assert err is not None


@pytest.mark.asyncio
async def test_validate_confirm_goto_context_no_player_service():
    player, err = await validate_confirm_goto_context(MagicMock(), None, "Admin")
    assert player is None
    assert "Player service" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_permission_utils.validate_admin_permission", new_callable=AsyncMock)
async def test_validate_confirm_goto_context_not_admin(mock_admin):
    mock_admin.return_value = False
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=MagicMock())
    player, err = await validate_confirm_goto_context(MagicMock(), svc, "Admin")
    assert player is None
    assert "permission" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_target_player_for_goto_offline(mock_online):
    mock_online.return_value = None
    info, player, err = await resolve_target_player_for_goto("Bob", MagicMock(), MagicMock())
    assert info is None
    assert player is None
    assert "not online" in err["result"]


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.get_online_player_by_display_name", new_callable=AsyncMock)
async def test_resolve_target_player_for_goto_not_in_db(mock_online):
    mock_online.return_value = {"player_id": "1"}
    svc = MagicMock()
    svc.get_player_by_name = AsyncMock(return_value=None)
    info, player, err = await resolve_target_player_for_goto("Bob", MagicMock(), svc)
    assert info is None
    assert "not found in database" in err["result"]


@patch("server.commands.goto_helpers.get_admin_actions_logger")
@patch("server.commands.goto_helpers.logger")
def test_log_goto_failure_swallows_logger_error(mock_logger, mock_admin_cls):
    admin_logger = MagicMock()
    admin_logger.log_teleport_action.side_effect = OSError("log failed")
    mock_admin_cls.return_value = admin_logger
    log_goto_failure("Admin", "Bob", MagicMock(current_room_id="a"), MagicMock(current_room_id="b"), ValueError("boom"))
    mock_logger.error.assert_called_once()


@pytest.mark.asyncio
@patch("server.commands.goto_helpers.notify_player_of_teleport", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.broadcast_teleport_effects", new_callable=AsyncMock)
@patch("server.commands.goto_helpers.get_admin_actions_logger")
async def test_execute_goto_teleport_without_online_admin(mock_admin_cls, mock_broadcast, mock_notify):
    mock_admin_cls.return_value = MagicMock()
    svc = MagicMock()
    svc.update_player_location = AsyncMock(return_value=True)
    conn = MagicMock()
    conn.get_online_player_by_display_name.return_value = None
    result = await execute_goto_teleport(
        svc, conn, MagicMock(current_room_id="a"), MagicMock(current_room_id="b"), "Bob", "Admin"
    )
    assert "teleport" in result["result"]
    mock_broadcast.assert_awaited_once()


@pytest.mark.asyncio
async def test_execute_confirm_goto_db_failure():
    svc = MagicMock()
    svc.update_player_location = AsyncMock(return_value=False)
    result = await execute_confirm_goto(
        "Admin", MagicMock(current_room_id="a"), "Bob", MagicMock(current_room_id="b"), svc, MagicMock()
    )
    assert "database update failed" in result["result"]
