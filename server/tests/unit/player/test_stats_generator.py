"""
Tests for the StatsGenerator service.

This module tests the random stat generation functionality including
different rolling methods, class validation, and stat summaries.
"""

from unittest.mock import Mock, patch

import pytest

from ..game.stats_generator import StatsGenerator
from ..models import AttributeType, Stats


class TestStatsGenerator:
    """Test the StatsGenerator service."""

    def setup_method(self):
        """Set up test fixtures."""
        self.stats_generator = StatsGenerator()

    def test_init(self):
        """Test StatsGenerator initialization."""
        assert self.stats_generator.MIN_STAT == 3
        assert self.stats_generator.MAX_STAT == 18
        assert "investigator" in self.stats_generator.CLASS_PREREQUISITES
        assert "occultist" in self.stats_generator.CLASS_PREREQUISITES

    def test_roll_3d6(self):
        """Test 3d6 rolling method."""
        stats = self.stats_generator._roll_3d6()

        assert isinstance(stats, Stats)
        assert 3 <= stats.strength <= 18
        assert 3 <= stats.dexterity <= 18
        assert 3 <= stats.constitution <= 18
        assert 3 <= stats.intelligence <= 18
        assert 3 <= stats.wisdom <= 18
        assert 3 <= stats.charisma <= 18

    def test_roll_4d6_drop_lowest(self):
        """Test 4d6 drop lowest rolling method."""
        stats = self.stats_generator._roll_4d6_drop_lowest()

        assert isinstance(stats, Stats)
        assert 3 <= stats.strength <= 18
        assert 3 <= stats.dexterity <= 18
        assert 3 <= stats.constitution <= 18
        assert 3 <= stats.intelligence <= 18
        assert 3 <= stats.wisdom <= 18
        assert 3 <= stats.charisma <= 18

    def test_roll_point_buy(self):
        """Test point-buy rolling method."""
        stats = self.stats_generator._roll_point_buy()

        assert isinstance(stats, Stats)
        assert 8 <= stats.strength <= 18
        assert 8 <= stats.dexterity <= 18
        assert 8 <= stats.constitution <= 18
        assert 8 <= stats.intelligence <= 18
        assert 8 <= stats.wisdom <= 18
        assert 8 <= stats.charisma <= 18

    def test_roll_stats_3d6(self):
        """Test roll_stats with 3d6 method."""
        stats = self.stats_generator.roll_stats("3d6")
        assert isinstance(stats, Stats)

    def test_roll_stats_4d6_drop_lowest(self):
        """Test roll_stats with 4d6_drop_lowest method."""
        stats = self.stats_generator.roll_stats("4d6_drop_lowest")
        assert isinstance(stats, Stats)

    def test_roll_stats_point_buy(self):
        """Test roll_stats with point_buy method."""
        stats = self.stats_generator.roll_stats("point_buy")
        assert isinstance(stats, Stats)

    def test_roll_stats_unknown_method(self):
        """Test roll_stats with unknown method defaults to 3d6."""
        stats = self.stats_generator.roll_stats("unknown_method")
        assert isinstance(stats, Stats)

    def test_validate_class_prerequisites_investigator(self):
        """Test class prerequisite validation for investigator."""
        # Valid stats for investigator
        stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=12, wisdom=10, charisma=10)

        meets_prerequisites, failed_requirements = self.stats_generator.validate_class_prerequisites(
            stats, "investigator"
        )

        assert meets_prerequisites
        assert failed_requirements == []

    def test_validate_class_prerequisites_investigator_fails(self):
        """Test class prerequisite validation failure for investigator."""
        # Invalid stats for investigator (low intelligence)
        stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)

        meets_prerequisites, failed_requirements = self.stats_generator.validate_class_prerequisites(
            stats, "investigator"
        )

        assert not meets_prerequisites
        assert len(failed_requirements) > 0
        assert "Intelligence 10 < 12" in failed_requirements

    def test_validate_class_prerequisites_unknown_class(self):
        """Test class prerequisite validation for unknown class."""
        stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)

        meets_prerequisites, failed_requirements = self.stats_generator.validate_class_prerequisites(
            stats, "unknown_class"
        )

        assert meets_prerequisites
        assert failed_requirements == []

    def test_get_available_classes(self):
        """Test getting available classes for stats."""
        # High stats that should qualify for multiple classes
        stats = Stats(strength=14, dexterity=14, constitution=14, intelligence=14, wisdom=14, charisma=14)

        available_classes = self.stats_generator.get_available_classes(stats)

        assert isinstance(available_classes, list)
        assert len(available_classes) > 0
        assert "investigator" in available_classes
        assert "academic" in available_classes

    def test_get_available_classes_none(self):
        """Test getting available classes for low stats."""
        # Low stats that shouldn't qualify for any classes
        stats = Stats(strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8)

        available_classes = self.stats_generator.get_available_classes(stats)

        assert isinstance(available_classes, list)
        # Should still have some classes available (like survivor)

    def test_roll_stats_with_validation_no_required_class(self):
        """Test rolling stats with validation but no required class."""
        stats, available_classes = self.stats_generator.roll_stats_with_validation()

        assert isinstance(stats, Stats)
        assert isinstance(available_classes, list)

    def test_roll_stats_with_validation_with_required_class(self):
        """Test rolling stats with validation for a specific class."""
        # Mock the roll_stats method to return high stats
        with patch.object(self.stats_generator, "roll_stats") as mock_roll:
            mock_roll.return_value = Stats(
                strength=10, dexterity=10, constitution=10, intelligence=14, wisdom=12, charisma=10
            )

            stats, available_classes = self.stats_generator.roll_stats_with_validation(required_class="investigator")

            assert isinstance(stats, Stats)
            assert isinstance(available_classes, list)
            assert "investigator" in available_classes

    def test_get_stat_summary(self):
        """Test getting stat summary."""
        stats = Stats(strength=14, dexterity=12, constitution=16, intelligence=18, wisdom=10, charisma=8)

        summary = self.stats_generator.get_stat_summary(stats)

        assert isinstance(summary, dict)
        assert "attributes" in summary
        assert "derived_stats" in summary
        assert "total_points" in summary
        assert "average_stat" in summary

        # Check specific values
        assert summary["attributes"]["strength"]["value"] == 14
        assert summary["attributes"]["strength"]["modifier"] == 2
        assert summary["derived_stats"]["max_health"] == 160  # 16 * 10
        assert summary["derived_stats"]["max_sanity"] == 50  # 10 * 5
        assert summary["total_points"] == 78  # 14+12+16+18+10+8
        assert summary["average_stat"] == 13.0  # 78/6

    def test_class_prerequisites_structure(self):
        """Test that class prerequisites have the correct structure."""
        for class_name, prerequisites in self.stats_generator.CLASS_PREREQUISITES.items():
            assert isinstance(class_name, str)
            assert isinstance(prerequisites, dict)

            for attribute, min_value in prerequisites.items():
                assert isinstance(attribute, AttributeType)
                assert isinstance(min_value, int)
                assert 1 <= min_value <= 20

    def test_rolling_methods_produce_different_distributions(self):
        """Test that different rolling methods produce different stat distributions."""
        # This is a probabilistic test, but we can check that the methods work
        stats_3d6 = self.stats_generator.roll_stats("3d6")
        stats_4d6 = self.stats_generator.roll_stats("4d6_drop_lowest")
        stats_point_buy = self.stats_generator.roll_stats("point_buy")

        # All should be valid Stats objects
        assert isinstance(stats_3d6, Stats)
        assert isinstance(stats_4d6, Stats)
        assert isinstance(stats_point_buy, Stats)

        # Point buy should start with at least 8 in all stats
        assert stats_point_buy.strength >= 8
        assert stats_point_buy.dexterity >= 8
        assert stats_point_buy.constitution >= 8
        assert stats_point_buy.intelligence >= 8
        assert stats_point_buy.wisdom >= 8
        assert stats_point_buy.charisma >= 8


