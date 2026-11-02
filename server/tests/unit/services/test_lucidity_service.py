"""Unit tests for LucidityService on a real player registry (ADR-029 step 5b-i)."""

from __future__ import annotations

import json
import uuid
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast
from unittest.mock import patch

import pytest

from server.constants.lucidity import STARTING_LCD
from server.game.player_registry import LucidityData
from server.services.lucidity_event_dispatcher import LucidityChangeEventExtras
from server.services.lucidity_helpers import LIABILITY_CATALOG, PlayerGoneError, decode_liabilities, encode_liabilities
from server.services.lucidity_service import LucidityService, max_lcd_from_stats
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PID = uuid.uuid4()
T0 = datetime(2026, 10, 30, 12, 0, tzinfo=UTC)


class _Send:
    """Stands in for one of the client event senders: records the keyword arguments of every call."""

    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    async def __call__(self, *args: object, **kwargs: object) -> None:
        _ = args
        self.calls.append(kwargs)


class _Observer:
    """A catatonia observer (CatatoniaObserverProtocol) that records what it was told."""

    def __init__(self) -> None:
        self.entered: list[uuid.UUID] = []
        self.cleared: list[uuid.UUID] = []

    def on_catatonia_entered(self, *, player_id: uuid.UUID, entered_at: datetime, current_lcd: int) -> None:
        _ = entered_at, current_lcd
        self.entered.append(player_id)

    def on_catatonia_cleared(self, *, player_id: uuid.UUID, resolved_at: datetime) -> None:
        _ = resolved_at
        self.cleared.append(player_id)

    def on_sanitarium_failover(self, *, player_id: uuid.UUID, current_lcd: int) -> None:
        _ = player_id, current_lcd

    def should_trigger_sanitarium_failover(self, player_id: uuid.UUID | str) -> bool:
        _ = player_id
        return False


@dataclass
class _Sends:
    change: _Send
    catatonia: _Send
    rescue: _Send


@pytest.fixture(autouse=True)
def sends() -> Iterator[_Sends]:
    """Every client send the service and its trigger handlers make, captured."""
    captured = _Sends(_Send(), _Send(), _Send())
    with (
        patch("server.services.lucidity_service.send_lucidity_change_event", new=captured.change),
        patch("server.services.lucidity_trigger_handlers.send_catatonia_event", new=captured.catatonia),
        patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=captured.rescue),
    ):
        yield captured


def _night_frayed(player_id: str, previous_lcd: int, new_lcd: int, reason_code: str) -> str:
    _ = player_id, previous_lcd, new_lcd, reason_code
    return "night_frayed_reflexes"


def _harness(
    lcd: int = 50, tier: str = "uneasy", *, liabilities: str = "[]", catatonia_entered_at: datetime | None = None
) -> LucidityHarness:
    return lucidity_registry({PID: LucidityData(lcd, tier, liabilities, catatonia_entered_at)})


async def test_a_positive_delta_raises_lcd_and_its_tier() -> None:
    harness = _harness(50, "uneasy")

    result = await LucidityService(harness.registry).apply_lucidity_adjustment(PID, 25, reason_code="pray")

    assert (result.previous_lcd, result.new_lcd, result.previous_tier, result.new_tier) == (50, 75, "uneasy", "lucid")
    assert (harness.lucidity(PID).lcd, harness.lucidity(PID).tier) == (75, "lucid")


async def test_lcd_is_clamped_to_its_range() -> None:
    harness = _harness(95, "lucid")
    service = LucidityService(harness.registry)

    assert (await service.apply_lucidity_adjustment(PID, 50, reason_code="up")).new_lcd == 100
    assert (await service.apply_lucidity_adjustment(PID, -500, reason_code="down")).new_lcd == -100


