"""
In-memory cache of each player's current lucidity tier (#714).

Exit hallucination (#626) needs to know "is this player currently deranged?" on every room
broadcast. A DB lookup there would cost a round trip per broadcast even in the common case,
unlike phantom visibility (#625), which is already a cheap in-memory dict lookup via
`phantom_hostile_service`. This cache gives tier the same property.

Kept fresh two ways:
1. `LucidityService._finalize_lucidity_adjustment` writes through immediately whenever a
   player's tier is (re-)computed.
2. `PassiveLucidityFluxService`'s tick loop refreshes every active player's tier every tick
   (`server_tick_rate` = 0.1s) as a backstop, so even a missed write-through path self-heals
   within roughly one tick.

A cache miss means "no data yet" and is treated as non-deranged -- fail safe to truthful exits
rather than guessing.
"""

from __future__ import annotations

import uuid


class LucidityTierCache:
    """Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share this instance."""

    def __init__(self) -> None:
        self._tiers: dict[str, str] = {}

    def set_tier(self, player_id: uuid.UUID | str, tier: str) -> None:
        """Record this player's current tier."""
        self._tiers[str(player_id)] = tier

    def get_tier(self, player_id: uuid.UUID | str) -> str | None:
        """Return the cached tier, or None if this player has never been recorded."""
        return self._tiers.get(str(player_id))

    def is_deranged(self, player_id: uuid.UUID | str) -> bool:
        """True only if the cached tier is exactly 'deranged' -- a cache miss is never deranged."""
        return self.get_tier(player_id) == "deranged"

    def clear(self, player_id: uuid.UUID | str) -> None:
        """Drop a player's cached tier (e.g. on disconnect)."""
        _ = self._tiers.pop(str(player_id), None)


lucidity_tier_cache = LucidityTierCache()

__all__ = ["LucidityTierCache", "lucidity_tier_cache"]
