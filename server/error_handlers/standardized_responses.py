"""
Standardized error response formats for all API endpoints.

This module provides comprehensive error response standardization to ensure
all API endpoints return consistent error formats across the entire application.
It integrates with the existing error handling infrastructure while providing
enhanced standardization and user-friendly message generation.

As noted in the Necronomicon: "The responses of the ancients must be
consistent in form and structure, lest the mortal mind be overwhelmed
by the chaos of inconsistent error reporting."
"""

from typing import Any

from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from ..error_handlers.pydantic_error_handler import PydanticErrorHandler
from ..error_types import (
    ErrorMessages,
    ErrorSeverity,
    ErrorType,
    create_sse_error_response,
    create_standard_error_response,
    create_websocket_error_response,
)
from ..exceptions import (
    AuthenticationError,
    DatabaseError,
    ErrorContext,
    GameLogicError,
    LoggedHTTPException,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    create_error_context,
)
from ..exceptions import (
    ValidationError as MythosValidationError,
)
from ..logging_config import get_logger

logger = get_logger(__name__)


class StandardizedErrorResponse:
    """
    Standardized error response handler for all API endpoints.

    This class provides comprehensive error response standardization
    with automatic error type detection, user-friendly message generation,
    and consistent formatting across all response types.
    """

    # HTTP status code mappings for different error types
    STATUS_CODE_MAPPINGS = {
        # Authentication errors
        ErrorType.AUTHENTICATION_FAILED: status.HTTP_401_UNAUTHORIZED,
        ErrorType.AUTHORIZATION_DENIED: status.HTTP_403_FORBIDDEN,
        ErrorType.INVALID_TOKEN: status.HTTP_401_UNAUTHORIZED,
        ErrorType.TOKEN_EXPIRED: status.HTTP_401_UNAUTHORIZED,
        # Validation errors
        ErrorType.VALIDATION_ERROR: status.HTTP_422_UNPROCESSABLE_ENTITY,
        ErrorType.INVALID_INPUT: status.HTTP_400_BAD_REQUEST,
        ErrorType.MISSING_REQUIRED_FIELD: status.HTTP_400_BAD_REQUEST,
        ErrorType.INVALID_FORMAT: status.HTTP_400_BAD_REQUEST,
        # Resource errors
        ErrorType.RESOURCE_NOT_FOUND: status.HTTP_404_NOT_FOUND,
        ErrorType.RESOURCE_ALREADY_EXISTS: status.HTTP_409_CONFLICT,
        ErrorType.RESOURCE_CONFLICT: status.HTTP_409_CONFLICT,
        # Game logic errors
        ErrorType.GAME_LOGIC_ERROR: status.HTTP_400_BAD_REQUEST,
        ErrorType.INVALID_COMMAND: status.HTTP_400_BAD_REQUEST,
        ErrorType.INVALID_MOVEMENT: status.HTTP_400_BAD_REQUEST,
        ErrorType.PLAYER_NOT_IN_ROOM: status.HTTP_400_BAD_REQUEST,
        # Database errors
        ErrorType.DATABASE_ERROR: status.HTTP_503_SERVICE_UNAVAILABLE,
        ErrorType.DATABASE_CONNECTION_ERROR: status.HTTP_503_SERVICE_UNAVAILABLE,
        ErrorType.DATABASE_QUERY_ERROR: status.HTTP_503_SERVICE_UNAVAILABLE,
        # Network errors
        ErrorType.NETWORK_ERROR: status.HTTP_503_SERVICE_UNAVAILABLE,
        ErrorType.CONNECTION_ERROR: status.HTTP_503_SERVICE_UNAVAILABLE,
        ErrorType.TIMEOUT_ERROR: status.HTTP_504_GATEWAY_TIMEOUT,
        # Rate limiting
        ErrorType.RATE_LIMIT_EXCEEDED: status.HTTP_429_TOO_MANY_REQUESTS,
        ErrorType.TOO_MANY_REQUESTS: status.HTTP_429_TOO_MANY_REQUESTS,
        # System errors
        ErrorType.CONFIGURATION_ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR,
        ErrorType.SYSTEM_ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR,
        ErrorType.INTERNAL_ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR,
        # Real-time communication
        ErrorType.WEBSOCKET_ERROR: status.HTTP_400_BAD_REQUEST,
        ErrorType.SSE_ERROR: status.HTTP_400_BAD_REQUEST,
        ErrorType.MESSAGE_PROCESSING_ERROR: status.HTTP_400_BAD_REQUEST,
    }

    # User-friendly message mappings for common scenarios
    USER_FRIENDLY_MESSAGES = {
        ErrorType.AUTHENTICATION_FAILED: ErrorMessages.AUTHENTICATION_REQUIRED,
        ErrorType.AUTHORIZATION_DENIED: "Access denied",
        ErrorType.INVALID_TOKEN: "Invalid authentication token",
        ErrorType.TOKEN_EXPIRED: ErrorMessages.TOKEN_EXPIRED,
        ErrorType.VALIDATION_ERROR: ErrorMessages.INVALID_INPUT,
        ErrorType.INVALID_INPUT: ErrorMessages.INVALID_INPUT,
        ErrorType.MISSING_REQUIRED_FIELD: ErrorMessages.MISSING_REQUIRED_FIELD,
        ErrorType.INVALID_FORMAT: ErrorMessages.INVALID_FORMAT,
        ErrorType.RESOURCE_NOT_FOUND: ErrorMessages.RESOURCE_NOT_FOUND,
        ErrorType.RESOURCE_ALREADY_EXISTS: "Resource already exists",
        ErrorType.RESOURCE_CONFLICT: "Resource conflict occurred",
        ErrorType.GAME_LOGIC_ERROR: "Invalid game action",
        ErrorType.INVALID_COMMAND: ErrorMessages.INVALID_COMMAND,
        ErrorType.INVALID_MOVEMENT: ErrorMessages.INVALID_MOVEMENT,
        ErrorType.PLAYER_NOT_IN_ROOM: ErrorMessages.PLAYER_NOT_IN_ROOM,
        ErrorType.DATABASE_ERROR: "Database error occurred",
        ErrorType.DATABASE_CONNECTION_ERROR: "Database connection failed",
        ErrorType.DATABASE_QUERY_ERROR: "Database query failed",
        ErrorType.NETWORK_ERROR: ErrorMessages.CONNECTION_ERROR,
        ErrorType.CONNECTION_ERROR: ErrorMessages.CONNECTION_ERROR,
        ErrorType.TIMEOUT_ERROR: ErrorMessages.TIMEOUT_ERROR,
        ErrorType.RATE_LIMIT_EXCEEDED: ErrorMessages.TOO_MANY_REQUESTS,
        ErrorType.TOO_MANY_REQUESTS: ErrorMessages.TOO_MANY_REQUESTS,
        ErrorType.CONFIGURATION_ERROR: "Configuration error",
        ErrorType.SYSTEM_ERROR: "System error occurred",
        ErrorType.INTERNAL_ERROR: ErrorMessages.INTERNAL_ERROR,
        ErrorType.WEBSOCKET_ERROR: ErrorMessages.WEBSOCKET_ERROR,
        ErrorType.SSE_ERROR: ErrorMessages.SSE_ERROR,
        ErrorType.MESSAGE_PROCESSING_ERROR: ErrorMessages.MESSAGE_PROCESSING_ERROR,
    }

    def __init__(self, request: Request | None = None):
        """
        Initialize standardized error response handler.

        Args:
            request: Optional FastAPI request for context extraction
        """
        self.request = request
        self.context = self._extract_context_from_request(request)

    def _extract_context_from_request(self, request: Request | None) -> ErrorContext:
        """Extract error context from FastAPI request."""
        if not request:
            return create_error_context()

        # Extract context information from request
        context_data = {}

        # Extract user information if available
        if hasattr(request.state, "user") and request.state.user:
            # Handle both dict and object-style user attributes
            try:
                # Try dict-style access first
                if hasattr(request.state.user, "get"):
                    context_data["user_id"] = str(request.state.user.get("id", ""))
                elif hasattr(request.state.user, "__getitem__"):
                    context_data["user_id"] = str(request.state.user["id"])
                elif hasattr(request.state.user, "id"):
                    context_data["user_id"] = str(request.state.user.id)
            except (KeyError, AttributeError, TypeError):
                # Silently skip if user information cannot be extracted
                pass

        # Extract session information
        if hasattr(request.state, "session_id"):
            context_data["session_id"] = request.state.session_id

        # Extract request information
        context_data["request_id"] = getattr(request.state, "request_id", None)

        # Extract additional metadata
        metadata = {}
        if hasattr(request, "url"):
            metadata["url"] = str(request.url)
        if hasattr(request, "method"):
            metadata["method"] = request.method
        if hasattr(request, "headers"):
            metadata["user_agent"] = request.headers.get("user-agent", "")
            metadata["content_type"] = request.headers.get("content-type", "")

        context_data["metadata"] = metadata

        return create_error_context(**context_data)

    def handle_exception(
        self, exc: Exception, include_details: bool = False, response_type: str = "http"
    ) -> JSONResponse:
        """
        Handle any exception and return a standardized error response.

        Args:
            exc: The exception to handle
            include_details: Whether to include detailed error information
            response_type: Type of response ("http", "websocket", "sse")

        Returns:
            Standardized JSONResponse
        """
        try:
            # Handle different exception types
            if isinstance(exc, MythosMUDError):
                return self._handle_mythos_error(exc, include_details, response_type)
            elif isinstance(exc, ValidationError):
                return self._handle_pydantic_validation_error(exc, include_details, response_type)
            elif isinstance(exc, LoggedHTTPException):
                return self._handle_logged_http_exception(exc, include_details, response_type)
            elif isinstance(exc, HTTPException):
                return self._handle_http_exception(exc, include_details, response_type)
            else:
                return self._handle_generic_exception(exc, include_details, response_type)

        except Exception as e:
            # Fallback error handling
            logger.error(f"Error in StandardizedErrorResponse: {e}", exc_info=True)
            return self._create_fallback_response(exc, response_type)

    def _handle_mythos_error(self, error: MythosMUDError, include_details: bool, response_type: str) -> JSONResponse:
        """Handle MythosMUDError instances."""
        # Determine error type and status code
        error_type = self._determine_error_type_from_exception(error)
        status_code = self.STATUS_CODE_MAPPINGS.get(error_type, status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Generate user-friendly message
        user_friendly = self._generate_user_friendly_message(error_type, error)

        # Create error details
        details = self._create_error_details(error, include_details)

        # Create appropriate response
        if response_type == "websocket":
            response_data = create_websocket_error_response(
                error_type=error_type, message=error.message, user_friendly=user_friendly, details=details
            )
            return JSONResponse(status_code=status_code, content=response_data)
        elif response_type == "sse":
            response_data = create_sse_error_response(
                error_type=error_type, message=error.message, user_friendly=user_friendly, details=details
            )
            return JSONResponse(status_code=status_code, content=response_data)
        else:  # HTTP
            response_data = create_standard_error_response(
                error_type=error_type,
                message=error.message,
                user_friendly=user_friendly,
                details=details,
                severity=ErrorSeverity.MEDIUM,
            )
            return JSONResponse(status_code=status_code, content=response_data)

    def _handle_pydantic_validation_error(
        self, error: ValidationError, include_details: bool, response_type: str
    ) -> JSONResponse:
        """Handle Pydantic ValidationError instances."""
        # Use PydanticErrorHandler for consistent processing
        handler = PydanticErrorHandler(context=self.context)
        response_data = handler.handle_validation_error(error, response_type=response_type)

        # Determine status code
        error_type = ErrorType(response_data.get("error_type", "validation_error"))
        status_code = self.STATUS_CODE_MAPPINGS.get(error_type, status.HTTP_422_UNPROCESSABLE_ENTITY)

        return JSONResponse(status_code=status_code, content=response_data)

    def _handle_logged_http_exception(
        self, exc: LoggedHTTPException, include_details: bool, response_type: str
    ) -> JSONResponse:
        """Handle LoggedHTTPException instances."""
        # Map status code to error type
        error_type = self._map_status_code_to_error_type(exc.status_code)
        user_friendly = self.USER_FRIENDLY_MESSAGES.get(error_type, ErrorMessages.INTERNAL_ERROR)

        # Create error details
        details = {"status_code": exc.status_code}
        if include_details:
            details["original_detail"] = str(exc.detail)

        # Create appropriate response
        if response_type == "websocket":
            response_data = create_websocket_error_response(
                error_type=error_type, message=str(exc.detail), user_friendly=user_friendly, details=details
            )
        elif response_type == "sse":
            response_data = create_sse_error_response(
                error_type=error_type, message=str(exc.detail), user_friendly=user_friendly, details=details
            )
        else:  # HTTP
            response_data = create_standard_error_response(
                error_type=error_type,
                message=str(exc.detail),
                user_friendly=user_friendly,
                details=details,
                severity=ErrorSeverity.MEDIUM,
            )

        return JSONResponse(status_code=exc.status_code, content=response_data)

    def _handle_http_exception(self, exc: HTTPException, include_details: bool, response_type: str) -> JSONResponse:
        """Handle standard HTTPException instances."""
        # Map status code to error type
        error_type = self._map_status_code_to_error_type(exc.status_code)
        user_friendly = self.USER_FRIENDLY_MESSAGES.get(error_type, ErrorMessages.INTERNAL_ERROR)

        # Create error details
        details = {"status_code": exc.status_code}
        if include_details:
            details["original_detail"] = str(exc.detail)

        # Create appropriate response
        response_data = create_standard_error_response(
            error_type=error_type,
            message=str(exc.detail),
            user_friendly=user_friendly,
            details=details,
            severity=ErrorSeverity.MEDIUM,
        )

        return JSONResponse(status_code=exc.status_code, content=response_data)

    def _handle_generic_exception(self, exc: Exception, include_details: bool, response_type: str) -> JSONResponse:
        """Handle generic exceptions."""
        error_type = ErrorType.INTERNAL_ERROR
        message = str(exc) if str(exc) else "An unexpected error occurred"
        user_friendly = ErrorMessages.INTERNAL_ERROR

        # Create error details
        details = {}
        if include_details:
            details["exception_type"] = type(exc).__name__
            details["exception_message"] = str(exc)

        # Log the error
        logger.error(f"Unhandled exception: {exc}", exc_info=True, context=self.context.to_dict())

        # Create appropriate response
        response_data = create_standard_error_response(
            error_type=error_type,
            message=message,
            user_friendly=user_friendly,
            details=details,
            severity=ErrorSeverity.HIGH,
        )

        status_code = self.STATUS_CODE_MAPPINGS.get(error_type, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JSONResponse(status_code=status_code, content=response_data)

    def _determine_error_type_from_exception(self, error: MythosMUDError) -> ErrorType:
        """Determine ErrorType from MythosMUDError instance."""
        # Map exception types to error types
        if isinstance(error, AuthenticationError):
            return ErrorType.AUTHENTICATION_FAILED
        elif isinstance(error, MythosValidationError):
            return ErrorType.VALIDATION_ERROR
        elif isinstance(error, GameLogicError):
            return ErrorType.GAME_LOGIC_ERROR
        elif isinstance(error, DatabaseError):
            return ErrorType.DATABASE_ERROR
        elif isinstance(error, NetworkError):
            return ErrorType.NETWORK_ERROR
        elif isinstance(error, RateLimitError):
            return ErrorType.RATE_LIMIT_EXCEEDED
        elif isinstance(error, ResourceNotFoundError):
            return ErrorType.RESOURCE_NOT_FOUND
        else:
            return ErrorType.INTERNAL_ERROR

    def _map_status_code_to_error_type(self, status_code: int) -> ErrorType:
        """Map HTTP status code to ErrorType."""
        mapping = {
            400: ErrorType.INVALID_INPUT,
            401: ErrorType.AUTHENTICATION_FAILED,
            403: ErrorType.AUTHORIZATION_DENIED,
            404: ErrorType.RESOURCE_NOT_FOUND,
            409: ErrorType.RESOURCE_CONFLICT,
            422: ErrorType.VALIDATION_ERROR,
            429: ErrorType.RATE_LIMIT_EXCEEDED,
            500: ErrorType.INTERNAL_ERROR,
            503: ErrorType.SYSTEM_ERROR,
            504: ErrorType.TIMEOUT_ERROR,
        }
        return mapping.get(status_code, ErrorType.INTERNAL_ERROR)

    def _generate_user_friendly_message(self, error_type: ErrorType, error: MythosMUDError) -> str:
        """Generate user-friendly message for error."""
        # Use error's user_friendly message if available
        if hasattr(error, "user_friendly") and error.user_friendly:
            return error.user_friendly

        # Fall back to predefined messages
        return self.USER_FRIENDLY_MESSAGES.get(error_type, ErrorMessages.INTERNAL_ERROR)

    def _create_error_details(self, error: MythosMUDError, include_details: bool) -> dict[str, Any]:
        """Create error details dictionary."""
        details = {}

        if include_details:
            # Include error details
            details.update(error.details)

            # Include context information
            details["context"] = {
                "user_id": error.context.user_id,
                "session_id": error.context.session_id,
                "request_id": error.context.request_id,
            }

        return details

    def _create_fallback_response(self, exc: Exception, response_type: str) -> JSONResponse:
        """Create fallback error response when normal handling fails."""
        message = "An unexpected error occurred"
        user_friendly = "Please try again later"

        if response_type == "websocket":
            response_data = create_websocket_error_response(
                error_type=ErrorType.INTERNAL_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
            )
        elif response_type == "sse":
            response_data = create_sse_error_response(
                error_type=ErrorType.INTERNAL_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
            )
        else:
            response_data = create_standard_error_response(
                error_type=ErrorType.INTERNAL_ERROR,
                message=message,
                user_friendly=user_friendly,
                details={"fallback": True},
                severity=ErrorSeverity.HIGH,
            )

        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=response_data)


# Convenience functions for common use cases
def create_standardized_error_response(
    request: Request | None = None, include_details: bool = False, response_type: str = "http"
) -> StandardizedErrorResponse:
    """
    Create a standardized error response handler.

    Args:
        request: Optional FastAPI request for context
        include_details: Whether to include detailed error information
        response_type: Type of response ("http", "websocket", "sse")

    Returns:
        StandardizedErrorResponse instance
    """
    return StandardizedErrorResponse(request=request)


def handle_api_error(
    exc: Exception, request: Request | None = None, include_details: bool = False, response_type: str = "http"
) -> JSONResponse:
    """
    Convenience function to handle API errors with standardized responses.

    Args:
        exc: The exception to handle
        request: Optional FastAPI request for context
        include_details: Whether to include detailed error information
        response_type: Type of response ("http", "websocket", "sse")

    Returns:
        Standardized JSONResponse
    """
    handler = StandardizedErrorResponse(request=request)
    return handler.handle_exception(exc, include_details, response_type)
