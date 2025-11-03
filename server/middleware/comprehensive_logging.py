"""
Comprehensive logging middleware for MythosMUD server.

This module provides a unified logging middleware that consolidates access,
error, and request logging functionality into a single, efficient component.

As noted in the Pnakotic Manuscripts, the proper organization of arcane
knowledge requires both efficiency and comprehensiveness. This middleware
provides both, consolidating multiple logging concerns into a single,
well-ordered component.

IMPLEMENTATION NOTE: This uses pure ASGI middleware instead of BaseHTTPMiddleware
for better performance and proper type safety with mypy.
"""

import time
from typing import Any

from starlette.requests import Request
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ComprehensiveLoggingMiddleware:
    """
    Pure ASGI middleware that combines access, error, and request logging.

    This middleware consolidates all logging functionality into a single,
    efficient middleware component that handles request/response logging,
    error logging, and performance monitoring.

    Unlike BaseHTTPMiddleware, this uses pure ASGI for better performance and type safety.
    """

    def __init__(self, app: ASGIApp) -> None:
        """
        Initialize comprehensive logging middleware.

        Args:
            app: ASGI application instance
        """
        self.app = app
        logger.info("ComprehensiveLoggingMiddleware initialized")

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        ASGI application interface.

        Args:
            scope: ASGI connection scope
            receive: ASGI receive callable
            send: ASGI send callable
        """
        if scope["type"] != "http":
            # Pass through non-HTTP connections
            await self.app(scope, receive, send)
            return

        # Create Request for logging
        request = Request(scope, receive)
        start_time = time.time()

        # Log request start
        self._log_request_start(request)

        # Track response status code
        status_code = 500  # Default for errors
        response_started = False

        async def send_with_logging(message: Message) -> None:
            """Wrap send to log response details."""
            nonlocal status_code, response_started

            if message["type"] == "http.response.start":
                status_code = message.get("status", 500)
                response_started = True

            await send(message)

        try:
            # Process the request
            await self.app(scope, receive, send_with_logging)

            # Log successful completion
            if response_started:
                process_time = time.time() - start_time
                self._log_request_success_with_status(request, status_code, process_time)

        except Exception as e:
            # Log error
            process_time = time.time() - start_time
            self._log_request_error(request, e, process_time)
            raise

    async def dispatch(self, request: Request, call_next: Any) -> Any:
        """
        Backward-compatible dispatch method for BaseHTTPMiddleware interface.

        This method provides compatibility with tests and code that expects
        the BaseHTTPMiddleware.dispatch() signature.

        Args:
            request: HTTP request
            call_next: Callable to invoke next middleware/handler

        Returns:
            HTTP response
        """

        start_time = time.time()
        self._log_request_start(request)

        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            self._log_request_success_with_status(request, response.status_code, process_time)
            return response
        except Exception as e:
            process_time = time.time() - start_time
            self._log_request_error(request, e, process_time)
            raise

    def _log_request_start(self, request: Request) -> None:
        """Log request start information."""
        # Get authorization header preview (for security)
        auth_header = request.headers.get("Authorization", "Not provided")
        auth_preview = (
            auth_header[:30] + "..." if auth_header != "Not provided" and len(auth_header) > 30 else auth_header
        )

        logger.info(
            "HTTP request started",
            method=request.method,
            url=str(request.url),
            client_ip=request.client.host if request.client else "unknown",
            user_agent=request.headers.get("user-agent", "unknown"),
        )

        logger.debug(
            "Request details",
            method=request.method,
            url=str(request.url),
            headers={
                "user-agent": request.headers.get("user-agent", "Not provided"),
                "content-type": request.headers.get("content-type", "Not provided"),
                "authorization": auth_preview,
            },
            client=request.client.host if request.client else "Unknown",
        )

    def _log_request_success_with_status(self, request: Request, status_code: int, process_time: float) -> None:
        """Log successful request completion."""
        logger.info(
            "HTTP request completed",
            method=request.method,
            url=str(request.url),
            status_code=status_code,
            process_time=process_time,
            client_ip=request.client.host if request.client else "unknown",
        )

        logger.debug(
            f"Response: {status_code} for {request.method} {request.url.path}",
            status_code=status_code,
            process_time=process_time,
        )

    def _log_request_error(self, request: Request, error: Exception, process_time: float) -> None:
        """Log request error."""
        logger.error(
            "Unhandled exception in request",
            path=request.url.path,
            method=request.method,
            error=str(error),
            process_time=process_time,
            client_ip=request.client.host if request.client else "unknown",
            exc_info=True,
        )
