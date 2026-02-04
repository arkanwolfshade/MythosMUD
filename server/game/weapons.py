"""Weapon resolution helpers for combat.

Resolves equipped main-hand items to weapon attack info (base damage roll,
damage type) using item prototype metadata. Used by player auto-attack and
future combat command flows.
"""

from __future__ import annotations

import random
from typing import Any, NamedTuple

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


def resolve_weapon_attack_from_equipped(  # pylint: disable=too-many-nested-blocks  # Reason: Weapon metadata validation and roll logic is sequential; flattening would obscure intent
    main_hand_stack: dict[str, Any] | None,
    registry: PrototypeRegistry | None,
) -> WeaponAttackInfo | None:
    """Resolve equipped main-hand stack to weapon attack info, or indicate non-weapon.

    If the equipped item has metadata.weapon with min_damage and max_damage,
    rolls base damage and returns WeaponAttackInfo. Otherwise returns None
    (caller should use basic_unarmed_damage).

    Args:
        main_hand_stack: Equipped stack for main_hand slot (e.g. from get_equipped_items()).
        registry: Item prototype registry to look up the item prototype.

    Returns:
        WeaponAttackInfo with rolled base_damage and damage_type, or None if not a weapon.
    """
    result: WeaponAttackInfo | None = None
    if main_hand_stack and registry and isinstance(main_hand_stack, dict):
        prototype_id = main_hand_stack.get("prototype_id") or main_hand_stack.get("item_id")
        if prototype_id:
            try:
                prototype = registry.get(prototype_id)
            except PrototypeRegistryError:
                prototype = None
            if prototype and prototype.metadata:
                weapon = prototype.metadata.get("weapon")
                if isinstance(weapon, dict):
                    min_damage = weapon.get("min_damage")
                    max_damage = weapon.get("max_damage")
                    if min_damage is not None and max_damage is not None:
                        min_d: int | None = None
                        max_d: int | None = None
                        try:
                            min_d = int(min_damage)
                            max_d = int(max_damage)
                        except (TypeError, ValueError):
                            min_d = max_d = None
                        if min_d is not None and max_d is not None:
                            try:
                                mod = int(weapon.get("modifier", 0))
                            except (TypeError, ValueError):
                                mod = 0
                            base_damage = random.randint(min_d, max_d) + mod
                            damage_types = weapon.get("damage_types")
                            if isinstance(damage_types, list) and damage_types and isinstance(damage_types[0], str):
                                damage_type = damage_types[0]
                            else:
                                damage_type = "physical"
                            result = WeaponAttackInfo(base_damage=base_damage, damage_type=damage_type)
    return result
