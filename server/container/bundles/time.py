"""
Time bundle: the Temporal bounded context (docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md) --
holiday_service, schedule_service, mythos_tick_scheduler, and the mythos time event consumer.

Depends on Core (async_persistence, event_bus, task_registry, config), Game (room_service),
NPC (npc_lifecycle_manager). holiday_service/schedule_service/mythos_tick_scheduler moved here
from GameBundle in #635 -- they were constructed there but documented as Temporal-context
services, splitting the context across two bundles.
"""

# pyright: reportImportCycles=false
# Reason: container/main.py imports this module (function-scoped) to construct TimeBundle;
# this file only imports ApplicationContainer under TYPE_CHECKING for parameter annotations.
# Same precedent as server/models/player.py and server/services/combat_service.py.

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import get_calendar_paths_for_environment, normalize_environment

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

TIME_ATTRS = ("holiday_service", "schedule_service", "mythos_tick_scheduler", "mythos_time_consumer")


class TimeBundle:  # pylint: disable=too-few-public-methods
    """Temporal context: holiday/schedule services, tick scheduler, mythos time consumer."""

    holiday_service: Any = None
    schedule_service: Any = None
    mythos_tick_scheduler: Any = None
    mythos_time_consumer: Any = None

    def _resolve_hourly_holidays(self, mythos_dt: datetime) -> list[str]:
        """Resolve active holiday names for tick scheduler; return empty list on error or no service."""
        if not self.holiday_service:
            return []
        try:
            active = self.holiday_service.refresh_active(mythos_dt)
            return [entry.name for entry in active]
        except (ValueError, TypeError, AttributeError, RuntimeError) as exc:
            logger.warning("Failed to resolve holiday window for tick scheduler", error=str(exc))
            return []

    def _init_temporal_services(self, container: ApplicationContainer) -> None:
        """Construct holiday_service, schedule_service, and mythos_tick_scheduler.

        Unconditional, matching GameBundle's prior behavior exactly: these only need
        async_persistence/event_bus/task_registry (all Core), not room_service/
        npc_lifecycle_manager (only the consumer below needs those).
        """
        normalized_environment = normalize_environment(container.config.logging.environment)
        async_persistence = container.async_persistence
        from server.services.holiday_service import HolidayService
        from server.services.schedule_service import ScheduleService
        from server.time.time_service import get_mythos_chronicle

        holidays_path, schedules_dir = get_calendar_paths_for_environment(normalized_environment)
        self.holiday_service = HolidayService(
            chronicle=get_mythos_chronicle(),
            data_path=holidays_path,
            environment=normalized_environment,
            async_persistence=async_persistence,
        )
        self.schedule_service = ScheduleService(
            schedule_dir=schedules_dir,
            environment=normalized_environment,
            async_persistence=async_persistence,
        )
        logger.info(
            "Temporal schedule and holiday services initialized",
            holiday_count=len(self.holiday_service.collection.holidays),
            schedule_entries=self.schedule_service.entry_count if self.schedule_service else 0,
        )
        from server.time.tick_scheduler import MythosTickScheduler

        self.mythos_tick_scheduler = MythosTickScheduler(
            chronicle=get_mythos_chronicle(),
            event_bus=container.event_bus,
            task_registry=container.task_registry,
            holiday_resolver=self._resolve_hourly_holidays,
        )
        logger.info("Mythos tick scheduler prepared")

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize the Temporal context: holiday/schedule/tick-scheduler, then the consumer."""
        self._init_temporal_services(container)

        if (
            container.event_bus
            and self.holiday_service
            and self.schedule_service
            and container.room_service
            and container.npc_lifecycle_manager
        ):
            from server.time.time_event_consumer import MythosTimeEventConsumer
            from server.time.time_service import get_mythos_chronicle

            self.mythos_time_consumer = MythosTimeEventConsumer(
                event_bus=container.event_bus,
                chronicle=get_mythos_chronicle(),
                holiday_service=self.holiday_service,
                schedule_service=self.schedule_service,
                room_service=container.room_service,
                npc_lifecycle_manager=container.npc_lifecycle_manager,
            )
            logger.info("Mythos time consumer initialized and subscribed to hour ticks")
        else:
            logger.warning("Mythos time consumer not initialized due to missing dependencies")
