"""
Time bundle: mythos time event consumer.

Depends on Core (event_bus), Game (holiday_service, schedule_service, room_service),
NPC (npc_lifecycle_manager).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

TIME_ATTRS = ("mythos_time_consumer",)


class TimeBundle:  # pylint: disable=too-few-public-methods
    """Mythos time consumer service."""

    mythos_time_consumer: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize Mythos time event consumer."""
        if (
            container.event_bus
            and container.holiday_service
            and container.schedule_service
            and container.room_service
            and container.npc_lifecycle_manager
        ):
            from server.time.time_event_consumer import MythosTimeEventConsumer
            from server.time.time_service import get_mythos_chronicle

            self.mythos_time_consumer = MythosTimeEventConsumer(
                event_bus=container.event_bus,
                chronicle=get_mythos_chronicle(),
                holiday_service=container.holiday_service,
                schedule_service=container.schedule_service,
                room_service=container.room_service,
                npc_lifecycle_manager=container.npc_lifecycle_manager,
            )
            logger.info("Mythos time consumer initialized and subscribed to hour ticks")
        else:
            logger.warning("Mythos time consumer not initialized due to missing dependencies")
