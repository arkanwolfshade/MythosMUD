"""
Metrics API endpoint for monitoring NATS message delivery.

Provides metrics about message processing, failures, retries,
circuit breaker state, and dead letter queue status.

AI: Metrics are essential for observability and incident response.
"""

from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status

from ..auth.users import get_current_user
from ..dependencies import NatsMessageHandlerDep
from ..exceptions import LoggedHTTPException
from ..middleware.metrics_collector import metrics_collector
from ..models.user import User
from ..schemas.metrics import (
    DLQMessagesResponse,
    DLQReplayResponse,
    MetricsResponse,
    MetricsSummaryResponse,
    StatusMessageResponse,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request

logger = get_logger(__name__)

router = APIRouter(prefix="/metrics", tags=["metrics"])


def verify_admin_access(request: Request, current_user: User | None = Depends(get_current_user)) -> User:
    """
    Verify user has admin access to metrics.

    Args:
        request: FastAPI request object for error context
        current_user: Current authenticated user

    Returns:
        Current user if admin

    Raises:
        LoggedHTTPException: If user is not admin or not authenticated

    AI: Metrics may contain sensitive operational data - admin only.
    """
    if not current_user:
        context = create_context_from_request(request)
        context.metadata["operation"] = "verify_admin_access"
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required for metrics", context=context
        )

    # Check if user is admin
    is_admin = current_user.is_admin or current_user.is_superuser

    if not is_admin:
        # Create context before logging to ensure full context in logs
        context = create_context_from_request(request)
        context.user_id = str(current_user.id)
        context.metadata["operation"] = "verify_admin_access"
        context.metadata["username"] = current_user.username
        logger.warning(
            "Non-admin user attempted to access metrics", username=current_user.username, context=context.to_dict()
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required for metrics", context=context
        )

    return current_user


@router.get("", response_model=MetricsResponse)
async def get_metrics(
    request: Request,
    current_user: User = Depends(verify_admin_access),
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> MetricsResponse:
    """
    Get comprehensive system metrics.

    Returns metrics about NATS message delivery, circuit breaker state,
    dead letter queue, and performance statistics.

    Requires admin authentication.

    Returns:
        Dictionary containing all metrics

    AI: For monitoring dashboards and alerting systems.
    """
    try:
        from ..services.nats_service import nats_service

        # Get base metrics from collector
        base_metrics = metrics_collector.get_metrics()

        # Add circuit breaker stats if handler is available
        if nats_message_handler:
            circuit_stats = nats_message_handler.circuit_breaker.get_stats()
            # DeadLetterQueue exposes sync API; call directly
            dlq_stats = nats_message_handler.dead_letter_queue.get_statistics()

            base_metrics["circuit_breaker"].update(circuit_stats)
            base_metrics["dead_letter_queue"] = dlq_stats

        # Add NATS connection state machine stats
        if nats_service:
            base_metrics["nats_connection"] = nats_service.get_connection_stats()
            # Add subscription metrics
            base_metrics["nats_subscriptions"] = {
                "active_subscriptions": nats_service.get_active_subscriptions(),
                "subscription_count": len(nats_service.get_active_subscriptions()),
                "last_cleanup_time": getattr(nats_service, "_last_cleanup_time", None),
                "subscription_count_total": getattr(nats_service, "_subscription_count", 0),
                "unsubscription_count_total": getattr(nats_service, "_unsubscription_count", 0),
            }

        logger.info("Metrics retrieved", admin_user=current_user.username)

        if not isinstance(base_metrics, dict):
            raise TypeError("base_metrics must be a dict")
        return MetricsResponse(metrics=base_metrics)

    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "get_metrics"
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics", context=context
        ) from e


@router.get("/summary", response_model=MetricsSummaryResponse)
async def get_metrics_summary(
    request: Request,
    _current_user: User = Depends(verify_admin_access),  # pylint: disable=unused-argument  # Required by Depends for auth
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> MetricsSummaryResponse:
    """
    Get concise metrics summary.

    Returns high-level health indicators without detailed breakdowns.
    Faster than full metrics endpoint.

    Requires admin authentication.

    Returns:
        Dictionary with summary metrics

    AI: For quick health checks and status dashboards.
    """
    try:
        summary = metrics_collector.get_summary()

        # Add DLQ count

        dlq_pending = None
        circuit_state = None
        if nats_message_handler:
            dlq_pending = nats_message_handler.dead_letter_queue.get_statistics().get("total_messages", 0)
            circuit_state = nats_message_handler.circuit_breaker.get_state().value

        if not isinstance(summary, dict):
            raise TypeError("summary must be a dict")
        return MetricsSummaryResponse(summary=summary, dlq_pending=dlq_pending, circuit_state=circuit_state)

    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(_current_user.id) if _current_user else None
        context.metadata["operation"] = "get_metrics_summary"
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics", context=context
        ) from e


