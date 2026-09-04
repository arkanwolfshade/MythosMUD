"""
Reconnect catch-up summary for disconnect-grace players (`#297`).

While a player sits in the disconnect-grace "zombie" window (`disconnect_grace_period.py`), they
remain attackable. On reconnect within the window, `player_presence_tracker.track_player_connected_impl`
calls `build_catchup_message` -- before the grace period itself is torn down -- to tell the player
what they missed.

The summary is derived from a DP snapshot taken when the grace window started
(`capture_grace_snapshot`), compared against the player's current DP on reconnect. Deliberately not
a buffered event log: a leaking per-player event buffer is exactly the shape `#768` spent a session
chasing, and a before/after DP delta answers the only question that actually matters ("why am I
hurt?") with O(1) state per grace player.

Death during the window is a distinct case, not a damage line: `game_tick_death.py`'s
`_process_dead_players` moves a dead player to limbo on the very next DP-decay tick, independent of
connection state, so by the time a reconnect can happen the character has already been relocated --
the existing reconnect room-resolution path (reading `player.current_room_id` from the DB) already
lands them there correctly. This module's job is only to say what happened, not to orchestrate it.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Protocol stubs (PEP 544)

from __future__ import annotations

import uuid
from typing import Protocol


class CatchupPlayer(Protocol):
    def get_stats(self) -> dict[str, object]: ...
    def is_dead(self) -> bool: ...


class CatchupManager(Protocol):
    grace_period_snapshots: dict[uuid.UUID, dict[str, int]]


def _dp_snapshot(player: CatchupPlayer) -> dict[str, int] | None:
    """Read (current_dp, max_dp) off a player's stats, if both are present and well-typed."""
    stats = player.get_stats()
    current_dp = stats.get("current_dp")
    max_dp = stats.get("max_dp")
    if not isinstance(current_dp, int) or not isinstance(max_dp, int):
        return None
    return {"current_dp": current_dp, "max_dp": max_dp}


def capture_grace_snapshot(player_id: uuid.UUID, player: CatchupPlayer, manager: CatchupManager) -> None:
    """Snapshot DP at the moment a disconnect-grace window starts.

    Called from `disconnect_grace_period.start_grace_period`. A missing/unreadable snapshot is not
    an error -- `build_catchup_message` just stays silent on reconnect rather than guessing.
    """
    snapshot = _dp_snapshot(player)
    if snapshot is not None:
        manager.grace_period_snapshots[player_id] = snapshot


def build_catchup_message(player_id: uuid.UUID, player: CatchupPlayer, manager: CatchupManager) -> str | None:
    """Build a reconnect catch-up summary, or None if there is nothing worth telling the player.

    Must be called before `cancel_grace_period` removes the snapshot for `player_id`.
    """
    before = manager.grace_period_snapshots.get(player_id)
    if before is None:
        return None

    after = _dp_snapshot(player)
    if after is None:
        return None

    if player.is_dead():
        return "While you were disconnected, you succumbed to your wounds and were moved to recovery."

    damage = before["current_dp"] - after["current_dp"]
    if damage <= 0:
        return None
    return (
        f"While you were disconnected you were attacked and took {damage} damage. "
        f"You are at {after['current_dp']}/{after['max_dp']} DP."
    )
