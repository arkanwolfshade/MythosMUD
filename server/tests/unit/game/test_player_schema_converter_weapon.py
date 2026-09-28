"""Unit tests for PlayerSchemaConverter weapon stats enrichment."""

import uuid
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest

from server.game.items.prototype_registry import PrototypeRegistryError
from server.game.player_schema_converter import (
    PlayerSchemaConverter,
    _inventory_item_with_weapon,
    _weapon_from_prototype_registry,
)
from server.models.game import InventoryItem
from server.schemas.game.weapon import WeaponStats, weapon_stats_from_metadata
from server.tests.fixtures.shared.weapon_metadata import SLING_PROTOTYPE_WEAPON


def test_weapon_from_prototype_registry_none_registry_returns_none() -> None:
    """When registry is None, returns None."""
    assert _weapon_from_prototype_registry(None, "weapon.main_hand.switchblade") is None


def test_weapon_from_prototype_registry_empty_prototype_id_returns_none() -> None:
    """When prototype_id is empty, returns None."""
    registry = MagicMock()
    assert _weapon_from_prototype_registry(registry, "") is None


def test_weapon_from_prototype_registry_missing_prototype_returns_none() -> None:
    """When prototype is not found, returns None."""
    registry = MagicMock()
    registry.get.side_effect = PrototypeRegistryError("Prototype not found: missing")
    assert _weapon_from_prototype_registry(registry, "missing") is None


def test_weapon_from_prototype_registry_no_metadata_returns_none() -> None:
    """When prototype has no metadata.weapon, returns None."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.metadata = {}
    registry.get.return_value = prototype
    assert _weapon_from_prototype_registry(registry, "weapon.main_hand.switchblade") is None


def test_weapon_from_prototype_registry_weapon_present_returns_dict() -> None:
    """When prototype has metadata.weapon, returns weapon dict."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.metadata = {
        "weapon": {
            "min_damage": 1,
            "max_damage": 4,
            "modifier": 0,
            "damage_types": ["slashing", "piercing"],
            "magical": False,
        }
    }
    registry.get.return_value = prototype
    result = _weapon_from_prototype_registry(registry, "weapon.main_hand.switchblade")
    assert result is not None
    assert result.min_damage == 1
    assert result.max_damage == 4
    assert result.damage_types == ["slashing", "piercing"]


class _StubRegistry:
    """Typed stand-in for the prototype registry; only ``get`` and ``metadata`` are read.

    A MagicMock works here too, but reading ``registry.get`` off one yields ``Any`` and
    trips reportAny (see .claude/rules/basedpyright.md).
    """

    class _Prototype:
        def __init__(self, weapon: dict[str, object]) -> None:
            self.metadata: dict[str, object] = {"weapon": weapon}

    def __init__(self, weapon: dict[str, object]) -> None:
        self._prototype: _StubRegistry._Prototype = _StubRegistry._Prototype(weapon)

    def get(self, prototype_id: str) -> _Prototype:
        """Return the single stub prototype regardless of the id requested."""
        _ = prototype_id
        return self._prototype


def test_weapon_stats_from_metadata_drops_unmodelled_prototype_keys() -> None:
    """The rich ADR-026 metadata keys are projected away, not rejected by extra='forbid'."""
    result = weapon_stats_from_metadata(SLING_PROTOTYPE_WEAPON)
    assert result.min_damage == 1
    assert result.max_damage == 4
    assert result.damage_types == ["bludgeoning"]
    assert not hasattr(result, "damage_expr")


def test_weapon_from_prototype_registry_parses_real_catalog_shape() -> None:
    """Regression: the full prototype metadata.weapon dict must not fail validation.

    WeaponStats sets extra='forbid' and models only five keys, so passing a whole
    metadata.weapon dict used to raise ValidationError for every weapon in the catalog --
    weapon stats never reached the client and each conversion logged a warning. The older
    tests here all passed pre-trimmed dicts, which is why this went unnoticed.
    """
    registry = _StubRegistry(dict(SLING_PROTOTYPE_WEAPON))

    result = _weapon_from_prototype_registry(registry, "pack_dark_ages.weapon.sling")

    assert result is not None, "full catalog weapon metadata must resolve to WeaponStats"
    assert result.min_damage == 1
    assert result.max_damage == 4
    assert result.damage_types == ["bludgeoning"]


