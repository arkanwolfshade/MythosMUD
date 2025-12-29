"""
Unit tests for population statistics.

Tests the PopulationStats class.
"""

import time

from server.npc.population_stats import PopulationStats


def test_population_stats_init():
    """Test PopulationStats initialization."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    assert stats.zone_id == "arkhamcity"
    assert stats.sub_zone_id == "downtown"
    assert stats.total_npcs == 0
    assert stats.npcs_by_type == {}
    assert stats.npcs_by_definition == {}
    assert stats.npcs_by_room == {}
    assert stats.required_npcs == 0
    assert stats.optional_npcs == 0
    assert stats.last_updated > 0


def test_add_npc_required():
    """Test add_npc() adds required NPC."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 1
    assert stats.npcs_by_type["aggressive_mob"] == 1
    assert stats.npcs_by_room["room-123"] == 1
    assert stats.npcs_by_definition[1] == 1
    assert stats.required_npcs == 1
    assert stats.optional_npcs == 0


def test_add_npc_optional():
    """Test add_npc() adds optional NPC."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="passive_mob", room_id="room-456", is_required=False, npc_definition_id=2)
    assert stats.total_npcs == 1
    assert stats.npcs_by_type["passive_mob"] == 1
    assert stats.npcs_by_room["room-456"] == 1
    assert stats.npcs_by_definition[2] == 1
    assert stats.required_npcs == 0
    assert stats.optional_npcs == 1


def test_add_npc_multiple_same_type():
    """Test add_npc() increments count for same type."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="aggressive_mob", room_id="room-456", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 2
    assert stats.npcs_by_type["aggressive_mob"] == 2
    assert stats.npcs_by_definition[1] == 2


def test_add_npc_multiple_same_room():
    """Test add_npc() increments count for same room."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="passive_mob", room_id="room-123", is_required=False, npc_definition_id=2)
    assert stats.total_npcs == 2
    assert stats.npcs_by_room["room-123"] == 2


def test_add_npc_without_definition_id():
    """Test add_npc() handles None definition_id."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=None)
    assert stats.total_npcs == 1
    assert stats.npcs_by_definition == {}


def test_add_npc_updates_timestamp():
    """Test add_npc() updates last_updated timestamp."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    initial_time = stats.last_updated
    time.sleep(0.01)  # Small delay
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.last_updated > initial_time


def test_remove_npc_required():
    """Test remove_npc() removes required NPC."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 0
    assert stats.npcs_by_type["aggressive_mob"] == 0
    assert stats.npcs_by_room["room-123"] == 0
    assert stats.npcs_by_definition[1] == 0
    assert stats.required_npcs == 0
    assert stats.optional_npcs == 0


def test_remove_npc_optional():
    """Test remove_npc() removes optional NPC."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="passive_mob", room_id="room-456", is_required=False, npc_definition_id=2)
    stats.remove_npc(npc_type="passive_mob", room_id="room-456", is_required=False, npc_definition_id=2)
    assert stats.total_npcs == 0
    assert stats.required_npcs == 0
    assert stats.optional_npcs == 0


def test_remove_npc_partial():
    """Test remove_npc() decrements count when multiple exist."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 1
    assert stats.npcs_by_type["aggressive_mob"] == 1
    assert stats.npcs_by_definition[1] == 1


def test_remove_npc_not_found():
    """Test remove_npc() handles removal when NPC not found."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    # Remove without adding first
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 0
    assert stats.npcs_by_type["aggressive_mob"] == 0
    assert stats.npcs_by_definition[1] == 0
    assert stats.required_npcs == 0


def test_remove_npc_prevents_negative():
    """Test remove_npc() prevents negative counts."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    # Remove multiple times without adding
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.total_npcs == 0
    assert stats.npcs_by_type["aggressive_mob"] == 0
    assert stats.required_npcs == 0


def test_remove_npc_without_definition_id():
    """Test remove_npc() handles None definition_id."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=None)
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=None)
    assert stats.total_npcs == 0


def test_remove_npc_updates_timestamp():
    """Test remove_npc() updates last_updated timestamp."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    initial_time = stats.last_updated
    time.sleep(0.01)  # Small delay
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.last_updated > initial_time


def test_to_dict():
    """Test to_dict() returns complete dictionary."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="passive_mob", room_id="room-456", is_required=False, npc_definition_id=2)
    result = stats.to_dict()
    assert result["zone_id"] == "arkhamcity"
    assert result["sub_zone_id"] == "downtown"
    assert result["total_npcs"] == 2
    assert result["npcs_by_type"] == {"aggressive_mob": 1, "passive_mob": 1}
    assert result["npcs_by_definition"] == {1: 1, 2: 1}
    assert result["npcs_by_room"] == {"room-123": 1, "room-456": 1}
    assert result["required_npcs"] == 1
    assert result["optional_npcs"] == 1
    assert result["last_updated"] > 0


def test_to_dict_copies():
    """Test to_dict() returns copies of dictionaries."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    result = stats.to_dict()
    # Modify the returned dict
    result["npcs_by_type"]["new_type"] = 999
    # Original should not be affected
    assert "new_type" not in stats.npcs_by_type


def test_mixed_required_optional():
    """Test population stats with mixed required and optional NPCs."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="passive_mob", room_id="room-456", is_required=False, npc_definition_id=2)
    stats.add_npc(npc_type="shopkeeper", room_id="room-789", is_required=True, npc_definition_id=3)
    assert stats.total_npcs == 3
    assert stats.required_npcs == 2
    assert stats.optional_npcs == 1


def test_multiple_definitions_same_type():
    """Test tracking multiple NPC definitions of same type."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="aggressive_mob", room_id="room-456", is_required=True, npc_definition_id=2)
    assert stats.npcs_by_type["aggressive_mob"] == 2
    assert stats.npcs_by_definition[1] == 1
    assert stats.npcs_by_definition[2] == 1


def test_remove_npc_different_definition():
    """Test remove_npc() correctly removes specific definition."""
    stats = PopulationStats(zone_id="arkhamcity", sub_zone_id="downtown")
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    stats.add_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=2)
    stats.remove_npc(npc_type="aggressive_mob", room_id="room-123", is_required=True, npc_definition_id=1)
    assert stats.npcs_by_definition[1] == 0
    assert stats.npcs_by_definition[2] == 1
    assert stats.npcs_by_type["aggressive_mob"] == 1
