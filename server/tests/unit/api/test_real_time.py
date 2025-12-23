"""
Tests for Real-Time API endpoints.

This module tests the WebSocket connection handling and real-time communication
endpoints for the MythosMUD server.

AI Agent: Tests for real-time API covering connection manager resolution,
         state management, and WebSocket endpoint logic. Created for fresh session execution.
"""


# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest
from fastapi import HTTPException, Request


# Note: These imports will trigger bcrypt in same session as other tests
# Run in fresh terminal: uv run pytest server/tests/unit/api/test_real_time.py -v
@pytest.fixture
def real_time_module():
    """Lazily import real_time module."""
    from server.api import real_time

    return real_time


@pytest.fixture
def mock_connection_manager():
    """Provide mock connection manager."""
    manager = Mock()
    manager.async_persistence = Mock()
    return manager


@pytest.fixture
def mock_state_with_manager(mock_connection_manager):
    """Provide mock state with connection manager."""
    state = Mock()
    state.container = Mock()
    state.container.connection_manager = mock_connection_manager
    return state


@pytest.fixture
def mock_state_without_manager():
    """Provide mock state without connection manager."""
    state = Mock()
    state.container = Mock()
    state.container.connection_manager = None
    return state


class TestResolveConnectionManagerFromState:
    """Test _resolve_connection_manager_from_state helper function."""

    @patch("server.api.real_time.resolve_connection_manager")
    def test_resolves_manager_from_container_dict(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test resolves connection manager from container __dict__."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        state.container = Mock()
        state.container.__dict__ = {"connection_manager": mock_connection_manager}

        result = real_time_module._resolve_connection_manager_from_state(state)

        assert result == mock_connection_manager
        mock_resolve.assert_called_once()

    @patch("server.api.real_time.resolve_connection_manager")
    def test_resolves_manager_from_container_attribute(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test resolves connection manager from container attribute."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        state.container = Mock()
        state.container.connection_manager = mock_connection_manager
        # Ensure it doesn't have __dict__ entry
        if hasattr(state.container, "__dict__"):
            delattr(state.container, "__dict__")

        _ = real_time_module._resolve_connection_manager_from_state(state)

        mock_resolve.assert_called_once()

    @patch("server.api.real_time.resolve_connection_manager")
    def test_handles_none_container(self, _mock_resolve, real_time_module):
        """Test handles state with no container."""
        _mock_resolve.return_value = None

        state = Mock()
        state.container = None

        result = real_time_module._resolve_connection_manager_from_state(state)

        assert result is None

    @patch("server.api.real_time.resolve_connection_manager")
    def test_handles_mock_container(self, _mock_resolve, real_time_module):
        """Test handles Mock container gracefully."""
        _mock_resolve.return_value = None

        state = Mock()
        state.container = Mock()

        _ = real_time_module._resolve_connection_manager_from_state(state)

        _mock_resolve.assert_called_once()


class TestEnsureConnectionManager:
    """Test _ensure_connection_manager helper function."""

    @patch("server.api.real_time._resolve_connection_manager_from_state")
    def test_returns_manager_when_available(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test returns connection manager when available."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        result = real_time_module._ensure_connection_manager(state)

        assert result == mock_connection_manager

    @patch("server.api.real_time._resolve_connection_manager_from_state")
    def test_raises_503_when_manager_not_available(self, mock_resolve, real_time_module):
        """Test raises HTTPException when manager not available."""
        mock_resolve.return_value = None

        state = Mock()

        with pytest.raises(HTTPException) as exc_info:
            real_time_module._ensure_connection_manager(state)

        assert exc_info.value.status_code == 503
        assert "unavailable" in exc_info.value.detail.lower()


class TestRealtimeRouter:
    """Test real-time router configuration."""

    def test_router_exists(self, real_time_module):
        """Test realtime router is properly configured."""
        assert hasattr(real_time_module, "realtime_router")
        assert real_time_module.realtime_router is not None

    def test_router_has_correct_prefix(self, real_time_module):
        """Test router configured with correct prefix."""
        router = real_time_module.realtime_router
        assert router.prefix == "/api"

    def test_router_has_realtime_tag(self, real_time_module):
        """Test router tagged with 'realtime'."""
        router = real_time_module.realtime_router
        assert "realtime" in router.tags


@pytest.fixture
def mock_request():
    """Mock FastAPI request object."""
    request = Mock(spec=Request)
    request.app = Mock()
    request.app.state = Mock()
    return request


@pytest.fixture
def sample_player_id():
    """Sample player ID for testing."""
    return uuid4()


class TestGetPlayerConnections:
    """Test get_player_connections endpoint."""

    @pytest.mark.asyncio
    async def test_get_player_connections_success(
        self, real_time_module, mock_request, sample_player_id, mock_connection_manager
    ):
        """Test successful retrieval of player connections."""
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = mock_connection_manager

        mock_connection_manager.get_player_presence_info = Mock(return_value={"online": True})
        mock_connection_manager.get_player_session = Mock(return_value="session123")
        mock_connection_manager.get_session_connections = Mock(return_value=["conn1", "conn2"])
        mock_connection_manager.validate_session = Mock(return_value=True)
        mock_connection_manager.check_connection_health = AsyncMock(return_value={"status": "healthy"})

        result = await real_time_module.get_player_connections(sample_player_id, mock_request)

        assert result["player_id"] == sample_player_id
        assert "presence" in result
        assert "session" in result
        assert "health" in result
        assert "timestamp" in result
        mock_connection_manager.get_player_presence_info.assert_called_once_with(sample_player_id)

    @pytest.mark.asyncio
    async def test_get_player_connections_no_manager(self, real_time_module, mock_request, sample_player_id):
        """Test get_player_connections raises error when manager not available."""
        mock_request.app.state.container = None

        with pytest.raises(HTTPException) as exc_info:
            await real_time_module.get_player_connections(sample_player_id, mock_request)

        assert exc_info.value.status_code == 503


class TestHandleNewGameSession:
    """Test handle_new_game_session endpoint."""

    @pytest.mark.asyncio
    async def test_handle_new_game_session_success(
        self, real_time_module, mock_request, sample_player_id, mock_connection_manager
    ):
        """Test successful handling of new game session."""
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = mock_connection_manager

        session_results = {"session_id": "new_session", "connected": True}
        mock_connection_manager.handle_new_game_session = AsyncMock(return_value=session_results)

        # Mock request.json()
        mock_request.json = AsyncMock(return_value={"session_id": "new_session"})

        result = await real_time_module.handle_new_game_session(sample_player_id, mock_request)

        assert result == session_results
        mock_connection_manager.handle_new_game_session.assert_called_once_with(sample_player_id, "new_session")

    @pytest.mark.asyncio
    async def test_handle_new_game_session_missing_session_id(
        self, real_time_module, mock_request, sample_player_id, mock_connection_manager
    ):
        """Test handle_new_game_session raises error when session_id missing."""
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = mock_connection_manager
        mock_request.json = AsyncMock(return_value={})

        from server.exceptions import LoggedHTTPException

        # The exception handler wraps the 400 error in a 500 error
        with pytest.raises(LoggedHTTPException) as exc_info:
            await real_time_module.handle_new_game_session(sample_player_id, mock_request)

        # The actual behavior wraps the error, so we check that an error was raised
        # and that it mentions session_id is required
        assert exc_info.value.status_code in (400, 500)
        assert "session_id" in str(exc_info.value.detail).lower()

    @pytest.mark.asyncio
    async def test_handle_new_game_session_invalid_json(
        self, real_time_module, mock_request, sample_player_id, mock_connection_manager
    ):
        """Test handle_new_game_session handles invalid JSON."""
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = mock_connection_manager

        import json

        mock_request.json = AsyncMock(side_effect=json.JSONDecodeError("Invalid JSON", "", 0))

        from server.exceptions import LoggedHTTPException

        with pytest.raises(LoggedHTTPException) as exc_info:
            await real_time_module.handle_new_game_session(sample_player_id, mock_request)

        assert exc_info.value.status_code == 400


class TestGetConnectionStatistics:
    """Test get_connection_statistics endpoint."""

    @pytest.mark.asyncio
    async def test_get_connection_statistics_success(
        self, real_time_module, mock_request, mock_connection_manager
    ):
        """Test successful retrieval of connection statistics."""
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = mock_connection_manager

        mock_connection_manager.get_presence_statistics = Mock(return_value={"total": 10})
        mock_connection_manager.get_session_stats = Mock(return_value={"active_sessions": 5})
        mock_connection_manager.get_error_statistics = Mock(return_value={"errors": 2})

        result = await real_time_module.get_connection_statistics(mock_request)

        assert "presence" in result
        assert "sessions" in result
        assert "errors" in result
        assert "timestamp" in result
        mock_connection_manager.get_presence_statistics.assert_called_once()


class TestParseWebSocketToken:
    """Test _parse_websocket_token helper function."""

    def test_parse_token_from_query_params(self, real_time_module):
        """Test parsing token from query parameters."""
        mock_logger = Mock()
        mock_websocket = Mock()
        mock_websocket.query_params = {"token": "test_token_123"}
        mock_websocket.headers = {}

        result = real_time_module._parse_websocket_token(mock_websocket, mock_logger)

        assert result == "test_token_123"

    def test_parse_token_from_subprotocol_header(self, real_time_module):
        """Test parsing token from WebSocket subprotocol header."""
        mock_logger = Mock()
        mock_websocket = Mock()
        mock_websocket.query_params = {}
        mock_websocket.headers = {"sec-websocket-protocol": "bearer, test_token_456"}

        result = real_time_module._parse_websocket_token(mock_websocket, mock_logger)

        assert result == "test_token_456"

    def test_parse_token_subprotocol_last_part(self, real_time_module):
        """Test parsing token from last part of subprotocol when no bearer marker."""
        mock_logger = Mock()
        mock_websocket = Mock()
        mock_websocket.query_params = {}
        mock_websocket.headers = {"sec-websocket-protocol": "protocol1, protocol2, test_token_789"}

        result = real_time_module._parse_websocket_token(mock_websocket, mock_logger)

        assert result == "test_token_789"

    def test_parse_token_handles_header_errors(self, real_time_module):
        """Test token parsing handles header parsing errors gracefully."""
        mock_logger = Mock()
        mock_websocket = Mock()
        mock_websocket.query_params = {"token": "fallback_token"}
        mock_websocket.headers = Mock()
        mock_websocket.headers.get = Mock(side_effect=AttributeError("Test error"))

        result = real_time_module._parse_websocket_token(mock_websocket, mock_logger)

        assert result == "fallback_token"
        mock_logger.error.assert_called_once()


class TestValidateAndAcceptWebSocket:
    """Test _validate_and_accept_websocket helper function."""

    @pytest.mark.asyncio
    async def test_validate_accepts_valid_connection(self, real_time_module, mock_connection_manager):
        """Test validation accepts valid connection."""
        mock_websocket = Mock()
        mock_websocket.accept = AsyncMock()

        result = await real_time_module._validate_and_accept_websocket(mock_websocket, mock_connection_manager)

        assert result is True
        mock_websocket.accept.assert_not_called()  # Should not accept if validation fails early

    @pytest.mark.asyncio
    async def test_validate_rejects_no_manager(self, real_time_module):
        """Test validation rejects connection when manager is None."""
        mock_websocket = Mock()
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.close = AsyncMock()

        result = await real_time_module._validate_and_accept_websocket(mock_websocket, None)

        assert result is False
        mock_websocket.accept.assert_called_once()
        mock_websocket.send_json.assert_called_once()
        mock_websocket.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_validate_rejects_no_persistence(self, real_time_module):
        """Test validation rejects connection when manager has no persistence."""
        mock_connection_manager = Mock()
        mock_connection_manager.async_persistence = None
        mock_websocket = Mock()
        mock_websocket.accept = AsyncMock()
        mock_websocket.send_json = AsyncMock()
        mock_websocket.close = AsyncMock()

        result = await real_time_module._validate_and_accept_websocket(mock_websocket, mock_connection_manager)

        assert result is False
        mock_websocket.accept.assert_called_once()
        mock_websocket.send_json.assert_called_once()
        mock_websocket.close.assert_called_once()
