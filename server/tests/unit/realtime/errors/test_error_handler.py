"""
Tests for Connection Error Handler.

This module tests the error handling component for connection management,
including error detection, logging, and recovery mechanisms.

AI Agent: Tests for ConnectionErrorHandler covering error classification,
         fatal error handling, and error recovery with mocked callbacks.
"""


# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.realtime.errors.error_handler import (
    CRITICAL_WEBSOCKET_ERRORS,
    FATAL_ERROR_TYPES,
    ConnectionErrorHandler,
)


@pytest.fixture
def mock_callbacks():
    """Provide mock callback functions for error handler."""
    return {
        "force_disconnect": AsyncMock(),
        "disconnect_connection": AsyncMock(return_value=True),
        "cleanup_dead_connections": AsyncMock(return_value={"connections_cleaned": 2}),
        "get_player_session": Mock(return_value="session123"),
        "get_session_connections_callback": Mock(return_value=["conn1", "conn2"]),
        "get_player_websockets": Mock(return_value=["ws1", "ws2"]),
        "get_online_players": Mock(return_value={}),
        "get_session_connections_dict": Mock(return_value={}),
        "get_player_sessions": Mock(return_value={}),
    }


@pytest.fixture
def error_handler(mock_callbacks):
    """Provide ConnectionErrorHandler instance for testing."""
    return ConnectionErrorHandler(
        force_disconnect_callback=mock_callbacks["force_disconnect"],
        disconnect_connection_callback=mock_callbacks["disconnect_connection"],
        cleanup_dead_connections_callback=mock_callbacks["cleanup_dead_connections"],
        get_player_session_callback=mock_callbacks["get_player_session"],
        get_session_connections_callback=mock_callbacks["get_session_connections_callback"],
        get_player_websockets=mock_callbacks["get_player_websockets"],
        get_online_players=mock_callbacks["get_online_players"],
        get_session_connections=mock_callbacks["get_session_connections_dict"],
        get_player_sessions=mock_callbacks["get_player_sessions"],
    )


@pytest.fixture
def sample_player_id():
    """Provide sample player ID for testing."""
    return uuid.UUID("12345678-1234-5678-1234-567812345678")


class TestConnectionErrorHandlerInit:
    """Test ConnectionErrorHandler initialization."""

    def test_initialization(self, error_handler, mock_callbacks):
        """Test error handler initializes with all callbacks."""
        assert error_handler.force_disconnect == mock_callbacks["force_disconnect"]
        assert error_handler.disconnect_connection == mock_callbacks["disconnect_connection"]
        assert error_handler.cleanup_dead_connections == mock_callbacks["cleanup_dead_connections"]
        assert error_handler.get_player_session == mock_callbacks["get_player_session"]
        assert error_handler.get_session_connections == mock_callbacks["get_session_connections_callback"]
        assert error_handler.get_player_websockets == mock_callbacks["get_player_websockets"]
        assert error_handler.get_online_players == mock_callbacks["get_online_players"]
        assert error_handler.get_session_connections_dict == mock_callbacks["get_session_connections_dict"]
        assert error_handler.get_player_sessions == mock_callbacks["get_player_sessions"]


