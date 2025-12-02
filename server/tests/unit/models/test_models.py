"""
Tests for models.py - Pydantic models for game data.

This module tests the Pydantic models defined in the models package including
Player, Stats, StatusEffect, and Alias models.

Note: Tests for Item, InventoryItem, and NPC models are commented out pending
implementation of those systems.
"""

from server.models.alias import Alias
from server.models.game import AttributeType, Player, Stats, StatusEffect, StatusEffectType

# Note: Item, InventoryItem, and NPC models have not been implemented yet.
# Tests for these models are commented out pending implementation.


class TestStats:
    """Test the Stats model."""

    def test_stats_default_values(self):
        """Test that Stats has correct default values."""
        stats = Stats()

        # Attributes are randomly generated between 15-90, so we check the range
        assert 15 <= stats.strength <= 90
        assert 15 <= stats.dexterity <= 90
        assert 15 <= stats.constitution <= 90
        assert 15 <= stats.intelligence <= 90
        assert 15 <= stats.wisdom <= 90
        assert 15 <= stats.charisma <= 90
        assert stats.lucidity == 100
        assert stats.occult_knowledge == 0
        assert stats.fear == 0
        assert stats.corruption == 0
        assert stats.cult_affiliation == 0
        assert stats.current_health == 100

    def test_stats_custom_values(self):
        """Test that Stats can be created with custom values."""
        stats = Stats(
            strength=75,
            dexterity=60,
            constitution=70,
            intelligence=80,
            wisdom=65,
            charisma=55,
            lucidity=85,
            occult_knowledge=25,
            fear=15,
            corruption=5,
            cult_affiliation=10,
            current_health=95,
        )

        assert stats.strength == 75
        assert stats.dexterity == 60
        assert stats.constitution == 70
        assert stats.intelligence == 80
        assert stats.wisdom == 65
        assert stats.charisma == 55
        assert stats.lucidity == 85
        assert stats.occult_knowledge == 25
        assert stats.fear == 15
        assert stats.corruption == 5
        assert stats.cult_affiliation == 10
        assert stats.current_health == 95

    def test_stats_max_health_property(self):
        """Test the max_health computed property."""
        stats = Stats(constitution=75)
        assert stats.max_health == 75  # Direct constitution value

    def test_stats_max_Lucidity_property(self):
        """Test the max_Lucidity computed property."""
        stats = Stats(wisdom=90)
        assert stats.max_Lucidity == 90  # Direct wisdom value

    def test_stats_get_attribute_modifier(self):
        """Test the get_attribute_modifier method."""
        stats = Stats(strength=75, dexterity=40, intelligence=60)

        assert stats.get_attribute_modifier(AttributeType.STR) == 12  # (75-50)/2
        assert stats.get_attribute_modifier(AttributeType.DEX) == -5  # (40-50)/2
        assert stats.get_attribute_modifier(AttributeType.INT) == 5  # (60-50)/2

    def test_stats_is_lucid(self):
        """Test the is_lucid method."""
        stats = Stats(lucidity=100)
        assert stats.is_lucid() is True

        stats = Stats(lucidity=50)
        assert stats.is_lucid() is True

        stats = Stats(lucidity=0)
        assert stats.is_lucid() is False

    def test_stats_is_corrupted(self):
        """Test the is_corrupted method."""
        stats = Stats(corruption=0)
        assert stats.is_corrupted() is False

        stats = Stats(corruption=50)
        assert stats.is_corrupted() is True

    def test_stats_is_delirious(self):
        """Test the is_delirious method."""
        stats = Stats(lucidity=100)
        assert stats.is_delirious() is False

        stats = Stats(lucidity=0)
        assert stats.is_delirious() is True

    def test_stats_ignores_extra_fields(self):
        """Test that Stats model ignores extra fields (security: extra='ignore')."""
        # Create Stats with extra fields that should be ignored
        stats = Stats(
            strength=15,
            dexterity=12,
            # Extra fields that should be ignored, not stored
            malicious_field="injection_attempt",
            another_extra_field=999,
            nested_extra={"key": "value"},
        )

        # Verify valid fields are set
        assert stats.strength == 15
        assert stats.dexterity == 12

        # Verify extra fields are NOT stored (ignored)
        assert not hasattr(stats, "malicious_field")
        assert not hasattr(stats, "another_extra_field")
        assert not hasattr(stats, "nested_extra")

        # Verify model_dump() doesn't include extra fields
        dumped = stats.model_dump()
        assert "malicious_field" not in dumped
        assert "another_extra_field" not in dumped
        assert "nested_extra" not in dumped


class TestStatusEffect:
    """Test the StatusEffect model."""

    def test_status_effect_is_active(self):
        """Test the is_active method."""
        effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        # Should be active at tick 5
        assert effect.is_active(5) is True

        # Should not be active at tick 15
        assert effect.is_active(15) is False

    def test_status_effect_permanent(self):
        """Test permanent status effects (duration=0)."""
        effect = StatusEffect(
            effect_type=StatusEffectType.CORRUPTED,
            duration=0,  # Permanent
            intensity=8,
        )

        # Should always be active
        assert effect.is_active(0) is True
        assert effect.is_active(100) is True
        assert effect.is_active(1000) is True


