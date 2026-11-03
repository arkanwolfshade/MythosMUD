"""Unit tests for CorruptionService (#804) on a real player registry (ADR-029 step 5c).

The value is the row part's ``stats.corruption``; the ledger row and any cleanse cooldown are parts of the same
aggregate. Each operation is one sync unit, so it commits (one commit) before it returns, and the announcements
(client event, tier cache, tier-crossing message) follow it.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, patch

import pytest

from server.exceptions import ValidationError
from server.models.corruption import CorruptionTier
from server.services.corruption_service import CorruptionActionError, CorruptionActionOnCooldownError, CorruptionService
from server.services.corruption_tier_cache import corruption_tier_cache
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PID = uuid.uuid4()


@pytest.fixture(autouse=True)
def _quiet() -> Iterator[AsyncMock]:
    """The client event and tier-crossing message (asserted where they matter); the tier cache is reset after."""
    with (
        patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock),
        patch("server.game.chat_npc_system.deliver_personal_system", new_callable=AsyncMock) as notify,
    ):
        yield notify
    corruption_tier_cache.clear(PID)


def _harness(corruption: int = 0, *, cleanse_until: datetime | None = None) -> LucidityHarness:
    return lucidity_registry(
        {PID: None},
        stats={"current_dp": 20, "max_dp": 20, "corruption": corruption},
        corruption_cooldowns={"cleanse": cleanse_until} if cleanse_until else None,
    )


def _stats_writes(harness: LucidityHarness) -> list[dict[str, object]]:
    """The ``stats_changes`` of every players-row write."""
    return [
        json.loads(str(params["stats_changes"]))
        for params in harness.db.executed
        if params is not None and "stats_changes" in params
    ]


async def test_an_adjustment_commits_the_value_and_its_ledger_row_in_one_unit() -> None:
    harness = _harness(10)

    result = await CorruptionService(harness.registry).apply_corruption_adjustment(
        PID, 5, reason_code="spell_cast", metadata={"spell_id": "x"}, location_id="room-1"
    )

    assert (result.previous_value, result.new_value, result.delta) == (10, 15, 5)
    assert harness.corruption(PID) == 15
    assert harness.db.commits == 1  # sync: written before the call returned
    assert _stats_writes(harness) == [{"corruption": 15}]  # only the key it changed, never DP
    [row] = harness.ledger()
    assert (row["delta"], row["reason_code"], row["location_id"]) == (5, "spell_cast", "room-1")
    assert json.loads(str(row["metadata"])) == {"spell_id": "x"}


async def test_an_adjustment_pushes_a_player_update_event() -> None:
    """A live client only ever learns its own corruption changed via this event -- nothing else
    pushes it (no dedicated wire event, per SUBSYSTEM_CORRUPTION_DESIGN.md §4)."""
    harness = _harness(10)

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event:
        _ = await CorruptionService(harness.registry).apply_corruption_adjustment(PID, 5, reason_code="spell_cast")

    send_event.assert_awaited_once_with(PID, "player_update", {"stats": {"corruption": 15}})


async def test_a_failed_commit_rolls_the_value_back_and_announces_nothing(_quiet: AsyncMock) -> None:
    harness = _harness(48)
    harness.db.fail_commits = 1

    with pytest.raises(RuntimeError):
        _ = await CorruptionService(harness.registry).apply_corruption_adjustment(PID, 5, reason_code="test")

    assert harness.corruption(PID) == 48
    assert corruption_tier_cache.get_tier(PID) is CorruptionTier.PURE  # never written: the miss default
    _quiet.assert_not_awaited()  # the marked -> corrupted crossing was never narrated


async def test_an_unknown_player_is_a_validation_error() -> None:
    with pytest.raises(ValidationError, match="Player not found"):
        _ = await CorruptionService(lucidity_registry({}).registry).apply_corruption_adjustment(
            PID, 5, reason_code="test"
        )


@pytest.mark.parametrize(
    ("starting_value", "delta", "expected_new_value"),
    [
        (98, 50, 100),  # clamped to 100
        (0, -5, 0),  # #815: never touched, so no floor -- 0 is a real, reachable value
        (5, -8, 1),  # #815: a partial cleanse cannot fully cleanse
        (1, -8, 1),  # the scar holds even when already at the floor
        (50, -1000, 1),  # no negative delta, however large, crosses back to 0
    ],
)
async def test_an_adjustment_is_clamped_and_floored_once_touched(
    starting_value: int, delta: int, expected_new_value: int
) -> None:
    harness = _harness(starting_value)

    result = await CorruptionService(harness.registry).apply_corruption_adjustment(PID, delta, reason_code="test")

    assert result.new_value == expected_new_value == harness.corruption(PID)


async def test_bypass_permanence_floor_allows_zero_and_still_logs() -> None:
    """#816: admin setstat may wipe corruption to 0 via bypass_permanence_floor."""
    harness = _harness(40)

    result = await CorruptionService(harness.registry).apply_corruption_adjustment(
        PID, -40, reason_code="admin_set", bypass_permanence_floor=True
    )

    assert (result.previous_value, result.new_value) == (40, 0)
    assert [row["reason_code"] for row in harness.ledger()] == ["admin_set"]
    assert corruption_tier_cache.get_tier(PID) is CorruptionTier.PURE