class TestDetectAndHandleErrorState:
    """Test error state detection and handling."""

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_fatal_error_terminates_all_connections(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test fatal errors terminate all player connections."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.detect_and_handle_error_state(
            player_id=sample_player_id,
            error_type="AUTHENTICATION_FAILURE",
            error_details="Invalid token",
            connection_id="conn1",
        )

        assert result["fatal_error"] is True
        assert result["success"] is True
        assert result["connections_terminated"] == 2
        assert result["connections_kept"] == 0
        mock_callbacks["force_disconnect"].assert_called_once_with(sample_player_id)

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_connection_specific_error_terminates_one_connection(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test connection-specific non-fatal errors disconnect only that connection."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.detect_and_handle_error_state(
            player_id=sample_player_id, error_type="WEBSOCKET_ERROR", error_details="Frame error", connection_id="conn1"
        )

        assert result["fatal_error"] is False
        assert result["success"] is True
        assert result["connections_terminated"] == 1
        assert result["connections_kept"] == 1
        mock_callbacks["disconnect_connection"].assert_called_once_with("conn1")

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_non_fatal_error_without_connection_id_keeps_all(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id
    ):
        """Test non-fatal errors without connection ID keep all connections."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.detect_and_handle_error_state(
            player_id=sample_player_id, error_type="MINOR_ERROR", error_details="Non-critical issue"
        )

        assert result["fatal_error"] is False
        assert result["success"] is True
        assert result["connections_terminated"] == 0
        assert result["connections_kept"] == 2


class TestHandleWebSocketError:
    """Test WebSocket error handling."""

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_critical_websocket_error_is_fatal(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test critical WebSocket errors are treated as fatal."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.handle_websocket_error(
            player_id=sample_player_id,
            connection_id="conn1",
            error_type="CONNECTION_CLOSED_UNEXPECTEDLY",
            error_details="Unexpected close",
        )

        assert result["fatal_error"] is True
        mock_callbacks["force_disconnect"].assert_called_once()

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_non_critical_websocket_error_disconnects_connection(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test non-critical WebSocket errors disconnect specific connection."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.handle_websocket_error(
            player_id=sample_player_id,
            connection_id="conn1",
            error_type="NORMAL_CLOSE",
            error_details="Client closed connection",
        )

        assert result["fatal_error"] is False
        assert result["connections_terminated"] == 1
        mock_callbacks["disconnect_connection"].assert_called_once_with("conn1")


class TestHandleAuthenticationError:
    """Test authentication error handling."""

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_authentication_error_is_fatal(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test authentication errors are treated as fatal."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.handle_authentication_error(
            player_id=sample_player_id, error_type="INVALID_TOKEN", error_details="Token expired"
        )

        assert result["fatal_error"] is True
        mock_callbacks["force_disconnect"].assert_called_once()


class TestHandleSecurityViolation:
    """Test security violation handling."""

    @pytest.mark.asyncio
    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    @patch("builtins.open", create=True)
    async def test_security_violation_is_fatal(
        self, _mock_open, mock_resolve_log_base, mock_get_config, error_handler, sample_player_id, mock_callbacks
    ):
        """Test security violations are treated as fatal."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        result = await error_handler.handle_security_violation(
            player_id=sample_player_id, violation_type="INJECTION_ATTEMPT", violation_details="SQL injection detected"
        )

        assert result["fatal_error"] is True
        mock_callbacks["force_disconnect"].assert_called_once()


class TestRecoverFromError:
    """Test error recovery mechanisms."""

    @pytest.mark.asyncio
    async def test_full_recovery_cleans_connections_and_sessions(self, error_handler, sample_player_id, mock_callbacks):
        """Test FULL recovery cleans both connections and sessions."""
        # Setup: player has session and connections
        mock_callbacks["get_player_sessions"].return_value = {sample_player_id: "session123"}
        mock_callbacks["get_session_connections_dict"].return_value = {"session123": ["conn1"]}

        result = await error_handler.recover_from_error(player_id=sample_player_id, recovery_type="FULL")

        assert result["success"] is True
        assert result["connections_restored"] == 2
        assert result["sessions_cleared"] == 1
        mock_callbacks["cleanup_dead_connections"].assert_called_once()

    @pytest.mark.asyncio
    async def test_connections_only_recovery(self, error_handler, sample_player_id, mock_callbacks):
        """Test CONNECTIONS_ONLY recovery only cleans connections."""
        result = await error_handler.recover_from_error(player_id=sample_player_id, recovery_type="CONNECTIONS_ONLY")

        assert result["success"] is True
        assert result["connections_restored"] == 2
        assert result["sessions_cleared"] == 0
        mock_callbacks["cleanup_dead_connections"].assert_called_once()


class TestGetErrorStatistics:
    """Test error statistics retrieval."""

    @patch("server.realtime.errors.error_handler.get_config")
    @patch("server.realtime.errors.error_handler._resolve_log_base")
    def test_get_error_statistics(self, mock_resolve_log_base, mock_get_config, error_handler):
        """Test error statistics calculation."""
        from pathlib import Path

        mock_get_config.return_value.logging.log_base = "logs"
        mock_get_config.return_value.logging.environment = "test"
        mock_resolve_log_base.return_value = Path("logs")

        player1 = uuid.uuid4()
        player2 = uuid.uuid4()
        online_players = {player1: {"name": "Player1"}, player2: {"name": "Player2"}}
        player_websockets = {player1: ["ws1", "ws2"], player2: ["ws3"]}

        stats = error_handler.get_error_statistics(online_players, player_websockets)

        assert stats["total_players"] == 2
        assert stats["total_connections"] == 3
        assert "error_log_path" in stats


class TestFatalErrorTypeConstants:
    """Test fatal error type constants are properly defined."""

    def test_fatal_error_types_exist(self) -> None:
        """Test FATAL_ERROR_TYPES constant is defined."""
        assert isinstance(FATAL_ERROR_TYPES, list)
        assert "AUTHENTICATION_FAILURE" in FATAL_ERROR_TYPES
        assert "SECURITY_VIOLATION" in FATAL_ERROR_TYPES

    def test_critical_websocket_errors_exist(self) -> None:
        """Test CRITICAL_WEBSOCKET_ERRORS constant is defined."""
        assert isinstance(CRITICAL_WEBSOCKET_ERRORS, list)
        assert "CONNECTION_CLOSED_UNEXPECTEDLY" in CRITICAL_WEBSOCKET_ERRORS