class TestAlias:
    """Test the Alias model."""

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


# NOTE: Item and InventoryItem models have not been implemented yet.
# These tests are commented out pending implementation of the Item system.
#
# class TestItem:
#     """Test the Item model."""
#
#     def test_item_creation(self):
#         """Test creating an Item."""
#         item = Item(
#             name="Rusty Sword", description="A rusty but serviceable sword", item_type="weapon", weight=5.0, value=10
#         )
#
#         assert item.name == "Rusty Sword"
#         assert item.description == "A rusty but serviceable sword"
#         assert item.item_type == "weapon"
#         assert item.weight == 5.0
#         assert item.value == 10
#         assert isinstance(item.id, str)
#
#     def test_item_get_property(self):
#         """Test the get_property method."""
#         item = Item(
#             name="Magic Ring",
#             description="A ring with magical properties",
#             item_type="accessory",
#             custom_properties={"magic_power": 5, "durability": 100},
#         )
#
#         assert item.get_property("magic_power") == 5
#         assert item.get_property("durability") == 100
#         assert item.get_property("nonexistent", "default") == "default"
#
#
# class TestInventoryItem:
#     """Test the InventoryItem model."""
#
#     def test_inventory_item_creation(self):
#         """Test creating an InventoryItem."""
#         inv_item = InventoryItem(item_id="sword_001", quantity=2, custom_properties={"condition": "worn"})
#
#         assert inv_item.item_id == "sword_001"
#         assert inv_item.quantity == 2
#         assert inv_item.custom_properties == {"condition": "worn"}
#
#     def test_inventory_item_get_property(self):
#         """Test the get_property method."""
#         inv_item = InventoryItem(
#             item_id="potion_001", quantity=1, custom_properties={"effect": "healing", "strength": 25}
#         )
#
#         assert inv_item.get_property("effect") == "healing"
#         assert inv_item.get_property("strength") == 25
#         assert inv_item.get_property("nonexistent", "default") == "default"


class TestPlayer:
    """Test the Player model."""

    def test_player_creation(self):
        """Test creating a Player."""
        player = Player(name="TestPlayer", current_room_id="earth_arkhamcity_intersection_derby_high")

        assert player.name == "TestPlayer"
        assert player.current_room_id == "earth_arkhamcity_intersection_derby_high"
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

    def test_player_remove_item_insufficient_quantity(self):
        """Test removing more items than available.

        AI: Tests line 248 in models/game.py where we return False when trying to
        remove more items than the player has in inventory. Covers the edge case
        where item exists but quantity is insufficient.
        """
        player = Player(name="TestPlayer")
        player.add_item("potion", 2)  # Add 2 potions

        # Try to remove more than we have
        assert player.remove_item("potion", 5) is False
        # Inventory should remain unchanged
        assert len(player.inventory) == 1
        assert player.inventory[0].quantity == 2

    def test_player_add_status_effect(self):
        """Test the add_status_effect method."""
        player = Player(name="TestPlayer")
        effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

        player.add_status_effect(effect)
        assert len(player.status_effects) == 1
        assert player.status_effects[0] == effect

    def test_player_remove_status_effect(self):
        """Test the remove_status_effect method."""
        player = Player(name="TestPlayer")
        effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)

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
        active_effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=5)
        player.add_status_effect(active_effect)

        # Add inactive effect
        inactive_effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=5, intensity=3)
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


# NOTE: NPC model has not been implemented yet.
# These tests are commented out pending implementation of the NPC system.
#
# class TestNPC:
#     """Test the NPC model."""
#
#     def test_npc_creation(self):
#         """Test creating an NPC."""
#         npc = NPC(
#             name="Shopkeeper",
#             description="A friendly shopkeeper",
#             current_room_id="arkham_002",
#             npc_type="merchant",
#             is_hostile=False,
#         )
#
#         assert npc.name == "Shopkeeper"
#         assert npc.description == "A friendly shopkeeper"
#         assert npc.current_room_id == "arkham_002"
#         assert npc.npc_type == "merchant"
#         assert npc.is_hostile is False
#         assert isinstance(npc.id, str)
#         assert isinstance(npc.stats, Stats)
#
#     def test_npc_is_alive(self):
#         """Test the is_alive method."""
#         npc = NPC(name="Enemy", description="A hostile creature", current_room_id="arkham_003")
#
#         # Should be alive with default health
#         assert npc.is_alive() is True
#
#         # Should be dead with 0 health
#         npc.stats.current_health = 0
#         assert npc.is_alive() is False
#
#         # Should be dead with negative health
#         npc.stats.current_health = -10
#         assert npc.is_alive() is False


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
        assert AttributeType.LCD == "lucidity"
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
        assert StatusEffectType.delirious == "delirious"
