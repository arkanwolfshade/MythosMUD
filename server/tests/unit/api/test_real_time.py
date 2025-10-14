"""
Tests for api/real_time.py module.

Tests the real-time API endpoints including WebSocket connections,
Server-Sent Events, and authentication flows.
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import HTTPException, Request, WebSocket
from fastapi.responses import StreamingResponse

from server.api.real_time import (
    realtime_router,
    sse_events,
    sse_events_token,
    websocket_endpoint,
    websocket_endpoint_route,
)


class TestSSEEvents:
    """Test SSE events endpoint."""

    @pytest.mark.asyncio
    async def test_sse_events_success(self):
        """Test successful SSE events endpoint."""
        # Mock the request
        mock_request = Mock(spec=Request)
        mock_request.query_params = Mock()
        mock_request.query_params.get.return_value = None  # No session_id

        # Mock the game_event_stream function
        with patch("server.api.real_time.game_event_stream") as mock_stream:
            mock_stream.return_value = ["event1", "event2"]

            # Call the endpoint
            response = await sse_events("test_player", mock_request)

            # Verify response
            assert isinstance(response, StreamingResponse)
            assert response.media_type == "text/event-stream"
            assert response.headers["Cache-Control"] == "no-cache"
            assert response.headers["Connection"] == "keep-alive"
            assert response.headers["Access-Control-Allow-Origin"] == "*"
            assert response.headers["Access-Control-Allow-Headers"] == "Cache-Control"

            # Verify the stream was called with correct player_id and session_id
            mock_stream.assert_called_once_with("test_player", None)


class TestSSEEventsToken:
    """Test token-authenticated SSE events endpoint."""

    @pytest.mark.asyncio
    async def test_sse_events_token_success(self):
        """Test successful token-authenticated SSE events."""
        # Mock the request with valid token
        mock_request = Mock(spec=Request)
        mock_request.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.game_event_stream") as mock_stream,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "test_player_id"
            mock_persistence.get_player_by_user_id.return_value = mock_player
            mock_stream.return_value = ["event1", "event2"]
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            response = await sse_events_token(mock_request)

            # Verify response
            assert isinstance(response, StreamingResponse)
            assert response.media_type == "text/event-stream"
            assert response.headers["Cache-Control"] == "no-cache"
            assert response.headers["Connection"] == "keep-alive"
            assert response.headers["Access-Control-Allow-Origin"] == "*"
            assert response.headers["Access-Control-Allow-Headers"] == "Cache-Control"

            # Verify the stream was called with correct player_id and session_id
            mock_stream.assert_called_once_with("test_player_id", None)
            mock_logger.info.assert_called_once_with(
                "SSE connection attempt for player test_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_sse_events_token_missing_token(self):
        """Test SSE events with missing token."""
        # Mock the request without token
        mock_request = Mock(spec=Request)
        mock_request.query_params = {}

        # Mock decode_access_token to return None
        with patch("server.api.real_time.decode_access_token") as mock_decode:
            mock_decode.return_value = None

            # Call the endpoint and expect HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await sse_events_token(mock_request)

            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Invalid or missing token"

    @pytest.mark.asyncio
    async def test_sse_events_token_invalid_token_no_sub(self):
        """Test SSE events with invalid token (no 'sub' field)."""
        # Mock the request with token
        mock_request = Mock(spec=Request)
        mock_request.query_params = {"token": "invalid_token"}

        # Mock decode_access_token to return payload without 'sub'
        with patch("server.api.real_time.decode_access_token") as mock_decode:
            mock_decode.return_value = {"other_field": "value"}

            # Call the endpoint and expect HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await sse_events_token(mock_request)

            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Invalid or missing token"

    @pytest.mark.asyncio
    async def test_sse_events_token_no_player_record(self):
        """Test SSE events when user has no player record."""
        # Mock the request with valid token
        mock_request = Mock(spec=Request)
        mock_request.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_persistence.get_player_by_user_id.return_value = None

            # Call the endpoint and expect HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await sse_events_token(mock_request)

            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "User has no player record"


class TestWebSocketEndpoint:
    """Test WebSocket endpoint."""

    @pytest.mark.asyncio
    async def test_websocket_endpoint_success_with_token(self):
        """Test successful WebSocket connection with valid token."""
        # Mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "test_player_id"
            mock_persistence.get_player_by_user_id.return_value = mock_player
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint(mock_websocket)

            # Verify handle_websocket_connection was called with correct parameters
            mock_handle.assert_called_once_with(mock_websocket, "test_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket connection attempt for player test_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_success_with_player_id_fallback(self):
        """Test successful WebSocket connection with player_id fallback."""
        # Mock WebSocket with player_id but no valid token
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token", "player_id": "test_player_id"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = None  # Invalid token
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "test_player_id"
            mock_persistence.get_player.return_value = mock_player
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint(mock_websocket)

            # Verify handle_websocket_connection was called with player_id from query params
            mock_handle.assert_called_once_with(mock_websocket, "test_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket connection attempt for player test_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_no_token_no_player_id(self):
        """Test WebSocket endpoint with no token and no player_id."""
        # Mock WebSocket without token or player_id
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}

        # Mock decode_access_token to return None
        with patch("server.api.real_time.decode_access_token") as mock_decode:
            mock_decode.return_value = None

            # Call the endpoint and expect HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await websocket_endpoint(mock_websocket)

            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "Invalid or missing token"

    @pytest.mark.asyncio
    async def test_websocket_endpoint_no_player_record(self):
        """Test WebSocket endpoint when user has no player record."""
        # Mock WebSocket with valid token
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_persistence.get_player_by_user_id.return_value = None

            # Call the endpoint and expect HTTPException
            with pytest.raises(HTTPException) as exc_info:
                await websocket_endpoint(mock_websocket)

            assert exc_info.value.status_code == 401
            assert exc_info.value.detail == "User has no player record"

    @pytest.mark.asyncio
    async def test_websocket_endpoint_handle_websocket_connection_exception(self):
        """Test WebSocket endpoint when handle_websocket_connection raises an exception."""
        # Mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "test_player_id"
            mock_persistence.get_player_by_user_id.return_value = mock_player
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Make handle_websocket_connection raise an exception
            test_exception = Exception("Test exception")
            mock_handle.side_effect = test_exception

            # Call the endpoint and expect the exception to be re-raised
            with pytest.raises(Exception) as exc_info:
                await websocket_endpoint(mock_websocket)

            assert exc_info.value == test_exception
            mock_logger.error.assert_called_once_with(
                "Error in WebSocket endpoint for player test_player_id: Test exception", exc_info=True
            )


class TestWebSocketEndpointRoute:
    """Test backward-compatible WebSocket endpoint."""

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_success_with_token(self):
        """Test successful WebSocket connection with valid token."""
        # Mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "resolved_player_id"
            mock_persistence.get_player_by_user_id.return_value = mock_player
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint_route(mock_websocket, "path_player_id")

            # Verify handle_websocket_connection was called with resolved player_id
            mock_handle.assert_called_once_with(mock_websocket, "resolved_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket (compat) connection attempt for player path_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_success_without_token(self):
        """Test successful WebSocket connection without token (uses path player_id)."""
        # Mock WebSocket without token
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = None  # No token
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint_route(mock_websocket, "path_player_id")

            # Verify handle_websocket_connection was called with path player_id
            mock_handle.assert_called_once_with(mock_websocket, "path_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket (compat) connection attempt for player path_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_without_sub(self):
        """Test WebSocket connection with token but no 'sub' field."""
        # Mock WebSocket with token
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "invalid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"other_field": "value"}  # No 'sub' field
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint_route(mock_websocket, "path_player_id")

            # Verify handle_websocket_connection was called with path player_id (fallback)
            mock_handle.assert_called_once_with(mock_websocket, "path_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket (compat) connection attempt for player path_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_token_no_player_record(self):
        """Test WebSocket connection with token but no player record."""
        # Mock WebSocket with token
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_persistence.get_player_by_user_id.return_value = None  # No player record
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Call the endpoint
            await websocket_endpoint_route(mock_websocket, "path_player_id")

            # Verify handle_websocket_connection was called with path player_id (fallback)
            mock_handle.assert_called_once_with(mock_websocket, "path_player_id", None)
            mock_logger.info.assert_called_once_with(
                "WebSocket (compat) connection attempt for player path_player_id with session None"
            )

    @pytest.mark.asyncio
    async def test_websocket_endpoint_route_handle_websocket_connection_exception(self):
        """Test WebSocket endpoint when handle_websocket_connection raises an exception."""
        # Mock WebSocket
        mock_websocket = AsyncMock(spec=WebSocket)
        mock_websocket.query_params = {"token": "valid_token"}

        # Mock dependencies
        with (
            patch("server.api.real_time.decode_access_token") as mock_decode,
            patch("server.api.real_time.get_persistence") as mock_get_persistence,
            patch("server.api.real_time.handle_websocket_connection") as mock_handle,
            patch("server.logging_config.get_logger") as mock_get_logger,
        ):
            # Setup mocks
            mock_decode.return_value = {"sub": "test_user_id"}
            mock_persistence = Mock()
            mock_get_persistence.return_value = mock_persistence
            mock_player = Mock()
            mock_player.player_id = "resolved_player_id"
            mock_persistence.get_player_by_user_id.return_value = mock_player
            mock_logger = Mock()
            mock_get_logger.return_value = mock_logger

            # Make handle_websocket_connection raise an exception
            test_exception = Exception("Test exception")
            mock_handle.side_effect = test_exception

            # Call the endpoint and expect the exception to be re-raised
            with pytest.raises(Exception) as exc_info:
                await websocket_endpoint_route(mock_websocket, "path_player_id")

            assert exc_info.value == test_exception
            mock_logger.error.assert_called_once_with(
                "Error in WebSocket endpoint for player path_player_id: Test exception", exc_info=True
            )


class TestRealtimeRouter:
    """Test the realtime router configuration."""

    def test_realtime_router_configuration(self):
        """Test that the realtime router is properly configured."""
        assert realtime_router.prefix == "/api"
        assert "realtime" in realtime_router.tags

        # Check that all expected routes are registered
        routes = [route.path for route in realtime_router.routes]
        expected_routes = ["/api/events/{player_id}", "/api/events", "/api/ws", "/api/ws/{player_id}"]

        for expected_route in expected_routes:
            assert expected_route in routes
