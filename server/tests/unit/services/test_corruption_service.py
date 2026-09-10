"""Unit tests for CorruptionService (#804)."""

# pyright: reportAny=false
# TEST_MOCK: MagicMock/AsyncMock attribute and call chains (persistence.get_player_by_id,
# mock_repo.add_adjustment_log, .await_args, .assert_awaited_once, ...) resolve to Any throughout
# this file, mirroring test_lucidity_service.py's identical, already-baselined pattern for the
# same session/repository mocking shape -- this file is new, so it has no baseline entry of its
# own for the same, otherwise-unavoidable mock-typing noise.

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.corruption import CorruptionTier
from server.services.corruption_service import (
    CorruptionActionOnCooldownError,
    CorruptionService,
)
from server.services.corruption_tier_cache import corruption_tier_cache


async def _async_session_gen(session: AsyncMock):
    yield session


def _player(corruption: int = 0) -> MagicMock:
    player = MagicMock()
    stats: dict[str, object] = {"corruption": corruption}
    player.get_stats = MagicMock(return_value=stats)
    player.set_stats = MagicMock(side_effect=stats.update)
    return player


@pytest.fixture(autouse=True)
def _clear_tier_cache():  # pyright: ignore[reportUnusedFunction] -- pytest autouse fixture, used implicitly
    """The tier cache is a module-level singleton -- reset it around each test."""
    yield
    corruption_tier_cache._tiers.clear()  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]


@pytest.fixture
def persistence() -> MagicMock:
    p = MagicMock()
    p.get_player_by_id = AsyncMock()
    p.save_player = AsyncMock()
    return p


@pytest.fixture
def mock_repo() -> MagicMock:
    return MagicMock(
        add_adjustment_log=AsyncMock(),
        get_cooldown=AsyncMock(return_value=None),
        set_cooldown=AsyncMock(),
    )


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_positive_delta(persistence: MagicMock, mock_repo: MagicMock) -> None:
    player = _player(corruption=10)
    persistence.get_player_by_id.return_value = player
    player_id = uuid.uuid4()

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(
            player_id, 5, reason_code="spell_cast"
        )

    assert result.previous_value == 10
    assert result.new_value == 15
    assert result.delta == 5
    persistence.save_player.assert_awaited_once()
    mock_repo.add_adjustment_log.assert_awaited_once_with(player_id, 5, "spell_cast", "{}", None)


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_pushes_a_player_update_event(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    """A live client only ever learns its own corruption changed via this event -- nothing else
    pushes it (no dedicated wire event, per SUBSYSTEM_CORRUPTION_DESIGN.md §4)."""
    player = _player(corruption=10)
    persistence.get_player_by_id.return_value = player
    player_id = uuid.uuid4()

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
        patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send_event,
    ):
        _ = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 5, reason_code="spell_cast")

    send_event.assert_awaited_once_with(player_id, "player_update", {"stats": {"corruption": 15}})


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_clamps_to_100(persistence: MagicMock, mock_repo: MagicMock) -> None:
    player_id = uuid.uuid4()
    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        persistence.get_player_by_id.return_value = _player(corruption=98)
        high = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 50, reason_code="test")
        assert high.new_value == 100


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_stays_at_0_when_never_touched(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    """#815: a player who has never been corrupted has no floor -- 0 is a real, reachable value."""
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=0)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(player_id, -50, reason_code="test")

    assert result.new_value == 0


@pytest.mark.parametrize(
    ("starting_value", "delta", "expected_new_value"),
    [
        (5, -8, 1),  # a partial cleanse cannot fully cleanse
        (1, -8, 1),  # the scar holds even when already at the floor
        (50, -1000, 1),  # no negative delta, however large, crosses back to 0
    ],
)
@pytest.mark.asyncio
async def test_apply_corruption_adjustment_floors_at_1_once_touched(
    persistence: MagicMock, mock_repo: MagicMock, starting_value: int, delta: int, expected_new_value: int
) -> None:
    """#815: once corruption exceeds 0, this service can never take it back below 1."""
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=starting_value)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(player_id, delta, reason_code="test")

    assert result.new_value == expected_new_value


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_notifies_on_first_taint(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    """#815: the very first point of corruption is a real tier crossing (pure -> touched) and
    must narrate exactly once, same as any other crossing."""
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=0)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
        patch("server.services.corruption_service.deliver_personal_system", new_callable=AsyncMock) as notify,
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 3, reason_code="test")

    assert result.previous_tier is CorruptionTier.PURE
    assert result.new_tier is CorruptionTier.TOUCHED
    notify.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_writes_through_the_tier_cache(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    """#804: mirrors lucidity's write-through-cache test -- every adjustment updates the cache."""
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=10)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 5, reason_code="test")

    assert corruption_tier_cache.get_tier(player_id) == result.new_tier


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_notifies_on_tier_crossing(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=48)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
        patch("server.services.corruption_service.deliver_personal_system", new_callable=AsyncMock) as notify,
    ):
        result = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 5, reason_code="test")

    assert result.previous_tier is CorruptionTier.MARKED
    assert result.new_tier is CorruptionTier.CORRUPTED
    notify.assert_awaited_once()
    await_args = notify.await_args
    assert await_args is not None
    assert await_args.args[0] == player_id


@pytest.mark.asyncio
async def test_apply_corruption_adjustment_no_notification_within_a_tier(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=10)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
        patch("server.services.corruption_service.deliver_personal_system", new_callable=AsyncMock) as notify,
    ):
        _ = await CorruptionService(persistence).apply_corruption_adjustment(player_id, 5, reason_code="test")

    notify.assert_not_awaited()


@pytest.mark.asyncio
async def test_perform_recovery_action_cleanse_reduces_corruption(persistence: MagicMock, mock_repo: MagicMock) -> None:
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=20)

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).perform_recovery_action(player_id, action_code="cleanse")

    assert result.new_value == 12  # 20 - 8
    mock_repo.set_cooldown.assert_awaited_once()
    ledger_call = mock_repo.add_adjustment_log.await_args
    assert ledger_call.args[2] == "ritual_cleanse"


@pytest.mark.asyncio
async def test_perform_recovery_action_rejects_on_cooldown(persistence: MagicMock, mock_repo: MagicMock) -> None:
    player_id = uuid.uuid4()
    mock_repo.get_cooldown = AsyncMock(
        return_value=MagicMock(cooldown_expires_at=datetime.now(UTC) + timedelta(hours=1))
    )

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        with pytest.raises(CorruptionActionOnCooldownError):
            _ = await CorruptionService(persistence).perform_recovery_action(player_id, action_code="cleanse")

    persistence.get_player_by_id.assert_not_awaited()


@pytest.mark.asyncio
async def test_perform_recovery_action_allows_after_cooldown_expires(
    persistence: MagicMock, mock_repo: MagicMock
) -> None:
    player_id = uuid.uuid4()
    persistence.get_player_by_id.return_value = _player(corruption=20)
    mock_repo.get_cooldown = AsyncMock(
        return_value=MagicMock(cooldown_expires_at=datetime.now(UTC) - timedelta(hours=1))
    )

    with (
        patch("server.services.corruption_service.CorruptionRepository", return_value=mock_repo),
        patch(
            "server.services.corruption_service.get_async_session",
            side_effect=lambda: _async_session_gen(AsyncMock()),
        ),
    ):
        result = await CorruptionService(persistence).perform_recovery_action(player_id, action_code="cleanse")

    assert result.new_value == 12
