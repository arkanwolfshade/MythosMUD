"""
In-memory cache of each player's previous corruption tier (#804).

Unlike `LucidityTierCache`, this cache has no eligibility check reading it on every broadcast --
corruption's current tier is a pure function of a value callers already hold in memory
(`server.models.corruption.compute_tier`), so there is no round trip to avoid.

What this cache is actually for: `CorruptionService.apply_corruption_adjustment` needs the
player's *previous* tier to detect a crossing (e.g. "just entered `corrupted`") so it can fire
the tier-change personal message exactly once, not on every adjustment. That comparison is this
cache's only reader.

Kept fresh by `CorruptionService`, which writes through immediately on every adjustment. There is
no tick-loop backstop (unlike lucidity) -- corruption has no passive decay, so nothing else could
cause the cached tier to drift from the stored value between adjustments.

A cache miss reads as `pure` -- fail safe to the least-corrupted reading rather than guessing.
"""

from __future__ import annotations

import uuid

from ..models.corruption import CorruptionTier


class CorruptionTierCache:
    """Module-level singleton (mirrors `lucidity_tier_cache`) -- callers MUST share this instance."""

    def __init__(self) -> None:
        self._tiers: dict[str, CorruptionTier] = {}

    def set_tier(self, player_id: uuid.UUID | str, tier: CorruptionTier) -> None:
        """Record this player's current tier."""
        self._tiers[str(player_id)] = tier

    def get_tier(self, player_id: uuid.UUID | str) -> CorruptionTier:
        """Return the cached tier, or `pure` if this player has never been recorded."""
        return self._tiers.get(str(player_id), CorruptionTier.PURE)

    def clear(self, player_id: uuid.UUID | str) -> None:
        """Drop a player's cached tier (e.g. on disconnect)."""
        _ = self._tiers.pop(str(player_id), None)


corruption_tier_cache = CorruptionTierCache()

__all__ = ["CorruptionTierCache", "corruption_tier_cache"]
