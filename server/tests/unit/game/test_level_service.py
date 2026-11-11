"""
Unit tests for LevelService: grant_xp and the level-up hook.

Character creation revamp plan 4.1 (L3). XP is granted as a unit of work on the player registry (ADR-029 step 7b); the
level follows the curve in models.player_xp, which an integration test checks against the SQL function.
"""

import json
import uuid
from unittest.mock import AsyncMock

import pytest

from server.events.event_types import PlayerXPAwardEvent
from server.game.level_service import LevelService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry


def _rig(
    *, xp: int = 0, level: int = 1, known: bool = True
) -> tuple[LevelService, LucidityHarness, uuid.UUID, AsyncMock]:
    pid = uuid.uuid4()
    harness = lucidity_registry({pid: None} if known else {}, row={"experience_points": xp, "level": level})
    hook = AsyncMock()
    return LevelService(harness.registry, level_up_hook=hook), harness, pid, hook


def _committed(harness: LucidityHarness) -> list[dict[str, object]]:
    """The changed columns of every update_player_row the registry committed."""
    return [
        json.loads(str(params["changes"]))
        for params in harness.db.executed
        if params is not None and "changes" in params
    ]


def _xp_events(harness: LucidityHarness) -> list[PlayerXPAwardEvent]:
    return [event for event in harness.published if isinstance(event, PlayerXPAwardEvent)]


@pytest.mark.asyncio
async def test_grant_xp_zero_is_a_no_op() -> None:
    service, harness, pid, hook = _rig()

    await service.grant_xp(pid, 0)

    assert not harness.registry.is_loaded(pid)
    assert harness.db.commits == 0
    hook.assert_not_awaited()


@pytest.mark.asyncio
async def test_grant_xp_negative_raises() -> None:
    service, _, pid, _ = _rig()

    with pytest.raises(ValueError, match="non-negative"):
        await service.grant_xp(pid, -1)


@pytest.mark.asyncio
async def test_grant_xp_for_a_player_who_does_not_exist_raises_value_error() -> None:
    service, harness, pid, hook = _rig(known=False)

    with pytest.raises(ValueError, match="not found"):
        await service.grant_xp(pid, 50)

    assert harness.db.commits == 0
    hook.assert_not_awaited()


@pytest.mark.asyncio
async def test_an_award_adds_to_the_live_total_and_commits_only_xp_and_level() -> None:
    service, harness, pid, _ = _rig(xp=20)

    await service.grant_xp(pid, 30)

    view = harness.registry.peek(pid)
    assert view is not None and (view.row.experience_points, view.row.level) == (50, 1)
    assert _committed(harness) == [{"experience_points": 50}]  # level 1 did not change, so it is not written
    assert harness.db.commits == 1


@pytest.mark.asyncio
async def test_an_award_tells_the_client_after_the_commit() -> None:
    service, harness, pid, _ = _rig()

    await service.grant_xp(pid, 100)

    [event] = _xp_events(harness)
    assert (event.player_id, event.xp_amount, event.new_level) == (pid, 100, 2)


@pytest.mark.asyncio
async def test_a_level_up_calls_the_hook_with_the_new_level() -> None:
    service, harness, pid, hook = _rig(xp=50)

    await service.grant_xp(pid, 50)  # 100 XP is level 2

    hook.assert_awaited_once_with(pid, 2)
    assert _committed(harness) == [{"experience_points": 100, "level": 2}]


@pytest.mark.asyncio
async def test_no_level_change_does_not_call_the_hook() -> None:
    service, _, pid, hook = _rig(xp=0)

    await service.grant_xp(pid, 50)

    hook.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_level_never_goes_down() -> None:
    """A character whose stored level is above the curve (an admin set it) keeps it."""
    service, harness, pid, hook = _rig(xp=0, level=5)

    await service.grant_xp(pid, 1)

    view = harness.registry.peek(pid)
    assert view is not None and view.row.level == 5
    hook.assert_not_awaited()


@pytest.mark.asyncio
async def test_without_a_hook_a_level_up_still_completes() -> None:
    pid = uuid.uuid4()
    harness = lucidity_registry({pid: None}, row={"experience_points": 250, "level": 2})

    await LevelService(harness.registry).grant_xp(pid, 100)  # 350 XP is level 3

    view = harness.registry.peek(pid)
    assert view is not None and view.row.level == 3


@pytest.mark.asyncio
async def test_a_failed_commit_awards_nothing_and_tells_nobody() -> None:
    service, harness, pid, hook = _rig(xp=50)
    harness.db.fail_commits = 1

    with pytest.raises(RuntimeError):
        await service.grant_xp(pid, 50)

    view = harness.registry.peek(pid)
    assert view is not None and (view.row.experience_points, view.row.level) == (50, 1)
    assert _xp_events(harness) == []
    hook.assert_not_awaited()
