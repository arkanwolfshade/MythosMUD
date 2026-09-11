"""Data models for passive corruption flux (#815 PR-5)."""

from __future__ import annotations

from dataclasses import dataclass, field

# CachedRoom is identical in shape and purpose to passive_lucidity_flux's -- a plain (room,
# timestamp) pair for TTL bookkeeping, with nothing lucidity-specific in it. Re-exported here so
# this package's public surface doesn't leak an import from a sibling flux package.
from ..passive_lucidity_flux.models import CachedRoom

__all__ = ["CachedRoom", "PassiveCorruptionFluxContext"]


@dataclass(frozen=True)
class PassiveCorruptionFluxContext:
    """
    Resolved environmental context for one player's passive corruption flux evaluation.

    Unlike lucidity's PassiveFluxContext (a signed flux value only), corruption flux converges
    toward a `target` at a given `rate` (magnitude, direction derived from current-vs-target) --
    see server/services/passive_corruption_flux/service.py for why a room can't just supply a
    signed rate the way a lucidity drain/recovery zone does.
    """

    target: float
    rate: float
    tags: frozenset[str] = field(default_factory=frozenset)
    source: str = "unspecified"
    metadata: dict[str, object] = field(default_factory=dict)