@router.post("/reset", response_model=StatusMessageResponse)
async def reset_metrics(request: Request, current_user: User = Depends(verify_admin_access)) -> StatusMessageResponse:
    """
    Reset metrics counters.

    Clears all metrics counters. Use after maintenance or deployment.

    Requires admin authentication.

    Returns:
        Confirmation message

    AI: Use sparingly - metrics history is valuable.
    """
    try:
        metrics_collector.reset_metrics()

        logger.warning("Metrics reset by admin", admin_user=current_user.username)

        return StatusMessageResponse(status="success", message="Metrics counters reset")

    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "reset_metrics"
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error resetting metrics", context=context
        ) from e


@router.get("/dlq", response_model=DLQMessagesResponse)
async def get_dlq_messages(
    request: Request,
    limit: int = 100,
    current_user: User = Depends(verify_admin_access),
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> DLQMessagesResponse:
    """
    Get messages from dead letter queue.

    Returns failed messages for manual inspection and potential replay.

    Args:
        limit: Maximum number of messages to return

    Requires admin authentication.

    Returns:
        Dictionary with DLQ messages and statistics

    AI: For incident investigation and manual message replay.
    """
    try:
        if not nats_message_handler:
            return DLQMessagesResponse(messages=[], count=0, total_in_dlq=0)

        messages = nats_message_handler.dead_letter_queue.list_messages(limit=limit)
        total_count = nats_message_handler.dead_letter_queue.get_statistics().get("total_messages", 0)

        logger.info("DLQ messages retrieved", count=len(messages), total=total_count, admin_user=current_user.username)

        return DLQMessagesResponse(messages=messages, count=len(messages), total_in_dlq=total_count)

    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "get_dlq_messages"
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving DLQ messages", context=context
        ) from e


@router.post("/circuit-breaker/reset", response_model=StatusMessageResponse)
async def reset_circuit_breaker(
    request: Request,
    current_user: User = Depends(verify_admin_access),
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> StatusMessageResponse:
    """
    Manually reset circuit breaker to CLOSED state.

    Use this to force the circuit closed after manual service recovery.

    Requires admin authentication.

    Returns:
        Confirmation message

    AI: Emergency admin action - use when you know service is healthy.
    """
    try:
        if not nats_message_handler:
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "reset_circuit_breaker"
            raise LoggedHTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available", context=context
            )

        nats_message_handler.circuit_breaker.reset()

        logger.warning("Circuit breaker manually reset", admin_user=current_user.username)

        return StatusMessageResponse(status="success", message="Circuit breaker reset to CLOSED state")

    except HTTPException:
        # Re-raise HTTPExceptions (like 503 SERVICE_UNAVAILABLE) without wrapping
        raise
    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "reset_circuit_breaker"
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error resetting circuit breaker", context=context
        ) from e


async def _load_dlq_message(dlq_path: Path) -> dict[str, Any]:
    """
    Load and validate DLQ message data from file (async version using aiofiles).

    Args:
        dlq_path: Path to the DLQ file

    Returns:
        Message data dictionary

    Raises:
        HTTPException: If file not found or data is invalid
    """
    import json

    import aiofiles

    if not dlq_path.exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"DLQ file not found: {dlq_path}")

    async with aiofiles.open(dlq_path, encoding="utf-8") as f:
        content = await f.read()
        dlq_entry = json.loads(content)

    # DeadLetterQueue stores entries via DeadLetterMessage.to_dict(),
    # where the original message is under the "data" key (not "message").
    # Support legacy shape that may have used "message".
    message_data = dlq_entry.get("data") or dlq_entry.get("message")
    if not isinstance(message_data, dict):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid DLQ entry: missing or malformed message data",
        )

    return message_data


async def _replay_message_safely(
    nats_message_handler: Any, message_data: dict[str, Any], dlq_path: Path, filepath: str, current_user: User
) -> DLQReplayResponse:
    """
    Attempt to replay a DLQ message and handle errors safely.

    Args:
        nats_message_handler: NATS message handler instance
        message_data: Message data to replay
        dlq_path: Path to DLQ file
        filepath: Original filepath for logging
        current_user: Current admin user

    Returns:
        Success response dict

    Raises:
        Exception: If replay fails (logged but not exposed to user)
    """
    await nats_message_handler._process_single_message(message_data)  # pylint: disable=protected-access  # Reason: Internal method access required for DLQ replay functionality

    # Success! Remove from DLQ
    nats_message_handler.dead_letter_queue.delete_message(str(dlq_path))

    logger.info(
        "DLQ message replayed successfully",
        filepath=filepath,
        message_id=message_data.get("message_id"),
        admin_user=current_user.username,
    )

    return DLQReplayResponse(
        status="success", message=f"Message replayed and removed from DLQ: {filepath}", filepath=filepath
    )


