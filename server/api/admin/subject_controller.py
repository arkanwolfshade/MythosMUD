"""
NATS Subject Management API Controller for MythosMUD.

This module provides REST API endpoints for managing and monitoring NATS subject patterns.
It enables administrators to view pattern statistics, validate subjects, and register new patterns.

As noted in the Pnakotic Manuscripts, proper subject management APIs
are essential for maintaining oversight of our messaging infrastructure.

AI: Implements admin API endpoints for subject pattern management.
AI: Includes health monitoring, pattern validation, and dynamic registration.
"""

import time
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from ...auth.dependencies import get_current_user
from ...exceptions import LoggedHTTPException, create_error_context
from ...services.nats_subject_manager import (
    InvalidPatternError,
    NATSSubjectManager,
    PatternNotFoundError,
    nats_subject_manager,
)
from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ...models.user import User

logger = get_logger("api.admin.subject_controller")

router = APIRouter(prefix="/nats/subjects", tags=["admin", "nats", "subjects"])


# Request/Response Models


class ValidateSubjectRequest(BaseModel):
    """Request model for subject validation."""

    subject: str = Field(..., description="NATS subject to validate")


class ValidateSubjectResponse(BaseModel):
    """Response model for subject validation."""

    subject: str
    is_valid: bool
    validation_time_ms: float
    details: str | None = None


class RegisterPatternRequest(BaseModel):
    """Request model for pattern registration."""

    name: str = Field(..., description="Unique name for the pattern")
    pattern: str = Field(..., description="Pattern template with {param} placeholders")
    required_params: list[str] = Field(..., description="List of required parameter names")
    description: str = Field(default="", description="Human-readable description")


class RegisterPatternResponse(BaseModel):
    """Response model for pattern registration."""

    success: bool
    pattern_name: str
    message: str


class SubjectStatisticsResponse(BaseModel):
    """Response model for subject management statistics."""

    status: str
    metrics: dict[str, Any] | None
    patterns_registered: int
    cache_enabled: bool
    strict_validation: bool


class PatternsResponse(BaseModel):
    """Response model for pattern listing."""

    patterns: dict[str, dict[str, Any]]
    total_count: int


# Dependency Functions


def get_subject_manager_dependency() -> NATSSubjectManager:
    """
    Dependency function to inject NATSSubjectManager.

    Returns:
        Global NATSSubjectManager instance

    AI: Provides subject manager instance for endpoint dependency injection.
    """
    return nats_subject_manager


def require_admin_user(current_user: "User" = Depends(get_current_user)) -> "User":
    """
    Dependency to require admin permissions.

    Args:
        current_user: Current authenticated user

    Returns:
        User if admin, raises 403 otherwise

    Raises:
        LoggedHTTPException: If user is not an admin

    AI: Enforces admin-only access for sensitive endpoints.
    """
    if not getattr(current_user, "is_admin", False):
        raise LoggedHTTPException(
            status_code=403,
            detail="Admin permissions required",
            context=create_error_context(
                user_id=getattr(current_user, "id", None),
                metadata={"operation": "admin_check", "username": getattr(current_user, "username", None)},
            ),
        )
    return current_user


# API Endpoints


@router.get("/health", response_model=SubjectStatisticsResponse)
async def get_subject_statistics(
    subject_manager: NATSSubjectManager = Depends(get_subject_manager_dependency),
) -> SubjectStatisticsResponse:
    """
    Get NATS subject management statistics and health status.

    This endpoint provides observability into subject pattern usage,
    validation performance, and cache efficiency.

    Returns:
        Subject management statistics including metrics and configuration

    Raises:
        LoggedHTTPException: If metrics retrieval fails

    AI: Public health endpoint - no admin required for monitoring.
    AI: Provides performance metrics for observability and alerting.
    """
    try:
        # Get performance metrics
        metrics = subject_manager.get_performance_metrics()

        # Get configuration info
        patterns_count = len(subject_manager.patterns)
        cache_enabled = subject_manager._cache_enabled  # pylint: disable=protected-access  # Reason: Configuration access required for admin statistics
        strict_validation = subject_manager._strict_validation  # pylint: disable=protected-access  # Reason: Configuration access required for admin statistics

        logger.info(
            "Subject statistics requested",
            patterns_count=patterns_count,
            metrics_available=metrics is not None,
        )

        return SubjectStatisticsResponse(
            status="healthy",
            metrics=metrics,
            patterns_registered=patterns_count,
            cache_enabled=cache_enabled,
            strict_validation=strict_validation,
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Statistics retrieval errors unpredictable, must create error context
        logger.error("Error retrieving subject statistics", error=str(e), error_type=type(e).__name__)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to retrieve subject statistics",
            context=create_error_context(metadata={"operation": "get_subject_statistics", "error": str(e)}),
        ) from e


