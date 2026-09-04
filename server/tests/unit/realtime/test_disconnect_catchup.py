"""
Unit tests for the disconnect-grace reconnect catch-up summary (`#297`).

Covers the DP-snapshot capture/consume cycle in `disconnect_catchup.py`: a damage delta produces
a summary, a zero/negative delta stays silent, death produces a distinct message, and missing or
malformed state degrades to None rather than raising.
"""

import uuid
from typing import cast
from unittest.mock import MagicMock

from server.realtime.disconnect_catchup import (
    CatchupManager,
    CatchupPlayer,
    build_catchup_message,
    capture_grace_snapshot,
)

PLAYER_ID = uuid.uuid4()


class _FakePlayer:
    """A minimal, fully-typed `CatchupPlayer` double -- avoids MagicMock's inherently
    Any-typed attributes (`reportAny`) for the two methods this module actually calls."""

    def __init__(self, stats: dict[str, object], *, is_dead: bool = False) -> None:
        self._stats: dict[str, object] = stats
        self._is_dead: bool = is_dead

    def get_stats(self) -> dict[str, object]:
        """Return the stats dict set at construction."""
        return self._stats

    def is_dead(self) -> bool:
        """Return the death flag set at construction."""
        return self._is_dead


def _player(current_dp: int, max_dp: int = 20, *, is_dead: bool = False) -> CatchupPlayer:
    return _FakePlayer({"current_dp": current_dp, "max_dp": max_dp}, is_dead=is_dead)


def _manager(snapshots: dict[uuid.UUID, dict[str, int]] | None = None) -> CatchupManager:
    manager = MagicMock()
    manager.grace_period_snapshots = {} if snapshots is None else snapshots
    return cast(CatchupManager, manager)


def test_capture_grace_snapshot_stores_dp() -> None:
    """capture_grace_snapshot() stores current/max DP keyed by player_id."""
    manager = _manager()

    capture_grace_snapshot(PLAYER_ID, _player(current_dp=15, max_dp=20), manager)

    assert manager.grace_period_snapshots[PLAYER_ID] == {"current_dp": 15, "max_dp": 20}


def test_capture_grace_snapshot_skips_unreadable_stats() -> None:
    """A player whose get_stats() doesn't return usable DP fields is not snapshotted."""
    manager = _manager()
    player = _FakePlayer({"current_dp": "not-an-int"})

    capture_grace_snapshot(PLAYER_ID, player, manager)

    assert manager.grace_period_snapshots == {}


def test_build_catchup_message_reports_damage_taken() -> None:
    """A DP drop between snapshot and reconnect produces a damage summary."""
    manager = _manager({PLAYER_ID: {"current_dp": 20, "max_dp": 20}})

    message = build_catchup_message(PLAYER_ID, _player(current_dp=12, max_dp=20), manager)

    assert message is not None
    assert "8 damage" in message
    assert "12/20" in message


def test_build_catchup_message_silent_on_no_change() -> None:
    """A clean reconnect (no DP change) produces no message."""
    manager = _manager({PLAYER_ID: {"current_dp": 20, "max_dp": 20}})

    message = build_catchup_message(PLAYER_ID, _player(current_dp=20, max_dp=20), manager)

    assert message is None


def test_build_catchup_message_silent_on_dp_gain() -> None:
    """Healing during the window (DP went up) is not reported as damage."""
    manager = _manager({PLAYER_ID: {"current_dp": 10, "max_dp": 20}})

    message = build_catchup_message(PLAYER_ID, _player(current_dp=15, max_dp=20), manager)

    assert message is None


def test_build_catchup_message_reports_death_distinctly() -> None:
    """Dying during the window produces the death-specific message, not a damage line."""
    manager = _manager({PLAYER_ID: {"current_dp": 5, "max_dp": 20}})

    message = build_catchup_message(PLAYER_ID, _player(current_dp=-12, max_dp=20, is_dead=True), manager)

    assert message is not None
    assert "succumbed" in message
    assert "damage" not in message


def test_build_catchup_message_none_without_snapshot() -> None:
    """No snapshot on record (e.g. capture failed) means no message, not an error."""
    manager = _manager()

    message = build_catchup_message(PLAYER_ID, _player(current_dp=10), manager)

    assert message is None
