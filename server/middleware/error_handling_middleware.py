"""
Error handling middleware for FastAPI integration.

This module provides middleware to automatically handle exceptions across
all API endpoints, ensuring consistent error responses and comprehensive logging.

As noted in the Pnakotic Manuscripts: "Every error must be intercepted and
properly catalogued, lest the system descend into chaos."
"""

from collections.abc import Callable

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.middleware.base import BaseHTTPMiddleware

from ..error_handlers.standardized_responses import StandardizedErrorResponse
from ..exceptions import (
    LoggedHTTPException,
    MythosMUDError,
)
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle all exceptions across FastAPI endpoints.

    This middleware intercepts all exceptions, converts them to standardized
    error responses, and ensures proper logging with context information.
    """

    def __init__(self, app: FastAPI, include_details: bool = False):
        """
        Initialize error handling middleware.

        Args:
            app: FastAPI application instance
            include_details: Whether to include detailed error information in responses
        """
        super().__init__(app)
        self.include_details = include_details

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and handle any exceptions.

        Args:
            request: FastAPI request object
            call_next: Next middleware or endpoint handler

        Returns:
            Response object (may be error response)
        """
        try:
            # Add request ID to state for tracking
            if not hasattr(request.state, "request_id"):
                import uuid

                request.state.request_id = str(uuid.uuid4())

            # Process the request
            response = await call_next(request)
            return response

        except Exception as exc:
            # Handle the exception and return standardized error response
            return await self._handle_exception(request, exc)

    async def _handle_exception(self, request: Request, exc: Exception) -> JSONResponse:
        """
        Handle an exception and return a standardized error response.

        Args:
            request: FastAPI request object
            exc: The exception to handle

        Returns:
            Standardized JSON error response
        """
        try:
            # Create standardized error response handler with request context
            handler = StandardizedErrorResponse(request=request)

            # Handle the exception and get response
            response = handler.handle_exception(exc, include_details=self.include_details, response_type="http")

            # Log the exception with full context
            self._log_exception(request, exc, response.status_code)

            return response

        except Exception as handler_error:
            # Fallback error handling if the handler itself fails
            logger.error(
                f"Error in error handler: {handler_error}",
                exc_info=True,
                request_id=getattr(request.state, "request_id", None),
            )
            return self._create_fallback_response(request)

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
                f"Server error: {type(exc).__name__}: {str(exc)}",
                exc_info=True,
                **context_data,
            )
        elif status_code >= 400:
            # Client errors are warnings
            logger.warning(
                f"Client error: {type(exc).__name__}: {str(exc)}",
                **context_data,
            )
        else:
            # Other errors are informational
            logger.info(
                f"Request error: {type(exc).__name__}: {str(exc)}",
                **context_data,
            )

    def _create_fallback_response(self, request: Request) -> JSONResponse:
        """
        Create a fallback error response when normal error handling fails.

        Args:
            request: FastAPI request object

        Returns:
            Fallback JSON error response
        """
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "type": "internal_error",
                    "message": "An unexpected error occurred",
                    "user_friendly": "Please try again later",
                    "details": {
                        "request_id": getattr(request.state, "request_id", None),
                        "fallback": True,
                    },
                    "severity": "high",
                }
            },
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
