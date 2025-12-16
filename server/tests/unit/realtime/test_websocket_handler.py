"""
Tests for WebSocket handler.

This module tests WebSocket message processing, command handling,
and real-time communication functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.error_types import ErrorMessages, ErrorType
from server.realtime.websocket_handler import (
    _check_rate_limit,
    _handle_json_decode_error,
    _handle_websocket_disconnect,
    _is_websocket_disconnected,
    _send_error_response,
    _validate_message,
    get_help_content,
    handle_chat_message,
    handle_game_command,
    process_websocket_command,
    send_system_message,
)


class TestIsWebSocketDisconnected:
    """Test _is_websocket_disconnected helper function."""

    def test_is_websocket_disconnected_with_disconnected_message(self):
        """Test detecting WebSocket disconnected message."""
        assert _is_websocket_disconnected("WebSocket is not connected")
        assert _is_websocket_disconnected("WebSocket is not connected to client")

    def test_is_websocket_disconnected_with_accept_message(self):
        """Test detecting WebSocket accept message."""
        assert _is_websocket_disconnected('Need to call "accept" first')
        assert _is_websocket_disconnected('Need to call "accept" first before sending')

    def test_is_websocket_disconnected_with_other_error(self):
        """Test with other error messages."""
        assert not _is_websocket_disconnected("Some other error")
        assert not _is_websocket_disconnected("")


class TestCheckRateLimit:
    """Test _check_rate_limit function."""

    @pytest.mark.asyncio
    async def test_check_rate_limit_no_connection_id(self):
        """Test rate limit check when connection_id is None."""
        mock_websocket = MagicMock()
        mock_connection_manager = MagicMock()

        result = await _check_rate_limit(mock_websocket, None, "player-123", mock_connection_manager)

        assert result is True
        mock_connection_manager.rate_limiter.check_message_rate_limit.assert_not_called()

    @pytest.mark.asyncio
    async def test_check_rate_limit_passed(self):
        """Test rate limit check when limit is not exceeded."""
        mock_websocket = MagicMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.rate_limiter.check_message_rate_limit.return_value = True

        result = await _check_rate_limit(mock_websocket, "conn-123", "player-123", mock_connection_manager)

        assert result is True
        mock_websocket.send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_check_rate_limit_exceeded(self):
        """Test rate limit check when limit is exceeded."""
        import time

        mock_websocket = AsyncMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.rate_limiter.check_message_rate_limit.return_value = False
        mock_connection_manager.rate_limiter.get_message_rate_limit_info.return_value = {
            "max_attempts": 10,
            "reset_time": time.time() + 60,
        }

        with patch("server.realtime.websocket_handler.logger"):
            result = await _check_rate_limit(mock_websocket, "conn-123", "player-123", mock_connection_manager)

            assert result is False
            mock_websocket.send_json.assert_called_once()


class TestValidateMessage:
    """Test _validate_message function."""

    @pytest.mark.asyncio
    async def test_validate_message_success(self):
        """Test successful message validation."""
        mock_websocket = AsyncMock()
        mock_validator = MagicMock()
        mock_validator.parse_and_validate.return_value = {"type": "command", "data": "look"}

        result = await _validate_message(mock_websocket, '{"type": "command"}', "player-123", mock_validator)

        assert result == {"type": "command", "data": "look"}
        mock_websocket.send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_validate_message_validation_error(self):
        """Test message validation when validation fails."""
        from server.realtime.message_validator import MessageValidationError

        mock_websocket = AsyncMock()
        mock_validator = MagicMock()
        mock_validator.parse_and_validate.side_effect = MessageValidationError(
            error_type=ErrorType.INVALID_FORMAT, message="Invalid message format"
        )

        with patch("server.realtime.websocket_handler.logger"):
            result = await _validate_message(mock_websocket, "invalid json", "player-123", mock_validator)

            assert result is None
            mock_websocket.send_json.assert_called_once()


class TestSendErrorResponse:
    """Test _send_error_response function."""

    @pytest.mark.asyncio
    async def test_send_error_response_success(self):
        """Test successfully sending error response."""
        mock_websocket = AsyncMock()

        result = await _send_error_response(
            mock_websocket, ErrorType.INVALID_FORMAT, "Error message", ErrorMessages.INVALID_FORMAT, {}
        )

        assert result is True
        mock_websocket.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_error_response_websocket_disconnect(self):
        """Test sending error response when WebSocket is disconnected."""
        mock_websocket = AsyncMock()
        # The function checks if the error message contains disconnection indicators
        # WebSocketDisconnect exception itself doesn't have that message, so we need to raise RuntimeError
        mock_websocket.send_json.side_effect = RuntimeError("WebSocket is not connected")

        with patch("server.realtime.websocket_handler.logger"):
            result = await _send_error_response(
                mock_websocket, ErrorType.INVALID_FORMAT, "Error message", ErrorMessages.INVALID_FORMAT, {}
            )

            assert result is False

    @pytest.mark.asyncio
    async def test_send_error_response_runtime_error_disconnected(self):
        """Test sending error response with RuntimeError indicating disconnection."""
        mock_websocket = AsyncMock()
        mock_websocket.send_json.side_effect = RuntimeError("WebSocket is not connected")

        with patch("server.realtime.websocket_handler.logger"):
            result = await _send_error_response(
                mock_websocket, ErrorType.INVALID_FORMAT, "Error message", ErrorMessages.INVALID_FORMAT, {}
            )

            assert result is False

    @pytest.mark.asyncio
    async def test_send_error_response_runtime_error_other(self):
        """Test sending error response with other RuntimeError."""
        mock_websocket = AsyncMock()
        mock_websocket.send_json.side_effect = RuntimeError("Some other error")

        with patch("server.realtime.websocket_handler.logger"):
            result = await _send_error_response(
                mock_websocket, ErrorType.INVALID_FORMAT, "Error message", ErrorMessages.INVALID_FORMAT, {}
            )

            assert result is True


class TestHandleJsonDecodeError:
    """Test _handle_json_decode_error function."""

    @pytest.mark.asyncio
    async def test_handle_json_decode_error(self):
        """Test handling JSON decode error."""
        mock_websocket = AsyncMock()
        player_id = uuid4()

        with patch("server.realtime.websocket_handler.logger"):
            with patch("server.realtime.websocket_handler._send_error_response", new_callable=AsyncMock) as mock_send:
                await _handle_json_decode_error(mock_websocket, player_id, str(player_id))

                mock_send.assert_called_once()
                call_args = mock_send.call_args
                assert call_args[0][1] == ErrorType.INVALID_FORMAT
                assert "Invalid JSON format" in call_args[0][2]


class TestHandleWebSocketDisconnect:
    """Test _handle_websocket_disconnect function."""

    def test_handle_websocket_disconnect(self):
        """Test handling WebSocket disconnect."""
        with patch("server.realtime.websocket_handler.logger"):
            result = _handle_websocket_disconnect("player-123", "conn-123")

            assert result is True


class TestGetHelpContent:
    """Test get_help_content function."""

    def test_get_help_content_specific_command(self):
        """Test getting help for a specific command."""
        result = get_help_content("look")

        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_help_content_no_command(self):
        """Test getting general help."""
        result = get_help_content(None)

        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_help_content_empty_string(self):
        """Test getting help with empty string."""
        result = get_help_content("")

        assert isinstance(result, str)


class TestSendSystemMessage:
    """Test send_system_message function."""

    @pytest.mark.asyncio
    async def test_send_system_message_success(self):
        """Test successfully sending system message."""
        mock_websocket = AsyncMock()

        await send_system_message(mock_websocket, "Test message", "info")

        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        # build_event returns {"event_type": "system", "data": {...}}
        assert call_args["event_type"] == "system"
        assert call_args["data"]["message"] == "Test message"
        assert call_args["data"]["message_type"] == "info"

    @pytest.mark.asyncio
    async def test_send_system_message_default_type(self):
        """Test sending system message with default type."""
        mock_websocket = AsyncMock()

        await send_system_message(mock_websocket, "Test message")

        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["data"]["message_type"] == "info"

    @pytest.mark.asyncio
    async def test_send_system_message_different_types(self):
        """Test sending system message with different types."""
        for msg_type in ["info", "warning", "error", "success"]:
            mock_websocket = AsyncMock()
            await send_system_message(mock_websocket, f"Test {msg_type}", msg_type)
            call_args = mock_websocket.send_json.call_args[0][0]
            # build_event wraps the data, so check the data field
            if "data" in call_args:
                assert call_args["data"]["message_type"] == msg_type
            else:
                # Fallback: check if message_type is at top level
                assert (
                    call_args.get("message_type") == msg_type
                    or call_args.get("data", {}).get("message_type") == msg_type
                )


class TestProcessWebSocketCommand:
    """Test process_websocket_command function."""

    @pytest.mark.asyncio
    async def test_process_websocket_command_player_not_found(self):
        """Test processing command when player is not found."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_player = AsyncMock(return_value=None)

        with patch("server.realtime.websocket_handler.logger"):
            result = await process_websocket_command("look", [], "player-123", mock_connection_manager)

            assert result == {"result": "Player not found"}


