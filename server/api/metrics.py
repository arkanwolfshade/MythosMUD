"""
Metrics API endpoint for monitoring NATS message delivery.

Provides metrics about message processing, failures, retries,
circuit breaker state, and dead letter queue status.

AI: Metrics are essential for observability and incident response.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from ..auth.users import get_current_user
from ..logging.enhanced_logging_config import get_logger
from ..middleware.metrics_collector import metrics_collector

logger = get_logger(__name__)

router = APIRouter(prefix="/metrics", tags=["metrics"])


def verify_admin_access(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Verify user has admin access to metrics.

    Args:
        current_user: Current authenticated user

    Returns:
        Current user dict if admin

    Raises:
        HTTPException: If user is not admin

    AI: Metrics may contain sensitive operational data - admin only.
    """
    # Check if user is admin
    is_admin = current_user.get("is_admin", False) or current_user.get("is_superuser", False)

    if not is_admin:
        logger.warning("Non-admin user attempted to access metrics", username=current_user.get("username"))
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required for metrics")

    return current_user


@router.get("")  # type: ignore[misc]
async def get_metrics(current_user: dict = Depends(verify_admin_access)) -> dict[str, Any]:
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
        from ..realtime.nats_message_handler import nats_message_handler
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

        logger.info("Metrics retrieved", admin_user=current_user.get("username"))

        assert isinstance(base_metrics, dict)
        return base_metrics

    except Exception as e:
        logger.error("Error retrieving metrics", error=str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics") from e


@router.get("/summary")  # type: ignore[misc]
async def get_metrics_summary(current_user: dict = Depends(verify_admin_access)) -> dict[str, Any]:
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
        from ..realtime.nats_message_handler import nats_message_handler

        if nats_message_handler:
            dlq_count = nats_message_handler.dead_letter_queue.get_statistics().get("total_messages", 0)
            summary["dlq_pending"] = dlq_count
            summary["circuit_state"] = nats_message_handler.circuit_breaker.get_state().value

        assert isinstance(summary, dict)
        return summary

    except Exception as e:
        logger.error("Error retrieving metrics summary", error=str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics") from e


@router.post("/reset")  # type: ignore[misc]
async def reset_metrics(current_user: dict = Depends(verify_admin_access)) -> dict[str, str]:
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

        logger.warning("Metrics reset by admin", admin_user=current_user.get("username"))

        return {"status": "success", "message": "Metrics counters reset"}

    except Exception as e:
        logger.error("Error resetting metrics", error=str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error resetting metrics") from e


@router.get("/dlq")  # type: ignore[misc]
async def get_dlq_messages(limit: int = 100, current_user: dict = Depends(verify_admin_access)) -> dict[str, Any]:
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
        from ..realtime.nats_message_handler import nats_message_handler

        if not nats_message_handler:
            return {"messages": [], "count": 0}

        messages = nats_message_handler.dead_letter_queue.list_messages(limit=limit)
        total_count = nats_message_handler.dead_letter_queue.get_statistics().get("total_messages", 0)

        logger.info(
            "DLQ messages retrieved", count=len(messages), total=total_count, admin_user=current_user.get("username")
        )

        return {"messages": messages, "count": len(messages), "total_in_dlq": total_count}

    except Exception as e:
        logger.error("Error retrieving DLQ messages", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving DLQ messages"
        ) from e


@router.post("/circuit-breaker/reset")  # type: ignore[misc]
async def reset_circuit_breaker(current_user: dict = Depends(verify_admin_access)) -> dict[str, str]:
    """
    Manually reset circuit breaker to CLOSED state.

    Use this to force the circuit closed after manual service recovery.

    Requires admin authentication.

    Returns:
        Confirmation message

    AI: Emergency admin action - use when you know service is healthy.
    """
    try:
        from ..realtime.nats_message_handler import nats_message_handler

        if not nats_message_handler:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available")

        nats_message_handler.circuit_breaker.reset()

        logger.warning("Circuit breaker manually reset", admin_user=current_user.get("username"))

        return {"status": "success", "message": "Circuit breaker reset to CLOSED state"}

    except Exception as e:
        logger.error("Error resetting circuit breaker", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error resetting circuit breaker"
        ) from e


@router.post("/dlq/{filepath:path}/replay")  # type: ignore[misc]
async def replay_dlq_message(filepath: str, current_user: dict = Depends(verify_admin_access)) -> dict[str, Any]:
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
        from ..realtime.nats_message_handler import nats_message_handler

        if not nats_message_handler:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available")

        # Read the DLQ message
        import json

        dlq_path = nats_message_handler.dead_letter_queue.storage_dir / filepath

        if not dlq_path.exists():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"DLQ file not found: {filepath}")

        # Load message data
        with open(dlq_path, encoding="utf-8") as f:
            dlq_entry = json.load(f)

        message_data = dlq_entry.get("message")
        if not message_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid DLQ entry: missing message data"
            )

        # Attempt to replay message
        try:
            await nats_message_handler._process_single_message(message_data)

            # Success! Remove from DLQ
            nats_message_handler.dead_letter_queue.delete_message(str(dlq_path))

            logger.info(
                "DLQ message replayed successfully",
                filepath=filepath,
                message_id=message_data.get("message_id"),
                admin_user=current_user.get("username"),
            )

            return {"status": "success", "message": f"Message replayed and removed from DLQ: {filepath}"}

        except Exception as replay_error:
            logger.error(
                "Failed to replay DLQ message",
                filepath=filepath,
                error=str(replay_error),
                admin_user=current_user.get("username"),
            )

            return {
                "status": "failed",
                "message": f"Replay failed: {str(replay_error)}. Message remains in DLQ.",
                "error": str(replay_error),
            }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error replaying DLQ message", filepath=filepath, error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error replaying DLQ message"
        ) from e


@router.delete("/dlq/{filepath:path}")  # type: ignore[misc]
async def delete_dlq_message(filepath: str, current_user: dict = Depends(verify_admin_access)) -> dict[str, str]:
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
        from ..realtime.nats_message_handler import nats_message_handler

        if not nats_message_handler:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="NATS handler not available")

        dlq_path = nats_message_handler.dead_letter_queue.storage_dir / filepath

        if not dlq_path.exists():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"DLQ file not found: {filepath}")

        nats_message_handler.dead_letter_queue.delete_message(str(dlq_path))

        if True:
            logger.warning("DLQ message deleted by admin", filepath=filepath, admin_user=current_user.get("username"))
            return {"status": "success", "message": f"DLQ message deleted: {filepath}"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete DLQ message"
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error deleting DLQ message", filepath=filepath, error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting DLQ message"
        ) from e
