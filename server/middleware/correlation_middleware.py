"""
Correlation middleware for request tracing and logging context.

This middleware ensures that all requests have proper correlation IDs and
context information for tracing and debugging across the application.

As noted in the Pnakotic Manuscripts, proper tracking of events through
the cosmic flow is essential for understanding the deeper patterns.

IMPLEMENTATION NOTE: This uses pure ASGI middleware instead of BaseHTTPMiddleware
for better performance and proper type safety with mypy.
"""

import uuid
from collections.abc import Callable
from typing import Any, cast

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from ..structured_logging.enhanced_logging_config import (
    bind_request_context,
    clear_request_context,
    get_logger,
)

logger = get_logger(__name__)


def _get_header(scope: Scope, name: str) -> str | None:
    """Return first header value for name (case-insensitive) from ASGI scope."""
    name_lower = name.lower().encode()
    for key, value in scope.get("headers", []):
        if key.lower() == name_lower:
            # value is bytes from ASGI headers; decode returns str. Cast for mypy (scope yields Any).
            return cast(str, value.decode("utf-8", errors="replace"))
    return None


class CorrelationMiddleware:  # pylint: disable=too-few-public-methods  # Reason: Middleware class with focused responsibility, minimal public interface
    """
    Pure ASGI middleware for adding correlation IDs and request context to all requests.

    This middleware automatically adds correlation IDs to all HTTP requests
    and sets up the logging context for the request duration.
    """

    def __init__(self, app: ASGIApp, correlation_header: str = "X-Correlation-ID") -> None:
        """
        Initialize the correlation middleware.

        Args:
            app: ASGI application instance
            correlation_header: HTTP header name for correlation ID
        """
        self.app = app
        self.correlation_header = correlation_header

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        ASGI application interface.

        Args:
            scope: ASGI connection scope
            receive: ASGI receive callable
            send: ASGI send callable
        """
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Generate or extract correlation ID from request headers
        correlation_id = _get_header(scope, self.correlation_header)
        if not correlation_id:
            correlation_id = str(uuid.uuid4())

        # Extract request context from scope
        method = scope.get("method", "")
        path = scope.get("path", "")
        query_string = scope.get("query_string", b"").decode("utf-8", errors="replace")
        request_id = path + ("?" + query_string if query_string else "")
        user_agent = _get_header(scope, "user-agent") or ""
        client = scope.get("client")
        remote_addr = client[0] if client else "unknown"

        bind_request_context(
            correlation_id=correlation_id,
            request_id=request_id,
            user_agent=user_agent,
            remote_addr=remote_addr,
            method=method,
            path=path,
        )

        logger.info(
            "Request started",
            method=method,
            path=path,
            user_agent=user_agent,
            remote_addr=remote_addr,
        )

        status_code = 500
        response_started = False

        async def send_with_correlation_header(message: Message) -> None:
            nonlocal status_code, response_started
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append(self.correlation_header, correlation_id)
                status_code = message.get("status", 500)
                response_started = True
            await send(message)

        try:
            await self.app(scope, receive, send_with_correlation_header)
            if response_started:
                logger.info(
                    "Request completed",
                    status_code=status_code,
                    response_time_ms="calculated_by_middleware",
                )
        except Exception as e:
            logger.error(
                "Request failed",
                error_type=type(e).__name__,
                error_message=str(e),
                exc_info=True,
            )
            raise
        finally:
            clear_request_context()


class WebSocketCorrelationMiddleware:  # pylint: disable=too-few-public-methods  # Reason: Middleware class with focused responsibility, minimal public interface
    """
    Middleware for adding correlation IDs to WebSocket connections.

    This middleware ensures that WebSocket connections also have proper
    correlation IDs and context information.
    """

    def __init__(self, correlation_header: str = "X-Correlation-ID") -> None:
        """
        Initialize the WebSocket correlation middleware.

        Args:
            correlation_header: HTTP header name for correlation ID
        """
        self.correlation_header = correlation_header

    async def __call__(self, websocket: Any, call_next: Any) -> Any:
        """
        Process the WebSocket connection with correlation ID.

        Args:
            websocket: WebSocket connection
            call_next: Next handler in the chain

        Returns:
            WebSocket response
        """
        # Generate or extract correlation ID
        correlation_id = websocket.headers.get(self.correlation_header)
        if not correlation_id:
            correlation_id = str(uuid.uuid4())

        # Extract connection context information
        request_id = str(websocket.url)
        user_agent = websocket.headers.get("user-agent", "")
        remote_addr = websocket.client.host if websocket.client else "unknown"

        # Set up logging context for this connection
        bind_request_context(
            correlation_id=correlation_id,
            request_id=request_id,
            user_agent=user_agent,
            remote_addr=remote_addr,
            connection_type="websocket",
            path=websocket.url.path,
        )

        # Log connection start
        logger.info(
            "WebSocket connection started",
            path=websocket.url.path,
            query_params=dict(websocket.query_params),
            user_agent=user_agent,
            remote_addr=remote_addr,
        )

        try:
            # Process the WebSocket connection
            response = await call_next(websocket)

            # Log connection completion
            logger.info("WebSocket connection completed")

            return response

        except Exception as e:
            # Log connection error
            logger.error(
                "WebSocket connection failed",
                error_type=type(e).__name__,
                error_message=str(e),
                exc_info=True,
            )

            # Re-raise the exception
            raise

        finally:
            # Clear the connection context
            clear_request_context()


def create_correlation_middleware(
    correlation_header: str = "X-Correlation-ID",
) -> Callable[[Any], CorrelationMiddleware]:
    """
    Create a correlation middleware factory.

    Args:
        correlation_header: HTTP header name for correlation ID

    Returns:
        Factory function that creates configured correlation middleware
    """

    def middleware_factory(app: Any) -> CorrelationMiddleware:
        return CorrelationMiddleware(app, correlation_header)

    return middleware_factory


def create_websocket_correlation_middleware(
    correlation_header: str = "X-Correlation-ID",
) -> WebSocketCorrelationMiddleware:
    """
    Create a WebSocket correlation middleware instance.

    Args:
        correlation_header: HTTP header name for correlation ID

    Returns:
        Configured WebSocket correlation middleware
    """
    return WebSocketCorrelationMiddleware(correlation_header)