class TestHandleGameCommand:
    """Test handle_game_command function."""

    @pytest.mark.asyncio
    async def test_handle_game_command_empty_command(self):
        """Test handling empty command."""
        mock_websocket = AsyncMock()
        mock_connection_manager = MagicMock()

        # Patch logger methods to avoid emoji encoding issues and other logging
        with patch("server.realtime.websocket_handler.logger") as mock_logger:
            mock_logger.info = MagicMock()
            mock_logger.debug = MagicMock()
            mock_logger.error = MagicMock()
            mock_logger.warning = MagicMock()
            # Also patch process_websocket_command to avoid complex dependencies
            with patch("server.realtime.websocket_handler.process_websocket_command", new_callable=AsyncMock):
                await handle_game_command(mock_websocket, "player-123", "", None, mock_connection_manager)

                mock_websocket.send_json.assert_called_once()
                call_args = mock_websocket.send_json.call_args[0][0]
                # The error response structure from create_websocket_error_response has error_type at top level
                assert call_args["error_type"] == "invalid_command"
                assert "Empty command" in call_args["message"]


class TestHandleChatMessage:
    """Test handle_chat_message function."""

    @pytest.mark.asyncio
    async def test_handle_chat_message_success(self):
        """Test successfully handling a chat message."""
        mock_websocket = AsyncMock()
        mock_connection_manager = MagicMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "room-123"
        mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
        mock_connection_manager.broadcast_to_room = AsyncMock()

        with patch("server.realtime.websocket_handler.build_event", return_value={"type": "chat", "data": {}}):
            await handle_chat_message(mock_websocket, "player-123", "Hello world", mock_connection_manager)

            mock_connection_manager.broadcast_to_room.assert_called_once()
            mock_websocket.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_chat_message_player_not_found(self):
        """Test handling chat message when player is not found."""
        mock_websocket = AsyncMock()
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_player = AsyncMock(return_value=None)
        mock_connection_manager.broadcast_to_room = AsyncMock()

        with patch("server.realtime.websocket_handler.build_event", return_value={"type": "chat", "data": {}}):
            with patch("server.realtime.websocket_handler.logger"):
                await handle_chat_message(mock_websocket, "player-123", "Hello world", mock_connection_manager)

                mock_connection_manager.broadcast_to_room.assert_not_called()
                mock_websocket.send_json.assert_called_once()