def _handle_replay_error(replay_error: Exception, filepath: str, current_user: User) -> DLQReplayResponse:
    """
    Handle replay errors and return safe error response.

    Args:
        replay_error: The exception that occurred during replay
        filepath: Path to the DLQ file
        current_user: Current admin user

    Returns:
        Error response dict
    """
    logger.error(
        "Failed to replay DLQ message - details logged",
        filepath=filepath,
        error=str(replay_error),
        admin_user=current_user.username,
    )

    # Human reader: sanitize error message to prevent stack trace exposure.
    # AI reader: never expose stack traces in API responses, only in logs.
    # Human reader: CodeQL requires no exception information exposure to external users.
    # AI reader: return generic error message to prevent information leakage.
    return DLQReplayResponse(status="failed", message="Replay failed. Message remains in DLQ.", filepath=filepath)


def _get_nats_handler(nats_message_handler: Any | None) -> Any:
    """Get NATS message handler, raising exception if not available.

    Args:
        nats_message_handler: The NATS message handler from dependency injection

    Returns:
        NATSMessageHandler: The NATS message handler instance

    Raises:
        HTTPException: If handler is not available
    """
    if not nats_message_handler:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available")
    return nats_message_handler


@router.post("/dlq/{filepath:path}/replay", response_model=DLQReplayResponse)
async def replay_dlq_message(
    filepath: str,
    request: Request,
    current_user: User = Depends(verify_admin_access),
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> DLQReplayResponse:
    """
    Replay a message from the Dead Letter Queue.

    Attempts to reprocess a failed message. If successful, removes it from DLQ.

    Args:
        filepath: Path to the DLQ file (relative to DLQ storage)

    Requires admin authentication.

    Returns:
        Confirmation message with replay status

    AI: For manual incident recovery - use after fixing underlying issue.
    """
    try:
        nats_message_handler = _get_nats_handler(nats_message_handler)
        dlq_path = nats_message_handler.dead_letter_queue.storage_dir / filepath
        message_data = await _load_dlq_message(dlq_path)

        # Attempt to replay message
        try:
            return await _replay_message_safely(nats_message_handler, message_data, dlq_path, filepath, current_user)
        except (ValueError, RuntimeError, OSError, AttributeError) as replay_error:
            # Catch specific exceptions that can occur during message replay
            return _handle_replay_error(replay_error, filepath, current_user)
        except Exception as replay_error:  # pylint: disable=broad-except  # Reason: Message replay errors unpredictable, must catch all exceptions to handle various failure modes during message processing
            # (network errors, processing errors, etc.) and we want to handle all of them
            # the same way (log and return generic error to user)
            return _handle_replay_error(replay_error, filepath, current_user)

    except HTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "replay_dlq_message"
        context.metadata["filepath"] = filepath
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error replaying DLQ message", context=context
        ) from e


@router.delete("/dlq/{filepath:path}", response_model=StatusMessageResponse)
async def delete_dlq_message(
    filepath: str,
    request: Request,
    current_user: User = Depends(verify_admin_access),
    nats_message_handler: Any = NatsMessageHandlerDep,
) -> StatusMessageResponse:
    """
    Delete a message from the Dead Letter Queue without replaying.

    Use this to discard a message that is not worth replaying.

    Args:
        filepath: Path to the DLQ file (relative to DLQ storage)

    Requires admin authentication.

    Returns:
        Confirmation message

    AI: For discarding permanently failed or invalid messages.
    """
    try:
        if not nats_message_handler:
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "delete_dlq_message"
            raise LoggedHTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available", context=context
            )

        dlq_path = nats_message_handler.dead_letter_queue.storage_dir / filepath

        if not dlq_path.exists():
            context = create_context_from_request(request)
            context.user_id = str(current_user.id) if current_user else None
            context.metadata["operation"] = "delete_dlq_message"
            context.metadata["filepath"] = filepath
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"DLQ file not found: {filepath}", context=context
            )

        nats_message_handler.dead_letter_queue.delete_message(str(dlq_path))
        logger.warning("DLQ message deleted by admin", filepath=filepath, admin_user=current_user.username)
        return StatusMessageResponse(status="success", message=f"DLQ message deleted: {filepath}")

    except LoggedHTTPException:
        raise
    except Exception as e:
        context = create_context_from_request(request)
        context.user_id = str(current_user.id) if current_user else None
        context.metadata["operation"] = "delete_dlq_message"
        context.metadata["filepath"] = filepath
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting DLQ message", context=context
        ) from e
