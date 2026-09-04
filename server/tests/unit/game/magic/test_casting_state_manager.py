"""Unit tests for server.game.magic.casting_state_manager."""

from __future__ import annotations

import uuid
from types import SimpleNamespace

import pytest

from server.game.magic.casting_state_manager import CastingStateManager, StartCastingTarget


def _spell(casting_time: int = 3) -> SimpleNamespace:
    return SimpleNamespace(
        spell_id="fireball",
        name="Fireball",
        casting_time_seconds=casting_time,
        mp_cost=5,
    )


def test_start_and_complete_casting() -> None:
    mgr = CastingStateManager()
    player_id = uuid.uuid4()
    state = mgr.start_casting(player_id, _spell(), start_tick=10)
    assert state.spell_id == "fireball"
    assert mgr.is_casting(player_id)
    done = mgr.complete_casting(player_id)
    assert done is not None
    assert not mgr.is_casting(player_id)


def test_start_casting_twice_raises() -> None:
    mgr = CastingStateManager()
    player_id = uuid.uuid4()
    mgr.start_casting(player_id, _spell(), start_tick=1)
    with pytest.raises(ValueError, match="already casting"):
        mgr.start_casting(player_id, _spell(), start_tick=2)


def test_interrupt_casting() -> None:
    mgr = CastingStateManager()
    player_id = uuid.uuid4()
    mgr.start_casting(player_id, _spell(), start_tick=1)
    interrupted = mgr.interrupt_casting(player_id)
    assert interrupted is not None
    assert mgr.get_casting_state(player_id) is None


def test_update_casting_progress_waits_for_initiative() -> None:
    mgr = CastingStateManager()
    player_id = uuid.uuid4()
    mgr.start_casting(player_id, _spell(3), start_tick=0, target=StartCastingTarget(next_initiative_tick=50))
    assert mgr.update_casting_progress(player_id, current_tick=10) is False
    assert mgr.update_casting_progress(player_id, current_tick=50) is False


def test_update_casting_progress_completes() -> None:
    mgr = CastingStateManager()
    player_id = uuid.uuid4()
    mgr.start_casting(player_id, _spell(1), start_tick=0)
    # 1 second = 10 ticks at 0.1s per tick
    assert mgr.update_casting_progress(player_id, current_tick=10) is True


def test_get_all_casting_players_and_clear() -> None:
    mgr = CastingStateManager()
    p1, p2 = uuid.uuid4(), uuid.uuid4()
    mgr.start_casting(p1, _spell(), start_tick=0)
    mgr.start_casting(p2, _spell(), start_tick=0)
    assert set(mgr.get_all_casting_players()) == {p1, p2}
    mgr.clear_all()
    assert mgr.get_all_casting_players() == []