def test_weapon_from_prototype_registry_still_returns_none_on_bad_modelled_keys() -> None:
    """Projection must not paper over a genuinely invalid modelled value."""
    registry = _StubRegistry({**SLING_PROTOTYPE_WEAPON, "min_damage": -5})

    assert _weapon_from_prototype_registry(registry, "pack_dark_ages.weapon.sling") is None


def test_inventory_item_with_weapon_minimal_dict() -> None:
    """Build InventoryItem from minimal dict (item_id, quantity) without registry."""
    item = {"item_id": "potion_001", "quantity": 2}
    result = _inventory_item_with_weapon(item, None)
    assert isinstance(result, InventoryItem)
    assert result.item_id == "potion_001"
    assert result.quantity == 2
    assert result.weapon is None


def test_inventory_item_with_weapon_with_registry_weapon() -> None:
    """Build InventoryItem with weapon stats when prototype has metadata.weapon."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.metadata = {"weapon": {"min_damage": 1, "max_damage": 4, "damage_types": ["slashing"]}}
    registry.get.return_value = prototype

    item = {"item_id": "weapon.main_hand.switchblade", "prototype_id": "weapon.main_hand.switchblade", "quantity": 1}
    result = _inventory_item_with_weapon(item, registry)
    assert isinstance(result, InventoryItem)
    assert result.item_id == "weapon.main_hand.switchblade"
    assert result.quantity == 1
    assert result.weapon is not None
    assert isinstance(result.weapon, WeaponStats)
    # Pylint incorrectly infers result.weapon as FieldInfo instead of WeaponStats after isinstance check
    # Runtime isinstance check ensures type safety, suppress Pylint false positive
    weapon = result.weapon  # pylint: disable=no-member
    assert weapon.min_damage == 1  # pylint: disable=no-member
    assert weapon.max_damage == 4  # pylint: disable=no-member


def test_inventory_item_with_weapon_uses_prototype_id_for_lookup() -> None:
    """When both item_id and prototype_id present, use prototype_id for registry lookup."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.metadata = {"weapon": {"min_damage": 2, "max_damage": 2}}
    registry.get.return_value = prototype

    item = {"item_id": "inst_123", "prototype_id": "weapon.main_hand.switchblade", "quantity": 1}
    result = _inventory_item_with_weapon(item, registry)
    assert result.item_id == "inst_123"
    assert result.weapon is not None
    registry.get.assert_called_once_with("weapon.main_hand.switchblade")


@pytest.mark.asyncio
async def test_create_player_read_from_object_enriches_inventory_weapon() -> None:
    """When converter has registry, inventory items with weapon prototype get weapon field."""
    persistence = MagicMock()
    registry = MagicMock()
    prototype = MagicMock()
    prototype.metadata = {"weapon": {"min_damage": 1, "max_damage": 4, "damage_types": ["slashing"]}}
    registry.get.return_value = prototype

    converter = PlayerSchemaConverter(persistence, item_prototype_registry=registry)
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    now = datetime.now(UTC).replace(tzinfo=None)
    player = MagicMock()
    player.player_id = player_id
    player.user_id = user_id
    player.name = "Test"
    player.current_room_id = "room_001"
    player.experience_points = 0
    player.level = 1
    player.created_at = now
    player.last_active = now
    player.is_admin = False
    player.get_stats = lambda: {"position": "standing", "constitution": 50, "size": 50, "power": 50, "education": 50}
    player.get_inventory = lambda: [
        {"item_id": "weapon.main_hand.switchblade", "prototype_id": "weapon.main_hand.switchblade", "quantity": 1}
    ]
    player.get_status_effects = lambda: []

    persistence.get_profession_by_id = MagicMock(return_value=None)

    result = await converter.create_player_read_from_object(
        player, in_combat=False, profession_data=(0, None, None, None)
    )
    assert len(result.inventory) == 1
    assert result.inventory[0].weapon is not None
    assert isinstance(result.inventory[0].weapon, WeaponStats)
    # Pylint incorrectly infers result.inventory[0].weapon as FieldInfo instead of WeaponStats after isinstance check
    # Runtime isinstance check ensures type safety, suppress Pylint false positive
    weapon = result.inventory[0].weapon  # pylint: disable=no-member
    assert weapon.min_damage == 1  # pylint: disable=no-member
    assert weapon.max_damage == 4  # pylint: disable=no-member
