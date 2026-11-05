"""
Magic point (MP) rules, as pure functions of a player's stats (ADR-029 step 6b).

Each rule returns an MpChange; PlayerMpService writes it through the player registry.
"""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass

from ..utils.int_coercion import coerce_int


@dataclass(frozen=True, slots=True)
class MpChange:
    """One MP change."""

    old_mp: int
    new_mp: int
    max_mp: int

    @property
    def gained(self) -> int:
        """MP gained by this change (negative for a spend)."""
        return self.new_mp - self.old_mp


def mp_of(stats: Mapping[str, object]) -> int:
    """The player's current MP."""
    return coerce_int(stats.get("magic_points", 0), default=0)


def max_mp_of(stats: Mapping[str, object]) -> int:
    """Max MP: the stored value, else ceil(POW * 0.2)."""
    if "max_magic_points" in stats:
        return coerce_int(stats["max_magic_points"], default=10)
    return math.ceil(coerce_int(stats.get("power", 50), default=50) * 0.2)


def after_spending(stats: Mapping[str, object], cost: int) -> MpChange:
    """Pay ``cost``, never below 0 MP."""
    old = mp_of(stats)
    return MpChange(old, max(0, old - cost), max_mp_of(stats))


def after_gaining(stats: Mapping[str, object], amount: float) -> MpChange:
    """Gain ``amount`` (whole MP are kept), capped at max MP; MP an admin set above the max is left alone."""
    old, top = mp_of(stats), max_mp_of(stats)
    return MpChange(old, old if old >= top else int(min(top, old + amount)), top)


def set_to(stats: Mapping[str, object], new_mp: int) -> MpChange:
    """An absolute MP (admin set), which may exceed the max."""
    return MpChange(mp_of(stats), new_mp, max_mp_of(stats))
