"""Unit tests for stats generation."""

from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from server.game.stats_generator import StatsGenerator, generate_random_stats
from server.models import Stats


def test_generate_random_stats_with_seed_is_reproducible():
    first = generate_random_stats(seed=42)
    second = generate_random_stats(seed=42)
    assert first.model_dump() == second.model_dump()


def test_generate_random_stats_values_in_range():
    stats = generate_random_stats(seed=7)
    for attr in ("strength", "dexterity", "constitution", "intelligence", "power", "education", "charisma", "luck"):
        value = getattr(stats, attr)
        assert 15 <= value <= 90
    assert 40 <= stats.size <= 90


def test_roll_stats_unknown_method_falls_back_to_3d6():
    generator = StatsGenerator()
    with patch.object(generator, "_roll_3d6", wraps=generator._roll_3d6) as roll_3d6:
        stats = generator.roll_stats("unknown_method")
        roll_3d6.assert_called_once()
        assert isinstance(stats, Stats)


def test_roll_stats_point_buy_within_bounds():
    generator = StatsGenerator()
    stats = generator.roll_stats("point_buy")
    assert 40 <= stats.strength <= 90


def test_validate_class_prerequisites_passes_investigator():
    generator = StatsGenerator()
    stats = Stats(
        strength=50,
        dexterity=50,
        constitution=50,
        size=50,
        intelligence=70,
        power=50,
        education=60,
        charisma=50,
        luck=50,
    )
    ok, failed = generator.validate_class_prerequisites(stats, "investigator")
    assert ok is True
    assert failed == []


def test_validate_class_prerequisites_fails_occultist():
    generator = StatsGenerator()
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
    ok, failed = generator.validate_class_prerequisites(stats, "occultist")
    assert ok is False
    assert failed


def test_validate_class_prerequisites_unknown_class():
    generator = StatsGenerator()
    stats = generate_random_stats(seed=1)
    ok, failed = generator.validate_class_prerequisites(stats, "unknown_class")
    assert ok is True
    assert failed == []


def test_get_available_classes_filters_by_prerequisites():
    generator = StatsGenerator()
    stats = Stats(
        strength=50,
        dexterity=50,
        constitution=70,
        size=50,
        intelligence=50,
        power=50,
        education=50,
        charisma=50,
        luck=50,
    )
    classes = generator.get_available_classes(stats)
    assert "survivor" in classes
    assert "occultist" not in classes


def test_roll_stats_with_validation_respects_required_class():
    generator = StatsGenerator()
    with patch.object(generator, "roll_stats") as roll_stats:
        roll_stats.side_effect = [
            Stats(
                strength=50,
                dexterity=50,
                constitution=50,
                size=50,
                intelligence=50,
                power=50,
                education=50,
                charisma=50,
                luck=50,
            ),
            Stats(
                strength=50,
                dexterity=50,
                constitution=70,
                size=50,
                intelligence=50,
                power=50,
                education=50,
                charisma=50,
                luck=50,
            ),
        ]
        stats, available = generator.roll_stats_with_validation(required_class="survivor", max_attempts=5)
        assert "survivor" in available
        assert stats.constitution == 70


def test_check_profession_requirements_maps_wisdom_to_power():
    generator = StatsGenerator()
    stats = Stats(
        strength=50,
        dexterity=50,
        constitution=50,
        size=50,
        intelligence=50,
        power=80,
        education=50,
        charisma=50,
        luck=50,
    )
    assert generator._check_profession_requirements(stats, {"wisdom": 70}) is True


def test_check_profession_requirements_unknown_stat_fails():
    generator = StatsGenerator()
    stats = generate_random_stats(seed=3)
    assert generator._check_profession_requirements(stats, {"sanity": 50}) is False


def test_get_stat_summary_includes_totals():
    generator = StatsGenerator()
    stats = generate_random_stats(seed=11)
    summary = generator.get_stat_summary(stats)
    assert "attributes" in summary
    assert summary["total_points"] == int(
        np.sum(
            [
                stats.strength,
                stats.dexterity,
                stats.constitution,
                stats.size,
                stats.intelligence,
                stats.power,
                stats.education,
                stats.charisma,
                stats.luck,
            ]
        )
    )


@pytest.mark.asyncio
async def test_roll_stats_with_profession_no_requirements():
    generator = StatsGenerator()
    profession = MagicMock()
    profession.get_stat_requirements.return_value = {}
    stats, meets = generator.roll_stats_with_profession(profession=profession)
    assert meets is True
    assert isinstance(stats, Stats)


def test_roll_stats_with_profession_missing_profession_raises():
    generator = StatsGenerator()
    with pytest.raises(ValueError, match="Invalid profession ID"):
        generator.roll_stats_with_profession(profession_id=99)
