"""Unit tests for ActiveLucidityService.apply_timed_recovery (shared by recovery actions and consumables, #870)."""

import uuid
from datetime import UTC, datetime, timedelta
from typing import final
from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.lucidity import LucidityCooldown
from server.services.active_lucidity_service import (
    ActiveLucidityService,
    LucidityActionOnCooldownError,
    UnknownLucidityActionError,
)
from server.services.lucidity_service import LucidityService, LucidityUpdateResult

NOW = datetime(2026, 10, 5, 12, 0, tzinfo=UTC)


@final
class Ledger:
    """Stands in for LucidityService's persistence calls and records what the service did."""

    def __init__(self, cooldown_expires_at: datetime | None) -> None:
        self.existing_expiry = cooldown_expires_at
        self.adjustments: list[tuple[uuid.UUID, int, str, str | None]] = []
        self.cooldowns_set: list[tuple[uuid.UUID, str, datetime]] = []

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> LucidityCooldown | None:
        if self.existing_expiry is None:
            return None
        return LucidityCooldown(
            player_id=str(player_id), action_code=action_code, cooldown_expires_at=self.existing_expiry
        )

    async def apply_lucidity_adjustment(
        self, player_id: uuid.UUID, delta: int, *, reason_code: str, location_id: str | None = None
    ) -> LucidityUpdateResult:
        self.adjustments.append((player_id, delta, reason_code, location_id))
        return LucidityUpdateResult(
            player_id=player_id,
            previous_lcd=50,
            new_lcd=50 + delta,
            previous_tier="lucid",
            new_tier="lucid",
            delta=delta,
            liabilities_added=[],
        )

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> LucidityCooldown:
        self.cooldowns_set.append((player_id, action_code, expires_at))
        return LucidityCooldown(player_id=str(player_id), action_code=action_code, cooldown_expires_at=expires_at)


def _service(monkeypatch: pytest.MonkeyPatch, ledger: Ledger) -> ActiveLucidityService:
    """A real ActiveLucidityService whose underlying LucidityService calls land in the ledger."""

    async def get_cooldown(_self: LucidityService, player_id: uuid.UUID, action_code: str) -> LucidityCooldown | None:
        return await ledger.get_cooldown(player_id, action_code)

    async def apply_lucidity_adjustment(
        _self: LucidityService,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: object = None,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        _ = metadata
        return await ledger.apply_lucidity_adjustment(
            player_id, delta, reason_code=reason_code, location_id=location_id
        )

    async def set_cooldown(
        _self: LucidityService, player_id: uuid.UUID, action_code: str, expires_at: datetime
    ) -> LucidityCooldown:
        return await ledger.set_cooldown(player_id, action_code, expires_at)

    monkeypatch.setattr(LucidityService, "get_cooldown", get_cooldown)
    monkeypatch.setattr(LucidityService, "apply_lucidity_adjustment", apply_lucidity_adjustment)
    monkeypatch.setattr(LucidityService, "set_cooldown", set_cooldown)
    return ActiveLucidityService(AsyncMock(spec=AsyncSession), now_provider=lambda: NOW)


@pytest.mark.asyncio
async def test_apply_timed_recovery_applies_gain_and_sets_cooldown(monkeypatch: pytest.MonkeyPatch) -> None:
    """The caller's key names the audit reason code and the cooldown row."""
    ledger = Ledger(cooldown_expires_at=None)
    player_id = uuid.uuid4()

    result = await _service(monkeypatch, ledger).apply_timed_recovery(
        player_id, cooldown_key="folk_tonic", lcd_delta=3, cooldown=timedelta(minutes=30), location_id="room-1"
    )

    assert (result.delta, result.new_lcd) == (3, 53)
    assert ledger.adjustments == [(player_id, 3, "recovery_folk_tonic", "room-1")]
    # Stored naive-UTC, as set_cooldown rows always have been.
    assert ledger.cooldowns_set == [(player_id, "folk_tonic", datetime(2026, 10, 5, 12, 30))]


@pytest.mark.asyncio
@pytest.mark.parametrize("expiry", [NOW + timedelta(minutes=5), (NOW + timedelta(minutes=5)).replace(tzinfo=None)])
async def test_apply_timed_recovery_refuses_during_cooldown(monkeypatch: pytest.MonkeyPatch, expiry: datetime) -> None:
    """An unexpired cooldown (tz-aware or the naive form stored in the DB) raises before any LCD change."""
    ledger = Ledger(cooldown_expires_at=expiry)

    with pytest.raises(LucidityActionOnCooldownError):
        _ = await _service(monkeypatch, ledger).apply_timed_recovery(
            uuid.uuid4(), cooldown_key="folk_tonic", lcd_delta=3, cooldown=timedelta(minutes=30)
        )

    assert ledger.adjustments == []
    assert ledger.cooldowns_set == []


@pytest.mark.asyncio
async def test_apply_timed_recovery_allows_an_expired_cooldown(monkeypatch: pytest.MonkeyPatch) -> None:
    ledger = Ledger(cooldown_expires_at=NOW - timedelta(seconds=1))

    _ = await _service(monkeypatch, ledger).apply_timed_recovery(
        uuid.uuid4(), cooldown_key="folk_tonic", lcd_delta=3, cooldown=timedelta(minutes=30)
    )

    assert len(ledger.adjustments) == 1


@pytest.mark.asyncio
async def test_perform_recovery_action_still_uses_its_profile_through_the_shared_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ledger = Ledger(cooldown_expires_at=None)
    player_id = uuid.uuid4()

    await _service(monkeypatch, ledger).perform_recovery_action(player_id, action_code="PRAY", location_id="room-1")

    assert ledger.adjustments == [(player_id, 8, "recovery_pray", "room-1")]
    assert ledger.cooldowns_set == [(player_id, "pray", datetime(2026, 10, 5, 12, 15))]


@pytest.mark.asyncio
async def test_folk_tonic_is_no_longer_a_recovery_action(monkeypatch: pytest.MonkeyPatch) -> None:
    """#870: folk tonic became a consumable item, so the action profile is gone."""
    ledger = Ledger(cooldown_expires_at=None)

    with pytest.raises(UnknownLucidityActionError):
        await _service(monkeypatch, ledger).perform_recovery_action(uuid.uuid4(), action_code="folk_tonic")

    assert ledger.adjustments == []
