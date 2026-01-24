"""Time event consumer for processing game time events.

This module provides the TimeEventConsumer class for consuming and processing
MythosHourTickEvent events from the event bus.
"""

# pylint: disable=too-few-public-methods,too-many-arguments,too-many-positional-arguments  # Reason: Event consumer class with focused responsibility, minimal public interface, and complex event processing logic

from __future__ import annotations

from collections.abc import Sequence
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from server.events.event_bus import EventBus
from server.events.event_types import MythosHourTickEvent
from server.exceptions import DatabaseError
from server.realtime.connection_manager_api import broadcast_game_event
from server.services.holiday_service import HolidayService
from server.services.schedule_service import ScheduleService
from server.structured_logging.enhanced_logging_config import get_logger
from server.time.time_service import ChronicleLike

if TYPE_CHECKING:
    from server.game.room_service import RoomService
    from server.npc.lifecycle_manager import NPCLifecycleManager

logger = get_logger(__name__)


class MythosTimeEventConsumer:  # pylint: disable=too-few-public-methods  # Reason: Event consumer class with focused responsibility, minimal public interface
    """Bridges hour tick events into downstream systems such as NPC schedules and room lighting."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event consumer initialization requires many service dependencies
        self,
        *,
        event_bus: EventBus,
        chronicle: ChronicleLike,
        holiday_service: HolidayService,
        schedule_service: ScheduleService,
        room_service: RoomService | None,
        npc_lifecycle_manager: NPCLifecycleManager | None = None,
    ) -> None:
        self._event_bus = event_bus
        self._chronicle = chronicle
        self._holiday_service = holiday_service
        self._schedule_service = schedule_service
        self._room_service = room_service
        self._npc_lifecycle_manager = npc_lifecycle_manager

        self._event_bus.subscribe(MythosHourTickEvent, self._handle_tick)
        logger.info("Mythos time event consumer subscribed to hour ticks")

    async def _handle_tick(self, event: MythosHourTickEvent) -> None:
        """Dispatch hour tick events to each dependent subsystem."""

        mythos_dt = event.mythos_datetime
        active_holidays = self._holiday_service.refresh_active(mythos_dt)
        active_schedules = self._schedule_service.get_active_entries(
            mythos_dt=event.mythos_datetime, day_name=event.day_name
        )

        if self._room_service:
            holiday_names = [holiday.name for holiday in active_holidays]
            try:
                self._room_service.update_environment_state(
                    daypart=event.daypart,
                    is_daytime=event.is_daytime,
                    active_holidays=holiday_names,
                )
            except (ValueError, TypeError, AttributeError, RuntimeError) as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to update room environment state", error=str(exc))

        if self._npc_lifecycle_manager and hasattr(self._npc_lifecycle_manager, "apply_schedule_state"):
            try:
                self._npc_lifecycle_manager.apply_schedule_state(active_schedules)
            except (ValueError, TypeError, AttributeError, RuntimeError) as exc:  # pragma: no cover - defensive logging
                logger.error("Failed to apply NPC schedule state", error=str(exc))

        logger.debug(
            "Processed Mythos hour tick",
            mythos_time=event.mythos_datetime.isoformat(),
            daypart=event.daypart,
            active_holiday_count=len(active_holidays),
            active_schedule_count=len(active_schedules),
        )

        payload = self._build_broadcast_payload(event, active_holidays, active_schedules)
        try:
            await broadcast_game_event("mythos_time_update", payload)
        except (
            RuntimeError,
            AttributeError,
            DatabaseError,
            ConnectionError,
            TimeoutError,
        ) as exc:  # pragma: no cover - defensive logging
            logger.error("Failed to broadcast Mythos time update", error=str(exc))

    def describe_state(self) -> dict[str, Any]:
        """Helper for admin diagnostics."""

        return {
            "current_mythos_time": self._chronicle.get_current_mythos_datetime().isoformat(),
            "active_holidays": self._holiday_service.get_active_holiday_names(),
            "upcoming_holidays": self._holiday_service.get_upcoming_summary(),
        }

    def _build_broadcast_payload(
        self,
        event: MythosHourTickEvent,
        active_holidays: Sequence[Any],
        active_schedules: Sequence[Any],
    ) -> dict[str, Any]:
        """Create the SSE payload consumed by the client HUD."""

        holiday_payload = [
            {
                "id": getattr(entry, "id", ""),
                "name": getattr(entry, "name", ""),
                "tradition": getattr(entry, "tradition", ""),
                "season": getattr(entry, "season", ""),
                "duration_hours": getattr(entry, "duration_hours", 24),
                "bonus_tags": list(getattr(entry, "bonus_tags", []) or []),
                "notes": getattr(entry, "notes", None),
            }
            for entry in active_holidays
        ]

        schedule_payload = [
            {
                "id": getattr(schedule, "id", ""),
                "name": getattr(schedule, "name", ""),
                "category": getattr(schedule, "category", ""),
                "start_hour": getattr(schedule, "start_hour", 0),
                "end_hour": getattr(schedule, "end_hour", 0),
                "days": list(getattr(schedule, "days", []) or []),
                "applies_to": list(getattr(schedule, "applies_to", []) or []),
                "effects": list(getattr(schedule, "effects", []) or []),
                "notes": getattr(schedule, "notes", None),
            }
            for schedule in active_schedules
        ]

        chronicle = self._chronicle
        mythos_clock = chronicle.format_clock(event.mythos_datetime)

        payload = {
            "mythos_datetime": event.mythos_datetime.isoformat(),
            "mythos_clock": mythos_clock,
            "month_name": event.month_name,
            "day_of_month": event.day_of_month,
            "day_name": event.day_name,
            "week_of_month": event.week_of_month,
            "season": event.season,
            "daypart": event.daypart,
            "is_daytime": event.is_daytime,
            "is_witching_hour": event.is_witching_hour,
            "server_timestamp": datetime.now(UTC).isoformat(),
            "active_holidays": holiday_payload,
            "upcoming_holidays": [
                {
                    "id": getattr(entry, "id", ""),
                    "name": getattr(entry, "name", ""),
                    "tradition": getattr(entry, "tradition", ""),
                    "season": getattr(entry, "season", ""),
                    "duration_hours": getattr(entry, "duration_hours", 24),
                    "bonus_tags": list(getattr(entry, "bonus_tags", []) or []),
                    "notes": getattr(entry, "notes", None),
                }
                for entry in self._holiday_service.get_upcoming_holidays()
            ],
            "active_schedules": schedule_payload,
        }

        return payload
