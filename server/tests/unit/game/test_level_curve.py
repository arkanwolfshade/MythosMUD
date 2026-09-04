"""
Unit tests for level curve (XP to level, level from total XP).

Character creation revamp plan 4.1: placeholder logarithmic-style curve.
"""

import pytest

from server.game.level_curve import (
    level_from_total_xp,
    total_xp_for_level,
    xp_required_for_level,
)


def test_total_xp_for_level_one():
    """Level 1 requires 0 cumulative XP."""
    assert total_xp_for_level(1) == 0


def test_total_xp_for_level_two_positive():
    """Level 2 requires positive cumulative XP."""
    assert total_xp_for_level(2) > 0


def test_total_xp_for_level_increases():
    """Cumulative XP increases with level."""
    prev = 0
    for level in range(1, 6):
        xp = total_xp_for_level(level)
        assert xp >= prev
        prev = xp


def test_total_xp_for_level_invalid():
    """total_xp_for_level raises for level < 1."""
    with pytest.raises(ValueError, match="level must be >= 1"):
        total_xp_for_level(0)
    with pytest.raises(ValueError, match="level must be >= 1"):
        total_xp_for_level(-1)


def test_xp_required_for_level_marginal():
    """xp_required_for_level(2) equals total_xp_for_level(2) - total_xp_for_level(1)."""
    assert xp_required_for_level(2) == total_xp_for_level(2) - total_xp_for_level(1)


def test_xp_required_for_level_invalid():
    """xp_required_for_level raises for level < 2."""
    with pytest.raises(ValueError, match="level must be >= 2"):
        xp_required_for_level(1)
    with pytest.raises(ValueError, match="level must be >= 2"):
        xp_required_for_level(0)


def test_level_from_total_xp_zero():
    """Zero XP gives level 1."""
    assert level_from_total_xp(0) == 1


def test_level_from_total_xp_negative():
    """Negative XP treated as zero gives level 1."""
    assert level_from_total_xp(-1) == 1


def test_level_from_total_xp_roundtrip():
    """level_from_total_xp(total_xp_for_level(n)) >= n (at least that level)."""
    for level in [1, 2, 3, 5, 10]:
        total = total_xp_for_level(level)
        assert level_from_total_xp(total) >= level


def test_level_from_total_xp_threshold_level_two():
    """XP just below total_xp_for_level(2) gives level 1; at or above gives level 2."""
    threshold = total_xp_for_level(2)
    assert level_from_total_xp(threshold - 1) == 1
    assert level_from_total_xp(threshold) == 2
    assert level_from_total_xp(threshold + 1) == 2
