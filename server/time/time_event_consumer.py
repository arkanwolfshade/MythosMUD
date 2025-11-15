from __future__ import annotations

from server.events.event_bus import EventBus
from server.events.event_types import MythosHourTickEvent
from server.logging.enhanced_logging_config import get_logger
from server.services.holiday_service import HolidayService
from server.services.schedule_service import ScheduleService
from server.time.time_service import ChronicleLike

logger = get_logger(__name__)


class MythosTimeEventConsumer:
    """Bridges hour tick events into downstream systems such as NPC schedules and room lighting."""

    def __init__(
        self,
        *,
        event_bus: EventBus,
        chronicle: ChronicleLike,
        holiday_service: HolidayService,
        schedule_service: ScheduleService,
        room_service,
        npc_lifecycle_manager=None,
    ) -> None:
        self._event_bus = event_bus
        self._chronicle = chronicle
        self._holiday_service = holiday_service
        self._schedule_service = schedule_service
        self._room_service = room_service
        self._npc_lifecycle_manager = npc_lifecycle_manager

        self._event_bus.subscribe(MythosHourTickEvent, self._handle_tick)
        logger.info("Mythos time event consumer subscribed to hour ticks")

    def _handle_tick(self, event: MythosHourTickEvent) -> None:
        """Dispatch hour tick events to each dependent subsystem."""

        mythos_dt = event.mythos_datetime
        active_holidays = self._holiday_service.refresh_active(mythos_dt)
        active_schedules = self._schedule_service.get_active_entries(mythos_dt=event.mythos_datetime, day_name=event.day_name)

        if self._room_service:
            holiday_names = [holiday.name for holiday in active_holidays]
            try:
                self._room_service.update_environment_state(
                    daypart=event.daypart,
                    is_daytime=event.is_daytime,
                    active_holidays=holiday_names,
                )
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to update room environment state", error=str(exc))

        if self._npc_lifecycle_manager and hasattr(self._npc_lifecycle_manager, "apply_schedule_state"):
            try:
                self._npc_lifecycle_manager.apply_schedule_state(active_schedules)
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to apply NPC schedule state", error=str(exc))

        logger.debug(
            "Processed Mythos hour tick",
            mythos_time=event.mythos_datetime.isoformat(),
            daypart=event.daypart,
            active_holiday_count=len(active_holidays),
            active_schedule_count=len(active_schedules),
        )

    def describe_state(self) -> dict:
        """Helper for admin diagnostics."""

        return {
            "current_mythos_time": self._chronicle.get_current_mythos_datetime().isoformat(),
            "active_holidays": self._holiday_service.get_active_holiday_names(),
            "upcoming_holidays": self._holiday_service.get_upcoming_summary(),
        }
