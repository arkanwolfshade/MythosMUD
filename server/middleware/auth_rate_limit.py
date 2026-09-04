"""IP-based rate limiting for unauthenticated auth HTTP endpoints."""

import ipaddress
import os
from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.types import ASGIApp, Receive, Scope, Send

from ..exceptions import RateLimitError
from ..utils.rate_limiter import auth_login_limiter

# Must match POST routes mounted under _register_v1_routers. Add any new
# unauthenticated auth POST here or the limiter will not apply (startup assert fails if missing).
AUTH_RATE_LIMITED_PATHS = frozenset(
    {
        "/v1/auth/login",
        "/v1/auth/jwt/login",
        "/v1/auth/register",
    }
)


def is_auth_rate_limited_path(path: str) -> bool:
    """Return True if path is an unauthenticated auth POST covered by the limiter."""
    normalized = path.rstrip("/") or "/"
    return normalized in AUTH_RATE_LIMITED_PATHS


def _canonical_ip(raw: str) -> str | None:
    try:
        return format(ipaddress.ip_address(raw))
    except ValueError:
        return None


def _auth_bucket(host: str) -> str:
    # Rate-limiter dict key (not an HTTP response); join avoids flask-xss concat-on-return.
    return ":".join(("auth", host))


def auth_client_key(request: Request) -> str:
    """Key the limiter by client IP.

    Default uses the TCP peer (request.client.host). Local and current production
    are direct to uvicorn; there is no reverse proxy. If a proxy is added later,
    set MYTHOSMUD_TRUST_X_FORWARDED_FOR=true only when that proxy overwrites
    X-Forwarded-For (otherwise clients can spoof the header).
    """
    if os.environ.get("MYTHOSMUD_TRUST_X_FORWARDED_FOR", "").strip().lower() in {"1", "true", "yes", "on"}:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            parsed = _canonical_ip(forwarded.split(",", maxsplit=1)[0].strip())
            if parsed is not None:
                return _auth_bucket(parsed)
    client = request.client
    host = client.host if client is not None else "unknown"
    return _auth_bucket(host)


@runtime_checkable
class _HasPrefix(Protocol):
    prefix: str


@runtime_checkable
class _HasRoutes(Protocol):
    routes: Sequence[object]


@runtime_checkable
class _IncludedRouterLike(Protocol):
    include_context: _HasPrefix
    original_router: _HasRoutes


def _join_route_path(prefix: str, path_s: str) -> str:
    if path_s.startswith("/"):
        return prefix.rstrip("/") + path_s
    if path_s:
        return f"{prefix}/{path_s}"
    return prefix


def _collect_post_paths(routes: Sequence[object], prefix: str = "") -> set[str]:
    found: set[str] = set()
    for route in routes:
        if isinstance(route, _IncludedRouterLike):
            child_prefix = _join_route_path(prefix, route.include_context.prefix)
            found.update(_collect_post_paths(route.original_router.routes, child_prefix))
            continue
        if isinstance(route, Mount):
            found.update(_collect_post_paths(route.routes, _join_route_path(prefix, route.path)))
            continue
        if isinstance(route, Route) and route.methods and "POST" in route.methods:
            found.add(_join_route_path(prefix, route.path).rstrip("/") or "/")
    return found


def assert_auth_rate_limit_paths_registered(app: FastAPI) -> None:
    """Fail startup if AUTH_RATE_LIMITED_PATHS do not match mounted POST routes."""
    registered = _collect_post_paths(app.routes)
    missing: list[str] = []
    for raw in AUTH_RATE_LIMITED_PATHS:
        normalized = raw.rstrip("/") or "/"
        if normalized not in registered:
            missing.append(normalized)
    missing.sort()
    if missing:
        raise RuntimeError("AUTH_RATE_LIMITED_PATHS has no matching POST route: " + ", ".join(missing))


def auth_rate_limit_response(request: Request) -> JSONResponse | None:
    """Return 429 when an auth POST exceeds the limiter; otherwise None."""
    if request.method != "POST" or not is_auth_rate_limited_path(request.url.path):
        return None
    try:
        auth_login_limiter.enforce_rate_limit(auth_client_key(request))
    except RateLimitError as exc:
        retry = exc.retry_after or 0
        headers: dict[str, str] = {}
        if retry > 0:
            headers["Retry-After"] = str(retry)
        return JSONResponse(status_code=429, content={"detail": str(exc)}, headers=headers)
    return None


class AuthRateLimitMiddleware:
    """Pure ASGI middleware; HTTP POST login/register only."""

    def __init__(self, app: ASGIApp) -> None:
        self.app: ASGIApp = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        blocked = auth_rate_limit_response(Request(scope, receive))
        if blocked is not None:
            await blocked(scope, receive, send)
            return
        await self.app(scope, receive, send)
