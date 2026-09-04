"""
Error handling middleware for FastAPI integration.

This module provides middleware to automatically handle exceptions across
all API endpoints, ensuring consistent error responses and comprehensive logging.

As noted in the Pnakotic Manuscripts: "Every error must be intercepted and
properly catalogued, lest the system descend into chaos."

IMPLEMENTATION NOTE: This uses pure ASGI middleware instead of BaseHTTPMiddleware
for better performance and proper type safety with mypy.
"""

import json
import uuid
from collections.abc import Awaitable, Callable, Mapping
from typing import Protocol, cast

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.responses import Response
from starlette.types import ASGIApp, Receive, Scope, Send

from ..error_handlers.standardized_responses import StandardizedErrorResponse
from ..exceptions import (
    LoggedHTTPException,
    MythosMUDError,
)
from ..structured_logging.enhanced_logging_config import get_logger

# Starlette types HTTP exception handlers as (Request, Exception) -> ...; narrower handlers are safe
# at runtime because the router only invokes them for the registered exception type.
HttpExceptionHandler = Callable[[Request, Exception], Awaitable[Response]]

logger = get_logger(__name__)

# Sentinel: user id could not be read (contrast with value None from user.get("id")).
USER_ID_UNAVAILABLE = object()


class _UserObjectWithId(Protocol):
    """Narrowing for dynamic request.state.user shapes that expose .id (non-Mapping)."""

    id: object


def extract_user_id_from_non_mapping(user: object) -> object:
    """
    Read user id from a non-Mapping request.state.user (object with get and/or id).

    Returns USER_ID_UNAVAILABLE when no id can be read (matches prior try/except swallow).
    """
    get_fn = getattr(user, "get", None)
    if callable(get_fn):
        try:
            return get_fn("id")
        except (AttributeError, KeyError, TypeError):
            return USER_ID_UNAVAILABLE
    if hasattr(user, "id"):
        try:
            return cast(_UserObjectWithId, user).id
        except (AttributeError, TypeError):
            return USER_ID_UNAVAILABLE
    return USER_ID_UNAVAILABLE


def request_id_from_scope(scope: Scope) -> str | None:
    """Read request_id from ASGI scope.state (Scope values are Any; avoid untyped .get chains)."""
    state_raw: object = scope.get("state")
    if not isinstance(state_raw, Mapping):
        return None
    state = cast(Mapping[str, object], state_raw)
    rid_obj = state.get("request_id")
    if rid_obj is None:
        return None
    if isinstance(rid_obj, str):
        return rid_obj
    return str(rid_obj)


class ErrorHandlingMiddleware:
    """
    Pure ASGI middleware to handle all exceptions across FastAPI endpoints.

    This middleware intercepts all exceptions, converts them to standardized
    error responses, and ensures proper logging with context information.

    Unlike BaseHTTPMiddleware, this uses pure ASGI for better performance and type safety.
    """

    app: ASGIApp
    include_details: bool

    def __init__(self, app: ASGIApp, include_details: bool = False) -> None:
        """
        Initialize error handling middleware.

        Args:
            app: ASGI application instance
            include_details: Whether to include detailed error information in responses
        """
        self.app = app
        self.include_details = include_details

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

        # Add request ID to scope
        if "state" not in scope:
            scope["state"] = {}
        if "request_id" not in scope["state"]:
            scope["state"]["request_id"] = str(uuid.uuid4())

        try:
            # Process the request
            await self.app(scope, receive, send)

        except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904
            # JUSTIFICATION: This is error handling middleware that must catch ALL exceptions to ensure
            # proper error responses are sent. The exception is then passed to _handle_exception which
            # properly categorizes and handles different exception types (HTTPException, ValidationError, etc.)
            # Handle the exception and send error response
            await self._handle_exception(scope, receive, send, exc)

    async def _handle_exception(self, scope: Scope, receive: Receive, send: Send, exc: Exception) -> None:
        """
        Handle an exception and send a standardized error response.

        Args:
            scope: ASGI scope
            receive: ASGI receive callable
            send: ASGI send callable
            exc: The exception to handle
        """
        # Create Request for error handling
        request = Request(scope, receive)

        try:
            # Create standardized error response handler with request context
            handler = StandardizedErrorResponse(request=request)

            # Handle the exception and get response
            response = handler.handle_exception(exc, include_details=self.include_details, response_type="http")

            # Log the exception with full context
            self.log_exception(request, exc, response.status_code)

            await send(
                {
                    "type": "http.response.start",
                    "status": response.status_code,
                    "headers": [(b"content-type", b"application/json")],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": response.body,
                }
            )

        except Exception as handler_error:  # pylint: disable=broad-exception-caught  # noqa: B904
            # JUSTIFICATION: This is a fallback error handler that catches ALL exceptions when the error
            # handler itself fails. This is the last resort to ensure some error response is sent even
            # if the primary error handling code encounters an unexpected error.
            # Fallback error handling if the handler itself fails
            logger.error(
                "Error in error handler",
                error=str(handler_error),
                exc_info=True,
                request_id=request_id_from_scope(scope),
            )
            # Send fallback response
            fallback_body = json.dumps(
                {
                    "error": {
                        "type": "internal_error",
                        "message": "An unexpected error occurred",
                        "user_friendly": "Please try again later",
                        "details": {
                            "request_id": request_id_from_scope(scope),
                            "fallback": True,
                        },
                        "severity": "high",
                    }
                }
            ).encode("utf-8")

            await send(
                {
                    "type": "http.response.start",
                    "status": 500,
                    "headers": [(b"content-type", b"application/json")],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": fallback_body,
                }
            )

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        """
        Backward-compatible dispatch method for BaseHTTPMiddleware interface.

        This method provides compatibility with tests and code that expects
        the BaseHTTPMiddleware.dispatch() signature.

        Args:
            request: HTTP request
            call_next: Callable to invoke next middleware/handler

        Returns:
            HTTP response or JSON error response
        """
        # Add request ID to state for tracking
        if not hasattr(request.state, "request_id"):
            request.state.request_id = str(uuid.uuid4())

        try:
            response = await call_next(request)
            return response
        except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904
            # JUSTIFICATION: This is error handling middleware that must catch ALL exceptions to ensure
            # proper error responses are returned. The exception is then passed to StandardizedErrorResponse
            # which properly categorizes and handles different exception types (HTTPException, ValidationError, etc.)
            # Handle exception and return JSON response
            handler = StandardizedErrorResponse(request=request)
            response = handler.handle_exception(exc, include_details=self.include_details, response_type="http")
            self.log_exception(request, exc, response.status_code)
            return response

    def log_exception(self, request: Request, exc: Exception, status_code: int) -> None:
        """
        Log the exception with full context information.

        Public entry point so unit tests can assert structured log context; also used from
        ASGI and dispatch paths after StandardizedErrorResponse runs.

        Args:
            request: FastAPI request object
            exc: The exception that occurred
            status_code: HTTP status code of the response
        """
        # Extract context from request
        context_data = {
            "request_id": getattr(request.state, "request_id", None),
            "method": request.method,
            "url": str(request.url),
            "status_code": status_code,
        }

        # Add user information if available
        if hasattr(request.state, "user"):
            user_obj = cast(object, request.state.user)
            if isinstance(user_obj, Mapping):
                user_map = cast(Mapping[str, object], user_obj)
                context_data["user_id"] = user_map.get("id")
            else:
                extracted = extract_user_id_from_non_mapping(user_obj)
                if extracted is not USER_ID_UNAVAILABLE:
                    context_data["user_id"] = extracted

        # Add session information if available
        if hasattr(request.state, "session_id"):
            context_data["session_id"] = cast(object, request.state.session_id)

        # Determine log level based on exception type and status code
        if isinstance(exc, MythosMUDError | LoggedHTTPException):
            # These are already logged by their constructors
            pass
        elif status_code >= 500:
            # Server errors are critical
            logger.error(
                "Server error",
                error_type=type(exc).__name__,
                error=str(exc),
                exc_info=True,
                **context_data,
            )
        elif status_code >= 400:
            # Client errors are warnings
            logger.warning(
                "Client error",
                error_type=type(exc).__name__,
                error=str(exc),
                **context_data,
            )
        else:
            # Other errors are informational
            logger.info(
                "Request error",
                error_type=type(exc).__name__,
                error=str(exc),
                **context_data,
            )


