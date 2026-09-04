"""Weapon resolution helpers for combat.

Resolves equipped main-hand items to weapon attack info (base damage roll,
damage type) using item prototype metadata. Used by player auto-attack and
future combat command flows.
"""

from __future__ import annotations

import random
from typing import NamedTuple

from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class WeaponAttackInfo(NamedTuple):
    """Result of resolving an equipped item to a weapon attack.

    base_damage: Rolled weapon damage (min_damage..max_damage + modifier).
    damage_type: Primary damage type from weapon metadata, or "physical" if none.
    """

    base_damage: int
    damage_type: str


def _weapon_damage_bounds(weapon: dict[str, object]) -> tuple[int, int] | None:
    min_damage = weapon.get("min_damage")
    max_damage = weapon.get("max_damage")
    if min_damage is None or max_damage is None:
        return None
    if isinstance(min_damage, int | float) and isinstance(max_damage, int | float):
        return int(min_damage), int(max_damage)
    return None


def _roll_weapon_attack(weapon: dict[str, object], min_d: int, max_d: int) -> WeaponAttackInfo:
    mod_raw = weapon.get("modifier", 0)
    try:
        mod = int(mod_raw) if isinstance(mod_raw, int | float | str) else 0
    except (TypeError, ValueError):
        mod = 0
    base_damage = random.randint(min_d, max_d) + mod  # nosec B311  # game damage roll, not crypto
    damage_types = weapon.get("damage_types")
    if isinstance(damage_types, list) and damage_types and isinstance(damage_types[0], str):
        damage_type = damage_types[0]
    else:
        damage_type = "physical"
    return WeaponAttackInfo(base_damage=base_damage, damage_type=damage_type)


def _prototype_from_equipped_stack(
    main_hand_stack: dict[str, object],
    registry: PrototypeRegistry,
) -> ItemPrototypeModel | None:
    prototype_id_raw = main_hand_stack.get("prototype_id") or main_hand_stack.get("item_id")
    if not isinstance(prototype_id_raw, str) or not prototype_id_raw:
        return None
    try:
        prototype = registry.get(prototype_id_raw)
    except PrototypeRegistryError:
        return None
    if not prototype or not prototype.metadata:
        return None
    return prototype


def resolve_weapon_attack_from_equipped(
    main_hand_stack: dict[str, object] | None,
    registry: PrototypeRegistry | None,
) -> WeaponAttackInfo | None:
    """Resolve equipped main-hand stack to weapon attack info, or None if unarmed."""
    if not main_hand_stack or not registry or not isinstance(main_hand_stack, dict):
        return None
    prototype = _prototype_from_equipped_stack(main_hand_stack, registry)
    if prototype is None:
        return None
    weapon_raw: object = prototype.metadata.get("weapon")
    if not isinstance(weapon_raw, dict):
        return None
    weapon: dict[str, object] = dict(weapon_raw)
    bounds = _weapon_damage_bounds(weapon)
    if bounds is None:
        return None
    return _roll_weapon_attack(weapon, bounds[0], bounds[1])
