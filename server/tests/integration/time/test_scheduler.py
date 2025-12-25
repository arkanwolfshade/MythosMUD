from __future__ import annotations

import asyncio
from datetime import UTC, datetime
from pathlib import Path

import pytest

from server.app.task_registry import TaskRegistry
from server.config.models import TimeConfig
from server.events.event_bus import EventBus
from server.events.event_types import MythosHourTickEvent
from server.time.tick_scheduler import MythosTickScheduler
from server.time.time_service import MythosChronicle

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
async def test_scheduler_emits_hourly_events(tmp_path: Path) -> None:
    config = TimeConfig(
        compression_ratio=3600.0,  # 1 real second ≈ 1 Mythos hour for fast tests
        real_epoch_utc=datetime(2025, 1, 1, 0, 0, tzinfo=UTC),
        mythos_epoch=datetime(1930, 1, 1, 0, 0, tzinfo=UTC),
        state_file=str(tmp_path / "scheduler_state.json"),
    )
    chronicle = MythosChronicle(config=config, state_path=Path(config.state_file))
    event_bus = EventBus()
    task_registry = TaskRegistry()
    scheduler = MythosTickScheduler(chronicle=chronicle, event_bus=event_bus, task_registry=task_registry)

    received: list[MythosHourTickEvent] = []

    def _handler(event: MythosHourTickEvent) -> None:
        received.append(event)

    event_bus.subscribe(MythosHourTickEvent, _handler)

    await scheduler.start()

    try:
        event = await _wait_for_event(received)
        assert isinstance(event, MythosHourTickEvent)
        assert event.mythos_datetime.minute == 0
        assert event.event_type == "MythosHourTickEvent"
        assert event.daypart in {"day", "night", "dawn", "dusk", "witching"}
        assert event.season in {"winter", "spring", "summer", "autumn"}
        assert event.active_holidays == []
    finally:
        await scheduler.stop()
        await task_registry.shutdown_all()


async def _wait_for_event(events: list[MythosHourTickEvent]) -> MythosHourTickEvent:
    for _ in range(40):
        if events:
            return events[0]
        await asyncio.sleep(0.1)
    raise AssertionError("Timed out waiting for mythos hour tick event")