async def test_a_change_is_lazy_and_its_ledger_row_is_written_with_it() -> None:
    harness = _harness(50, "uneasy")

    _ = await LucidityService(harness.registry).apply_lucidity_adjustment(
        PID, -5, reason_code="passive_flux", metadata={"source": "night"}, location_id="room_1"
    )

    assert harness.db.commits == 0  # nothing written until the sweep
    assert await harness.flush() == 1
    [row] = harness.ledger()
    assert (row["delta"], row["reason_code"], row["location_id"]) == (-5, "passive_flux", "room_1")
    assert json.loads(str(row["metadata"])) == {"source": "night"}


async def test_a_computed_delta_reads_the_live_value_and_a_zero_changes_nothing() -> None:
    harness = _harness(5, "deranged")
    service = LucidityService(harness.registry)

    def to_floor(current: int) -> int:
        return max(0 - current, -2) if current > 0 else 0

    first = await service.apply_lucidity_adjustment(PID, to_floor, reason_code="drain")
    assert (first.previous_lcd, first.new_lcd, first.delta) == (5, 3, -2)

    _ = await service.apply_lucidity_adjustment(PID, -3, reason_code="hit")  # now 0
    unchanged = await service.apply_lucidity_adjustment(PID, to_floor, reason_code="drain")

    assert (unchanged.previous_lcd, unchanged.new_lcd, unchanged.delta) == (0, 0, 0)
    _ = await harness.flush()
    assert [row["reason_code"] for row in harness.ledger()] == ["drain", "hit"]  # the no-op is not logged


async def test_an_unknown_player_is_gone() -> None:
    service = LucidityService(_harness().registry)

    with pytest.raises(PlayerGoneError):
        _ = await service.apply_lucidity_adjustment(uuid.uuid4(), -1, reason_code="x")
    with pytest.raises(PlayerGoneError):
        _ = await service.get_lucidity(uuid.uuid4())


async def test_get_lucidity_is_the_starting_value_for_a_player_with_no_record() -> None:
    harness = lucidity_registry({PID: None})

    data = await LucidityService(harness.registry).get_lucidity(PID)

    assert (data.lcd, data.tier) == (STARTING_LCD, "lucid")


async def test_a_large_drop_adds_the_pickers_liability() -> None:
    harness = _harness(80, "lucid")
    service = LucidityService(harness.registry, liability_picker=_night_frayed)

    result = await service.apply_lucidity_adjustment(PID, -20, reason_code="shock")

    assert result.liabilities_added == ["night_frayed_reflexes"]
    assert decode_liabilities(harness.lucidity(PID).liabilities) == [{"code": "night_frayed_reflexes", "stacks": 1}]


async def test_a_worsened_tier_adds_the_first_liability_the_player_lacks() -> None:
    first = LIABILITY_CATALOG[0]
    harness = _harness(72, "lucid", liabilities=encode_liabilities([{"code": first, "stacks": 1}]))

    result = await LucidityService(harness.registry).apply_lucidity_adjustment(PID, -5, reason_code="fright")

    assert result.new_tier == "uneasy" and result.liabilities_added == [LIABILITY_CATALOG[1]]


async def test_a_small_loss_in_the_same_tier_adds_no_liability() -> None:
    harness = _harness(60, "uneasy")

    result = await LucidityService(harness.registry).apply_lucidity_adjustment(PID, -3, reason_code="chill")

    assert result.liabilities_added == []


async def test_add_liability_adds_then_stacks() -> None:
    harness = _harness()
    service = LucidityService(harness.registry)

    _ = await service.add_liability(PID, "ritual_compulsion")
    _ = await service.add_liability(PID, "ritual_compulsion")

    assert decode_liabilities(harness.lucidity(PID).liabilities) == [{"code": "ritual_compulsion", "stacks": 2}]


async def test_clear_liability_decrements_removes_and_reports_absence() -> None:
    harness = _harness(liabilities=encode_liabilities([{"code": "bleak_outlook", "stacks": 2}]))
    service = LucidityService(harness.registry)

    assert await service.clear_liability(PID, "bleak_outlook")
    assert decode_liabilities(harness.lucidity(PID).liabilities) == [{"code": "bleak_outlook", "stacks": 1}]
    assert await service.clear_liability(PID, "bleak_outlook", remove_all=True)
    assert decode_liabilities(harness.lucidity(PID).liabilities) == []
    assert not await service.clear_liability(PID, "bleak_outlook")


