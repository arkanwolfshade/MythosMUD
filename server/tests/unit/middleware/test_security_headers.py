"""
Unit tests for security headers middleware.

Tests the SecurityHeadersMiddleware class that adds security headers to HTTP responses.
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from starlette.responses import Response

from server.middleware.security_headers import SecurityHeadersMiddleware


@pytest.fixture
def mock_app():
    """Create a mock ASGI app."""
    return AsyncMock()


@pytest.fixture
def middleware(mock_app):
    """Create SecurityHeadersMiddleware instance."""
    return SecurityHeadersMiddleware(mock_app)


def test_security_headers_middleware_init(mock_app):
    """Test SecurityHeadersMiddleware initialization."""
    middleware = SecurityHeadersMiddleware(mock_app)

    assert middleware.app == mock_app
    assert isinstance(middleware.hsts_max_age, int)
    assert isinstance(middleware.hsts_include_subdomains, bool)
    assert isinstance(middleware.csp_policy, str)
    assert isinstance(middleware.referrer_policy, str)


def test_security_headers_middleware_init_with_env_vars(mock_app):
    """Test SecurityHeadersMiddleware initialization with environment variables."""
    with patch.dict(
        os.environ,
        {
            "HSTS_MAX_AGE": "63072000",
            "HSTS_INCLUDE_SUBDOMAINS": "false",
            "CSP_POLICY": "default-src 'none'",
            "REFERRER_POLICY": "no-referrer",
        },
    ):
        middleware = SecurityHeadersMiddleware(mock_app)

        assert middleware.hsts_max_age == 63072000
        assert middleware.hsts_include_subdomains is False
        assert middleware.csp_policy == "default-src 'none'"
        assert middleware.referrer_policy == "no-referrer"


@pytest.mark.asyncio
async def test_security_headers_middleware_non_http_scope(middleware, mock_app):
    """Test middleware passes through non-HTTP connections."""
    scope = {"type": "websocket"}
    receive = AsyncMock()
    send = AsyncMock()

    await middleware(scope, receive, send)

    mock_app.assert_awaited_once_with(scope, receive, send)


@pytest.mark.asyncio
async def test_security_headers_middleware_adds_headers(middleware, mock_app):
    """Test middleware adds security headers to HTTP responses."""
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/test",
        "headers": [],
    }
    receive = AsyncMock()
    send = AsyncMock()

    # Mock the response start message
    response_start = {
        "type": "http.response.start",
        "status": 200,
        "headers": [],
    }

    async def mock_send(message):
        if message["type"] == "http.response.start":
            # Verify headers were added
            headers = MutableHeaders(scope=message)
            assert "Strict-Transport-Security" in headers
            assert "X-Frame-Options" in headers
            assert "X-Content-Type-Options" in headers
            assert "Referrer-Policy" in headers
            assert "Content-Security-Policy" in headers
            assert "X-XSS-Protection" in headers
            assert "Permissions-Policy" in headers

    send.side_effect = mock_send

    # Mock app to call send
    async def mock_app_call(scope, receive, send_func):
        await send_func(response_start)
        await send_func({"type": "http.response.body", "body": b"test"})

    mock_app.side_effect = mock_app_call

    await middleware(scope, receive, send)

    mock_app.assert_awaited_once()


@pytest.mark.asyncio
async def test_security_headers_middleware_error_handling(middleware, mock_app):
    """Test middleware error handling."""
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/test",
        "headers": [],
    }
    receive = AsyncMock()
    send = AsyncMock()

    # Mock app to raise an error
    mock_app.side_effect = ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        await middleware(scope, receive, send)


def test_add_security_headers_to_response(middleware):
    """Test _add_security_headers_to_response adds headers to Response."""
    response = Response(content="test", status_code=200)

    middleware._add_security_headers_to_response(response)

    assert "Strict-Transport-Security" in response.headers
    assert "X-Frame-Options" in response.headers
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_add_security_headers_to_response_hsts_with_subdomains(middleware):
    """Test _add_security_headers_to_response includes subdomains in HSTS."""
    middleware.hsts_include_subdomains = True
    response = Response(content="test", status_code=200)

    middleware._add_security_headers_to_response(response)

    hsts_value = response.headers["Strict-Transport-Security"]
    assert "includeSubDomains" in hsts_value


def test_add_security_headers_to_response_hsts_without_subdomains(middleware):
    """Test _add_security_headers_to_response without subdomains in HSTS."""
    middleware.hsts_include_subdomains = False
    response = Response(content="test", status_code=200)

    middleware._add_security_headers_to_response(response)

    hsts_value = response.headers["Strict-Transport-Security"]
    assert "includeSubDomains" not in hsts_value


def test_add_security_headers(middleware):
    """Test _add_security_headers adds all security headers."""
    headers = MutableHeaders()

    middleware._add_security_headers(headers)

    assert "Strict-Transport-Security" in headers
    assert "X-Frame-Options" in headers
    assert "X-Content-Type-Options" in headers
    assert "Referrer-Policy" in headers
    assert "Content-Security-Policy" in headers
    assert "X-XSS-Protection" in headers
    assert "Permissions-Policy" in headers


def test_add_security_headers_hsts_value(middleware):
    """Test _add_security_headers sets correct HSTS value."""
    middleware.hsts_max_age = 31536000
    middleware.hsts_include_subdomains = True
    headers = MutableHeaders()

    middleware._add_security_headers(headers)

    hsts_value = headers["Strict-Transport-Security"]
    assert "max-age=31536000" in hsts_value
    assert "includeSubDomains" in hsts_value


@pytest.mark.asyncio
async def test_dispatch_method(middleware):
    """Test dispatch method (backward compatibility)."""
    request = MagicMock(spec=Request)
    request.method = "GET"
    request.url = MagicMock()
    request.url.__str__ = MagicMock(return_value="http://test.com/test")
    request.headers = {"User-Agent": "test-agent"}

    mock_response = Response(content="test", status_code=200)
    call_next = AsyncMock(return_value=mock_response)

    result = await middleware.dispatch(request, call_next)

    assert result == mock_response
    call_next.assert_awaited_once_with(request)
    # Verify headers were added
    assert "Strict-Transport-Security" in mock_response.headers


@pytest.mark.asyncio
async def test_dispatch_method_error_handling(middleware):
    """Test dispatch method error handling."""
    request = MagicMock(spec=Request)
    request.method = "GET"
    request.url = MagicMock()
    request.url.__str__ = MagicMock(return_value="http://test.com/test")
    request.headers = {"User-Agent": "test-agent"}

    call_next = AsyncMock(side_effect=ValueError("Test error"))

    with pytest.raises(ValueError, match="Test error"):
        await middleware.dispatch(request, call_next)


def test_add_security_headers_permissions_policy(middleware):
    """Test _add_security_headers includes Permissions-Policy."""
    headers = MutableHeaders()

    middleware._add_security_headers(headers)

    permissions_policy = headers["Permissions-Policy"]
    assert "geolocation=()" in permissions_policy
    assert "microphone=()" in permissions_policy
    assert "camera=()" in permissions_policy


def test_add_security_headers_csp_policy(middleware):
    """Test _add_security_headers uses configured CSP policy."""
    middleware.csp_policy = "default-src 'self'; script-src 'none'"
    headers = MutableHeaders()

    middleware._add_security_headers(headers)

    assert headers["Content-Security-Policy"] == "default-src 'self'; script-src 'none'"


def test_add_security_headers_referrer_policy(middleware):
    """Test _add_security_headers uses configured referrer policy."""
    middleware.referrer_policy = "no-referrer"
    headers = MutableHeaders()

    middleware._add_security_headers(headers)

    assert headers["Referrer-Policy"] == "no-referrer"
