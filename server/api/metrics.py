"""
Metrics API endpoint for monitoring NATS message delivery.

Provides metrics about message processing, failures, retries,
circuit breaker state, and dead letter queue status.

AI: Metrics are essential for observability and incident response.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from ..auth.users import get_current_user
from ..logging_config import get_logger
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


@router.get("")
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

        # Get base metrics from collector
        base_metrics = metrics_collector.get_metrics()

        # Add circuit breaker stats if handler is available
        if nats_message_handler:
            circuit_stats = nats_message_handler.circuit_breaker.get_stats()
            dlq_stats = await nats_message_handler.dead_letter_queue.get_statistics()

            base_metrics["circuit_breaker"].update(circuit_stats)
            base_metrics["dead_letter_queue"] = dlq_stats

        logger.info("Metrics retrieved", admin_user=current_user.get("username"))

        return base_metrics

    except Exception as e:
        logger.error("Error retrieving metrics", error=str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics") from e


@router.get("/summary")
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
            dlq_count = await nats_message_handler.dead_letter_queue.get_pending_count()
            summary["dlq_pending"] = dlq_count
            summary["circuit_state"] = nats_message_handler.circuit_breaker.get_state().value

        return summary

    except Exception as e:
        logger.error("Error retrieving metrics summary", error=str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving metrics") from e


@router.post("/reset")
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


@router.get("/dlq")
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

        messages = await nats_message_handler.dead_letter_queue.get_messages(limit=limit)
        total_count = await nats_message_handler.dead_letter_queue.get_pending_count()

        logger.info(
            "DLQ messages retrieved", count=len(messages), total=total_count, admin_user=current_user.get("username")
        )

        return {"messages": messages, "count": len(messages), "total_in_dlq": total_count}

    except Exception as e:
        logger.error("Error retrieving DLQ messages", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving DLQ messages"
        ) from e


@router.post("/circuit-breaker/reset")
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
