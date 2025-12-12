"""
Tests for population statistics tracking.

This module tests the population statistics system that tracks
NPC counts by type, room, and requirement status.

As documented in the Cultes des Goules, proper population tracking is essential
for maintaining the delicate balance between the mundane and the eldritch forces
that lurk in the shadows of our world.
"""

from server.npc.population_control import PopulationStats


class TestPopulationStats:
    """Test population statistics tracking."""

    def test_population_stats_creation(self):
        """Test creating population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        assert stats.zone_id == "arkhamcity"
        assert stats.sub_zone_id == "downtown"
        assert stats.total_npcs == 0
        assert stats.npcs_by_type == {}
        assert stats.npcs_by_room == {}
        assert stats.required_npcs == 0
        assert stats.optional_npcs == 0

    def test_add_npc_to_stats(self):
        """Test adding NPCs to population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Add required NPC
        stats.add_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 1
        assert stats.npcs_by_type["shopkeeper"] == 1
        assert stats.npcs_by_room["room_001"] == 1
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 0

        # Add optional NPC
        stats.add_npc("passive_mob", "room_002", False)
        assert stats.total_npcs == 2
        assert stats.npcs_by_type["passive_mob"] == 1
        assert stats.npcs_by_room["room_002"] == 1
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 1

        # Add another NPC of same type
        stats.add_npc("shopkeeper", "room_003", True)
        assert stats.total_npcs == 3
        assert stats.npcs_by_type["shopkeeper"] == 2
        assert stats.npcs_by_room["room_003"] == 1
        assert stats.required_npcs == 2
        assert stats.optional_npcs == 1

    def test_remove_npc_from_stats(self):
        """Test removing NPCs from population statistics."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Add some NPCs first
        stats.add_npc("shopkeeper", "room_001", True)
        stats.add_npc("passive_mob", "room_002", False)
        stats.add_npc("shopkeeper", "room_003", True)

        # Remove one NPC
        stats.remove_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 2
        assert stats.npcs_by_type["shopkeeper"] == 1
        assert stats.npcs_by_room["room_001"] == 0
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 1

        # Remove another NPC
        stats.remove_npc("passive_mob", "room_002", False)
        assert stats.total_npcs == 1
        assert stats.npcs_by_type["passive_mob"] == 0
        assert stats.npcs_by_room["room_002"] == 0
        assert stats.required_npcs == 1
        assert stats.optional_npcs == 0

    def test_population_stats_negative_protection(self):
        """Test that population stats don't go negative."""
        stats = PopulationStats("arkhamcity", "downtown")

        # Try to remove from empty stats
        stats.remove_npc("shopkeeper", "room_001", True)
        assert stats.total_npcs == 0
        assert stats.npcs_by_type == {"shopkeeper": 0}  # Key exists but value is 0
        assert stats.npcs_by_room == {"room_001": 0}  # Key exists but value is 0
        assert stats.required_npcs == 0
        assert stats.optional_npcs == 0

    def test_population_stats_to_dict(self):
        """Test converting population stats to dictionary."""
        stats = PopulationStats("arkhamcity", "downtown")
        stats.add_npc("shopkeeper", "room_001", True)
        stats.add_npc("passive_mob", "room_002", False)

        stats_dict = stats.to_dict()

        assert stats_dict["zone_id"] == "arkhamcity"
        assert stats_dict["sub_zone_id"] == "downtown"
        assert stats_dict["total_npcs"] == 2
        assert stats_dict["npcs_by_type"]["shopkeeper"] == 1
        assert stats_dict["npcs_by_type"]["passive_mob"] == 1
        assert stats_dict["npcs_by_room"]["room_001"] == 1
        assert stats_dict["npcs_by_room"]["room_002"] == 1
        assert stats_dict["required_npcs"] == 1
        assert stats_dict["optional_npcs"] == 1
        assert "last_updated" in stats_dict
