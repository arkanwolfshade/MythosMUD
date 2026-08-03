"""Unit tests for MythosTickScheduler."""

from __future__ import annotations

import asyncio
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.time.tick_scheduler import MythosTickScheduler


@pytest.fixture
def mock_chronicle() -> MagicMock:
    chronicle = MagicMock()
    chronicle.get_current_mythos_datetime.return_value = datetime(1930, 1, 1, 12, 30, tzinfo=UTC)
    chronicle.to_real_datetime.side_effect = lambda dt: dt
    components = MagicMock()
    components.mythos_datetime = datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    components.month_name = "January"
    components.day_of_month = 1
    components.week_of_month = 1
    components.day_of_week = 3
    components.day_name = "Wednesday"
    components.season = "winter"
    components.is_daytime = True
    components.is_witching_hour = False
    components.daypart = "afternoon"
    chronicle.get_calendar_components.return_value = components
    return chronicle


@pytest.fixture
def mock_event_bus() -> MagicMock:
    return MagicMock()


@pytest.fixture
def mock_task_registry() -> MagicMock:
    registry = MagicMock()

    def _register(coro: object, *_args: object, **_kwargs: object) -> MagicMock:
        # Tests do not run the scheduler loop; close the coro so GC stays quiet.
        if asyncio.iscoroutine(coro):
            coro.close()
        return MagicMock()

    registry.register_task.side_effect = _register
    registry.cancel_task = AsyncMock()
    return registry


@pytest.fixture
def scheduler(
    mock_chronicle: MagicMock, mock_event_bus: MagicMock, mock_task_registry: MagicMock
) -> MythosTickScheduler:
    return MythosTickScheduler(
        chronicle=mock_chronicle,
        event_bus=mock_event_bus,
        task_registry=mock_task_registry,
    )


def test_truncate_to_hour() -> None:
    candidate = datetime(1930, 6, 15, 14, 45, 30, tzinfo=UTC)
    result = MythosTickScheduler._truncate_to_hour(candidate)
    assert result == datetime(1930, 6, 15, 14, 0, 0, tzinfo=UTC)


@pytest.mark.asyncio
async def test_start_registers_task(scheduler: MythosTickScheduler, mock_task_registry: MagicMock) -> None:
    await scheduler.start()
    mock_task_registry.register_task.assert_called_once()
    assert scheduler._running is True


@pytest.mark.asyncio
async def test_start_idempotent(scheduler: MythosTickScheduler, mock_task_registry: MagicMock) -> None:
    await scheduler.start()
    await scheduler.start()
    mock_task_registry.register_task.assert_called_once()


@pytest.mark.asyncio
async def test_stop_cancels_task(scheduler: MythosTickScheduler, mock_task_registry: MagicMock) -> None:
    await scheduler.start()
    await scheduler.stop()
    mock_task_registry.cancel_task.assert_awaited_once()
    assert scheduler._running is False
    assert scheduler._task is None


@pytest.mark.asyncio
async def test_emit_pending_ticks_publishes_hours(
    scheduler: MythosTickScheduler, mock_chronicle: MagicMock, mock_event_bus: MagicMock
) -> None:
    mock_chronicle.get_current_mythos_datetime.return_value = datetime(1930, 1, 1, 14, 0, tzinfo=UTC)
    scheduler._last_emitted_hour = datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    await scheduler._emit_pending_ticks()
    assert mock_event_bus.publish.call_count == 2


@pytest.mark.asyncio
async def test_emit_pending_ticks_initializes_last_hour(
    scheduler: MythosTickScheduler, mock_event_bus: MagicMock, mock_chronicle: MagicMock
) -> None:
    await scheduler._emit_pending_ticks()
    assert scheduler._last_emitted_hour == datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_sleep_until_next_hour_no_last_emitted(scheduler: MythosTickScheduler) -> None:
    with patch("server.time.tick_scheduler.sleep", new_callable=AsyncMock) as mock_sleep:
        await scheduler._sleep_until_next_hour()
        mock_sleep.assert_awaited_once_with(MythosTickScheduler.MIN_SLEEP_SECONDS)


@pytest.mark.asyncio
async def test_sleep_until_next_hour_clamps_min(scheduler: MythosTickScheduler, mock_chronicle: MagicMock) -> None:
    scheduler._last_emitted_hour = datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    mock_chronicle.to_real_datetime.side_effect = lambda _dt: datetime.now(UTC) - timedelta(seconds=5)
    with patch("server.time.tick_scheduler.sleep", new_callable=AsyncMock) as mock_sleep:
        await scheduler._sleep_until_next_hour()
        mock_sleep.assert_awaited_once_with(MythosTickScheduler.MIN_SLEEP_SECONDS)


@pytest.mark.asyncio
async def test_sleep_until_next_hour_clamps_max(scheduler: MythosTickScheduler, mock_chronicle: MagicMock) -> None:
    scheduler._last_emitted_hour = datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    mock_chronicle.to_real_datetime.side_effect = lambda _dt: datetime.now(UTC) + timedelta(hours=2)
    with patch("server.time.tick_scheduler.sleep", new_callable=AsyncMock) as mock_sleep:
        await scheduler._sleep_until_next_hour()
        mock_sleep.assert_awaited_once_with(MythosTickScheduler.MAX_SLEEP_SECONDS)


def test_publish_tick_with_holidays(
    scheduler: MythosTickScheduler, mock_event_bus: MagicMock, mock_chronicle: MagicMock
) -> None:
    mythos_hour = datetime(1930, 1, 1, 13, 0, tzinfo=UTC)
    scheduler._holiday_resolver = lambda _dt: ("Yuletide",)
    scheduler._publish_tick(mythos_hour)
    mock_event_bus.publish.assert_called_once()
    mock_chronicle.get_calendar_components.assert_called_once_with(mythos_hour)
