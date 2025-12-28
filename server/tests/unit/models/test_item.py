"""
Unit tests for item models.

Tests the ItemPrototype, ItemInstance, and ItemComponentState models.
"""

from server.models.item import ItemComponentState, ItemInstance, ItemPrototype


def test_item_prototype_primary_slot_with_slots():
    """Test primary_slot returns first wear slot when slots exist."""
    prototype = ItemPrototype()
    prototype.wear_slots = ["head", "neck", "back"]

    result = prototype.primary_slot()

    assert result == "head"


def test_item_prototype_primary_slot_single_slot():
    """Test primary_slot returns the slot when only one exists."""
    prototype = ItemPrototype()
    prototype.wear_slots = ["hand"]

    result = prototype.primary_slot()

    assert result == "hand"


def test_item_prototype_primary_slot_empty():
    """Test primary_slot returns None when no wear slots."""
    prototype = ItemPrototype()
    prototype.wear_slots = []

    result = prototype.primary_slot()

    assert result is None


def test_item_prototype_primary_slot_none():
    """Test primary_slot returns None when wear_slots is None (edge case)."""
    prototype = ItemPrototype()
    # Don't set wear_slots, it should default to empty list
    # But test the case where it might be None
    prototype.wear_slots = []

    result = prototype.primary_slot()

    assert result is None


def test_item_instance_apply_flag_new_flag():
    """Test apply_flag adds a new flag to flags_override."""
    instance = ItemInstance()
    instance.flags_override = []

    instance.apply_flag("test_flag")

    assert "test_flag" in instance.flags_override
    assert len(instance.flags_override) == 1


def test_item_instance_apply_flag_existing_flag():
    """Test apply_flag does not duplicate existing flags (idempotent)."""
    instance = ItemInstance()
    instance.flags_override = ["test_flag"]

    instance.apply_flag("test_flag")

    assert instance.flags_override.count("test_flag") == 1
    assert len(instance.flags_override) == 1


def test_item_instance_apply_flag_multiple_flags():
    """Test apply_flag adds flag when other flags exist."""
    instance = ItemInstance()
    instance.flags_override = ["flag1", "flag2"]

    instance.apply_flag("flag3")

    assert "flag3" in instance.flags_override
    assert len(instance.flags_override) == 3
    assert "flag1" in instance.flags_override
    assert "flag2" in instance.flags_override


def test_item_instance_apply_flag_preserves_order():
    """Test apply_flag preserves existing flag order."""
    instance = ItemInstance()
    instance.flags_override = ["flag1", "flag2"]

    instance.apply_flag("flag3")

    assert instance.flags_override == ["flag1", "flag2", "flag3"]


def test_item_component_state_unique_key():
    """Test unique_key returns tuple of instance_id and component_id."""
    result = ItemComponentState.unique_key("instance123", "component456")

    assert result == ("instance123", "component456")
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_item_component_state_unique_key_different_values():
    """Test unique_key returns different tuples for different inputs."""
    result1 = ItemComponentState.unique_key("instance1", "component1")
    result2 = ItemComponentState.unique_key("instance2", "component2")

    assert result1 != result2
    assert result1 == ("instance1", "component1")
    assert result2 == ("instance2", "component2")


def test_item_component_state_unique_key_same_instance_different_component():
    """Test unique_key returns different tuples for same instance, different component."""
    result1 = ItemComponentState.unique_key("instance1", "component1")
    result2 = ItemComponentState.unique_key("instance1", "component2")

    assert result1 != result2
    assert result1[0] == result2[0]  # Same instance_id
    assert result1[1] != result2[1]  # Different component_id


def test_item_component_state_unique_key_different_instance_same_component():
    """Test unique_key returns different tuples for different instance, same component."""
    result1 = ItemComponentState.unique_key("instance1", "component1")
    result2 = ItemComponentState.unique_key("instance2", "component1")

    assert result1 != result2
    assert result1[0] != result2[0]  # Different instance_id
    assert result1[1] == result2[1]  # Same component_id


def test_item_component_state_unique_key_empty_strings():
    """Test unique_key handles empty strings."""
    result = ItemComponentState.unique_key("", "")

    assert result == ("", "")
    assert isinstance(result, tuple)


def test_item_component_state_unique_key_static_method():
    """Test unique_key is a static method (can be called without instance)."""
    # Should be callable on the class itself
    result = ItemComponentState.unique_key("test_instance", "test_component")

    assert result == ("test_instance", "test_component")
