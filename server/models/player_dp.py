"""
Determination points (DP) rules, as pure functions of a player's stats (ADR-029 step 6a).

Each rule returns a DpChange: the stats keys to set and what crossed a threshold. The ORM Player and the player
registry's PlayerHealthService both apply them, so damage, healing, decay and combat sync follow one set of rules
whichever side holds the player. ``DpAdjusting`` is the service as the persistence layer sees it (it is injected at
startup, like the corruption service, and cannot be imported there without a cycle).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Protocol

from ..utils.int_coercion import coerce_int
from .game import PositionState

DEAD_DP = -10  # at or below this a player is dead (mortally wounded between 0 and here)


@dataclass(frozen=True, slots=True)
class DpChange:
    """One DP change: the stats keys to write, and the thresholds it crossed."""

    old_dp: int
    new_dp: int
    max_dp: int
    changes: Mapping[str, object] = field(default_factory=dict[str, object])
    became_mortally_wounded: bool = False
    became_dead: bool = False


class DpAdjusting(Protocol):
    """Damage and healing as the persistence layer delegates them (PlayerHealthService)."""

    async def damage(self, player_id: uuid.UUID, amount: int, damage_type: str = "physical") -> DpChange:
        """Apply damage after resistances, never below 0 DP."""
        ...

    async def heal(self, player_id: uuid.UUID, amount: int) -> DpChange:
        """Heal, never above max DP."""
        ...


def dp_of(stats: Mapping[str, object], default: int = 0) -> int:
    """The player's current DP."""
    return coerce_int(stats.get("current_dp", default), default=default)


def max_dp_of(stats: Mapping[str, object]) -> int:
    """Max DP: the stored value, else (CON + SIZ) / 5; never 0 (callers divide by it)."""
    from_body = coerce_int(stats.get("constitution", 50), default=50) + coerce_int(stats.get("size", 50), default=50)
    return coerce_int(stats.get("max_dp", from_body // 5), default=from_body // 5) or 20


def effective_damage(stats: Mapping[str, object], amount: int, damage_type: str) -> int:
    """Damage after resistances: cold and water damage are cut by ``cold_resistance`` percent, to at least 1."""
    if amount <= 0:
        return 0
    if damage_type not in {"cold", "water"}:
        return amount
    resist = max(0, min(100, coerce_int(stats.get("cold_resistance", 0), default=0)))
    if not resist:
        return amount
    return max(1, int(round(amount * (1.0 - resist / 100.0))))


def damaged(stats: Mapping[str, object], amount: int, damage_type: str = "physical") -> DpChange:
    """Damage that never goes below 0 DP (status effects, mechanics); the posture is left alone."""
    old = dp_of(stats, 20)
    new = max(0, old - effective_damage(stats, amount, damage_type))
    return DpChange(old, new, max_dp_of(stats), {"current_dp": new})


def healed(stats: Mapping[str, object], amount: int) -> DpChange:
    """Healing, capped at max DP; the posture is left alone."""
    old = dp_of(stats, 100)
    top = max_dp_of(stats)
    new = min(top, old + max(0, amount))
    return DpChange(old, new, top, {"current_dp": new})


def set_to(stats: Mapping[str, object], new_dp: int) -> DpChange:
    """An absolute DP (combat sync, admin set): lying at 0 or below, standing again when revived."""
    old = dp_of(stats)
    changes: dict[str, object] = {"current_dp": new_dp}
    if new_dp <= 0:
        changes["position"] = PositionState.LYING
    elif old <= 0:
        changes["position"] = PositionState.STANDING
    return DpChange(
        old,
        new_dp,
        max_dp_of(stats),
        changes,
        became_mortally_wounded=old > 0 >= new_dp > DEAD_DP,
        became_dead=new_dp <= DEAD_DP < old,
    )


def decayed(stats: Mapping[str, object], amount: int = 1) -> DpChange:
    """Bleeding while mortally wounded: down by ``amount`` to at most -10, lying at 0 or below."""
    old = dp_of(stats)
    new = max(old - amount, DEAD_DP)
    changes: dict[str, object] = {"current_dp": new}
    if new <= 0 and stats.get("position") != PositionState.LYING:
        changes["position"] = PositionState.LYING
    return DpChange(old, new, max_dp_of(stats), changes, became_dead=new <= DEAD_DP < old)


def restored(stats: Mapping[str, object]) -> DpChange:
    """Respawn: full DP (the stored max, else 100) and standing."""
    top = coerce_int(stats.get("max_dp", 100), default=100)
    return DpChange(dp_of(stats), top, top, {"current_dp": top, "position": PositionState.STANDING})
