"""
Security headers middleware for MythosMUD server.

This module provides comprehensive security headers middleware to protect
against common web vulnerabilities including XSS, clickjacking, and
information disclosure attacks.

As noted in the Pnakotic Manuscripts, proper defense against the eldritch
forces requires multiple layers of protection. This middleware provides
the first line of defense against web-based threats.

IMPLEMENTATION NOTE: This uses pure ASGI middleware instead of BaseHTTPMiddleware
for better performance and proper type safety with mypy.
"""

import os
from typing import Any

from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SecurityHeadersMiddleware:
    """
    Pure ASGI middleware to add comprehensive security headers to all HTTP responses.

    This middleware adds essential security headers to protect against common
    web vulnerabilities including XSS, clickjacking, and information disclosure.

    Unlike BaseHTTPMiddleware, this uses pure ASGI for better performance and type safety.
    """

    def __init__(self, app: ASGIApp) -> None:
        """
        Initialize security headers middleware.

        Args:
            app: ASGI application instance
        """
        self.app = app

        # Get security configuration from environment variables
        self.hsts_max_age = int(os.getenv("HSTS_MAX_AGE", "31536000"))  # 1 year default
        self.hsts_include_subdomains = os.getenv("HSTS_INCLUDE_SUBDOMAINS", "true").lower() == "true"
        self.csp_policy = os.getenv("CSP_POLICY", "default-src 'self'")
        self.referrer_policy = os.getenv("REFERRER_POLICY", "strict-origin-when-cross-origin")

        logger.info(
            "SecurityHeadersMiddleware initialized",
            hsts_max_age=self.hsts_max_age,
            hsts_include_subdomains=self.hsts_include_subdomains,
            csp_policy=self.csp_policy,
            referrer_policy=self.referrer_policy,
        )

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        ASGI application interface.

        Args:
            scope: ASGI connection scope
            receive: ASGI receive callable
            send: ASGI send callable
        """
        if scope["type"] != "http":
            # Pass through non-HTTP connections (WebSocket, lifespan)
            await self.app(scope, receive, send)
            return

        # Create Request for logging
        request = Request(scope, receive)

        logger.debug(
            "Processing request through security headers middleware",
            method=request.method,
            url=str(request.url),
            user_agent=request.headers.get("user-agent", "unknown"),
        )

        async def send_with_headers(message: Message) -> None:
            """Wrap send to add security headers to the response."""
            if message["type"] == "http.response.start":
                # Add security headers to response
                headers = MutableHeaders(scope=message)
                self._add_security_headers(headers)

                logger.debug(
                    "Security headers added to response",
                    headers_added=len(
                        [
                            h
                            for h in headers.keys()
                            if h.startswith(("x-", "content-security", "strict-transport", "referrer"))
                        ]
                    ),
                )

            await send(message)

        try:
            await self.app(scope, receive, send_with_headers)
        except Exception as e:
            logger.error(
                "Error in security headers middleware",
                method=request.method,
                url=str(request.url),
                error=str(e),
                exc_info=True,
            )
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

        logger.debug(
            "Processing request through security headers middleware",
            method=request.method,
            url=str(request.url),
            user_agent=request.headers.get("user-agent", "unknown"),
        )

        try:
            response = await call_next(request)
            self._add_security_headers_to_response(response)
            logger.debug(
                "Security headers added to response",
                status_code=response.status_code,
                headers_added=len(
                    [
                        h
                        for h in response.headers
                        if h.lower().startswith(("x-", "content-security", "strict-transport", "referrer"))
                    ]
                ),
            )
            return response
        except Exception as e:
            logger.error(
                "Error in security headers middleware",
                method=request.method,
                url=str(request.url),
                error=str(e),
                exc_info=True,
            )
            raise

    def _add_security_headers_to_response(self, response: Any) -> None:
        """Add security headers to Response object (compatibility method)."""

        if isinstance(response, Response):
            # Response.headers is a mutable dict-like object
            # Directly modify response.headers like correlation middleware does
            # Strict Transport Security (HSTS)
            hsts_value = f"max-age={self.hsts_max_age}"
            if self.hsts_include_subdomains:
                hsts_value += "; includeSubDomains"
            response.headers["Strict-Transport-Security"] = hsts_value

            # X-Frame-Options (clickjacking protection)
            response.headers["X-Frame-Options"] = "DENY"

            # X-Content-Type-Options (MIME type sniffing protection)
            response.headers["X-Content-Type-Options"] = "nosniff"

            # Referrer Policy (information disclosure protection)
            response.headers["Referrer-Policy"] = self.referrer_policy

            # Content Security Policy (XSS protection)
            response.headers["Content-Security-Policy"] = self.csp_policy

            # X-XSS-Protection (legacy XSS protection for older browsers)
            response.headers["X-XSS-Protection"] = "1; mode=block"

            # Permissions Policy (feature policy replacement)
            response.headers["Permissions-Policy"] = (
                "geolocation=(), microphone=(), camera=(), "
                "payment=(), usb=(), magnetometer=(), gyroscope=(), "
                "accelerometer=(), ambient-light-sensor=()"
            )

    def _add_security_headers(self, headers: MutableHeaders) -> None:
        """Add all security headers to the response."""

        # Strict Transport Security (HSTS)
        hsts_value = f"max-age={self.hsts_max_age}"
        if self.hsts_include_subdomains:
            hsts_value += "; includeSubDomains"
        headers["Strict-Transport-Security"] = hsts_value

        # X-Frame-Options (clickjacking protection)
        headers["X-Frame-Options"] = "DENY"

        # X-Content-Type-Options (MIME type sniffing protection)
        headers["X-Content-Type-Options"] = "nosniff"

        # Referrer Policy (information disclosure protection)
        headers["Referrer-Policy"] = self.referrer_policy

        # Content Security Policy (XSS protection)
        headers["Content-Security-Policy"] = self.csp_policy

        # X-XSS-Protection (legacy XSS protection for older browsers)
        headers["X-XSS-Protection"] = "1; mode=block"

        # Permissions Policy (feature policy replacement)
        headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=(), "
            "payment=(), usb=(), magnetometer=(), gyroscope=(), "
            "accelerometer=(), ambient-light-sensor=()"
        )

        logger.debug(
            "Security headers configuration applied",
            headers_added=[
                "Strict-Transport-Security",
                "X-Frame-Options",
                "X-Content-Type-Options",
                "Referrer-Policy",
                "Content-Security-Policy",
                "X-XSS-Protection",
                "Permissions-Policy",
            ],
        )
