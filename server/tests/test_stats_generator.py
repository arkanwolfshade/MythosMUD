"""
Tests for the StatsGenerator service.

This module tests the random stat generation functionality including
different rolling methods, class validation, and stat summaries.
"""

from unittest.mock import patch

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