async def test_the_first_taint_is_a_tier_crossing_narrated_once(_quiet: AsyncMock) -> None:
    """#815: the very first point of corruption is a real tier crossing (pure -> touched)."""
    result = await CorruptionService(_harness(0).registry).apply_corruption_adjustment(PID, 3, reason_code="test")

    assert (result.previous_tier, result.new_tier) == (CorruptionTier.PURE, CorruptionTier.TOUCHED)
    _quiet.assert_awaited_once()


async def test_a_tier_crossing_writes_the_cache_and_notifies_the_player(_quiet: AsyncMock) -> None:
    result = await CorruptionService(_harness(48).registry).apply_corruption_adjustment(PID, 5, reason_code="test")

    assert (result.previous_tier, result.new_tier) == (CorruptionTier.MARKED, CorruptionTier.CORRUPTED)
    assert corruption_tier_cache.get_tier(PID) is CorruptionTier.CORRUPTED
    _quiet.assert_awaited_once()
    assert _quiet.await_args is not None and _quiet.await_args.args[0] == PID


async def test_no_notification_within_a_tier(_quiet: AsyncMock) -> None:
    result = await CorruptionService(_harness(10).registry).apply_corruption_adjustment(PID, 5, reason_code="test")

    assert corruption_tier_cache.get_tier(PID) == result.new_tier  # #804: every adjustment writes the cache
    _quiet.assert_not_awaited()


# ---- recovery (cleanse) ----


async def test_cleanse_reduces_corruption_and_starts_its_cooldown_in_one_commit() -> None:
    harness = _harness(20)

    result = await CorruptionService(harness.registry).perform_recovery_action(
        PID, action_code="CLEANSE", location_id="room-1"
    )

    assert result.new_value == 12  # 20 - 8
    expires_at = harness.corruption_cooldowns(PID).expires_at("cleanse")
    assert expires_at is not None and expires_at > datetime.now(UTC) + timedelta(hours=5)
    assert harness.db.commits == 1
    assert [row["reason_code"] for row in harness.ledger()] == ["ritual_cleanse"]


async def test_cleanse_during_its_cooldown_changes_nothing() -> None:
    until = datetime.now(UTC) + timedelta(hours=1)
    harness = _harness(20, cleanse_until=until)

    with pytest.raises(CorruptionActionOnCooldownError):
        _ = await CorruptionService(harness.registry).perform_recovery_action(PID, action_code="cleanse")

    assert harness.corruption(PID) == 20
    assert harness.db.commits == 0
    assert await CorruptionService(harness.registry).get_cooldown_expiry(PID, "cleanse") == until


async def test_cleanse_is_allowed_once_its_cooldown_expires() -> None:
    harness = _harness(20, cleanse_until=datetime.now(UTC) - timedelta(hours=1))

    result = await CorruptionService(harness.registry).perform_recovery_action(PID, action_code="cleanse")

    assert result.new_value == 12


async def test_an_unknown_recovery_action_is_refused() -> None:
    with pytest.raises(CorruptionActionError, match="Unknown corruption recovery action"):
        _ = await CorruptionService(_harness(20).registry).perform_recovery_action(PID, action_code="pray")


async def test_get_cooldown_expiry_for_no_cooldown_or_no_player_is_none() -> None:
    assert await CorruptionService(_harness(20).registry).get_cooldown_expiry(PID, "cleanse") is None
    assert await CorruptionService(lucidity_registry({}).registry).get_cooldown_expiry(PID, "cleanse") is None
