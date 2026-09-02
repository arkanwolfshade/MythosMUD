"""
Unit tests for message handlers.

Tests the message_handlers module functions. Handlers take validated, typed envelope
messages (see `server/schemas/realtime/websocket_messages.py`, `#765`), not raw dicts.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket

from server.realtime.message_handlers import (
    handle_chat_message,
    handle_client_error_report_message,
    handle_command_message,
    handle_follow_response_message,
    handle_party_invite_response_message,
    handle_ping_message,
)
from server.schemas.realtime.websocket_messages import (
    ChatData,
    ChatMessage,
    ClientErrorReportData,
    ClientErrorReportMessage,
    CommandData,
    FollowResponseData,
    FollowResponseMessage,
    GameCommandMessage,
    PartyInviteResponseData,
    PartyInviteResponseMessage,
    PingMessage,
)


@pytest.mark.asyncio
async def test_handle_command_message():
    """Test handle_command_message() delegates to handle_game_command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = GameCommandMessage(type="game_command", data=CommandData(command="look", args=[]))

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_command():
    """Test handle_command_message() handles missing command."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = GameCommandMessage(type="game_command", data=CommandData(args=[]))

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "", [])


@pytest.mark.asyncio
async def test_handle_command_message_no_args():
    """Test handle_command_message() handles missing args."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = GameCommandMessage(type="game_command", data=CommandData(command="look"))

    with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle:
        await handle_command_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "look", [])


@pytest.mark.asyncio
async def test_handle_chat_message():
    """Test handle_chat_message() delegates to websocket_handler.handle_chat_message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = ChatMessage(type="chat", data=ChatData(message="Hello world"))

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "Hello world")


@pytest.mark.asyncio
async def test_handle_chat_message_no_message():
    """Test handle_chat_message() handles missing message."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = ChatMessage(type="chat")

    with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle:
        await handle_chat_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, "")


@pytest.mark.asyncio
async def test_handle_ping_message():
    """Test handle_ping_message() sends pong response."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = "player_123"
    message = PingMessage(type="ping")

    with patch("server.realtime.envelope.build_event") as mock_build_event:
        mock_build_event.return_value = {"type": "pong", "data": {}}
        await handle_ping_message(mock_websocket, player_id, message)

        mock_build_event.assert_called_once_with("pong", {}, player_id=player_id)
        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_handle_client_error_report_message():
    """Test handle_client_error_report_message logs error details."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = ClientErrorReportMessage(
        type="client_error_report",
        data=ClientErrorReportData(error_type="render", message="boom", context={"panel": "stats"}),
    )

    with patch("server.realtime.message_handlers.logger") as mock_logger:
        await handle_client_error_report_message(mock_websocket, "player_123", message)
        mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_follow_response_invalid_request_id():
    """Test follow_response without request_id returns error."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = FollowResponseMessage(type="follow_response")
    with patch("server.realtime.envelope.build_event") as mock_build:
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, "player_123", message)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_no_container():
    """Test follow_response when follow service unavailable."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = FollowResponseMessage(type="follow_response", data=FollowResponseData(request_id="r1", accept=True))
    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=None),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_follow_response_message(mock_websocket, "player_123", message)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_invalid():
    """Test party_invite_response without invite_id."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = PartyInviteResponseMessage(type="party_invite_response")
    with patch("server.realtime.envelope.build_event") as mock_build:
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", message)
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_accept():
    """Test party_invite_response accept path."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = PartyInviteResponseMessage(
        type="party_invite_response", data=PartyInviteResponseData(invite_id="inv1", accept=True)
    )
    container = MagicMock()
    party_service = AsyncMock()
    party_service.accept_party_invite = AsyncMock(return_value={"result": "Joined party."})
    container.party_service = party_service

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", message)
        party_service.accept_party_invite.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_decline():
    """Test party_invite_response decline path."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = PartyInviteResponseMessage(
        type="party_invite_response", data=PartyInviteResponseData(invite_id="inv1", accept=False)
    )
    container = MagicMock()
    party_service = AsyncMock()
    party_service.decline_party_invite = AsyncMock(return_value={"result": "Declined."})
    container.party_service = party_service

    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=container),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", message)
        party_service.decline_party_invite.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_accept_success():
    """Test follow_response accept notifies requestor."""
    import uuid

    player_id = str(uuid.uuid4())
    requestor_id = str(uuid.uuid4())
    mock_websocket = AsyncMock(spec=WebSocket)
    message = FollowResponseMessage(type="follow_response", data=FollowResponseData(request_id="req1", accept=True))
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
        await handle_follow_response_message(mock_websocket, player_id, message)
        follow_service.accept_follow.assert_awaited_once()
        send_event.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_follow_response_decline():
    """Test follow_response decline notifies requestor."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = FollowResponseMessage(type="follow_response", data=FollowResponseData(request_id="req1", accept=False))
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
        await handle_follow_response_message(mock_websocket, "player_123", message)
        follow_service.decline_follow.assert_awaited_once()
        send_event.assert_awaited_once()
        mock_websocket.send_json.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_party_invite_response_no_container():
    """Test party_invite_response when party service unavailable."""
    mock_websocket = AsyncMock(spec=WebSocket)
    message = PartyInviteResponseMessage(
        type="party_invite_response", data=PartyInviteResponseData(invite_id="inv1", accept=True)
    )
    with (
        patch("server.realtime.envelope.build_event") as mock_build,
        patch("server.container.get_container", return_value=None),
    ):
        mock_build.return_value = {"type": "command_response"}
        await handle_party_invite_response_message(mock_websocket, "player_123", message)
        mock_websocket.send_json.assert_awaited_once()