def add_error_handling_middleware(app: FastAPI, include_details: bool = False) -> None:
    """
    Add error handling middleware to FastAPI application.

    Args:
        app: FastAPI application instance
        include_details: Whether to include detailed error information in responses
                        (typically False in production, True in development)

    Example:
        ```python
        from fastapi import FastAPI
        from server.middleware.error_handling_middleware import add_error_handling_middleware

        app = FastAPI()
        add_error_handling_middleware(app, include_details=True)
        ```
    """
    app.add_middleware(ErrorHandlingMiddleware, include_details=include_details)
    logger.info("Error handling middleware added", include_details=include_details)


# Additional error handlers for FastAPI exception handlers
def register_error_handlers(app: FastAPI, include_details: bool = False) -> None:
    """
    Register error handlers for FastAPI application.

    This function registers exception handlers for common exception types
    to ensure consistent error responses across the application.

    Args:
        app: FastAPI application instance
        include_details: Whether to include detailed error information in responses

    Example:
        ```python
        from fastapi import FastAPI
        from server.middleware.error_handling_middleware import register_error_handlers

        app = FastAPI()
        register_error_handlers(app, include_details=True)
        ```
    """

    async def mythos_error_handler(request: Request, exc: MythosMUDError) -> JSONResponse:
        """Handle MythosMUDError exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    async def pydantic_validation_error_handler(request: Request, exc: ValidationError) -> JSONResponse:
        """Handle Pydantic ValidationError exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
        """Handle FastAPI HTTPException exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    async def logged_http_exception_handler(request: Request, exc: LoggedHTTPException) -> JSONResponse:
        """Handle LoggedHTTPException exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """Handle all other exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    app.add_exception_handler(MythosMUDError, cast(HttpExceptionHandler, mythos_error_handler))
    app.add_exception_handler(ValidationError, cast(HttpExceptionHandler, pydantic_validation_error_handler))
    app.add_exception_handler(HTTPException, cast(HttpExceptionHandler, http_exception_handler))
    app.add_exception_handler(LoggedHTTPException, cast(HttpExceptionHandler, logged_http_exception_handler))
    app.add_exception_handler(Exception, generic_exception_handler)

    logger.info("Error handlers registered for FastAPI application")


def setup_error_handling(app: FastAPI, include_details: bool = False) -> None:
    """
    Setup complete error handling for FastAPI application.

    This function sets up both middleware and exception handlers for
    comprehensive error handling across the application.

    Args:
        app: FastAPI application instance
        include_details: Whether to include detailed error information in responses

    Example:
        ```python
        from fastapi import FastAPI
        from server.middleware.error_handling_middleware import setup_error_handling

        app = FastAPI()
        setup_error_handling(app, include_details=True)
        ```
    """
    # Add middleware for catching exceptions
    add_error_handling_middleware(app, include_details=include_details)

    # Register exception handlers for specific exception types
    register_error_handlers(app, include_details=include_details)

    logger.info("Complete error handling setup completed")
