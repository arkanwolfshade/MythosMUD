"""Unit tests for auth HTTP rate limiting."""

from unittest.mock import patch

from starlette.requests import Request

from server.exceptions import RateLimitError
from server.middleware.auth_rate_limit import (
    auth_client_key,
    auth_rate_limit_response,
    is_auth_rate_limited_path,
)
from server.utils.rate_limiter import RateLimiter


def _post_request(path: str, host: str = "203.0.113.10") -> Request:
    scope: dict[str, object] = {
        "type": "http",
        "asgi": {"version": "3.0"},
        "http_version": "1.1",
        "method": "POST",
        "scheme": "http",
        "path": path,
        "raw_path": path.encode("ascii"),
        "query_string": b"",
        "headers": [],
        "client": (host, 12345),
        "server": ("test", 80),
    }
    return Request(scope)


def test_is_auth_rate_limited_path() -> None:
    assert is_auth_rate_limited_path("/v1/auth/login") is True
    assert is_auth_rate_limited_path("/v1/auth/jwt/login/") is True
    assert is_auth_rate_limited_path("/v1/auth/register") is True
    assert is_auth_rate_limited_path("/v1/players") is False


def test_auth_client_key_uses_ip() -> None:
    assert auth_client_key(_post_request("/v1/auth/login")) == "auth:203.0.113.10"


def test_auth_rate_limit_response_skips_other_paths() -> None:
    assert auth_rate_limit_response(_post_request("/v1/rooms")) is None


def test_auth_rate_limit_response_returns_429_when_exceeded() -> None:
    tight = RateLimiter(max_requests=1, window_seconds=60)
    request = _post_request("/v1/auth/login")
    with patch("server.middleware.auth_rate_limit.auth_login_limiter", tight):
        assert auth_rate_limit_response(request) is None
        blocked = auth_rate_limit_response(request)
    assert blocked is not None
    assert blocked.status_code == 429


def test_auth_rate_limit_response_maps_rate_limit_error() -> None:
    request = _post_request("/v1/auth/jwt/login")

    def _raise(_key: str) -> None:
        raise RateLimitError("too many", limit_type="api_endpoint", retry_after=12)

    with patch(
        "server.middleware.auth_rate_limit.auth_login_limiter.enforce_rate_limit",
        side_effect=_raise,
    ):
        blocked = auth_rate_limit_response(request)
    assert blocked is not None
    assert blocked.status_code == 429
    assert blocked.headers["Retry-After"] == "12"