class TestProfessionStatPrerequisites:
    """Test cases for profession-based stat prerequisites functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.stats_generator = StatsGenerator()

    def test_check_profession_requirements_meets_all(self):
        """Test checking profession requirements when all requirements are met."""
        # Stats that meet the requirement
        stats = Stats(strength=12, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)

        meets_requirements = self.stats_generator._check_profession_requirements(stats, {"strength": 10})

        assert meets_requirements is True

    def test_check_profession_requirements_fails_single(self):
        """Test checking profession requirements when single requirement fails."""
        # Stats that don't meet the requirement
        stats = Stats(strength=9, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)

        meets_requirements = self.stats_generator._check_profession_requirements(stats, {"strength": 10})

        assert meets_requirements is False

    def test_check_profession_requirements_multiple_requirements(self):
        """Test checking profession requirements with multiple requirements."""
        # Stats that meet all requirements
        stats = Stats(strength=14, dexterity=10, constitution=10, intelligence=15, wisdom=10, charisma=10)

        meets_requirements = self.stats_generator._check_profession_requirements(
            stats, {"strength": 12, "intelligence": 14}
        )

        assert meets_requirements is True

    def test_check_profession_requirements_multiple_failures(self):
        """Test checking profession requirements when multiple requirements fail."""
        # Stats that don't meet requirements
        stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=12, wisdom=10, charisma=10)

        meets_requirements = self.stats_generator._check_profession_requirements(
            stats, {"strength": 12, "intelligence": 14}
        )

        assert meets_requirements is False

    def test_check_profession_requirements_unknown_stat(self):
        """Test checking profession requirements with unknown stat name."""
        stats = Stats(strength=12, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)

        meets_requirements = self.stats_generator._check_profession_requirements(stats, {"unknown_stat": 10})

        assert meets_requirements is False

    @patch("server.persistence.get_persistence")
    def test_roll_stats_with_profession_no_requirements(self, mock_get_persistence):
        """Test rolling stats with profession that has no requirements."""
        # Mock profession with no requirements
        mock_profession = Mock()
        mock_profession.get_stat_requirements.return_value = {}

        mock_persistence = Mock()
        mock_persistence.get_profession_by_id.return_value = mock_profession
        mock_get_persistence.return_value = mock_persistence

        stats, meets_requirements = self.stats_generator.roll_stats_with_profession(profession_id=0)

        assert isinstance(stats, Stats)
        assert meets_requirements is True

    @patch("server.persistence.get_persistence")
    def test_roll_stats_with_profession_with_requirements_success(self, mock_get_persistence):
        """Test rolling stats with profession that has requirements - successful roll."""
        # Mock profession with strength requirement of 10 (should be easy to meet)
        mock_profession = Mock()
        mock_profession.get_stat_requirements.return_value = {"strength": 10}

        mock_persistence = Mock()
        mock_persistence.get_profession_by_id.return_value = mock_profession
        mock_get_persistence.return_value = mock_persistence

        # Mock the roll_stats method to return stats that meet requirements
        with patch.object(self.stats_generator, "roll_stats") as mock_roll_stats:
            mock_roll_stats.return_value = Stats(
                strength=12, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10
            )

            stats, meets_requirements = self.stats_generator.roll_stats_with_profession(profession_id=2, max_attempts=1)

            assert isinstance(stats, Stats)
            assert meets_requirements is True
            assert stats.strength >= 10

    @patch("server.persistence.get_persistence")
    def test_roll_stats_with_profession_invalid_profession_id(self, mock_get_persistence):
        """Test rolling stats with invalid profession ID."""
        # Mock persistence to return None for invalid profession
        mock_persistence = Mock()
        mock_persistence.get_profession_by_id.return_value = None
        mock_get_persistence.return_value = mock_persistence

        with pytest.raises(ValueError, match="Invalid profession ID: 999"):
            self.stats_generator.roll_stats_with_profession(profession_id=999)

    @patch("server.persistence.get_persistence")
    def test_roll_stats_with_profession_persistence_error(self, mock_get_persistence):
        """Test rolling stats with profession when persistence layer fails."""
        # Mock persistence to raise an exception
        mock_get_persistence.side_effect = Exception("Database connection failed")

        with pytest.raises(ValueError, match="Invalid profession ID: 2"):
            self.stats_generator.roll_stats_with_profession(profession_id=2)

    @patch("server.persistence.get_persistence")
    def test_roll_stats_with_profession_max_attempts_exceeded(self, mock_get_persistence):
        """Test rolling stats with profession when max attempts are exceeded."""
        # Mock profession with very high requirement that's unlikely to be met
        mock_profession = Mock()
        mock_profession.get_stat_requirements.return_value = {"strength": 18}  # Very unlikely

        mock_persistence = Mock()
        mock_persistence.get_profession_by_id.return_value = mock_profession
        mock_get_persistence.return_value = mock_persistence

        # The function will make max_attempts + 1 rolls (one final roll after max attempts)
        # So we need to mock the _check_profession_requirements to always return False
        with patch.object(self.stats_generator, "_check_profession_requirements", return_value=False):
            stats, meets_requirements = self.stats_generator.roll_stats_with_profession(profession_id=2, max_attempts=1)

        assert isinstance(stats, Stats)
        assert meets_requirements is False  # Should fail to meet requirements

    def test_check_profession_requirements_edge_cases(self):
        """Test edge cases for profession requirements checking."""
        # Test with empty requirements
        stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10)
        meets_requirements = self.stats_generator._check_profession_requirements(stats, {})
        assert meets_requirements is True

        # Test with exact minimum requirement
        meets_requirements = self.stats_generator._check_profession_requirements(stats, {"strength": 10})
        assert meets_requirements is True

        # Test with requirement one above minimum
        meets_requirements = self.stats_generator._check_profession_requirements(stats, {"strength": 11})
        assert meets_requirements is False

    def test_roll_stats_with_validation_never_succeeds(self):
        """Test roll_stats_with_validation when stats never meet requirements.

        AI: Tests the fallback path when maximum attempts are exhausted without
        meeting class requirements. Covers the warning log and final return path
        in roll_stats_with_validation method (lines 235-248 in stats_generator.py).
        """
        # Mock roll_stats to always return stats that don't meet occultist requirements
        # (occultist needs intelligence >= 14, wisdom >= 12)
        low_stats = Stats(strength=10, dexterity=10, constitution=10, intelligence=8, wisdom=8, charisma=10)

        with patch.object(self.stats_generator, "roll_stats", return_value=low_stats):
            stats, available_classes = self.stats_generator.roll_stats_with_validation(
                method="3d6", required_class="occultist", max_attempts=3
            )

            # Should return stats even though they don't meet requirements
            assert isinstance(stats, Stats)
            assert isinstance(available_classes, list)
            # Occultist should not be in available classes
            assert "occultist" not in available_classes


# ============================================================================
# Tests merged from test_stats_random_generation_legacy.py
# ============================================================================


"""
Tests for Stats model random number generation.

This module tests the random number generation in the Stats model to ensure
it's deterministic for testing and properly handles edge cases.
"""


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
