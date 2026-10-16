"""
What a player carries that belongs only to an instance, and how to clear it.

Two kinds of player state are tied to one instance and must not outlive it:

* items flagged INSTANCE_BOUND (see game.items.instance_bound), in the inventory, equipped, or inside a
  carried container;
* status effects marked ``"instance_scoped": true``.

When a player's instance has been lost (logout, restart) and they are given a fresh one, whatever
the old one handed them is cleared so the new run starts clean.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from .items.instance_bound import strip_instance_bound_stacks

if TYPE_CHECKING:
    from ..models.player import Player

# Status effects carrying this key set to true are removed by reset_instance_scoped_state.
INSTANCE_SCOPED_EFFECT_KEY = "instance_scoped"


def strip_instance_bound_items(player: Player) -> int:
    """Remove INSTANCE_BOUND items from the player's inventory and equipment; returns how many were removed."""
    inventory, inventory_removed = strip_instance_bound_stacks(player.get_inventory())
    equipped = player.get_equipped_items()
    slots = [(slot, cast(dict[str, object], stack)) for slot, stack in equipped.items() if isinstance(stack, dict)]
    kept_equipped: dict[str, dict[str, object]] = {}
    equipped_removed = 0
    for slot, stack in slots:
        kept, removed = strip_instance_bound_stacks([stack])
        equipped_removed += removed
        if kept:
            kept_equipped[slot] = kept[0]
    if inventory_removed:
        player.set_inventory(inventory)
    if equipped_removed:
        player.set_equipped_items(kept_equipped)
    return inventory_removed + equipped_removed


def strip_instance_scoped_effects(player: Player) -> int:
    """Remove status effects marked instance_scoped; returns how many were removed."""
    effects = player.get_status_effects()
    kept = [effect for effect in effects if effect.get(INSTANCE_SCOPED_EFFECT_KEY) is not True]
    if len(kept) != len(effects):
        player.set_status_effects(kept)
    return len(effects) - len(kept)


def reset_instance_scoped_state(player: Player) -> int:
    """Clear everything tied to the player's old instance; returns how many items and effects were removed."""
    return strip_instance_bound_items(player) + strip_instance_scoped_effects(player)
