"""Tick scheduler for managing game tick events.

This module provides the MythosTickScheduler class for scheduling and
executing game tick events at regular intervals.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Tick scheduler requires many state tracking and configuration attributes

from __future__ import annotations

import asyncio
from collections.abc import Callable, Sequence
from datetime import UTC, datetime, timedelta
from typing import Any

from anyio import Lock, sleep

from server.app.task_registry import TaskRegistry
from server.events.event_bus import EventBus
from server.events.event_types import MythosHourTickEvent
from server.structured_logging.enhanced_logging_config import get_logger

from .time_service import MythosChronicle

HolidayResolver = Callable[[datetime], Sequence[str]]


class MythosTickScheduler:  # pylint: disable=too-many-instance-attributes  # Reason: Tick scheduler requires many state tracking and configuration attributes
    """
    Periodic dispatcher that emits Mythos hour ticks based on the accelerated chronicle.

    The scheduler leverages the TaskRegistry so it can be cleanly cancelled during shutdowns and
    publishes structured events through the EventBus for downstream systems.
    """

    MIN_SLEEP_SECONDS = 1.0
    MAX_SLEEP_SECONDS = 60.0

    def __init__(
        self,
        *,
        chronicle: MythosChronicle,
        event_bus: EventBus,
        task_registry: TaskRegistry,
        holiday_resolver: HolidayResolver | None = None,
    ) -> None:
        self._chronicle = chronicle
        self._event_bus = event_bus
        self._task_registry = task_registry
        self._holiday_resolver = holiday_resolver or (lambda _dt: ())
        self._logger = get_logger(__name__)

        self._task: asyncio.Task[Any] | None = None
        self._running = False
        self._last_emitted_hour: datetime | None = None
        self._lock = Lock()

    async def start(self) -> None:
        """Register the scheduler loop with the task registry."""

        async with self._lock:
            if self._running:
                return
            self._running = True
            self._task = self._task_registry.register_task(
                self._run(),
                "lifecycle/mythos_tick_scheduler",
                "lifecycle",
            )
            self._logger.info("Mythos tick scheduler started")

    async def stop(self) -> None:
        """Cancel the scheduler loop and wait for the task to exit."""

        async with self._lock:
            self._running = False
            if self._task is not None:
                await self._task_registry.cancel_task(self._task)
                self._task = None
            self._logger.info("Mythos tick scheduler stopped")

    async def _run(self) -> None:
        """Background coroutine that emits ticks and waits for the next hour boundary."""

        try:
            while self._running:
                await self._emit_pending_ticks()
                await self._sleep_until_next_hour()
        except asyncio.CancelledError:
            self._logger.debug("Mythos tick scheduler cancelled")
        except Exception as exc:  # noqa: B904  # pragma: no cover - defensive logging  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Scheduler errors unpredictable, must log but continue
            self._logger.error("Mythos tick scheduler failed", error=str(exc), exc_info=True)

    async def _emit_pending_ticks(self) -> None:
        """Emit one or more hour tick events if we've crossed boundaries."""

        current_hour = self._truncate_to_hour(self._chronicle.get_current_mythos_datetime())
        if self._last_emitted_hour is None:
            self._last_emitted_hour = current_hour - timedelta(hours=1)

        while self._last_emitted_hour < current_hour:
            next_hour = self._last_emitted_hour + timedelta(hours=1)
            self._publish_tick(next_hour)
            self._last_emitted_hour = next_hour

    async def _sleep_until_next_hour(self) -> None:
        """Sleep until the next Mythos hour boundary, respecting compression ratio."""

        if self._last_emitted_hour is None:
            await sleep(self.MIN_SLEEP_SECONDS)
            return

        target_hour = self._last_emitted_hour + timedelta(hours=1)
        target_real = self._chronicle.to_real_datetime(target_hour)
        now_real = datetime.now(UTC)
        sleep_seconds = (target_real - now_real).total_seconds()

        if sleep_seconds < self.MIN_SLEEP_SECONDS:
            sleep_seconds = self.MIN_SLEEP_SECONDS
        elif sleep_seconds > self.MAX_SLEEP_SECONDS:
            sleep_seconds = self.MAX_SLEEP_SECONDS

        await sleep(sleep_seconds)

    def _publish_tick(self, mythos_hour: datetime) -> None:
        """Publish the hourly tick event to the EventBus."""

        components = self._chronicle.get_calendar_components(mythos_hour)
        holidays = list(self._holiday_resolver(mythos_hour))
        event = MythosHourTickEvent(
            mythos_datetime=components.mythos_datetime,
            month_name=components.month_name,
            day_of_month=components.day_of_month,
            week_of_month=components.week_of_month,
            day_of_week=components.day_of_week,
            day_name=components.day_name,
            season=components.season,
            is_daytime=components.is_daytime,
            is_witching_hour=components.is_witching_hour,
            daypart=components.daypart,
            active_holidays=holidays,
        )
        self._event_bus.publish(event)
        self._logger.debug(
            "Published Mythos hour tick",
            mythos_hour=event.mythos_datetime.isoformat(),
            daypart=event.daypart,
            holidays=len(event.active_holidays),
        )

    @staticmethod
    def _truncate_to_hour(candidate: datetime) -> datetime:
        """Return the same datetime truncated down to the closest hour."""

        return candidate.replace(minute=0, second=0, microsecond=0, tzinfo=UTC)
