"""
Tests for models.py - Pydantic models for game data.

This module tests all the Pydantic models defined in models.py including
Player, Stats, StatusEffect, Alias, Item, InventoryItem, and NPC models.
"""

import pytest
from datetime import UTC, datetime
from typing import Any

import importlib.util
import os

# Import models.py directly to avoid package conflicts
spec = importlib.util.spec_from_file_location(
    "models_module", 
    os.path.join(os.path.dirname(__file__), "..", "models.py")
)
models_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(models_module)

Player = models_module.Player
Stats = models_module.Stats
StatusEffect = models_module.StatusEffect
StatusEffectType = models_module.StatusEffectType
Alias = models_module.Alias
Item = models_module.Item
InventoryItem = models_module.InventoryItem
NPC = models_module.NPC
AttributeType = models_module.AttributeType


class TestStats:
    """Test the Stats model."""

    def test_stats_default_values(self):
        """Test that Stats has correct default values."""
        stats = Stats()
        
        assert stats.strength == 10
        assert stats.dexterity == 10
        assert stats.constitution == 10
        assert stats.intelligence == 10
        assert stats.wisdom == 10
        assert stats.charisma == 10
        assert stats.sanity == 100
        assert stats.occult_knowledge == 0
        assert stats.fear == 0
        assert stats.corruption == 0
        assert stats.cult_affiliation == 0
        assert stats.current_health == 100

    def test_stats_custom_values(self):
        """Test that Stats can be created with custom values."""
        stats = Stats(
            strength=15,
            dexterity=12,
            constitution=14,
            intelligence=16,
            wisdom=13,
            charisma=11,
            sanity=85,
            occult_knowledge=25,
            fear=15,
            corruption=5,
            cult_affiliation=10,
            current_health=95,
        )
        
        assert stats.strength == 15
        assert stats.dexterity == 12
        assert stats.constitution == 14
        assert stats.intelligence == 16
        assert stats.wisdom == 13
        assert stats.charisma == 11
        assert stats.sanity == 85
        assert stats.occult_knowledge == 25
        assert stats.fear == 15
        assert stats.corruption == 5
        assert stats.cult_affiliation == 10
        assert stats.current_health == 95

    def test_stats_max_health_property(self):
        """Test the max_health computed property."""
        stats = Stats(constitution=15)
        assert stats.max_health == 150  # 10 * constitution

    def test_stats_max_sanity_property(self):
        """Test the max_sanity computed property."""
        stats = Stats(wisdom=18)
        assert stats.max_sanity == 90  # 5 * wisdom

    def test_stats_get_attribute_modifier(self):
        """Test the get_attribute_modifier method."""
        stats = Stats(strength=15, dexterity=8, intelligence=12)
        
        assert stats.get_attribute_modifier(AttributeType.STR) == 2  # (15-10)/2
        assert stats.get_attribute_modifier(AttributeType.DEX) == -1  # (8-10)/2
        assert stats.get_attribute_modifier(AttributeType.INT) == 1  # (12-10)/2

    def test_stats_is_sane(self):
        """Test the is_sane method."""
        stats = Stats(sanity=100)
        assert stats.is_sane() is True
        
        stats = Stats(sanity=50)
        assert stats.is_sane() is True
        
        stats = Stats(sanity=0)
        assert stats.is_sane() is False

    def test_stats_is_corrupted(self):
        """Test the is_corrupted method."""
        stats = Stats(corruption=0)
        assert stats.is_corrupted() is False
        
        stats = Stats(corruption=50)
        assert stats.is_corrupted() is True

    def test_stats_is_insane(self):
        """Test the is_insane method."""
        stats = Stats(sanity=100)
        assert stats.is_insane() is False
        
        stats = Stats(sanity=0)
        assert stats.is_insane() is True


class TestStatusEffect:
    """Test the StatusEffect model."""

    def test_status_effect_creation(self):
        """Test creating a StatusEffect."""
        effect = StatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5,
            source="poison dart"
        )
        
        assert effect.effect_type == StatusEffectType.POISONED
        assert effect.duration == 10
        assert effect.intensity == 5
        assert effect.source == "poison dart"
        assert isinstance(effect.applied_at, datetime)

    def test_status_effect_is_active(self):
        """Test the is_active method."""
        effect = StatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5
        )
        
        # Should be active at tick 5
        assert effect.is_active(5) is True
        
        # Should not be active at tick 15
        assert effect.is_active(15) is False

    def test_status_effect_permanent(self):
        """Test permanent status effects (duration=0)."""
        effect = StatusEffect(
            effect_type=StatusEffectType.CORRUPTED,
            duration=0,  # Permanent
            intensity=8
        )
        
        # Should always be active
        assert effect.is_active(0) is True
        assert effect.is_active(100) is True
        assert effect.is_active(1000) is True


