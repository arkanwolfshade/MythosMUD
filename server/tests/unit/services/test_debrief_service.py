"""Unit tests for the debrief service: recap, optional therapy, and clearing DEBRIEF_PENDING (#872, ADR-028)."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from types import SimpleNamespace
from typing import cast

import pytest

from server.models.lucidity import LucidityActionCode
from server.models.player import Player
from server.services import debrief_service as service
from server.services.active_lucidity_service import LucidityActionOnCooldownError
from server.tests.fixtures.shared.player_registry import LucidityHarness, aggregate, lucidity_registry, raw_row

PID = uuid.uuid4()


@dataclass
class Rig:
    """The recap session (faked) and the registry holding DEBRIEF_PENDING (real; built by ``debrief``)."""

    pending: bool = True
    adjustments: list[SimpleNamespace] = field(default_factory=lambda: cast(list[SimpleNamespace], []))
    query_fails: bool = False
    commit_fails: bool = False
    therapy_error: Exception | None = None
    rollbacks: int = 0
    harness: LucidityHarness | None = None
    therapy_calls: list[tuple[uuid.UUID, str, str | None]] = field(
        default_factory=lambda: cast(list[tuple[uuid.UUID, str, str | None]], [])
    )


class FakeSession:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def execute(self, statement: object) -> SimpleNamespace:
        _ = statement
        if self._rig.query_fails:
            raise RuntimeError("query failed")
        return SimpleNamespace(scalars=lambda: SimpleNamespace(all=lambda: self._rig.adjustments))

    async def rollback(self) -> None:
        self._rig.rollbacks += 1


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    rig = Rig()

    async def fake_sessions() -> AsyncIterator[FakeSession]:
        yield FakeSession(rig)

    class FakeActiveLucidityService:
        def __init__(self, registry: object, *, catatonia_observer: object | None = None) -> None:
            _ = registry, catatonia_observer

        async def perform_recovery_action(
            self, player_id: uuid.UUID | str, *, action_code: str, location_id: str | None = None
        ) -> SimpleNamespace:
            if rig.therapy_error is not None:
                raise rig.therapy_error
            rig.therapy_calls.append((uuid.UUID(str(player_id)), action_code, location_id))
            return SimpleNamespace(delta=5, new_lcd=55)

    monkeypatch.setattr(service, "get_async_session", fake_sessions)
    monkeypatch.setattr(service, "ActiveLucidityService", FakeActiveLucidityService)
    return rig


def _player() -> Player:
    player = Player(player_id=str(PID), name="Tester")
    player.current_room_id = "ward_room"
    return player


async def debrief(rig: Rig, *, wants_therapy: bool = False) -> service.DebriefOutcome:
    """Debrief the player, with DEBRIEF_PENDING set (or not, per the rig) in a fresh registry."""
    flag: dict[str, datetime] | None = (
        {LucidityActionCode.DEBRIEF_PENDING: datetime.now(UTC) + timedelta(days=30)} if rig.pending else None
    )
    rig.harness = lucidity_registry({PID: None}, cooldowns=flag)
    rig.harness.db.fail_commits = 1 if rig.commit_fails else 0
    return await service.perform_debrief(_player(), rig.harness.registry, wants_therapy=wants_therapy)


def _pending(rig: Rig) -> bool:
    assert rig.harness is not None
    return rig.harness.cooldowns(PID).expires_at(LucidityActionCode.DEBRIEF_PENDING) is not None


def _commits(rig: Rig) -> int:
    assert rig.harness is not None
    return rig.harness.db.commits


def _adjustment(reason: str, delta: int) -> SimpleNamespace:
    return SimpleNamespace(reason_code=reason, delta=delta)


@pytest.mark.asyncio
async def test_no_pending_debrief_is_reported_and_nothing_changes(rig: Rig) -> None:
    rig.pending = False

    outcome = await debrief(rig)

    assert outcome.completed is False
    assert "No debrief session is available" in outcome.message
    assert _commits(rig) == 0


@pytest.mark.asyncio
async def test_a_pending_debrief_recaps_concludes_and_clears_the_flag(rig: Rig) -> None:
    rig.adjustments = [_adjustment("combat_stress", -10)]

    outcome = await debrief(rig)

    assert outcome.completed is True
    assert "Combat Stress" in outcome.message  # the recap query is awaited, not a coroutine left unread
    assert "-10 LCD" in outcome.message
    assert "debrief session concludes" in outcome.message
    assert not _pending(rig)
    assert _commits(rig) == 1  # the flag is a sync cooldown: cleared and committed in one unit
    assert rig.therapy_calls == []


@pytest.mark.asyncio
async def test_a_recap_with_no_records_falls_back_to_the_staff_note(rig: Rig) -> None:
    assert rig.adjustments == []
    outcome = await debrief(rig)

    assert "records are incomplete" in outcome.message


@pytest.mark.asyncio
async def test_a_failing_recap_query_falls_back_to_the_general_overview(rig: Rig) -> None:
    rig.query_fails = True

    outcome = await debrief(rig)

    assert outcome.completed is True
    assert "lucidity crisis" in outcome.message


@pytest.mark.asyncio
async def test_therapy_runs_only_when_requested_and_reports_the_result(rig: Rig) -> None:
    outcome = await debrief(rig, wants_therapy=True)

    assert rig.therapy_calls == [(PID, "therapy", "ward_room")]
    assert "immediate therapy" in outcome.message
    assert "+5" in outcome.message
    assert "55/100" in outcome.message


@pytest.mark.asyncio
async def test_therapy_on_cooldown_is_explained_and_the_debrief_still_completes(rig: Rig) -> None:
    rig.therapy_error = LucidityActionOnCooldownError("cooldown")

    outcome = await debrief(rig, wants_therapy=True)

    assert outcome.completed is True
    assert "Therapy is currently unavailable" in outcome.message


@pytest.mark.asyncio
async def test_a_therapy_failure_does_not_fail_the_debrief(rig: Rig) -> None:
    rig.therapy_error = RuntimeError("boom")

    outcome = await debrief(rig, wants_therapy=True)

    assert outcome.completed is True
    assert "could not be initiated" in outcome.message


@pytest.mark.asyncio
async def test_a_failure_while_completing_rolls_back_and_reports_complications(rig: Rig) -> None:
    rig.commit_fails = True

    outcome = await debrief(rig)

    assert outcome.completed is False
    assert "complications" in outcome.message
    assert rig.rollbacks == 1
    assert _pending(rig)  # the failed unit rolled the clear back, so the player can try again


def test_marking_a_debrief_pending_sets_a_long_lived_flag() -> None:
    """The flag waits for Dr. Morgan: set for about a year, on the DEBRIEF_PENDING action code."""
    player = aggregate(raw_row(PID))

    service.mark_debrief_pending(player)

    expires_at = player.cooldowns.expires_at(LucidityActionCode.DEBRIEF_PENDING)
    assert expires_at is not None
    assert player.cooldowns.sync_required  # the flag commits with the caller's unit
    days_left = (expires_at - datetime.now(UTC)).days
    assert service.DEBRIEF_PENDING_DAYS - 1 <= days_left <= service.DEBRIEF_PENDING_DAYS
