"""Application shutdown logic.

This module handles graceful shutdown of all services in the MythosMUD server.
"""

from fastapi import FastAPI

from ..container import ApplicationContainer
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

logger = get_logger("server.lifespan.shutdown")


async def _shutdown_mythos_chronicle() -> None:
    """Shutdown and persist mythos chronicle state."""
    logger.info("Freezing mythos chronicle state")
    try:
        chronicle = get_mythos_chronicle()
        frozen_state = chronicle.freeze()
        logger.info(
            "Mythos chronicle state persisted",
            real_timestamp=frozen_state.real_timestamp.isoformat(),
            mythos_timestamp=frozen_state.mythos_timestamp.isoformat(),
        )
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Failed to persist mythos chronicle state during shutdown", error=str(e))


async def _shutdown_nats_handler(app: FastAPI) -> None:
    """Shutdown NATS message handler if present."""
    # Prefer container, fallback to app.state for backward compatibility
    nats_message_handler = None
    if hasattr(app.state, "container") and app.state.container:
        nats_message_handler = app.state.container.nats_message_handler
    elif hasattr(app.state, "nats_message_handler"):
        nats_message_handler = app.state.nats_message_handler

    if not nats_message_handler:
        return

    logger.info("Stopping NATS message handler")
    try:
        await nats_message_handler.stop()
        logger.info("NATS message handler stopped successfully")
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error stopping NATS message handler", error=str(e))


async def _shutdown_connection_manager(app: FastAPI) -> None:
    """Shutdown connection manager if present."""
    # Prefer container, fallback to app.state for backward compatibility
    connection_manager = None
    if hasattr(app.state, "container") and app.state.container:
        connection_manager = app.state.container.connection_manager
    elif hasattr(app.state, "connection_manager"):
        connection_manager = app.state.connection_manager

    if not connection_manager:
        return

    logger.info("Stopping connection manager health checks")
    try:
        connection_manager.stop_health_checks()
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error stopping connection manager health checks", error=str(e))

    logger.info("Cleaning up connection manager tasks")
    try:
        await connection_manager.force_cleanup()
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error during connection manager cleanup", error=str(e))


async def _shutdown_mythos_tick_scheduler(app: FastAPI) -> None:
    """Shutdown mythos tick scheduler if present."""
    # Prefer container, fallback to app.state for backward compatibility
    mythos_tick_scheduler = None
    if hasattr(app.state, "container") and app.state.container:
        mythos_tick_scheduler = app.state.container.mythos_tick_scheduler
    elif hasattr(app.state, "mythos_tick_scheduler"):
        mythos_tick_scheduler = app.state.mythos_tick_scheduler

    if not mythos_tick_scheduler:
        return

    logger.info("Stopping Mythos tick scheduler")
    try:
        await mythos_tick_scheduler.stop()
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error stopping Mythos tick scheduler", error=str(e))


async def _shutdown_task_registry(container: ApplicationContainer) -> None:
    """Shutdown task registry if present."""
    if not container.task_registry:
        return

    logger.info("Executing TaskRegistry graceful shutdown coordination")
    try:
        shutdown_success = await container.task_registry.shutdown_all(timeout=5.0)
        if shutdown_success:
            logger.info("All tasks cancelled gracefully")
        else:
            logger.warning("TaskRegistry shutdown reached timeout - forcing termination of remaining tasks")
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("TaskRegistry shutdown coordination error", error=str(e))


async def _shutdown_event_bus(container: ApplicationContainer) -> None:
    """Shutdown event bus and clean up all service subscriptions."""
    if not container.event_bus:
        return

    logger.info("Shutting down EventBus and cleaning up service subscriptions")
    try:
        # Get subscriber stats before shutdown for logging
        stats = container.event_bus.get_subscriber_stats()
        logger.info(
            "EventBus subscriber stats before shutdown",
            total_subscribers=stats.get("total_subscribers", 0),
            services_tracked=stats.get("services_tracked", 0),
        )

        # Shutdown will automatically clean up all service subscriptions
        await container.event_bus.shutdown()
        logger.info("EventBus shutdown complete")
    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error("Error shutting down EventBus", error=str(e))


async def shutdown_services(app: FastAPI, container: ApplicationContainer) -> None:
    """Handle graceful shutdown of all services."""
    await _shutdown_mythos_chronicle()
    await _shutdown_nats_handler(app)
    await _shutdown_connection_manager(app)
    await _shutdown_mythos_tick_scheduler(app)
    await _shutdown_task_registry(container)
    # Shutdown EventBus before container to ensure service subscriptions are cleaned up
    await _shutdown_event_bus(container)

    logger.info("Shutting down ApplicationContainer")
    await container.shutdown()
    logger.info("ApplicationContainer shutdown complete")
