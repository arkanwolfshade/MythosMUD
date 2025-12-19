"""
Tests for comprehensive logging middleware to improve coverage.

This module provides targeted tests for comprehensive_logging.py
to cover the remaining uncovered lines, particularly error handling paths.

As noted in the Cultes des Goules, proper logging of errors is essential
for debugging the eldritch machinery of our server.
"""

from unittest.mock import Mock

import pytest
from starlette.requests import Request
from starlette.responses import Response

from server.middleware.comprehensive_logging import ComprehensiveLoggingMiddleware


class TestComprehensiveLoggingMiddleware:
    """Test comprehensive logging middleware."""

    @pytest.mark.asyncio
    async def test_middleware_logs_successful_request(self) -> None:
        """Test that middleware logs successful requests.

        AI: Tests the success path with logging.
        """
        app = Mock()
        middleware = ComprehensiveLoggingMiddleware(app)

        # Create mock request
        mock_request = Mock(spec=Request)
        mock_request.method = "GET"
        mock_request.url = Mock()
        mock_request.url.path = "/test"
        mock_request.url.__str__ = lambda self: "http://test.com/test"
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"
        mock_request.headers = {"user-agent": "test-agent"}

        # Create mock response
        mock_response = Mock(spec=Response)
        mock_response.status_code = 200

        # Mock call_next
        async def mock_call_next(_request: Request) -> Response:
            return mock_response

        # Execute
        result = await middleware.dispatch(mock_request, mock_call_next)

        assert result == mock_response

    @pytest.mark.asyncio
    async def test_middleware_logs_request_error(self) -> None:
        """Test that middleware logs request errors.

        AI: Tests the error path (lines 54-58, 107) to improve coverage.
        """
        app = Mock()
        middleware = ComprehensiveLoggingMiddleware(app)

        # Create mock request
        mock_request = Mock(spec=Request)
        mock_request.method = "POST"
        mock_request.url = Mock()
        mock_request.url.path = "/api/error"
        mock_request.url.__str__ = lambda self: "http://test.com/api/error"
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"
        mock_request.headers = {"user-agent": "test-agent", "content-type": "application/json"}

        # Mock call_next to raise an exception
        test_error = ValueError("Test error")

        async def mock_call_next_with_error(_request):
            raise test_error

        # Execute and verify exception is re-raised
        with pytest.raises(ValueError) as exc_info:
            await middleware.dispatch(mock_request, mock_call_next_with_error)

        assert exc_info.value == test_error

    @pytest.mark.asyncio
    async def test_middleware_handles_missing_client_info(self) -> None:
        """Test that middleware handles requests with no client info.

        AI: Tests handling of requests without client information.
        """
        app = Mock()
        middleware = ComprehensiveLoggingMiddleware(app)

        # Create mock request without client
        mock_request = Mock(spec=Request)
        mock_request.method = "GET"
        mock_request.url = Mock()
        mock_request.url.path = "/test"
        mock_request.url.__str__ = lambda self: "http://test.com/test"
        mock_request.client = None
        mock_request.headers = {}

        mock_response = Mock(spec=Response)
        mock_response.status_code = 200

        async def mock_call_next(_request: Request) -> Response:
            return mock_response

        result = await middleware.dispatch(mock_request, mock_call_next)

        assert result == mock_response

    @pytest.mark.asyncio
    async def test_middleware_logs_long_authorization_header(self) -> None:
        """Test that middleware truncates long authorization headers.

        AI: Tests authorization header preview functionality.
        """
        app = Mock()
        middleware = ComprehensiveLoggingMiddleware(app)

        # Create mock request with long auth header
        long_auth = "Bearer " + "x" * 100
        mock_request = Mock(spec=Request)
        mock_request.method = "GET"
        mock_request.url = Mock()
        mock_request.url.path = "/test"
        mock_request.url.__str__ = lambda self: "http://test.com/test"
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"
        mock_request.headers = {"Authorization": long_auth, "user-agent": "test-agent"}

        mock_response = Mock(spec=Response)
        mock_response.status_code = 200

        async def mock_call_next(_request: Request) -> Response:
            return mock_response

        result = await middleware.dispatch(mock_request, mock_call_next)

        assert result == mock_response
