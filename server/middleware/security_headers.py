"""
Security headers middleware for MythosMUD server.

This module provides comprehensive security headers middleware to protect
against common web vulnerabilities including XSS, clickjacking, and
information disclosure attacks.

As noted in the Pnakotic Manuscripts, proper defense against the eldritch
forces requires multiple layers of protection. This middleware provides
the first line of defense against web-based threats.
"""

import os

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from ..logging_config import get_logger

logger = get_logger(__name__)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add comprehensive security headers to all HTTP responses.

    This middleware adds essential security headers to protect against common
    web vulnerabilities including XSS, clickjacking, and information disclosure.
    """

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

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

    async def dispatch(self, request: Request, call_next) -> Response:
        """Add security headers to the response."""
        response = await call_next(request)

        # Add comprehensive security headers
        self._add_security_headers(response)

        return response

    def _add_security_headers(self, response: Response) -> None:
        """Add all security headers to the response."""

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

        logger.debug(
            "Security headers added to response",
            status_code=response.status_code,
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
