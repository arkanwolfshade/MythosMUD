import time

from server.models import (
    AttributeType,
    InventoryItem,
    Item,
    Player,
    Stats,
    StatusEffect,
    StatusEffectType,
)


def test_stats_creation():
    """Test creating a Stats object with default values."""
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


def test_stats_custom_values():
    """Test creating a Stats object with custom values."""
    stats = Stats(
        strength=15,
        dexterity=12,
        constitution=14,
        intelligence=16,
        wisdom=13,
        charisma=11,
        sanity=80,
        occult_knowledge=5,
        fear=10,
        corruption=2,
        cult_affiliation=0,
    )
    assert stats.strength == 15
    assert stats.dexterity == 12
    assert stats.constitution == 14
    assert stats.intelligence == 16
    assert stats.wisdom == 13
    assert stats.charisma == 11
    assert stats.sanity == 80
    assert stats.occult_knowledge == 5
    assert stats.fear == 10
    assert stats.corruption == 2


def test_stats_derived_values():
    """Test that derived stats are calculated correctly."""
    stats = Stats(constitution=15, wisdom=12)
    assert stats.max_health == 150  # constitution * 10
    assert stats.current_health == 100  # default value


def test_stats_modifiers_and_sanity():
    stats = Stats(strength=14, corruption=55, sanity=0)
    assert stats.get_attribute_modifier(AttributeType.STR) == 2
    assert stats.is_sane() is False
    assert stats.is_corrupted() is True
    assert stats.is_insane() is True


def test_item_and_inventoryitem_properties():
    item = Item(
        name="Tome",
        description="Forbidden book",
        item_type="book",
        weight=2.5,
        value=100,
    )
    item.custom_properties["magic"] = True
    assert item.get_property("magic") is True
    assert item.get_property("weight") == 2.5
    inv_item = InventoryItem(item_id=item.id, quantity=2, custom_properties={"enchanted": True})
    assert inv_item.get_property("enchanted") is True
    assert inv_item.get_property("nonexistent", 42) == 42


def test_player_inventory_and_status_effects():
    player = Player(name="Hero")
    item_id = "item123"
    # Add item
    assert player.add_item(item_id, quantity=2)
    assert any(inv.item_id == item_id for inv in player.inventory)
    # Remove item
    assert player.remove_item(item_id, quantity=1)
    # Remove remaining
    assert player.remove_item(item_id, quantity=1)
    # Remove non-existent
    assert player.remove_item("nope") is False
    # Status effects
    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=5, intensity=2)
    player.add_status_effect(effect)
    assert effect in player.status_effects
    assert player.remove_status_effect(StatusEffectType.STUNNED) is True
    assert player.remove_status_effect(StatusEffectType.POISONED) is False
    # Active effects
    player.add_status_effect(StatusEffect(effect_type=StatusEffectType.POISONED, duration=0, intensity=1))
    active = player.get_active_status_effects(current_tick=1)
    assert len(active) == 1
    # Update last active
    before = player.last_active
    time.sleep(0.01)
    player.update_last_active()
    assert player.last_active > before
    # Carry weight
    player.add_item("heavy", quantity=1, custom_properties={"weight": 100})
    assert not player.can_carry_weight(1)
