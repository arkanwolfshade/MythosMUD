"""Unit tests for ActiveLucidityService on a real player registry: encounters and timed recovery (ADR-029 step 5b-ii).

An encounter counts the meeting and takes the loss in one unit; a recovery checks its cooldown, applies the gain and
starts the cooldown in one unit. Both commit synchronously (exposure and cooldowns are sync parts).
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, patch

import pytest

from server.game.player_registry import Exposure, LucidityData
from server.services.active_lucidity_service import (
    ActiveLucidityService,
    LucidityActionOnCooldownError,
    UnknownEncounterCategoryError,
    UnknownLucidityActionError,
)
from server.services.lucidity_helpers import PlayerGoneError
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PID = uuid.uuid4()
NOW = datetime(2026, 10, 5, 12, 0, tzinfo=UTC)


@pytest.fixture(autouse=True)
def _quiet_sends() -> Iterator[None]:
    """The client sends a lucidity change makes (not under test here)."""
    with (
        patch("server.services.lucidity_service.send_lucidity_change_event", new=AsyncMock()),
        patch("server.services.lucidity_trigger_handlers.send_catatonia_event", new=AsyncMock()),
        patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()),
    ):
        yield


def _harness(
    lcd: int = 50, *, cooldowns: dict[str, datetime] | None = None, exposures: dict[str, Exposure] | None = None
) -> LucidityHarness:
    return lucidity_registry({PID: LucidityData(lcd, "uneasy")}, cooldowns=cooldowns, exposures=exposures)


def _service(harness: LucidityHarness) -> ActiveLucidityService:
    return ActiveLucidityService(harness.registry, now_provider=lambda: NOW)


async def _ledger(harness: LucidityHarness) -> list[tuple[object, object, object]]:
    _ = await harness.flush()
    return [(row["delta"], row["reason_code"], row["location_id"]) for row in harness.ledger()]


# ---- encounters ----


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("category", "seen_before", "delta"),
    [
        ("disturbing", 0, -6),  # first sight
        ("disturbing", 1, -2),  # a repeat
        ("disturbing", 5, -1),  # acclimated (6th): half of -2
        ("horrific", 0, -12),
        ("horrific", 5, -2),  # half of -5, truncated
        ("cosmic", 0, -20),
    ],
)
async def test_an_encounter_costs_by_category_and_how_often_the_archetype_was_met(
    category: str, seen_before: int, delta: int
) -> None:
    exposures = {"ghoul": Exposure(seen_before, NOW)} if seen_before else None
    harness = _harness(exposures=exposures)

    result = await _service(harness).apply_encounter_lucidity_loss(PID, "ghoul", category=category.upper())

    assert result.delta == delta and result.new_lcd == 50 + delta
    assert harness.encounters(PID, "ghoul") == seen_before + 1


@pytest.mark.asyncio
async def test_an_encounter_commits_its_count_and_logs_the_loss_with_its_metadata() -> None:
    harness = _harness()

    _ = await _service(harness).apply_encounter_lucidity_loss(
        str(PID), "ghoul", category="disturbing", location_id="room-1"
    )

    assert harness.db.commits == 1  # exposure is sync: the unit committed, lucidity and its ledger row with it
    assert [(row["delta"], row["reason_code"]) for row in harness.ledger()] == [(-6, "encounter_disturbing")]


@pytest.mark.asyncio
async def test_an_unknown_category_changes_nothing() -> None:
    harness = _harness()

    with pytest.raises(UnknownEncounterCategoryError):
        _ = await _service(harness).apply_encounter_lucidity_loss(PID, "ghoul", category="unknown")

    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_an_invalid_player_id_is_refused() -> None:
    with pytest.raises(ValueError, match="Invalid player_id format"):
        _ = await _service(_harness()).apply_encounter_lucidity_loss("not-a-uuid", "ghoul", category="disturbing")


@pytest.mark.asyncio
async def test_an_encounter_for_an_unknown_player_is_gone() -> None:
    with pytest.raises(PlayerGoneError):
        _ = await _service(_harness()).apply_encounter_lucidity_loss(uuid.uuid4(), "ghoul", category="disturbing")


# ---- recovery ----


@pytest.mark.asyncio
async def test_a_timed_recovery_applies_the_gain_and_starts_the_cooldown_in_one_commit() -> None:
    """The caller's key names the audit reason code and the cooldown."""
    harness = _harness()

    result = await _service(harness).apply_timed_recovery(
        PID, cooldown_key="folk_tonic", lcd_delta=3, cooldown=timedelta(minutes=30), location_id="room-1"
    )

    assert (result.delta, result.new_lcd) == (3, 53)
    assert harness.cooldowns(PID).expires_at("folk_tonic") == NOW + timedelta(minutes=30)
    assert harness.db.commits == 1
    assert await _ledger(harness) == [(3, "recovery_folk_tonic", "room-1")]


@pytest.mark.asyncio
async def test_a_timed_recovery_during_its_cooldown_changes_nothing() -> None:
    harness = _harness(cooldowns={"folk_tonic": NOW + timedelta(minutes=5)})

    with pytest.raises(LucidityActionOnCooldownError):
        _ = await _service(harness).apply_timed_recovery(
            PID, cooldown_key="folk_tonic", lcd_delta=3, cooldown=timedelta(minutes=30)
        )

    assert harness.lucidity(PID).lcd == 50
    assert harness.cooldowns(PID).expires_at("folk_tonic") == NOW + timedelta(minutes=5)
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_an_expired_cooldown_allows_the_recovery() -> None:
    harness = _harness(cooldowns={"pray": NOW - timedelta(seconds=1)})

    result = await _service(harness).perform_recovery_action(PID, action_code="pray")

    assert result.delta == 8


@pytest.mark.asyncio
@pytest.mark.parametrize(("action", "delta"), [("pray", 8), ("meditate", 6), ("group_solace", 4), ("therapy", 15)])
async def test_each_recovery_action_uses_its_profile(action: str, delta: int) -> None:
    harness = _harness(lcd=10)

    result = await _service(harness).perform_recovery_action(str(PID), action_code=action.upper())

    assert result.delta == delta
    assert harness.cooldowns(PID).expires_at(action) is not None


@pytest.mark.asyncio
async def test_an_unknown_recovery_action_is_refused() -> None:
    """#870: folk tonic became a consumable item, so the action profile is gone."""
    harness = _harness()

    with pytest.raises(UnknownLucidityActionError):
        _ = await _service(harness).perform_recovery_action(PID, action_code="folk_tonic")


@pytest.mark.asyncio
async def test_get_action_cooldown_reads_the_registry_and_lowercases_the_code() -> None:
    harness = _harness(cooldowns={"pray": NOW})
    service = _service(harness)

    assert await service.get_action_cooldown(str(PID), "PRAY") == NOW
    assert await service.get_action_cooldown(PID, "meditate") is None
    assert await service.get_action_cooldown(uuid.uuid4(), "pray") is None  # no such player
    with pytest.raises(ValueError, match="Invalid player_id format"):
        _ = await service.get_action_cooldown("not-a-uuid", "pray")
