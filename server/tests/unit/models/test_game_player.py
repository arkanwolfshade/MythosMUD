"""
Unit tests for Player model methods.
"""

import time

from server.models.game import InventoryItem, Player, Stats, StatusEffect, StatusEffectType


def test_player_add_item_new():
    """Test add_item adds new item to inventory."""
    player = Player(name="TestPlayer")
    player.inventory = []

    result = player.add_item("item1", quantity=3)

    assert result is True
    assert len(player.inventory) == 1
    assert player.inventory[0].item_id == "item1"
    assert player.inventory[0].quantity == 3


def test_player_add_item_existing():
    """Test add_item increases quantity for existing item."""
    player = Player(name="TestPlayer")
    player.inventory = [InventoryItem(item_id="item1", quantity=2)]

    result = player.add_item("item1", quantity=3)

    assert result is True
    assert len(player.inventory) == 1
    assert player.inventory[0].quantity == 5  # 2 + 3


def test_player_add_item_default_quantity():
    """Test add_item defaults quantity to 1."""
    player = Player(name="TestPlayer")
    player.inventory = []

    result = player.add_item("item1")

    assert result is True
    assert player.inventory[0].quantity == 1


def test_player_remove_item_success():
    """Test remove_item removes item when quantity is sufficient."""
    player = Player(name="TestPlayer")
    player.inventory = [InventoryItem(item_id="item1", quantity=5)]

    result = player.remove_item("item1", quantity=2)

    assert result is True
    assert player.inventory[0].quantity == 3  # 5 - 2


def test_player_remove_item_removes_when_zero():
    """Test remove_item removes item from inventory when quantity reaches 0."""
    player = Player(name="TestPlayer")
    player.inventory = [InventoryItem(item_id="item1", quantity=2)]

    result = player.remove_item("item1", quantity=2)

    assert result is True
    assert len(player.inventory) == 0


def test_player_remove_item_not_found():
    """Test remove_item returns False when item not in inventory."""
    player = Player(name="TestPlayer")
    player.inventory = []

    result = player.remove_item("item1")

    assert result is False


def test_player_remove_item_insufficient_quantity():
    """Test remove_item returns False when quantity is insufficient."""
    player = Player(name="TestPlayer")
    player.inventory = [InventoryItem(item_id="item1", quantity=2)]

    result = player.remove_item("item1", quantity=5)

    assert result is False
    assert player.inventory[0].quantity == 2  # Unchanged


def test_player_add_status_effect():
    """Test add_status_effect adds effect to status_effects list."""
    player = Player(name="TestPlayer")
    player.status_effects = []

    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)
    player.add_status_effect(effect)

    assert len(player.status_effects) == 1
    assert player.status_effects[0] == effect


def test_player_remove_status_effect_success():
    """Test remove_status_effect removes effect when found."""
    player = Player(name="TestPlayer")
    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)
    player.status_effects = [effect]

    result = player.remove_status_effect(StatusEffectType.STUNNED)

    assert result is True
    assert len(player.status_effects) == 0


def test_player_remove_status_effect_not_found():
    """Test remove_status_effect returns False when effect not found."""
    player = Player(name="TestPlayer")
    player.status_effects = []

    result = player.remove_status_effect(StatusEffectType.STUNNED)

    assert result is False


def test_player_get_active_status_effects():
    """Test get_active_status_effects returns only active effects."""
    player = Player(name="TestPlayer")
    active_effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)
    expired_effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=5, intensity=3)
    player.status_effects = [active_effect, expired_effect]

    result = player.get_active_status_effects(current_tick=7)

    assert len(result) == 1
    assert result[0] == active_effect


def test_player_get_active_status_effects_all_active():
    """Test get_active_status_effects returns all effects when all are active."""
    player = Player(name="TestPlayer")
    effect1 = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)
    effect2 = StatusEffect(effect_type=StatusEffectType.POISONED, duration=10, intensity=3)
    player.status_effects = [effect1, effect2]

    result = player.get_active_status_effects(current_tick=5)

    assert len(result) == 2


def test_player_update_last_active():
    """Test update_last_active updates last_active timestamp."""
    player = Player(name="TestPlayer")
    original_time = player.last_active

    time.sleep(0.01)

    player.update_last_active()

    assert player.last_active > original_time


def test_player_can_carry_weight_true():
    """Test can_carry_weight returns True when weight is within capacity."""
    player = Player(name="TestPlayer")
    player.stats = Stats(strength=50)
    # Max capacity = 50 * 10 = 500

    result = player.can_carry_weight(weight=100.0)

    assert result is True


def test_player_can_carry_weight_false():
    """Test can_carry_weight returns False when weight exceeds capacity."""
    player = Player(name="TestPlayer")
    player.stats = Stats(strength=10)
    # Max capacity = 10 * 10 = 100

    result = player.can_carry_weight(weight=10000.0)

    assert result is False
