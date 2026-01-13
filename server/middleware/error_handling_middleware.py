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
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from pydantic import ValidationError
from starlette.types import ASGIApp, Receive, Scope, Send

from ..error_handlers.standardized_responses import StandardizedErrorResponse
from ..exceptions import (
    LoggedHTTPException,
    MythosMUDError,
)
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ErrorHandlingMiddleware:
    """
    Pure ASGI middleware to handle all exceptions across FastAPI endpoints.

    This middleware intercepts all exceptions, converts them to standardized
    error responses, and ensures proper logging with context information.

    Unlike BaseHTTPMiddleware, this uses pure ASGI for better performance and type safety.
    """

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

        except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904            # JUSTIFICATION: This is error handling middleware that must catch ALL exceptions to ensure
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
            self._log_exception(request, exc, response.status_code)

            # Send the error response (guard against None send callable)
            # JUSTIFICATION: ASGI spec requires send to be callable, but defensive programming guards
            # against None. Mypy's type narrowing doesn't account for this runtime check.
            if send is None:
                logger.error("Cannot send error response: send callable is None", exc_info=True)  # type: ignore[unreachable]  # Reason: ASGI spec requires send to be callable, but defensive programming guards against None, mypy's type narrowing doesn't account for this runtime check
                return
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

        except Exception as handler_error:  # pylint: disable=broad-exception-caught  # noqa: B904            # JUSTIFICATION: This is a fallback error handler that catches ALL exceptions when the error
            # handler itself fails. This is the last resort to ensure some error response is sent even
            # if the primary error handling code encounters an unexpected error.
            # Fallback error handling if the handler itself fails
            logger.error(
                "Error in error handler",
                error=str(handler_error),
                exc_info=True,
                request_id=scope["state"].get("request_id"),
            )
            # Send fallback response
            fallback_body = json.dumps(
                {
                    "error": {
                        "type": "internal_error",
                        "message": "An unexpected error occurred",
                        "user_friendly": "Please try again later",
                        "details": {
                            "request_id": scope["state"].get("request_id"),
                            "fallback": True,
                        },
                        "severity": "high",
                    }
                }
            ).encode("utf-8")

            # Guard against None send callable
            # JUSTIFICATION: ASGI spec requires send to be callable, but defensive programming guards
            # against None. Mypy's type narrowing doesn't account for this runtime check.
            if send is None:
                logger.error("Cannot send fallback error response: send callable is None", exc_info=True)  # type: ignore[unreachable]  # Reason: ASGI spec requires send to be callable, but defensive programming guards against None, mypy's type narrowing doesn't account for this runtime check
                return
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

    async def dispatch(self, request: Request, call_next: Any) -> Any:
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
        except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904            # JUSTIFICATION: This is error handling middleware that must catch ALL exceptions to ensure
            # proper error responses are returned. The exception is then passed to StandardizedErrorResponse
            # which properly categorizes and handles different exception types (HTTPException, ValidationError, etc.)
            # Handle exception and return JSON response
            handler = StandardizedErrorResponse(request=request)
            response = handler.handle_exception(exc, include_details=self.include_details, response_type="http")
            self._log_exception(request, exc, response.status_code)
            return response

    def _log_exception(self, request: Request, exc: Exception, status_code: int):
        """
        Log the exception with full context information.

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
            try:
                if hasattr(request.state.user, "get"):
                    context_data["user_id"] = request.state.user.get("id")
                elif hasattr(request.state.user, "id"):
                    context_data["user_id"] = request.state.user.id
            except (AttributeError, KeyError, TypeError):
                pass

        # Add session information if available
        if hasattr(request.state, "session_id"):
            context_data["session_id"] = request.state.session_id

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


def add_error_handling_middleware(app: FastAPI, include_details: bool = False):
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
def register_error_handlers(app: FastAPI, include_details: bool = False):
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

    @app.exception_handler(MythosMUDError)
    async def mythos_error_handler(request: Request, exc: MythosMUDError):
        """Handle MythosMUDError exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    @app.exception_handler(ValidationError)
    async def pydantic_validation_error_handler(request: Request, exc: ValidationError):
        """Handle Pydantic ValidationError exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        """Handle FastAPI HTTPException exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    @app.exception_handler(LoggedHTTPException)
    async def logged_http_exception_handler(request: Request, exc: LoggedHTTPException):
        """Handle LoggedHTTPException exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        """Handle all other exceptions."""
        handler = StandardizedErrorResponse(request=request)
        return handler.handle_exception(exc, include_details=include_details)

    logger.info("Error handlers registered for FastAPI application")


def setup_error_handling(app: FastAPI, include_details: bool = False):
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