class TestAlias:
    """Test the Alias model."""

    def test_alias_creation(self):
        """Test creating an Alias."""
        alias = Alias(
            name="n",
            command="go north"
        )
        
        assert alias.name == "n"
        assert alias.command == "go north"
        assert alias.version == "1.0"
        assert isinstance(alias.created_at, datetime)
        assert isinstance(alias.updated_at, datetime)

    def test_alias_equality(self):
        """Test alias equality comparison."""
        alias1 = Alias(name="n", command="go north")
        alias2 = Alias(name="n", command="go north")
        alias3 = Alias(name="s", command="go south")
        
        assert alias1 == alias2
        assert alias1 != alias3
        assert alias1 != "not an alias"

    def test_alias_hash(self):
        """Test alias hash method."""
        alias1 = Alias(name="n", command="go north")
        alias2 = Alias(name="n", command="go north")
        
        assert hash(alias1) == hash(alias2)

    def test_alias_update_timestamp(self):
        """Test the update_timestamp method."""
        alias = Alias(name="n", command="go north")
        old_updated_at = alias.updated_at
        
        # Wait a moment to ensure timestamp difference
        import time
        time.sleep(0.001)
        
        alias.update_timestamp()
        assert alias.updated_at > old_updated_at

    def test_alias_is_reserved_command(self):
        """Test the is_reserved_command method."""
        alias1 = Alias(name="n", command="go north")
        alias2 = Alias(name="help", command="help")
        alias3 = Alias(name="alias", command="alias")
        
        assert alias1.is_reserved_command() is False
        assert alias2.is_reserved_command() is True
        assert alias3.is_reserved_command() is True

    def test_alias_validate_name(self):
        """Test the validate_name method."""
        alias1 = Alias(name="n", command="go north")
        alias2 = Alias(name="", command="go north")
        alias3 = Alias(name="very_long_name_that_exceeds_limit", command="go north")
        
        assert alias1.validate_name() is True
        assert alias2.validate_name() is False
        # The current implementation doesn't check length limits
        assert alias3.validate_name() is True

    def test_alias_get_expanded_command(self):
        """Test the get_expanded_command method."""
        alias = Alias(name="n", command="go north")
        
        # Test without args
        assert alias.get_expanded_command() == "go north"
        
        # Test with args - current implementation doesn't append args
        assert alias.get_expanded_command(["fast"]) == "go north"


class TestItem:
    """Test the Item model."""

    def test_item_creation(self):
        """Test creating an Item."""
        item = Item(
            name="Rusty Sword",
            description="A rusty but serviceable sword",
            item_type="weapon",
            weight=5.0,
            value=10
        )
        
        assert item.name == "Rusty Sword"
        assert item.description == "A rusty but serviceable sword"
        assert item.item_type == "weapon"
        assert item.weight == 5.0
        assert item.value == 10
        assert isinstance(item.id, str)

    def test_item_get_property(self):
        """Test the get_property method."""
        item = Item(
            name="Magic Ring",
            description="A ring with magical properties",
            item_type="accessory",
            custom_properties={"magic_power": 5, "durability": 100}
        )
        
        assert item.get_property("magic_power") == 5
        assert item.get_property("durability") == 100
        assert item.get_property("nonexistent", "default") == "default"


class TestInventoryItem:
    """Test the InventoryItem model."""

    def test_inventory_item_creation(self):
        """Test creating an InventoryItem."""
        inv_item = InventoryItem(
            item_id="sword_001",
            quantity=2,
            custom_properties={"condition": "worn"}
        )
        
        assert inv_item.item_id == "sword_001"
        assert inv_item.quantity == 2
        assert inv_item.custom_properties == {"condition": "worn"}

    def test_inventory_item_get_property(self):
        """Test the get_property method."""
        inv_item = InventoryItem(
            item_id="potion_001",
            quantity=1,
            custom_properties={"effect": "healing", "strength": 25}
        )
        
        assert inv_item.get_property("effect") == "healing"
        assert inv_item.get_property("strength") == 25
        assert inv_item.get_property("nonexistent", "default") == "default"


