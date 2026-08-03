"""
Unit tests for message handlers.

Tests the message_handlers module functions.
"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi import WebSocket

from server.realtime.message_handlers import handle_chat_message, handle_command_message, handle_ping_message


@pytest.mark.asyncio
async def test_handle_command_message():
    """Test handle_command_message() delegates to handle_game_command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"command": "look", "args": []}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_command():
    """Test handle_command_message() handles missing command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    from typing import Any

    data: dict[str, Any] = {"args": []}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_args():
    """Test handle_command_message() handles missing args."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"command": "look"}

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_chat_message():
    """Test handle_chat_message() delegates to websocket_handler.handle_chat_message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"message": "Hello world"}

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "Hello world")


@pytest.mark.asyncio
async def test_handle_chat_message_no_message():
    """Test handle_chat_message() handles missing message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    from typing import Any

    data: dict[str, Any] = {}

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "")


@pytest.mark.asyncio
async def test_handle_ping_message():
    """Test handle_ping_message() sends pong response."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    from typing import Any

    data: dict[str, Any] = {}

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "pong", "data": {}}
        await handle_ping_message(mock_websocket, player_id, data)

        mock_build_event.assert_called_once_with("pong", {}, player_id=player_id)
        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_handle_ping_message_with_data():
    """Test handle_ping_message() ignores data and sends pong."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    data = {"timestamp": 1234567890}

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "pong", "data": {}}
        await handle_ping_message(mock_websocket, player_id, data)

        mock_build_event.assert_called_once_with("pong", {}, player_id=player_id)
        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_handle_client_error_report_message():
    """Test handle_client_error_report_message logs error details."""
    from server.realtime.message_handlers import handle_client_error_report_message

    mock_websocket = AsyncMock(spec=WebSocket)
    data = {"error_type": "render", "message": "boom", "context": {"panel": "stats"}}

    with patch("server.realtime.message_handlers.logger") as mock_logger:
        await handle_client_error_report_message(mock_websocket, "player_123", data)
        mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_follow_response_invalid_request_id():
    """Test follow_response without request_id returns error."""
    from server.realtime.message_handlers import handle_follow_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    with patch("server.realtime.envelope.build_event") as mock_build:
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, "player_123", {})
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_no_container():
    """Test follow_response when follow service unavailable."""
    from server.realtime.message_handlers import handle_follow_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=None),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, "player_123", {"request_id": "r1", "accept": True})
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_invalid():
    """Test party_invite_response without invite_id."""
    from server.realtime.message_handlers import handle_party_invite_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    with patch("server.realtime.envelope.build_event") as mock_build:
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", {})
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_accept():
    """Test party_invite_response accept path."""
    from unittest.mock import MagicMock

    from server.realtime.message_handlers import handle_party_invite_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    container = MagicMock()
    party_service = AsyncMock()
    party_service.accept_party_invite = AsyncMock(return_value={"result": "Joined party."})
    container.party_service = party_service

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", {"invite_id": "inv1", "accept": True})
        party_service.accept_party_invite.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_decline():
    """Test party_invite_response decline path."""
    from unittest.mock import MagicMock

    from server.realtime.message_handlers import handle_party_invite_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    container = MagicMock()
    party_service = AsyncMock()
    party_service.decline_party_invite = AsyncMock(return_value={"result": "Declined."})
    container.party_service = party_service

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", {"invite_id": "inv1", "accept": False})
        party_service.decline_party_invite.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_accept_success():
    """Test follow_response accept notifies requestor."""
    import uuid
    from unittest.mock import MagicMock

    from server.realtime.message_handlers import handle_follow_response_message

    player_id = str(uuid.uuid4())
    requestor_id = str(uuid.uuid4())
    mock_websocket = AsyncMock(spec=WebSocket)
    container = MagicMock()
    follow_service = AsyncMock()
    follow_service.accept_follow = AsyncMock(
        return_value={"success": True, "requestor_id": requestor_id, "result": "You are now following."}
    )
    container.follow_service = follow_service
    persistence = AsyncMock()
    followee = MagicMock()
    followee.name = "Followee"
    persistence.get_player_by_id = AsyncMock(return_value=followee)
    container.async_persistence = persistence

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
        patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event,
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, player_id, {"request_id": "req1", "accept": True})
        follow_service.accept_follow.assert_awaited_once()
        send_event.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_decline():
    """Test follow_response decline notifies requestor."""
    from unittest.mock import MagicMock

    from server.realtime.message_handlers import handle_follow_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    container = MagicMock()
    follow_service = AsyncMock()
    follow_service.decline_follow = AsyncMock(return_value={"requestor_id": "req-player", "result": "Declined follow."})
    container.follow_service = follow_service

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
        patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event,
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, "player_123", {"request_id": "req1", "accept": False})
        follow_service.decline_follow.assert_awaited_once()
        send_event.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_no_container():
    """Test party_invite_response when party service unavailable."""
    from server.realtime.message_handlers import handle_party_invite_response_message

    mock_websocket = AsyncMock(spec=WebSocket)
    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=None),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", {"invite_id": "inv1", "accept": True})
        mock_websocket.send_json.assert_awaited_once()
