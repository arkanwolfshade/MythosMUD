"""Unit tests for the timed /ground channel (#713)."""

import asyncio
import uuid
from unittest.mock import patch

import pytest

from server.commands.ground_channel import (
    FinishOutcome,
    cancel_ground_channel,
    is_player_grounding,
    start_ground_channel,
)
from server.tests.unit.commands.ground_commands_test_support import FakeConnectionManager, RescueEventRecorder


class _FinishSpy:
    """`finish` stand-in: counts calls and returns a fixed outcome, optionally after a gate opens."""

    def __init__(self, outcome: FinishOutcome = "done", gate: asyncio.Event | None = None) -> None:
        self.outcome: FinishOutcome = outcome
        self.gate: asyncio.Event | None = gate
        self.calls: int = 0

    async def __call__(self) -> FinishOutcome:
        self.calls += 1
        if self.gate is not None:
            _ = await self.gate.wait()
        return self.outcome


@pytest.fixture(name="events")
def events_fixture() -> RescueEventRecorder:
    return RescueEventRecorder()


async def _start(
    manager: FakeConnectionManager,
    events: RescueEventRecorder,
    rescuer_id: uuid.UUID,
    target_id: uuid.UUID,
    finish: _FinishSpy | None = None,
    eta: float = 5.0,
) -> str | None:
    with patch("server.commands.ground_channel.ground_channel_seconds", return_value=eta):
        return await start_ground_channel(
            manager,
            rescuer_id=rescuer_id,
            target_id=target_id,
            rescuer_name="Armitage",
            target_name="Wilmarth",
            finish=finish or _FinishSpy(),
            notify=events,
        )


def _channel_task(manager: FakeConnectionManager, target_id: uuid.UUID) -> asyncio.Task[None]:
    task = manager.grounding_channels[target_id].task
    assert task is not None
    return task


@pytest.mark.asyncio
async def test_start_registers_channel_and_notifies_both_with_eta(events: RescueEventRecorder) -> None:
    manager, rescuer, target = FakeConnectionManager(), uuid.uuid4(), uuid.uuid4()

    assert await _start(manager, events, rescuer, target) is None

    assert is_player_grounding(rescuer, manager) and is_player_grounding(target, manager)
    assert [(e.player_id, e.status, e.role) for e in events.sent] == [
        (target, "channeling", "target"),
        (rescuer, "channeling", "rescuer"),
    ]
    assert all(e.eta_seconds == 5.0 for e in events.sent)
    await cancel_ground_channel(rescuer, manager)


@pytest.mark.asyncio
@pytest.mark.parametrize("interrupter", ["rescuer", "target"])
async def test_cancel_from_either_side_interrupts_both_and_clears_registry(
    events: RescueEventRecorder, interrupter: str
) -> None:
    manager, rescuer, target = FakeConnectionManager(), uuid.uuid4(), uuid.uuid4()
    finish = _FinishSpy()
    assert await _start(manager, events, rescuer, target, finish=finish) is None
    events.sent.clear()

    await cancel_ground_channel(rescuer if interrupter == "rescuer" else target, manager)

    assert [(e.player_id, e.status, e.role) for e in events.sent] == [
        (target, "interrupted", "target"),
        (rescuer, "interrupted", "rescuer"),
    ]
    assert manager.grounding_channels == {} and manager.grounding_by_rescuer == {}
    assert not is_player_grounding(rescuer, manager)
    assert finish.calls == 0


@pytest.mark.asyncio
async def test_completion_runs_finish_and_clears_registry(events: RescueEventRecorder) -> None:
    manager, rescuer, target = FakeConnectionManager(), uuid.uuid4(), uuid.uuid4()
    finish = _FinishSpy()
    assert await _start(manager, events, rescuer, target, finish=finish, eta=0.01) is None

    await _channel_task(manager, target)

    assert finish.calls == 1
    assert [e.status for e in events.sent] == ["channeling", "channeling"]  # finish owns the terminal events
    assert manager.grounding_channels == {} and manager.grounding_by_rescuer == {}


@pytest.mark.asyncio
async def test_finish_interrupted_outcome_notifies_both(events: RescueEventRecorder) -> None:
    manager, rescuer, target = FakeConnectionManager(), uuid.uuid4(), uuid.uuid4()
    assert await _start(manager, events, rescuer, target, finish=_FinishSpy("interrupted"), eta=0.01) is None

    await _channel_task(manager, target)

    assert [e.status for e in events.sent][-2:] == ["interrupted", "interrupted"]


@pytest.mark.asyncio
async def test_cancel_is_ignored_once_committing(events: RescueEventRecorder) -> None:
    manager, rescuer, target = FakeConnectionManager(), uuid.uuid4(), uuid.uuid4()
    gate = asyncio.Event()
    finish = _FinishSpy(gate=gate)
    assert await _start(manager, events, rescuer, target, finish=finish, eta=0.01) is None
    task = _channel_task(manager, target)
    await asyncio.sleep(0.05)  # sleep elapsed; finish is now waiting on the DB stand-in
    events.sent.clear()

    await cancel_ground_channel(rescuer, manager)

    assert events.sent == []
    assert not task.cancelled() and is_player_grounding(rescuer, manager)
    gate.set()
    await task


@pytest.mark.asyncio
async def test_second_rescuer_for_same_target_is_rejected(events: RescueEventRecorder) -> None:
    manager, target = FakeConnectionManager(), uuid.uuid4()
    first, second = uuid.uuid4(), uuid.uuid4()
    assert await _start(manager, events, first, target) is None

    assert await _start(manager, events, second, target) == "Wilmarth is already being grounded."

    await cancel_ground_channel(first, manager)


@pytest.mark.asyncio
async def test_rescuer_cannot_channel_two_rituals(events: RescueEventRecorder) -> None:
    manager, rescuer = FakeConnectionManager(), uuid.uuid4()
    assert await _start(manager, events, rescuer, uuid.uuid4()) is None

    assert await _start(manager, events, rescuer, uuid.uuid4()) == "You are already channeling a grounding ritual."

    await cancel_ground_channel(rescuer, manager)


@pytest.mark.asyncio
async def test_resting_rescuer_cannot_start(events: RescueEventRecorder) -> None:
    manager, rescuer = FakeConnectionManager(), uuid.uuid4()
    manager.resting_players[rescuer] = object()

    assert (
        await _start(manager, events, rescuer, uuid.uuid4()) == "You cannot channel a grounding ritual while resting."
    )
    assert manager.grounding_channels == {}
    assert events.sent == []


@pytest.mark.asyncio
async def test_manager_without_registries_is_a_noop(events: RescueEventRecorder) -> None:
    bare = object()
    player = uuid.uuid4()

    assert not is_player_grounding(player, bare)
    await cancel_ground_channel(player, bare)  # must not raise
    with patch("server.commands.ground_channel.ground_channel_seconds", return_value=1.0):
        message = await start_ground_channel(
            bare,
            rescuer_id=player,
            target_id=uuid.uuid4(),
            rescuer_name="Armitage",
            target_name="Wilmarth",
            finish=_FinishSpy(),
            notify=events,
        )
    assert message == "The ritual cannot be anchored right now."
