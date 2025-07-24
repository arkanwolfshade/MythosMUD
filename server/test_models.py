from models import (
    Stats,
    Player,
    NPC,
    Item,
    InventoryItem,
    StatusEffect,
    StatusEffectType,
    AttributeType,
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
    assert stats.max_sanity == 60  # wisdom * 5


def test_stats_attribute_modifiers():
    """Test attribute modifier calculations."""
    stats = Stats(strength=14, dexterity=8, intelligence=16)
    assert stats.get_attribute_modifier(AttributeType.STR) == 2  # (14-10)/2
    assert stats.get_attribute_modifier(AttributeType.DEX) == -1  # (8-10)/2
    assert stats.get_attribute_modifier(AttributeType.INT) == 3  # (16-10)/2


def test_stats_sanity_checks():
    """Test sanity-related boolean methods."""
    stats = Stats(sanity=50)
    assert stats.is_sane() is True

    stats.sanity = 0
    assert stats.is_sane() is False
    assert stats.is_insane() is True

    stats.corruption = 60
    assert stats.is_corrupted() is True


def test_status_effect_creation():
    """Test creating a StatusEffect."""
    effect = StatusEffect(
        effect_type=StatusEffectType.POISONED,
        duration=10,
        intensity=5,
        source="poison dart",
    )
    assert effect.effect_type == StatusEffectType.POISONED
    assert effect.duration == 10
    assert effect.intensity == 5
    assert effect.source == "poison dart"


def test_status_effect_active_check():
    """Test status effect active state checking."""
    effect = StatusEffect(
        effect_type=StatusEffectType.POISONED, duration=10, intensity=5
    )

    # Should be active immediately
    assert effect.is_active(0) is True

    # Should still be active within duration
    assert effect.is_active(5) is True

    # Should not be active after duration
    assert effect.is_active(15) is False


def test_permanent_status_effect():
    """Test permanent status effects (duration=0)."""
    effect = StatusEffect(
        effect_type=StatusEffectType.INSANE, duration=0, intensity=10  # Permanent
    )

    # Should always be active
    assert effect.is_active(0) is True
    assert effect.is_active(1000) is True
    assert effect.is_active(999999) is True


def test_item_creation():
    """Test creating an Item."""
    item = Item(
        name="Sword",
        description="A sharp blade",
        item_type="weapon",
        weight=5.0,
        value=100,
    )
    assert item.name == "Sword"
    assert item.description == "A sharp blade"
    assert item.item_type == "weapon"
    assert item.weight == 5.0
    assert item.value == 100


def test_item_custom_properties():
    """Test item custom properties."""
    item = Item(
        name="Magic Sword",
        description="A magical blade",
        item_type="weapon",
        custom_properties={"damage": 15, "magical": True},
    )
    assert item.get_property("damage") == 15
    assert item.get_property("magical") is True
    assert item.get_property("nonexistent", "default") == "default"


def test_inventory_item_creation():
    """Test creating an InventoryItem."""
    inv_item = InventoryItem(
        item_id="sword_001", quantity=3, custom_properties={"enchantment": "fire"}
    )
    assert inv_item.item_id == "sword_001"
    assert inv_item.quantity == 3
    assert inv_item.get_property("enchantment") == "fire"


def test_player_creation():
    """Test creating a Player."""
    player = Player(name="TestPlayer")
    assert player.name == "TestPlayer"
    assert isinstance(player.stats, Stats)
    assert len(player.inventory) == 0
    assert len(player.status_effects) == 0
    assert player.current_room_id == "arkham_001"
    assert player.experience_points == 0
    assert player.level == 1


def test_player_add_item():
    """Test adding items to player inventory."""
    player = Player(name="TestPlayer")

    # Add an item
    success = player.add_item("sword_001", 2, {"enchantment": "fire"})
    assert success is True
    assert len(player.inventory) == 1
    assert player.inventory[0].item_id == "sword_001"
    assert player.inventory[0].quantity == 2
    assert player.inventory[0].get_property("enchantment") == "fire"

    # Add same item again (should stack)
    success = player.add_item("sword_001", 1, {"enchantment": "fire"})
    assert success is True
    assert len(player.inventory) == 1
    assert player.inventory[0].quantity == 3


def test_player_remove_item():
    """Test removing items from player inventory."""
    player = Player(name="TestPlayer")
    player.add_item("sword_001", 3)

    # Remove some items
    success = player.remove_item("sword_001", 2)
    assert success is True
    assert player.inventory[0].quantity == 1

    # Remove remaining items
    success = player.remove_item("sword_001", 1)
    assert success is True
    assert len(player.inventory) == 0


def test_player_status_effects():
    """Test player status effect management."""
    player = Player(name="TestPlayer")

    # Add status effect
    effect = StatusEffect(
        effect_type=StatusEffectType.POISONED, duration=10, intensity=5
    )
    player.add_status_effect(effect)
    assert len(player.status_effects) == 1

    # Remove status effect
    success = player.remove_status_effect(StatusEffectType.POISONED)
    assert success is True
    assert len(player.status_effects) == 0


def test_player_carry_weight():
    """Test player carrying capacity."""
    player = Player(name="TestPlayer", stats=Stats(strength=10))

    # Should be able to carry 100 lbs (10 strength * 10)
    assert player.can_carry_weight(50) is True
    assert player.can_carry_weight(100) is True
    assert player.can_carry_weight(101) is False


def test_npc_creation():
    """Test creating an NPC."""
    npc = NPC(
        name="Shopkeeper",
        description="A friendly merchant",
        current_room_id="arkham_001",
        npc_type="merchant",
        is_hostile=False,
    )
    assert npc.name == "Shopkeeper"
    assert npc.description == "A friendly merchant"
    assert npc.current_room_id == "arkham_001"
    assert npc.npc_type == "merchant"
    assert npc.is_hostile is False
    assert isinstance(npc.stats, Stats)


def test_npc_alive_check():
    """Test NPC alive status."""
    npc = NPC(name="TestNPC", description="Test", current_room_id="arkham_001")
    assert npc.is_alive() is True

    npc.stats.current_health = 0
    assert npc.is_alive() is False
