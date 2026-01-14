"""
Correlation middleware for request tracing and logging context.

This middleware ensures that all requests have proper correlation IDs and
context information for tracing and debugging across the application.

As noted in the Pnakotic Manuscripts, proper tracking of events through
the cosmic flow is essential for understanding the deeper patterns.
"""

import uuid
from collections.abc import Callable
from typing import Any

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from ..structured_logging.enhanced_logging_config import (
    bind_request_context,
    clear_request_context,
    get_logger,
)

logger = get_logger(__name__)


class CorrelationMiddleware(BaseHTTPMiddleware):  # pylint: disable=too-few-public-methods  # Reason: Middleware class with focused responsibility, minimal public interface
    """
    Middleware for adding correlation IDs and request context to all requests.

    This middleware automatically adds correlation IDs to all HTTP requests
    and sets up the logging context for the request duration.
    """

    def __init__(self, app, correlation_header: str = "X-Correlation-ID"):
        """
        Initialize the correlation middleware.

        Args:
            app: FastAPI application instance
            correlation_header: HTTP header name for correlation ID
        """
        super().__init__(app)
        self.correlation_header = correlation_header
        self.correlation_header = correlation_header

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request with correlation ID and context.

        Args:
            request: Incoming HTTP request
            call_next: Next middleware/handler in the chain

        Returns:
            HTTP response with correlation ID header
        """
        # Generate or extract correlation ID
        correlation_id = request.headers.get(self.correlation_header)
        if not correlation_id:
            correlation_id = str(uuid.uuid4())

        # Extract request context information
        request_id = str(request.url)
        user_agent = request.headers.get("user-agent", "")
        remote_addr = request.client.host if request.client else "unknown"

        # Set up logging context for this request
        bind_request_context(
            correlation_id=correlation_id,
            request_id=request_id,
            user_agent=user_agent,
            remote_addr=remote_addr,
            method=request.method,
            path=request.url.path,
        )

        # Log request start
        logger.info(
            "Request started",
            method=request.method,
            path=request.url.path,
            query_params=dict(request.query_params),
            user_agent=user_agent,
            remote_addr=remote_addr,
        )

        try:
            # Process the request
            response = await call_next(request)

            # Add correlation ID to response headers
            response.headers[self.correlation_header] = correlation_id

            # Log request completion
            logger.info(
                "Request completed",
                status_code=response.status_code,
                response_time_ms="calculated_by_middleware",  # Could be enhanced with timing
            )

            return response

        except Exception as e:
            # Log request error
            logger.error(
                "Request failed",
                error_type=type(e).__name__,
                error_message=str(e),
                exc_info=True,
            )

            # Re-raise the exception
            raise

        finally:
            # Clear the request context
            clear_request_context()


class WebSocketCorrelationMiddleware:  # pylint: disable=too-few-public-methods  # Reason: Middleware class with focused responsibility, minimal public interface
    """
    Middleware for adding correlation IDs to WebSocket connections.

    This middleware ensures that WebSocket connections also have proper
    correlation IDs and context information.
    """

    def __init__(self, correlation_header: str = "X-Correlation-ID"):
        """
        Initialize the WebSocket correlation middleware.

        Args:
            correlation_header: HTTP header name for correlation ID
        """
        self.correlation_header = correlation_header

    async def __call__(self, websocket, call_next):
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
