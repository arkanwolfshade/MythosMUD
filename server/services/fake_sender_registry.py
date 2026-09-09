"""
In-memory registry of each player's most recent fake NPC whisper sender (#625, #714).

Mirrors `phantom_hostile_service`'s pattern: hallucinations are player-specific, in-memory,
tick-scale state, not database rows. This is what lets `reply` answer in-fiction instead of
leaking "the player you're trying to reply to is no longer available" the moment someone reacts
naturally to a fake whisper -- see `communication_commands_flows._deliver_reply_to_last_whisper`.
"""

from __future__ import annotations

import uuid


class FakeSenderRegistry:
    """Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share this instance."""

    def __init__(self) -> None:
        self._last_fake_sender: dict[str, str] = {}

    def record_fake_whisper(self, player_id: uuid.UUID | str, npc_name: str) -> None:
        """Record that this player's most recent whisper came from this fake NPC."""
        self._last_fake_sender[str(player_id)] = npc_name

    def get_last_fake_sender(self, player_id: uuid.UUID | str) -> str | None:
        """Return the fake NPC name this player was last whispered by, or None."""
        return self._last_fake_sender.get(str(player_id))

    def clear(self, player_id: uuid.UUID | str) -> None:
        """Drop this player's fake-sender record (e.g. leaving fractured/deranged, disconnect)."""
        _ = self._last_fake_sender.pop(str(player_id), None)


fake_sender_registry = FakeSenderRegistry()

__all__ = ["FakeSenderRegistry", "fake_sender_registry"]