@router.post("/validate", response_model=ValidateSubjectResponse)
async def validate_subject(
    request: ValidateSubjectRequest,
    current_user: "User" = Depends(require_admin_user),
    subject_manager: NATSSubjectManager = Depends(get_subject_manager_dependency),
) -> ValidateSubjectResponse:
    """
    Validate a NATS subject against registered patterns.

    This endpoint allows administrators to test subject validation
    and verify subject formatting before use.

    Args:
        request: Subject validation request
        current_user: Current authenticated admin user
        subject_manager: Subject manager dependency

    Returns:
        Validation result with timing information

    Raises:
        LoggedHTTPException: If validation fails or errors occur

    AI: Admin-only endpoint for subject validation testing.
    AI: Records validation time for performance monitoring.
    """
    try:
        start_time = time.perf_counter()

        # Validate the subject
        is_valid = subject_manager.validate_subject(request.subject)

        duration = time.perf_counter() - start_time

        logger.info(
            "Subject validation requested",
            subject=request.subject,
            is_valid=is_valid,
            duration_ms=duration * 1000,
            user_id=current_user.id,
        )

        details = None
        if not is_valid:
            details = "Subject does not match any registered patterns"

        return ValidateSubjectResponse(
            subject=request.subject,
            is_valid=is_valid,
            validation_time_ms=duration * 1000,
            details=details,
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subject validation errors unpredictable, must create error context
        logger.error(
            "Error validating subject",
            error=str(e),
            error_type=type(e).__name__,
            subject=request.subject,
            user_id=current_user.id,
        )
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to validate subject",
            context=create_error_context(
                metadata={"operation": "validate_subject", "subject": request.subject, "error": str(e)}
            ),
        ) from e


@router.get("/patterns", response_model=PatternsResponse)
async def get_patterns(
    current_user: "User" = Depends(require_admin_user),
    subject_manager: NATSSubjectManager = Depends(get_subject_manager_dependency),
) -> PatternsResponse:
    """
    Get all registered subject patterns.

    This endpoint allows administrators to view all available
    subject patterns and their configurations.

    Args:
        current_user: Current authenticated admin user
        subject_manager: Subject manager dependency

    Returns:
        All registered patterns with metadata

    Raises:
        LoggedHTTPException: If pattern retrieval fails

    AI: Admin-only endpoint for pattern introspection.
    AI: Useful for documentation and debugging.
    """
    try:
        # Get all patterns
        patterns = subject_manager.get_all_patterns()

        logger.info("Patterns requested", pattern_count=len(patterns), user_id=current_user.id)

        return PatternsResponse(patterns=patterns, total_count=len(patterns))

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Pattern retrieval errors unpredictable, must create error context
        logger.error("Error retrieving patterns", error=str(e), error_type=type(e).__name__, user_id=current_user.id)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to retrieve patterns",
            context=create_error_context(metadata={"operation": "get_patterns", "error": str(e)}),
        ) from e


@router.post("/patterns", response_model=RegisterPatternResponse)
async def register_pattern(
    request: RegisterPatternRequest,
    current_user: "User" = Depends(require_admin_user),
    subject_manager: NATSSubjectManager = Depends(get_subject_manager_dependency),
) -> RegisterPatternResponse:
    """
    Register a new subject pattern.

    This endpoint allows administrators to dynamically register
    new subject patterns without code changes.

    Args:
        request: Pattern registration request
        current_user: Current authenticated admin user
        subject_manager: Subject manager dependency

    Returns:
        Registration success confirmation

    Raises:
        LoggedHTTPException: If registration fails or pattern is invalid

    AI: Admin-only endpoint for dynamic pattern registration.
    AI: Validates pattern format before registration.
    """
    try:
        # Register the pattern
        subject_manager.register_pattern(
            name=request.name,
            pattern=request.pattern,
            required_params=request.required_params,
            description=request.description,
        )

        logger.info(
            "Pattern registered",
            pattern_name=request.name,
            pattern=request.pattern,
            required_params=request.required_params,
            user_id=current_user.id,
        )

        return RegisterPatternResponse(
            success=True, pattern_name=request.name, message="Pattern registered successfully"
        )

    except (InvalidPatternError, PatternNotFoundError) as e:
        logger.warning(
            "Pattern registration rejected",
            error=str(e),
            pattern_name=request.name,
            pattern=request.pattern,
            user_id=current_user.id,
        )
        raise LoggedHTTPException(
            status_code=400,
            detail=str(e),
            context=create_error_context(
                metadata={
                    "operation": "register_pattern",
                    "pattern_name": request.name,
                    "pattern": request.pattern,
                    "error": str(e),
                }
            ),
        ) from e

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Pattern registration errors unpredictable, must create error context
        logger.error(
            "Error registering pattern",
            error=str(e),
            error_type=type(e).__name__,
            pattern_name=request.name,
            user_id=current_user.id,
        )
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to register pattern",
            context=create_error_context(
                metadata={"operation": "register_pattern", "pattern_name": request.name, "error": str(e)}
            ),
        ) from e
