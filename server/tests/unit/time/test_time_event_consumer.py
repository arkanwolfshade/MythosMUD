"""Unit tests for MythosTimeEventConsumer hour tick handling."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import MythosHourTickEvent
from server.time.time_event_consumer import MythosTimeEventConsumer


@pytest.fixture
def tick_event() -> MythosHourTickEvent:
    mythos_dt = datetime(1930, 1, 1, 12, 0, tzinfo=UTC)
    return MythosHourTickEvent(
        mythos_datetime=mythos_dt,
        month_name="January",
        day_of_month=1,
        day_name="Wednesday",
        day_of_week=2,
        week_of_month=1,
        season="winter",
        daypart="afternoon",
        is_daytime=True,
        is_witching_hour=False,
    )


@pytest.mark.asyncio
async def test_handle_tick_updates_room_and_broadcasts(tick_event: MythosHourTickEvent) -> None:
    event_bus = MagicMock()
    chronicle = MagicMock()
    chronicle.get_current_mythos_datetime.return_value = tick_event.mythos_datetime
    chronicle.format_clock.return_value = "12:00"
    holiday_service = MagicMock()
    holiday_service.refresh_active.return_value = []
    holiday_service.get_upcoming_holidays.return_value = []
    holiday_service.get_active_holiday_names.return_value = []
    holiday_service.get_upcoming_summary.return_value = []
    schedule_service = MagicMock()
    schedule_service.get_active_entries.return_value = []
    room_service = MagicMock()
    npc_lifecycle = MagicMock()
    npc_lifecycle.apply_schedule_state = MagicMock()

    consumer = MythosTimeEventConsumer(
        event_bus=event_bus,
        chronicle=chronicle,
        holiday_service=holiday_service,
        schedule_service=schedule_service,
        room_service=room_service,
        npc_lifecycle_manager=npc_lifecycle,
    )

    with patch(
        "server.time.time_event_consumer.broadcast_game_event",
        new_callable=AsyncMock,
    ) as broadcast:
        await consumer._handle_tick(tick_event)  # pylint: disable=protected-access

    room_service.update_environment_state.assert_called_once()
    npc_lifecycle.apply_schedule_state.assert_called_once()
    broadcast.assert_awaited_once()
    assert broadcast.call_args[0][0] == "mythos_time_update"


def test_describe_state(tick_event: MythosHourTickEvent) -> None:
    event_bus = MagicMock()
    chronicle = MagicMock()
    chronicle.get_current_mythos_datetime.return_value = tick_event.mythos_datetime
    holiday_service = MagicMock()
    holiday_service.get_active_holiday_names.return_value = ["Yule"]
    holiday_service.get_upcoming_summary.return_value = ["Imbolc"]
    schedule_service = MagicMock()

    consumer = MythosTimeEventConsumer(
        event_bus=event_bus,
        chronicle=chronicle,
        holiday_service=holiday_service,
        schedule_service=schedule_service,
        room_service=None,
    )
    state = consumer.describe_state()
    assert "current_mythos_time" in state
    assert state["active_holidays"] == ["Yule"]
