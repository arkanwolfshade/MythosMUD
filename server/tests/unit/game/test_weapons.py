"""Unit tests for weapon resolution helpers."""

from unittest.mock import MagicMock

from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from server.game.weapons import WeaponAttackInfo, resolve_weapon_attack_from_equipped


def test_resolve_weapon_attack_from_equipped_none_stack_returns_none() -> None:
    """When main_hand_stack is None, returns None."""
    registry = MagicMock(spec=PrototypeRegistry)
    assert resolve_weapon_attack_from_equipped(None, registry) is None


def test_resolve_weapon_attack_from_equipped_none_registry_returns_none() -> None:
    """When registry is None, returns None."""
    stack = {"prototype_id": "weapon.main_hand.switchblade"}
    assert resolve_weapon_attack_from_equipped(stack, None) is None


def test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none() -> None:
    """When stack has no prototype_id, returns None."""
    registry = MagicMock(spec=PrototypeRegistry)
    stack = {"item_name": "switchblade"}
    assert resolve_weapon_attack_from_equipped(stack, registry) is None


def test_resolve_weapon_attack_from_equipped_registry_error_returns_none() -> None:
    """When registry.get raises PrototypeRegistryError, returns None."""
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.side_effect = PrototypeRegistryError("not found")
    stack = {"prototype_id": "weapon.main_hand.switchblade"}
    assert resolve_weapon_attack_from_equipped(stack, registry) is None


def test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none() -> None:
    """When prototype has no metadata.weapon, returns None."""
    prototype = MagicMock(spec=ItemPrototypeModel)
    prototype.metadata = {}
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.return_value = prototype
    stack = {"prototype_id": "equipment.main_hand.tonfa"}
    assert resolve_weapon_attack_from_equipped(stack, registry) is None


def test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none() -> None:
    """When metadata.weapon has no min_damage or max_damage, returns None."""
    prototype = MagicMock(spec=ItemPrototypeModel)
    prototype.metadata = {"weapon": {"damage_types": ["slashing"], "modifier": 0}}
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.return_value = prototype
    stack = {"prototype_id": "weapon.main_hand.broken"}
    assert resolve_weapon_attack_from_equipped(stack, registry) is None


def test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range() -> None:
    """When prototype has valid weapon metadata, returns WeaponAttackInfo with damage in [min, max]+modifier."""
    prototype = MagicMock(spec=ItemPrototypeModel)
    prototype.metadata = {
        "weapon": {
            "min_damage": 1,
            "max_damage": 4,
            "modifier": 0,
            "damage_types": ["slashing", "piercing"],
            "magical": False,
        }
    }
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.return_value = prototype
    stack = {"prototype_id": "weapon.main_hand.switchblade"}

    results: list[WeaponAttackInfo] = []
    for _ in range(50):
        info = resolve_weapon_attack_from_equipped(stack, registry)
        assert info is not None
        results.append(info)

    for info in results:
        assert 1 <= info.base_damage <= 4
        assert info.damage_type == "slashing"


def test_resolve_weapon_attack_from_equipped_weapon_with_modifier() -> None:
    """When weapon has modifier, base_damage includes modifier."""
    prototype = MagicMock(spec=ItemPrototypeModel)
    prototype.metadata = {"weapon": {"min_damage": 2, "max_damage": 2, "modifier": 3, "damage_types": ["physical"]}}
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.return_value = prototype
    stack = {"prototype_id": "weapon.main_hand.test"}
    info = resolve_weapon_attack_from_equipped(stack, registry)
    assert info is not None
    assert info.base_damage == 5  # 2 + 3
    assert info.damage_type == "physical"


def test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical() -> None:
    """When damage_types is empty or missing, damage_type is 'physical'."""
    prototype = MagicMock(spec=ItemPrototypeModel)
    prototype.metadata = {"weapon": {"min_damage": 1, "max_damage": 1, "modifier": 0}}
    registry = MagicMock(spec=PrototypeRegistry)
    registry.get.return_value = prototype
    stack = {"prototype_id": "weapon.main_hand.test"}
    info = resolve_weapon_attack_from_equipped(stack, registry)
    assert info is not None
    assert info.damage_type == "physical"
