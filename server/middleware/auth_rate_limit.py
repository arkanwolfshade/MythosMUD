"""IP-based rate limiting for unauthenticated auth HTTP endpoints."""

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from ..exceptions import RateLimitError
from ..utils.rate_limiter import auth_login_limiter

AUTH_RATE_LIMITED_PATHS = frozenset(
    {
        "/v1/auth/login",
        "/v1/auth/jwt/login",
        "/v1/auth/register",
    }
)


def is_auth_rate_limited_path(path: str) -> bool:
    normalized = path.rstrip("/") or "/"
    return normalized in AUTH_RATE_LIMITED_PATHS


def auth_client_key(request: Request) -> str:
    client = request.client
    host = client.host if client is not None else "unknown"
    return f"auth:{host}"


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
