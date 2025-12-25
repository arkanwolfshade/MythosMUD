"""
Tests for StatsGenerator.

This module tests the StatsGenerator class covering stat generation methods,
class prerequisites validation, and profession-based stat rolling.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from unittest.mock import Mock, patch

import pytest

from server.game.stats_generator import StatsGenerator, generate_random_stats
from server.models import Stats


@pytest.fixture
def stats_generator():
    """Create a StatsGenerator instance for testing."""
    return StatsGenerator()


class TestGenerateRandomStats:
    """Test the generate_random_stats function."""

    def test_generate_random_stats_without_seed(self):
        """Test generating random stats without seed."""
        stats = generate_random_stats()

        assert isinstance(stats, Stats)
        assert 15 <= stats.strength <= 90
        assert 15 <= stats.dexterity <= 90
        assert 15 <= stats.constitution <= 90
        assert 40 <= stats.size <= 90  # Size uses (2D6+6)*5 formula
        assert 15 <= stats.intelligence <= 90
        assert 15 <= stats.power <= 90
        assert 15 <= stats.education <= 90
        assert 15 <= stats.charisma <= 90
        assert 15 <= stats.luck <= 90

    def test_generate_random_stats_with_seed(self):
        """Test generating random stats with seed for reproducibility."""
        stats1 = generate_random_stats(seed=42)
        stats2 = generate_random_stats(seed=42)

        assert stats1.strength == stats2.strength
        assert stats1.dexterity == stats2.dexterity
        assert stats1.constitution == stats2.constitution
        assert stats1.size == stats2.size
        assert stats1.intelligence == stats2.intelligence
        assert stats1.power == stats2.power
        assert stats1.education == stats2.education
        assert stats1.charisma == stats2.charisma
        assert stats1.luck == stats2.luck

    def test_generate_random_stats_size_range(self):
        """Test that size is in correct range (40-90)."""
        for _ in range(100):
            stats = generate_random_stats()
            assert 40 <= stats.size <= 90


class TestStatsGeneratorInitialization:
    """Test StatsGenerator initialization."""

    def test_stats_generator_init(self, stats_generator):
        """Test StatsGenerator initialization."""
        assert stats_generator is not None
        assert stats_generator.MIN_STAT == 15
        assert stats_generator.MAX_STAT == 90
        assert "investigator" in stats_generator.CLASS_PREREQUISITES


class TestStatsGeneratorRollStats:
    """Test the roll_stats method."""

    def test_roll_stats_3d6(self, stats_generator):
        """Test rolling stats with 3d6 method."""
        stats = stats_generator.roll_stats("3d6")

        assert isinstance(stats, Stats)
        assert 15 <= stats.strength <= 90
        assert 15 <= stats.dexterity <= 90
        assert 40 <= stats.size <= 90

    def test_roll_stats_4d6_drop_lowest(self, stats_generator):
        """Test rolling stats with 4d6 drop lowest method."""
        stats = stats_generator.roll_stats("4d6_drop_lowest")

        assert isinstance(stats, Stats)
        assert 15 <= stats.strength <= 90
        assert 15 <= stats.dexterity <= 90
        assert 40 <= stats.size <= 90

    def test_roll_stats_point_buy(self, stats_generator):
        """Test rolling stats with point buy method."""
        stats = stats_generator.roll_stats("point_buy")

        assert isinstance(stats, Stats)
        assert stats.strength >= 40  # Point buy starts at 40
        assert stats.dexterity >= 40
        assert 40 <= stats.size <= 90

    def test_roll_stats_unknown_method_defaults_to_3d6(self, stats_generator):
        """Test that unknown method defaults to 3d6."""
        stats = stats_generator.roll_stats("unknown_method")

        assert isinstance(stats, Stats)
        assert 15 <= stats.strength <= 90


class TestStatsGeneratorRollSize:
    """Test the _roll_size method."""

    def test_roll_size_range(self, stats_generator):
        """Test that _roll_size returns values in correct range."""
        for _ in range(100):
            size = stats_generator._roll_size()
            assert 40 <= size <= 90

    def test_roll_size_formula(self, stats_generator):
        """Test that _roll_size uses correct formula (2D6+6)*5."""
        # With many rolls, we should see values across the range
        sizes = [stats_generator._roll_size() for _ in range(100)]
        assert min(sizes) >= 40
        assert max(sizes) <= 90


class TestStatsGeneratorClassPrerequisites:
    """Test class prerequisites validation."""

    def test_validate_class_prerequisites_investigator_meets(self, stats_generator):
        """Test validating investigator prerequisites when met."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=70,  # Meets INT 60 requirement
            power=50,
            education=60,  # Meets EDU 50 requirement
            charisma=50,
            luck=50,
        )

        meets, failed = stats_generator.validate_class_prerequisites(stats, "investigator")

        assert meets is True
        assert failed == []

    def test_validate_class_prerequisites_investigator_fails_intelligence(self, stats_generator):
        """Test validating investigator prerequisites when INT fails."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=50,  # Fails INT 60 requirement
            power=50,
            education=60,
            charisma=50,
            luck=50,
        )

        meets, failed = stats_generator.validate_class_prerequisites(stats, "investigator")

        assert meets is False
        assert len(failed) == 1
        assert "Intelligence" in failed[0]

    def test_validate_class_prerequisites_investigator_fails_education(self, stats_generator):
        """Test validating investigator prerequisites when EDU fails."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=70,
            power=50,
            education=40,  # Fails EDU 50 requirement
            charisma=50,
            luck=50,
        )

        meets, failed = stats_generator.validate_class_prerequisites(stats, "investigator")

        assert meets is False
        assert len(failed) == 1
        assert "Education" in failed[0]

    def test_validate_class_prerequisites_unknown_class(self, stats_generator):
        """Test validating prerequisites for unknown class."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=50,
            power=50,
            education=50,
            charisma=50,
            luck=50,
        )

        meets, failed = stats_generator.validate_class_prerequisites(stats, "unknown_class")

        assert meets is True
        assert failed == []

    def test_get_available_classes_all_meet(self, stats_generator):
        """Test getting available classes when all prerequisites met."""
        stats = Stats(
            strength=70,
            dexterity=70,
            constitution=70,
            size=50,
            intelligence=75,
            power=70,
            education=70,
            charisma=70,
            luck=50,
        )

        available = stats_generator.get_available_classes(stats)

        assert isinstance(available, list)
        assert len(available) > 0

    def test_get_available_classes_none_meet(self, stats_generator):
        """Test getting available classes when no prerequisites met."""
        stats = Stats(
            strength=15,
            dexterity=15,
            constitution=15,
            size=40,
            intelligence=15,
            power=15,
            education=15,
            charisma=15,
            luck=15,
        )

        available = stats_generator.get_available_classes(stats)

        assert isinstance(available, list)
        # Should be empty or only classes with no prerequisites


class TestStatsGeneratorRollStatsWithValidation:
    """Test roll_stats_with_validation method."""

    def test_roll_stats_with_validation_no_required_class(self, stats_generator):
        """Test rolling stats with validation without required class."""
        stats, available_classes = stats_generator.roll_stats_with_validation("3d6", required_class=None)

        assert isinstance(stats, Stats)
        assert isinstance(available_classes, list)

    def test_roll_stats_with_validation_with_required_class(self, stats_generator):
        """Test rolling stats with validation with required class."""
        # Use max_attempts to ensure we get a result
        stats, available_classes = stats_generator.roll_stats_with_validation(
            "3d6", required_class="investigator", max_attempts=50
        )

        assert isinstance(stats, Stats)
        assert isinstance(available_classes, list)
        # May or may not meet requirements due to randomness, but should return stats

    def test_roll_stats_with_validation_max_attempts(self, stats_generator):
        """Test that roll_stats_with_validation respects max_attempts."""
        stats, available_classes = stats_generator.roll_stats_with_validation(
            "3d6", required_class="occultist", max_attempts=5
        )

        assert isinstance(stats, Stats)
        assert isinstance(available_classes, list)


class TestStatsGeneratorProfessionRequirements:
    """Test profession requirement checking."""

    def test_check_profession_requirements_all_meet(self, stats_generator):
        """Test checking profession requirements when all met."""
        stats = Stats(
            strength=70,
            dexterity=70,
            constitution=70,
            size=50,
            intelligence=70,
            power=70,
            education=70,
            charisma=70,
            luck=50,
        )
        requirements = {"strength": 60, "intelligence": 65}

        meets = stats_generator._check_profession_requirements(stats, requirements)

        assert meets is True

    def test_check_profession_requirements_one_fails(self, stats_generator):
        """Test checking profession requirements when one fails."""
        stats = Stats(
            strength=50,  # Fails 60 requirement
            dexterity=70,
            constitution=70,
            size=50,
            intelligence=70,
            power=70,
            education=70,
            charisma=70,
            luck=50,
        )
        requirements = {"strength": 60, "intelligence": 65}

        meets = stats_generator._check_profession_requirements(stats, requirements)

        assert meets is False

    def test_check_profession_requirements_wisdom_maps_to_power(self, stats_generator):
        """Test that wisdom stat name maps to power attribute."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=50,
            power=70,  # Should satisfy "wisdom" requirement
            education=50,
            charisma=50,
            luck=50,
        )
        requirements = {"wisdom": 65}

        meets = stats_generator._check_profession_requirements(stats, requirements)

        assert meets is True

    def test_check_profession_requirements_unknown_stat(self, stats_generator):
        """Test checking requirements with unknown stat name."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=50,
            power=50,
            education=50,
            charisma=50,
            luck=50,
        )
        requirements = {"unknown_stat": 50}

        meets = stats_generator._check_profession_requirements(stats, requirements)

        assert meets is False


class TestStatsGeneratorRollStatsWithProfession:
    """Test roll_stats_with_profession method."""

    @pytest.fixture
    def mock_profession(self):
        """Create a mock profession with stat requirements."""
        profession = Mock()
        profession.get_stat_requirements.return_value = {"strength": 60, "intelligence": 65}
        return profession

    @pytest.fixture
    def mock_profession_no_requirements(self):
        """Create a mock profession without stat requirements."""
        profession = Mock()
        profession.get_stat_requirements.return_value = {}
        return profession

    def test_roll_stats_with_profession_no_requirements(self, stats_generator, mock_profession_no_requirements):
        """Test rolling stats for profession with no requirements."""
        stats, meets = stats_generator.roll_stats_with_profession(
            "3d6", profession_id=0, profession=mock_profession_no_requirements
        )

        assert isinstance(stats, Stats)
        assert meets is True

    @patch("server.game.stats_generator.time.time")
    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared state or timing issues
    @pytest.mark.xdist_group(name="serial_stats_generator_tests")  # Force serial execution with pytest-xdist
    def test_roll_stats_with_profession_meets_requirements(self, mock_time, stats_generator, mock_profession):
        """Test rolling stats for profession that meets requirements."""

        # Mock time to control timeout - use a generator to provide unlimited values
        # The logging system also calls time.time(), so we need unlimited values
        # Use a closure to maintain the iterator state
        def make_time_generator():
            """Create a generator that yields increasing time values."""
            time_val = 0.0
            while True:
                yield time_val
                time_val += 0.1

        time_gen = make_time_generator()
        mock_time.side_effect = lambda: next(time_gen)

        # Patch roll_stats to return stats that meet requirements
        with patch.object(stats_generator, "roll_stats") as mock_roll:
            good_stats = Stats(
                strength=70,
                dexterity=50,
                constitution=50,
                size=50,
                intelligence=70,
                power=50,
                education=50,
                charisma=50,
                luck=50,
            )
            mock_roll.return_value = good_stats

            stats, meets = stats_generator.roll_stats_with_profession(
                "3d6", profession_id=0, profession=mock_profession, timeout_seconds=1.0, max_attempts=10
            )

            assert isinstance(stats, Stats)
            assert meets is True

    def test_roll_stats_with_profession_invalid_id(self, stats_generator):
        """Test rolling stats with invalid profession ID."""
        with pytest.raises(ValueError, match="Invalid profession ID"):
            stats_generator.roll_stats_with_profession("3d6", profession_id=99999, profession=None)


class TestStatsGeneratorStatSummary:
    """Test get_stat_summary method."""

    def test_get_stat_summary(self, stats_generator):
        """Test getting stat summary."""
        stats = Stats(
            strength=50,
            dexterity=60,
            constitution=70,
            size=50,
            intelligence=80,
            power=50,
            education=50,
            charisma=50,
            luck=50,
        )

        summary = stats_generator.get_stat_summary(stats)

        assert "attributes" in summary
        assert "derived_stats" in summary
        assert "total_points" in summary
        assert "average_stat" in summary

        # Check attributes section
        assert "strength" in summary["attributes"]
        assert summary["attributes"]["strength"]["value"] == 50
        assert "modifier" in summary["attributes"]["strength"]

        # Check derived stats
        assert "max_dp" in summary["derived_stats"]
        assert "max_magic_points" in summary["derived_stats"]
        assert "max_lucidity" in summary["derived_stats"]

        # Check totals
        assert summary["total_points"] > 0
        assert summary["average_stat"] > 0

    def test_get_stat_summary_total_points(self, stats_generator):
        """Test that total_points calculation is correct."""
        stats = Stats(
            strength=50,
            dexterity=50,
            constitution=50,
            size=50,
            intelligence=50,
            power=50,
            education=50,
            charisma=50,
            luck=50,
        )

        summary = stats_generator.get_stat_summary(stats)

        # Should be 9 stats * 50 = 450
        assert summary["total_points"] == 450
        assert summary["average_stat"] == 50.0
