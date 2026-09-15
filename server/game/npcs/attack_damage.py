"""Resolve NPC outgoing attack damage from base_stats / behavior (ADR-027 Phase 3)."""

from __future__ import annotations

import random
from collections.abc import Mapping
from typing import cast

from server.game.dice_expr import roll_damage_expr


def _legacy_behavior_damage(behavior_config: Mapping[str, object] | None) -> int | None:
    if behavior_config is None:
        return None
    raw = behavior_config.get("attack_damage")
    if isinstance(raw, bool):
        return 1 if raw else 0
    if isinstance(raw, int | float):
        return int(raw)
    if isinstance(raw, str) and raw.isdigit():
        return int(raw)
    return None


def _first_attack(base_stats: Mapping[str, object]) -> Mapping[str, object] | None:
    attacks_raw = base_stats.get("attacks")
    if not isinstance(attacks_raw, list) or not attacks_raw:
        return None
    first = cast(list[object], attacks_raw)[0]
    if isinstance(first, dict):
        return cast(Mapping[str, object], first)
    return None


def _roll_int_bounds(lo: int, hi: int, *, rng: random.Random | None) -> int:
    low = min(lo, hi)
    high = max(lo, hi)
    if rng is None:
        return random.randint(low, high)  # nosec B311  # game damage roll, not crypto
    return rng.randint(low, high)


def _damage_from_attack(attack: Mapping[str, object], *, rng: random.Random | None) -> int | None:
    """Return damage from one attack entry, or None if it has no usable fields."""
    expr = attack.get("damage_expr")
    if isinstance(expr, str) and expr.strip():
        try:
            return max(0, roll_damage_expr(expr, rng=rng))
        except ValueError:
            pass
    lo = attack.get("min_damage")
    hi = attack.get("max_damage")
    if isinstance(lo, int) and isinstance(hi, int):
        return max(0, _roll_int_bounds(lo, hi, rng=rng))
    if isinstance(lo, int):
        return max(0, lo)
    return None


def resolve_npc_attack_damage(
    base_stats: Mapping[str, object] | None,
    behavior_config: Mapping[str, object] | None = None,
    *,
    rng: random.Random | None = None,
    fallback: int = 1,
) -> int:
    """Roll NPC damage: damage_expr if present, else min/max ints, else behavior, else fallback."""
    stats = base_stats or {}
    attack = _first_attack(stats)
    if attack is not None:
        rolled = _damage_from_attack(attack, rng=rng)
        if rolled is not None:
            return rolled

    legacy = _legacy_behavior_damage(behavior_config)
    if legacy is not None:
        return max(0, legacy)
    return max(0, fallback)


def armor_points_from_base_stats(base_stats: Mapping[str, object] | None) -> int:
    """Return armor_points from nested base_stats.armor, or 0."""
    if base_stats is None:
        return 0
    armor_raw = base_stats.get("armor")
    if not isinstance(armor_raw, dict):
        return 0
    points = cast(dict[str, object], armor_raw).get("armor_points")
    if isinstance(points, int) and points >= 0:
        return points
    return 0
