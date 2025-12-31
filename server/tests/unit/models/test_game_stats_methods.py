"""
Additional unit tests for Stats model methods.

Tests Stats methods that may not be fully covered in test_game.py.
"""

from server.models.game import AttributeType, Stats


def test_stats_validate_current_vs_max_stats_caps_dp():
    """Test validate_current_vs_max_stats() caps current_dp at max_dp."""
    stats = Stats(constitution=50, size=50, current_dp=1000)
    # max_dp = (50 + 50) // 5 = 20

    assert stats.current_dp == 20  # Capped at max_dp


def test_stats_validate_current_vs_max_stats_caps_magic_points():
    """Test validate_current_vs_max_stats() caps magic_points at max_magic_points."""
    stats = Stats(power=50, magic_points=1000)
    # max_magic_points = ceil(50 * 0.2) = 10

    assert stats.magic_points == 10  # Capped at max_magic_points


def test_stats_validate_current_vs_max_stats_caps_lucidity():
    """Test validate_current_vs_max_stats() caps lucidity at max_lucidity."""
    stats = Stats(education=50, lucidity=1000)

    assert stats.lucidity == 50  # Capped at max_lucidity (education)


def test_stats_validate_current_vs_max_stats_allows_valid_values():
    """Test validate_current_vs_max_stats() allows values within limits."""
    stats = Stats(constitution=50, size=50, current_dp=15, power=50, magic_points=5, education=50, lucidity=40)
    # max_dp = 20, max_magic_points = 10, max_lucidity = 50

    assert stats.current_dp == 15  # Within limit
    assert stats.magic_points == 5  # Within limit
    assert stats.lucidity == 40  # Within limit


def test_stats_get_attribute_modifier_negative():
    """Test get_attribute_modifier() returns correct modifier for low attribute."""
    stats = Stats(strength=25)

    result = stats.get_attribute_modifier(AttributeType.STR)

    assert result == -13  # (25 - 50) // 2 = -25 // 2 = -13 (integer division rounds down)


def test_stats_get_attribute_modifier_zero():
    """Test get_attribute_modifier() returns 0 for attribute at 50."""
    stats = Stats(strength=50)

    result = stats.get_attribute_modifier(AttributeType.STR)

    assert result == 0  # (50 - 50) // 2 = 0


def test_stats_get_attribute_modifier_different_attribute():
    """Test get_attribute_modifier() works with different attribute types."""
    stats = Stats(dexterity=60, intelligence=40)

    result_dex = stats.get_attribute_modifier(AttributeType.DEX)
    result_int = stats.get_attribute_modifier(AttributeType.INT)

    assert result_dex == 5  # (60 - 50) // 2 = 5
    assert result_int == -5  # (40 - 50) // 2 = -5


def test_stats_max_dp_calculation():
    """Test max_dp() calculation with specific values."""
    stats = Stats(constitution=100, size=50)

    result = stats.max_dp

    assert result == 30  # (100 + 50) // 5 = 30


def test_stats_max_magic_points_calculation():
    """Test max_magic_points() calculation with specific power."""
    stats = Stats(power=100)

    result = stats.max_magic_points

    assert result == 20  # ceil(100 * 0.2) = 20


def test_stats_max_lucidity_calculation():
    """Test max_lucidity() calculation with specific education."""
    stats = Stats(education=80)

    result = stats.max_lucidity

    assert result == 80  # Should equal education
