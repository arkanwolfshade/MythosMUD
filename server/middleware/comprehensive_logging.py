"""
Comprehensive logging middleware for MythosMUD server.

This module provides a unified logging middleware that consolidates access,
error, and request logging functionality into a single, efficient component.

As noted in the Pnakotic Manuscripts, the proper organization of arcane
knowledge requires both efficiency and comprehensiveness. This middleware
provides both, consolidating multiple logging concerns into a single,
well-ordered component.
"""

import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from ..logging_config import get_logger

logger = get_logger(__name__)


class ComprehensiveLoggingMiddleware(BaseHTTPMiddleware):
    """
    Comprehensive logging middleware that combines access, error, and request logging.

    This middleware consolidates all logging functionality into a single,
    efficient middleware component that handles request/response logging,
    error logging, and performance monitoring.
    """

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)
        logger.info("ComprehensiveLoggingMiddleware initialized")

    async def dispatch(self, request: Request, call_next) -> Response:
        """Handle comprehensive logging for requests and responses."""
        start_time = time.time()

        # Log request start
        self._log_request_start(request)

        try:
            # Process the request
            response = await call_next(request)

            # Log successful response
            process_time = time.time() - start_time
            self._log_request_success(request, response, process_time)

            return response

        except Exception as e:
            # Log error
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

    def _log_request_success(self, request: Request, response: Response, process_time: float) -> None:
        """Log successful request completion."""
        logger.info(
            "HTTP request completed",
            method=request.method,
            url=str(request.url),
            status_code=response.status_code,
            process_time=process_time,
            client_ip=request.client.host if request.client else "unknown",
        )

        logger.debug(
            f"Response: {response.status_code} for {request.method} {request.url.path}",
            status_code=response.status_code,
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
