"""
Unit tests for inventory command helper functions.

Tests helper functions used by inventory commands.
"""

import pytest

from server.commands.inventory_commands import (
    _format_metadata,
    _match_equipped_item_by_name,
    _match_inventory_item_by_name,
    _match_room_drop_by_name,
    _normalize_slot_name,
    _resolve_state,
)


def test_normalize_slot_name_none():
    """Test _normalize_slot_name with None."""
    result = _normalize_slot_name(None)
    assert result is None


def test_normalize_slot_name_valid():
    """Test _normalize_slot_name with valid slot name."""
    result = _normalize_slot_name("Main Hand")
    assert result == "main hand"


def test_normalize_slot_name_empty_string():
    """Test _normalize_slot_name with empty string."""
    result = _normalize_slot_name("")
    assert result is None


def test_normalize_slot_name_whitespace():
    """Test _normalize_slot_name with whitespace only."""
    result = _normalize_slot_name("   ")
    assert result is None


def test_match_room_drop_by_name_empty_search():
    """Test _match_room_drop_by_name with empty search term."""
    result = _match_room_drop_by_name([{"item_name": "sword"}], "")
    assert result is None


def test_match_room_drop_by_name_exact_match():
    """Test _match_room_drop_by_name with exact match."""
    drops = [{"item_name": "sword"}, {"item_name": "shield"}]
    result = _match_room_drop_by_name(drops, "sword")
    assert result == 0


def test_match_room_drop_by_name_prefix_match():
    """Test _match_room_drop_by_name with prefix match."""
    drops = [{"item_name": "sword"}, {"item_name": "shield"}]
    result = _match_room_drop_by_name(drops, "sw")
    assert result == 0


def test_match_room_drop_by_name_substring_match():
    """Test _match_room_drop_by_name with substring match."""
    drops = [{"item_name": "sword"}, {"item_name": "shield"}]
    result = _match_room_drop_by_name(drops, "ord")
    assert result == 0


def test_match_room_drop_by_name_item_id_match():
    """Test _match_room_drop_by_name with item_id match."""
    drops = [{"item_id": "item_123", "item_name": "sword"}]
    result = _match_room_drop_by_name(drops, "item_123")
    assert result == 0


def test_match_room_drop_by_name_prototype_id_match():
    """Test _match_room_drop_by_name with prototype_id match."""
    drops = [{"prototype_id": "proto_456", "item_name": "sword"}]
    result = _match_room_drop_by_name(drops, "proto_456")
    assert result == 0


def test_match_room_drop_by_name_no_match():
    """Test _match_room_drop_by_name with no match."""
    drops = [{"item_name": "sword"}]
    result = _match_room_drop_by_name(drops, "nonexistent")
    assert result is None


def test_match_inventory_item_by_name_exact_match():
    """Test _match_inventory_item_by_name with exact match."""
    inventory = [{"item_name": "potion"}, {"item_name": "scroll"}]
    result = _match_inventory_item_by_name(inventory, "potion")
    assert result == 0


def test_match_inventory_item_by_name_prefix_match():
    """Test _match_inventory_item_by_name with prefix match."""
    inventory = [{"item_name": "potion"}, {"item_name": "scroll"}]
    result = _match_inventory_item_by_name(inventory, "pot")
    assert result == 0


def test_match_inventory_item_by_name_substring_match():
    """Test _match_inventory_item_by_name with substring match."""
    inventory = [{"item_name": "potion"}, {"item_name": "scroll"}]
    result = _match_inventory_item_by_name(inventory, "tion")
    assert result == 0


def test_match_inventory_item_by_name_no_match():
    """Test _match_inventory_item_by_name with no match."""
    inventory = [{"item_name": "potion"}]
    result = _match_inventory_item_by_name(inventory, "nonexistent")
    assert result is None


def test_match_equipped_item_by_name_exact_match():
    """Test _match_equipped_item_by_name with exact match."""
    equipped = {"main_hand": {"item_name": "sword"}, "off_hand": {"item_name": "shield"}}
    result = _match_equipped_item_by_name(equipped, "sword")
    assert result == "main_hand"


def test_match_equipped_item_by_name_prefix_match():
    """Test _match_equipped_item_by_name with prefix match."""
    equipped = {"main_hand": {"item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "sw")
    assert result == "main_hand"


def test_match_equipped_item_by_name_substring_match():
    """Test _match_equipped_item_by_name with substring match."""
    equipped = {"main_hand": {"item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "ord")
    assert result == "main_hand"


def test_match_equipped_item_by_name_item_id_match():
    """Test _match_equipped_item_by_name with item_id match."""
    equipped = {"main_hand": {"item_id": "item_123", "item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "item_123")
    assert result == "main_hand"


def test_match_equipped_item_by_name_no_match():
    """Test _match_equipped_item_by_name with no match."""
    equipped = {"main_hand": {"item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "nonexistent")
    assert result is None


def test_match_equipped_item_by_name_empty_search():
    """Test _match_equipped_item_by_name with empty search term."""
    equipped = {"main_hand": {"item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "")
    assert result is None


def test_format_metadata_none():
    """Test _format_metadata with None."""
    result = _format_metadata(None)
    assert result == ""


def test_format_metadata_empty():
    """Test _format_metadata with empty dict."""
    result = _format_metadata({})
    assert result == ""


def test_format_metadata_simple():
    """Test _format_metadata with simple metadata."""
    metadata = {"key": "value"}
    result = _format_metadata(metadata)
    assert "key" in result
    assert "value" in result


def test_format_metadata_complex():
    """Test _format_metadata with complex metadata."""
    metadata = {"nested": {"key": "value"}, "list": [1, 2, 3]}
    result = _format_metadata(metadata)
    assert isinstance(result, str)
    assert len(result) > 0


def test_resolve_state_no_app():
    """Test _resolve_state when request has no app."""
    from unittest.mock import MagicMock
    
    request = MagicMock()
    del request.app
    
    persistence, connection_manager = _resolve_state(request)
    assert persistence is None
    assert connection_manager is None


def test_resolve_state_no_state():
    """Test _resolve_state when app has no state."""
    from unittest.mock import MagicMock
    
    request = MagicMock()
    request.app = MagicMock()
    del request.app.state
    
    persistence, connection_manager = _resolve_state(request)
    assert persistence is None
    assert connection_manager is None


def test_resolve_state_success():
    """Test _resolve_state successful resolution."""
    from unittest.mock import MagicMock
    
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = MagicMock()
    request.app.state.connection_manager = MagicMock()
    
    persistence, connection_manager = _resolve_state(request)
    assert persistence is not None
    assert connection_manager is not None
