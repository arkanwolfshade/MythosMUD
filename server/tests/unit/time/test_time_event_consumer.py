from __future__ import annotations

from datetime import UTC, datetime
from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import MythosHourTickEvent
from server.schemas.calendar import HolidayCollection, HolidayEntry, ScheduleCollection, ScheduleEntry
from server.services.holiday_service import HolidayService
from server.services.schedule_service import ScheduleService
from server.time.time_event_consumer import MythosTimeEventConsumer


class DummyChronicle:
    def __init__(self, dt: datetime) -> None:
        self._dt = dt

    def get_current_mythos_datetime(self) -> datetime:
        return self._dt

    def get_calendar_components(self, mythos_dt: datetime | None = None):
        return SimpleNamespace(daypart="day")

    def format_clock(self, mythos_dt: datetime | None = None) -> str:
        target = mythos_dt or self._dt
        return target.strftime("%H:%M Mythos")


class DummyRoomService:
    def __init__(self) -> None:
        self.environment_state: dict[str, Any] = {}

    def update_environment_state(self, **kwargs) -> None:
        self.environment_state = kwargs


class DummyNPCManager:
    def __init__(self) -> None:
        self.active_schedule_ids: list[str] = []

    def apply_schedule_state(self, schedules) -> None:
        self.active_schedule_ids = [entry.id for entry in schedules]


def _holiday_collection() -> HolidayCollection:
    return HolidayCollection(
        holidays=[
            HolidayEntry(
                id="witching_observance",
                name="Witching Observance",
                tradition="mythos",
                month=1,
                day=1,
                duration_hours=24,
                season="winter",
                bonus_tags=["mystic"],
            )
        ]
    )


def _schedule_collection() -> ScheduleCollection:
    return ScheduleCollection(
        schedules=[
            ScheduleEntry(
                id="night_watch_patrol",
                name="Night Watch Patrol",
                category="npc",
                start_hour=23,
                end_hour=24,
                days=["Primus", "Secundus"],
                applies_to=["watch_guard"],
                effects=["patrol"],
            )
        ]
    )


@pytest.mark.asyncio
async def test_time_event_consumer_updates_room_and_npc_state() -> None:
    event_bus = EventBus()
    chronicle = DummyChronicle(datetime(1930, 1, 1, 23, tzinfo=UTC))
    holiday_service = HolidayService(chronicle=chronicle, collection=_holiday_collection(), data_path="unused")
    # ScheduleService now loads from database - mock the database loading
    schedule_collection = _schedule_collection()
    mock_persistence = AsyncMock()

    # Mock the async load to return our test schedules
    async def mock_async_load(result_container):
        result_container["entries"] = schedule_collection.schedules
        result_container["error"] = None

    with patch.object(ScheduleService, "_async_load_from_database", side_effect=mock_async_load):
        schedule_service = ScheduleService(schedule_dir="unused", async_persistence=mock_persistence)
    room_service = DummyRoomService()
    npc_manager = DummyNPCManager()

    consumer = MythosTimeEventConsumer(
        event_bus=event_bus,
        chronicle=chronicle,
        holiday_service=holiday_service,
        schedule_service=schedule_service,
        room_service=room_service,
        npc_lifecycle_manager=npc_manager,
    )

    event = MythosHourTickEvent(
        mythos_datetime=datetime(1930, 1, 1, 23, tzinfo=UTC),
        month_name="January",
        day_of_month=1,
        week_of_month=1,
        day_of_week=0,
        day_name="Primus",
        season="winter",
        is_daytime=False,
        is_witching_hour=True,
        daypart="witching",
        active_holidays=[],
    )

    with patch(
        "server.time.time_event_consumer.broadcast_game_event", new=AsyncMock()
    ) as mock_broadcast:  # Prevent network usage
        await consumer._handle_tick(event)  # Direct invocation for unit test

    assert room_service.environment_state["daypart"] == "witching"
    assert npc_manager.active_schedule_ids == ["night_watch_patrol"]
    mock_broadcast.assert_awaited_once()
    assert mock_broadcast.await_args is not None
    payload = mock_broadcast.await_args.args[1]
    assert payload["daypart"] == "witching"
    assert payload["active_holidays"][0]["name"] == "Witching Observance"
