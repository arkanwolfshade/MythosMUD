"""
Tests for Stats model random number generation.

This module tests the random number generation in the Stats model to ensure
it's deterministic for testing and properly handles edge cases.
"""

from server.models.game import Stats


class TestStatsRandomGeneration:
    """Test random number generation in Stats model."""

    def test_stats_random_generation_deterministic(self):
        """Test that Stats generation is deterministic with same seed."""
        # Create two Stats instances without explicit values
        stats1 = Stats()
        stats2 = Stats()

        # They should have the same values due to fixed seed
        assert stats1.strength == stats2.strength
        assert stats1.dexterity == stats2.dexterity
        assert stats1.constitution == stats2.constitution
        assert stats1.intelligence == stats2.intelligence
        assert stats1.wisdom == stats2.wisdom
        assert stats1.charisma == stats2.charisma

    def test_stats_explicit_values_override_random(self):
        """Test that explicitly provided values override random generation."""
        # Create Stats with explicit values
        stats = Stats(strength=15, dexterity=12, constitution=14, intelligence=16, wisdom=13, charisma=11)

        # Values should match what was provided
        assert stats.strength == 15
        assert stats.dexterity == 12
        assert stats.constitution == 14
        assert stats.intelligence == 16
        assert stats.wisdom == 13
        assert stats.charisma == 11

    def test_stats_partial_explicit_values(self):
        """Test that partial explicit values work correctly."""
        # Create Stats with some explicit values
        stats = Stats(strength=18, intelligence=20)

        # Explicit values should be used
        assert stats.strength == 18
        assert stats.intelligence == 20

        # Other values should be randomly generated
        assert isinstance(stats.dexterity, int)
        assert isinstance(stats.constitution, int)
        assert isinstance(stats.wisdom, int)
        assert isinstance(stats.charisma, int)

        # Random values should be in valid range
        assert 3 <= stats.dexterity <= 18
        assert 3 <= stats.constitution <= 18
        assert 3 <= stats.wisdom <= 18
        assert 3 <= stats.charisma <= 18

    def test_stats_random_values_in_valid_range(self):
        """Test that randomly generated values are in valid range."""
        stats = Stats()

        # All random values should be in valid range (3-18)
        assert 3 <= stats.strength <= 18
        assert 3 <= stats.dexterity <= 18
        assert 3 <= stats.constitution <= 18
        assert 3 <= stats.intelligence <= 18
        assert 3 <= stats.wisdom <= 18
        assert 3 <= stats.charisma <= 18

    def test_stats_default_values_unchanged(self):
        """Test that default values for other fields are unchanged."""
        stats = Stats()

        # Default values should be preserved
        assert stats.sanity == 100
        assert stats.occult_knowledge == 0
        assert stats.fear == 0
        assert stats.corruption == 0
        assert stats.cult_affiliation == 0
        assert stats.current_health == 100

    def test_stats_computed_fields_work_with_random_values(self):
        """Test that computed fields work correctly with random values."""
        stats = Stats()

        # Computed fields should work
        assert stats.max_health == stats.constitution * 10
        assert stats.max_sanity == stats.wisdom * 5

        # Values should be positive
        assert stats.max_health > 0
        assert stats.max_sanity > 0

    def test_stats_validation_with_random_values(self):
        """Test that validation works correctly with random values."""
        stats = Stats()

        # All values should pass validation
        assert 1 <= stats.strength <= 20
        assert 1 <= stats.dexterity <= 20
        assert 1 <= stats.constitution <= 20
        assert 1 <= stats.intelligence <= 20
        assert 1 <= stats.wisdom <= 20
        assert 1 <= stats.charisma <= 20

    def test_stats_serialization_with_random_values(self):
        """Test that serialization works correctly with random values."""
        stats = Stats()

        # Should be able to serialize to dict
        stats_dict = stats.model_dump()

        # All fields should be present
        assert "strength" in stats_dict
        assert "dexterity" in stats_dict
        assert "constitution" in stats_dict
        assert "intelligence" in stats_dict
        assert "wisdom" in stats_dict
        assert "charisma" in stats_dict

        # Values should match
        assert stats_dict["strength"] == stats.strength
        assert stats_dict["dexterity"] == stats.dexterity
        assert stats_dict["constitution"] == stats.constitution
        assert stats_dict["intelligence"] == stats.intelligence
        assert stats_dict["wisdom"] == stats.wisdom
        assert stats_dict["charisma"] == stats.charisma

    def test_stats_deserialization_with_random_values(self):
        """Test that deserialization works correctly with random values."""
        stats = Stats()
        # Only serialize the actual fields, not computed fields
        stats_dict = stats.model_dump(exclude={"max_health", "max_sanity"})

        # Should be able to deserialize from dict
        stats_from_dict = Stats.model_validate(stats_dict)

        # Values should match
        assert stats_from_dict.strength == stats.strength
        assert stats_from_dict.dexterity == stats.dexterity
        assert stats_from_dict.constitution == stats.constitution
        assert stats_from_dict.intelligence == stats.intelligence
        assert stats_from_dict.wisdom == stats.wisdom
        assert stats_from_dict.charisma == stats.charisma

    def test_stats_multiple_instances_consistency(self):
        """Test that multiple instances have consistent random generation."""
        # Create multiple instances
        stats_list = [Stats() for _ in range(5)]

        # All instances should have the same values due to fixed seed
        for i in range(1, len(stats_list)):
            assert stats_list[i].strength == stats_list[0].strength
            assert stats_list[i].dexterity == stats_list[0].dexterity
            assert stats_list[i].constitution == stats_list[0].constitution
            assert stats_list[i].intelligence == stats_list[0].intelligence
            assert stats_list[i].wisdom == stats_list[0].wisdom
            assert stats_list[i].charisma == stats_list[0].charisma

    def test_stats_edge_case_empty_data(self):
        """Test Stats creation with empty data dict."""
        stats = Stats()

        # Should still generate random values
        assert isinstance(stats.strength, int)
        assert isinstance(stats.dexterity, int)
        assert isinstance(stats.constitution, int)
        assert isinstance(stats.intelligence, int)
        assert isinstance(stats.wisdom, int)
        assert isinstance(stats.charisma, int)

    def test_stats_edge_case_none_values(self):
        """Test Stats creation with None values."""
        stats = Stats(strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None)

        # Should generate random values for None fields
        assert isinstance(stats.strength, int)
        assert isinstance(stats.dexterity, int)
        assert isinstance(stats.constitution, int)
        assert isinstance(stats.intelligence, int)
        assert isinstance(stats.wisdom, int)
        assert isinstance(stats.charisma, int)