class TestPlayer:
    """Test the Player model."""

    def test_player_creation(self):
        """Test creating a Player."""
        player = Player(
            name="TestPlayer",
            current_room_id="arkham_001"
        )
        
        assert player.name == "TestPlayer"
        assert player.current_room_id == "arkham_001"
        assert player.experience_points == 0
        assert player.level == 1
        assert isinstance(player.id, str)
        assert isinstance(player.stats, Stats)
        assert isinstance(player.inventory, list)
        assert isinstance(player.status_effects, list)

    def test_player_add_item(self):
        """Test the add_item method."""
        player = Player(name="TestPlayer")
        
        # Add new item
        assert player.add_item("sword", 1) is True
        assert len(player.inventory) == 1
        assert player.inventory[0].item_id == "sword"
        assert player.inventory[0].quantity == 1
        
        # Add same item again (should increase quantity)
        assert player.add_item("sword", 2) is True
        assert len(player.inventory) == 1
        assert player.inventory[0].quantity == 3

    def test_player_remove_item(self):
        """Test the remove_item method."""
        player = Player(name="TestPlayer")
        player.add_item("sword", 3)
        
        # Remove some items
        assert player.remove_item("sword", 2) is True
        assert player.inventory[0].quantity == 1
        
        # Remove remaining items
        assert player.remove_item("sword", 1) is True
        assert len(player.inventory) == 0

    def test_player_remove_nonexistent_item(self):
        """Test removing an item that doesn't exist."""
        player = Player(name="TestPlayer")
        
        assert player.remove_item("nonexistent", 1) is False

    def test_player_add_status_effect(self):
        """Test the add_status_effect method."""
        player = Player(name="TestPlayer")
        effect = StatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5
        )
        
        player.add_status_effect(effect)
        assert len(player.status_effects) == 1
        assert player.status_effects[0] == effect

    def test_player_remove_status_effect(self):
        """Test the remove_status_effect method."""
        player = Player(name="TestPlayer")
        effect = StatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5
        )
        
        player.add_status_effect(effect)
        assert player.remove_status_effect(StatusEffectType.POISONED) is True
        assert len(player.status_effects) == 0

    def test_player_remove_nonexistent_status_effect(self):
        """Test removing a status effect that doesn't exist."""
        player = Player(name="TestPlayer")
        
        assert player.remove_status_effect(StatusEffectType.POISONED) is False

    def test_player_get_active_status_effects(self):
        """Test the get_active_status_effects method."""
        player = Player(name="TestPlayer")
        
        # Add active effect
        active_effect = StatusEffect(
            effect_type=StatusEffectType.POISONED,
            duration=10,
            intensity=5
        )
        player.add_status_effect(active_effect)
        
        # Add inactive effect
        inactive_effect = StatusEffect(
            effect_type=StatusEffectType.STUNNED,
            duration=5,
            intensity=3
        )
        player.add_status_effect(inactive_effect)
        
        active_effects = player.get_active_status_effects(7)
        assert len(active_effects) == 1
        assert active_effects[0].effect_type == StatusEffectType.POISONED

    def test_player_update_last_active(self):
        """Test the update_last_active method."""
        player = Player(name="TestPlayer")
        old_last_active = player.last_active
        
        # Wait a moment to ensure timestamp difference
        import time
        time.sleep(0.001)
        
        player.update_last_active()
        assert player.last_active > old_last_active

    def test_player_can_carry_weight(self):
        """Test the can_carry_weight method."""
        player = Player(name="TestPlayer")
        player.stats.strength = 10  # 100 lbs capacity
        
        # Should be able to carry 50 lbs
        assert player.can_carry_weight(50.0) is True
        
        # Should not be able to carry 150 lbs
        assert player.can_carry_weight(150.0) is False


class TestNPC:
    """Test the NPC model."""

    def test_npc_creation(self):
        """Test creating an NPC."""
        npc = NPC(
            name="Shopkeeper",
            description="A friendly shopkeeper",
            current_room_id="arkham_002",
            npc_type="merchant",
            is_hostile=False
        )
        
        assert npc.name == "Shopkeeper"
        assert npc.description == "A friendly shopkeeper"
        assert npc.current_room_id == "arkham_002"
        assert npc.npc_type == "merchant"
        assert npc.is_hostile is False
        assert isinstance(npc.id, str)
        assert isinstance(npc.stats, Stats)

    def test_npc_is_alive(self):
        """Test the is_alive method."""
        npc = NPC(
            name="Enemy",
            description="A hostile creature",
            current_room_id="arkham_003"
        )
        
        # Should be alive with default health
        assert npc.is_alive() is True
        
        # Should be dead with 0 health
        npc.stats.current_health = 0
        assert npc.is_alive() is False


class TestAttributeType:
    """Test the AttributeType enum."""

    def test_attribute_types(self):
        """Test that all attribute types are defined."""
        assert AttributeType.STR == "strength"
        assert AttributeType.DEX == "dexterity"
        assert AttributeType.CON == "constitution"
        assert AttributeType.INT == "intelligence"
        assert AttributeType.WIS == "wisdom"
        assert AttributeType.CHA == "charisma"
        assert AttributeType.SAN == "sanity"
        assert AttributeType.OCC == "occult_knowledge"
        assert AttributeType.FEAR == "fear"
        assert AttributeType.CORR == "corruption"
        assert AttributeType.CULT == "cult_affiliation"


class TestStatusEffectType:
    """Test the StatusEffectType enum."""

    def test_status_effect_types(self):
        """Test that all status effect types are defined."""
        assert StatusEffectType.STUNNED == "stunned"
        assert StatusEffectType.POISONED == "poisoned"
        assert StatusEffectType.HALLUCINATING == "hallucinating"
        assert StatusEffectType.PARANOID == "paranoid"
        assert StatusEffectType.TREMBLING == "trembling"
        assert StatusEffectType.CORRUPTED == "corrupted"
        assert StatusEffectType.INSANE == "insane"