async def test_entering_catatonia_stamps_it_and_is_announced_after_the_unit(sends: _Sends) -> None:
    harness = _harness(2, "deranged")
    observer = _Observer()

    _ = await LucidityService(harness.registry, catatonia_observer=observer).apply_lucidity_adjustment(
        PID, -5, reason_code="hit"
    )

    assert harness.lucidity(PID).catatonia_entered_at is not None
    assert observer.entered == [PID]
    assert len(sends.catatonia.calls) == 1


async def test_leaving_catatonia_clears_it_and_announces_success_unless_a_rescue_owns_it(sends: _Sends) -> None:
    harness = _harness(-3, "catatonic", catatonia_entered_at=T0)
    observer = _Observer()
    service = LucidityService(harness.registry, catatonia_observer=observer)

    _ = await service.apply_lucidity_adjustment(PID, 10, reason_code="tonic")

    assert harness.lucidity(PID).catatonia_entered_at is None
    assert observer.cleared == [PID]
    assert [call["status"] for call in sends.rescue.calls] == ["success"]

    rescued = _harness(-3, "catatonic", catatonia_entered_at=T0)
    sends.rescue.calls.clear()
    _ = await LucidityService(rescued.registry).apply_lucidity_adjustment(PID, 4, reason_code="ground_rescue")
    assert sends.rescue.calls == []  # the ground command announces its own success (#713)


async def test_the_change_event_carries_the_lcd_ceiling_from_the_players_stats(sends: _Sends) -> None:
    harness = lucidity_registry({PID: LucidityData(50, "uneasy")}, stats={"education": 60})

    _ = await LucidityService(harness.registry).apply_lucidity_adjustment(PID, 30, reason_code="pray")

    [kwargs] = sends.change.calls
    assert kwargs["current_lcd"] == 60
    assert cast(LucidityChangeEventExtras, kwargs["extras"]).max_lcd == 60


async def test_a_rolled_back_enclosing_unit_undoes_the_change_and_its_ledger_row() -> None:
    harness = _harness(50, "uneasy")
    service = LucidityService(harness.registry)

    with pytest.raises(RuntimeError):
        async with harness.registry.mutate(PID):
            _ = await service.apply_lucidity_adjustment(PID, -10, reason_code="hit")
            raise RuntimeError("the enclosing command failed")

    assert harness.lucidity(PID).lcd == 50
    _ = await harness.flush()
    assert harness.ledger() == []


async def test_leaving_the_hallucination_tiers_clears_phantoms_but_moving_within_them_does_not() -> None:
    harness = _harness(25, "fractured")
    service = LucidityService(harness.registry)
    with patch("server.services.phantom_hostile_service.phantom_hostile_service.clear_all_phantoms") as clear:
        _ = await service.apply_lucidity_adjustment(PID, -10, reason_code="worse")  # deranged: still eligible
        clear.assert_not_called()
        _ = await service.apply_lucidity_adjustment(PID, 40, reason_code="better")  # uneasy
        clear.assert_called_once_with(PID)


async def test_every_adjustment_writes_the_tier_cache_through() -> None:
    harness = _harness(20, "fractured")
    with patch("server.services.lucidity_tier_cache.lucidity_tier_cache.set_tier") as set_tier:
        result = await LucidityService(harness.registry).apply_lucidity_adjustment(PID, -10, reason_code="worse")
    set_tier.assert_called_once_with(PID, result.new_tier)


def test_max_lcd_from_stats() -> None:
    assert max_lcd_from_stats({"education": 80}) == 80
    assert max_lcd_from_stats({"max_lucidity": 90, "education": 80}) == 90
    assert max_lcd_from_stats({}) == 100
