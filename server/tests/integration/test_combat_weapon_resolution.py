"""
Integration tests for combat weapon resolution.

Verifies that the switchblade prototype metadata and resolve_weapon_attack_from_equipped
produce damage in the expected range (1d4+0) and correct damage_type.
"""

import pytest

from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.game.weapons import WeaponAttackInfo, resolve_weapon_attack_from_equipped

# Switchblade metadata matching data/db/migrations/07_add_switchblade_weapon.sql
SWITCHBLADE_WEAPON_METADATA = {
    "weapon": {
        "min_damage": 1,
        "max_damage": 4,
        "modifier": 0,
        "damage_types": ["slashing", "piercing"],
        "magical": False,
    }
}


@pytest.fixture
def switchblade_prototype():
    """Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade)."""
    return ItemPrototypeModel(
        prototype_id="weapon.main_hand.switchblade",
        name="Switchblade Knife",
        short_description="a folding blade with a sprung mechanism",
        long_description="A compact switchblade.",
        item_type="weapon",
        weight=0.2,
        base_value=80,
        durability=40,
        flags=[],
        wear_slots=["main_hand"],
        usage_restrictions={},
        stacking_rules={"max_stack": 1},
        effect_components=[],
        metadata=SWITCHBLADE_WEAPON_METADATA,
        tags=["weapon", "main_hand", "melee"],
    )


@pytest.fixture
def registry_with_switchblade(switchblade_prototype):
    """PrototypeRegistry containing only the switchblade."""
    return PrototypeRegistry(
        prototypes={switchblade_prototype.prototype_id: switchblade_prototype},
        invalid_entries=[],
    )


def test_weapon_resolution_switchblade_damage_in_range(registry_with_switchblade):
    """With switchblade equipped, resolved damage is in [1, 4] and damage_type is slashing."""
    stack = {"prototype_id": "weapon.main_hand.switchblade", "item_name": "Switchblade Knife"}
    for _ in range(30):
        info = resolve_weapon_attack_from_equipped(stack, registry_with_switchblade)
        assert info is not None
        assert isinstance(info, WeaponAttackInfo)
        assert 1 <= info.base_damage <= 4
        assert info.damage_type == "slashing"


def test_weapon_resolution_switchblade_no_main_hand_returns_none(registry_with_switchblade):
    """When main_hand is empty, resolve returns None."""
    assert resolve_weapon_attack_from_equipped(None, registry_with_switchblade) is None
