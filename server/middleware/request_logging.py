"""
Request logging middleware for MythosMUD.

This module provides middleware to log all incoming requests
with detailed information for debugging purposes.
"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from ..logging_config import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log all incoming requests."""

    async def dispatch(self, request: Request, call_next):
        """Log request details and process the request."""
        # Log request details
        auth_header = request.headers.get("Authorization", "Not provided")
        auth_preview = (
            auth_header[:30] + "..." if auth_header != "Not provided" and len(auth_header) > 30 else auth_header
        )

        logger.info(f"Request: {request.method} {request.url.path}")
        logger.debug(
            "Request details",
            {
                "method": request.method,
                "url": str(request.url),
                "headers": {
                    "user-agent": request.headers.get("user-agent", "Not provided"),
                    "content-type": request.headers.get("content-type", "Not provided"),
                    "authorization": auth_preview,
                },
                "client": request.client.host if request.client else "Unknown",
            },
        )

        # Process the request
        response = await call_next(request)

        # Log response details
        logger.debug(f"Response: {response.status_code} for {request.method} {request.url.path}")

        return response
