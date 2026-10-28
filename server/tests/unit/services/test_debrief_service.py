"""Unit tests for the debrief service: recap, optional therapy, and clearing DEBRIEF_PENDING (#872, ADR-028)."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from datetime import UTC, datetime
from types import SimpleNamespace
from typing import cast

import pytest

from server.models.lucidity import LucidityActionCode
from server.models.player import Player
from server.services import debrief_service as service
from server.services.active_lucidity_service import LucidityActionOnCooldownError
from server.services.lucidity_service import LucidityService


@dataclass
class Rig:
    pending: bool = True
    adjustments: list[SimpleNamespace] = field(default_factory=lambda: cast(list[SimpleNamespace], []))
    query_fails: bool = False
    commit_fails: bool = False
    therapy_error: Exception | None = None
    commits: int = 0
    rollbacks: int = 0
    cleared: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
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

    async def commit(self) -> None:
        if self._rig.commit_fails:
            raise RuntimeError("commit failed")
        self._rig.commits += 1

    async def rollback(self) -> None:
        self._rig.rollbacks += 1


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    rig = Rig()

    async def fake_sessions() -> AsyncIterator[FakeSession]:
        yield FakeSession(rig)

    class FakeLucidityService:
        def __init__(self, session: FakeSession) -> None:
            _ = session

        async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> object | None:
            _ = player_id, action_code
            return object() if rig.pending else None

        async def clear_cooldown(self, player_id: uuid.UUID, action_code: str) -> int:
            rig.cleared.append((player_id, action_code))
            return 1

    class FakeActiveLucidityService:
        def __init__(self, session: FakeSession, *, catatonia_observer: object | None = None) -> None:
            _ = session, catatonia_observer

        async def perform_recovery_action(
            self, player_id: uuid.UUID | str, *, action_code: str, location_id: str | None = None
        ) -> SimpleNamespace:
            if rig.therapy_error is not None:
                raise rig.therapy_error
            rig.therapy_calls.append((uuid.UUID(str(player_id)), action_code, location_id))
            return SimpleNamespace(delta=5, new_lcd=55)

    monkeypatch.setattr(service, "get_async_session", fake_sessions)
    monkeypatch.setattr(service, "LucidityService", FakeLucidityService)
    monkeypatch.setattr(service, "ActiveLucidityService", FakeActiveLucidityService)
    return rig


def _player() -> Player:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = "ward_room"
    return player


def _adjustment(reason: str, delta: int) -> SimpleNamespace:
    return SimpleNamespace(reason_code=reason, delta=delta)


@pytest.mark.asyncio
async def test_no_pending_debrief_is_reported_and_nothing_changes(rig: Rig) -> None:
    rig.pending = False

    outcome = await service.perform_debrief(_player())

    assert outcome.completed is False
    assert "No debrief session is available" in outcome.message
    assert rig.cleared == []
    assert rig.commits == 0


@pytest.mark.asyncio
async def test_a_pending_debrief_recaps_concludes_and_clears_the_flag(rig: Rig) -> None:
    player = _player()
    rig.adjustments = [_adjustment("combat_stress", -10)]

    outcome = await service.perform_debrief(player)

    assert outcome.completed is True
    assert "Combat Stress" in outcome.message  # the recap query is awaited, not a coroutine left unread
    assert "-10 LCD" in outcome.message
    assert "debrief session concludes" in outcome.message
    assert rig.cleared == [(uuid.UUID(str(player.player_id)), LucidityActionCode.DEBRIEF_PENDING)]
    assert rig.commits == 1
    assert rig.therapy_calls == []


@pytest.mark.asyncio
async def test_a_recap_with_no_records_falls_back_to_the_staff_note(rig: Rig) -> None:
    assert rig.adjustments == []
    outcome = await service.perform_debrief(_player())

    assert "records are incomplete" in outcome.message


@pytest.mark.asyncio
async def test_a_failing_recap_query_falls_back_to_the_general_overview(rig: Rig) -> None:
    rig.query_fails = True

    outcome = await service.perform_debrief(_player())

    assert outcome.completed is True
    assert "lucidity crisis" in outcome.message


@pytest.mark.asyncio
async def test_therapy_runs_only_when_requested_and_reports_the_result(rig: Rig) -> None:
    player = _player()

    outcome = await service.perform_debrief(player, wants_therapy=True)

    assert rig.therapy_calls == [(uuid.UUID(str(player.player_id)), "therapy", "ward_room")]
    assert "immediate therapy" in outcome.message
    assert "+5" in outcome.message
    assert "55/100" in outcome.message


@pytest.mark.asyncio
async def test_therapy_on_cooldown_is_explained_and_the_debrief_still_completes(rig: Rig) -> None:
    rig.therapy_error = LucidityActionOnCooldownError("cooldown")

    outcome = await service.perform_debrief(_player(), wants_therapy=True)

    assert outcome.completed is True
    assert "Therapy is currently unavailable" in outcome.message


@pytest.mark.asyncio
async def test_a_therapy_failure_does_not_fail_the_debrief(rig: Rig) -> None:
    rig.therapy_error = RuntimeError("boom")

    outcome = await service.perform_debrief(_player(), wants_therapy=True)

    assert outcome.completed is True
    assert "could not be initiated" in outcome.message


@pytest.mark.asyncio
async def test_a_failure_while_completing_rolls_back_and_reports_complications(rig: Rig) -> None:
    rig.commit_fails = True

    outcome = await service.perform_debrief(_player())

    assert outcome.completed is False
    assert "complications" in outcome.message
    assert rig.rollbacks == 1


@pytest.mark.asyncio
async def test_marking_a_debrief_pending_sets_a_long_lived_flag() -> None:
    """The flag waits for Dr. Morgan: set for about a year, on the DEBRIEF_PENDING action code."""
    set_calls: list[tuple[uuid.UUID, str, object]] = []

    class RecordingLucidityService:
        async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: object) -> object:
            set_calls.append((player_id, action_code, expires_at))
            return object()

    player_id = uuid.uuid4()
    await service.mark_debrief_pending(cast(LucidityService, cast(object, RecordingLucidityService())), player_id)

    [(marked, code, expires_at)] = set_calls
    assert (marked, code) == (player_id, LucidityActionCode.DEBRIEF_PENDING)
    assert isinstance(expires_at, datetime)
    days_left = (expires_at - datetime.now(UTC).replace(tzinfo=None)).days
    assert service.DEBRIEF_PENDING_DAYS - 1 <= days_left <= service.DEBRIEF_PENDING_DAYS
