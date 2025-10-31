from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import PlainTextResponse

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AllowedCORSMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *, allow_origins, allow_methods, allow_headers, allow_credentials, max_age):
        super().__init__(app)
        self.allow_origins = set(allow_origins or [])
        self.allow_methods = [m.upper() for m in (allow_methods or [])]
        self.allow_headers = allow_headers or []
        self.allow_credentials = bool(allow_credentials)
        self.max_age = int(max_age) if isinstance(max_age, (int, str)) and str(max_age).isdigit() else 600

    async def dispatch(self, request, call_next):
        origin = request.headers.get("origin")
        logger.debug("CORS dispatch", origin=origin, allowed_origins=list(self.allow_origins), method=request.method)
        if origin and origin in self.allow_origins:
            if request.method == "OPTIONS":
                req_method = request.headers.get("access-control-request-method")
                req_headers = request.headers.get("access-control-request-headers", "")
                if not req_method:
                    # Return 400 but include CORS and security headers
                    response = PlainTextResponse("Missing Access-Control-Request-Method", status_code=400)
                    response.headers["access-control-allow-origin"] = origin
                    response.headers["access-control-allow-credentials"] = (
                        "true" if self.allow_credentials else "false"
                    )
                    response.headers["access-control-max-age"] = str(self.max_age)
                    response.headers["access-control-allow-methods"] = ", ".join(sorted(set(self.allow_methods)))
                    response.headers["access-control-allow-headers"] = ", ".join(self.allow_headers)
                    response.headers["vary"] = "Origin"
                    response.headers.setdefault(
                        "Strict-Transport-Security", f"max-age={31536000}; includeSubDomains"
                    )
                    response.headers.setdefault("X-Frame-Options", "DENY")
                    response.headers.setdefault("X-Content-Type-Options", "nosniff")
                    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
                    response.headers.setdefault("Content-Security-Policy", "default-src 'self'")
                    response.headers.setdefault("X-XSS-Protection", "1; mode=block")
                    response.headers.setdefault(
                        "Permissions-Policy",
                        "geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), ambient-light-sensor=()",
                    )
                    return response

                response = PlainTextResponse("", status_code=200)
                response.headers["access-control-allow-origin"] = origin
                response.headers["access-control-allow-credentials"] = "true" if self.allow_credentials else "false"
                response.headers["access-control-max-age"] = str(self.max_age)
                allowed_methods_header = ", ".join(sorted(set(self.allow_methods + [req_method.upper()])))
                response.headers["access-control-allow-methods"] = allowed_methods_header
                response.headers["access-control-allow-headers"] = req_headers or ", ".join(self.allow_headers)
                response.headers["vary"] = "Origin"
                # Security headers on preflight responses
                response.headers.setdefault("Strict-Transport-Security", f"max-age={31536000}; includeSubDomains")
                response.headers.setdefault("X-Frame-Options", "DENY")
                response.headers.setdefault("X-Content-Type-Options", "nosniff")
                response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
                response.headers.setdefault("Content-Security-Policy", "default-src 'self'")
                response.headers.setdefault("X-XSS-Protection", "1; mode=block")
                response.headers.setdefault(
                    "Permissions-Policy",
                    "geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), ambient-light-sensor=()",
                )
                return response

            response = await call_next(request)
            response.headers.setdefault("access-control-allow-origin", origin)
            response.headers.setdefault("access-control-allow-credentials", "true" if self.allow_credentials else "false")
            return response

        if request.method == "OPTIONS":
            response = PlainTextResponse(
                "CORS origin not allowed",
                status_code=400,
                headers={
                    "vary": "Origin",
                    "access-control-allow-methods": ", ".join(self.allow_methods),
                    "access-control-allow-headers": ", ".join(self.allow_headers),
                    "access-control-allow-credentials": "true" if self.allow_credentials else "false",
                },
            )
            # Echo origin when provided, otherwise use wildcard
            req_origin = request.headers.get("origin")
            response.headers["access-control-allow-origin"] = req_origin or "*"
            # Add security headers even on 400 preflight responses
            response.headers.setdefault("Strict-Transport-Security", f"max-age={31536000}; includeSubDomains")
            response.headers.setdefault("X-Frame-Options", "DENY")
            response.headers.setdefault("X-Content-Type-Options", "nosniff")
            response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
            response.headers.setdefault("Content-Security-Policy", "default-src 'self'")
            response.headers.setdefault("X-XSS-Protection", "1; mode=block")
            response.headers.setdefault(
                "Permissions-Policy",
                "geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), ambient-light-sensor=()",
            )
            return response
        return await call_next(request)
