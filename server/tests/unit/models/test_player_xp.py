"""Unit tests for the XP and level rules (ADR-029 step 7b)."""

import pytest

from server.models.player_xp import awarded, level_for_xp


@pytest.mark.parametrize(
    ("xp", "level"),
    [(0, 1), (1, 1), (99, 1), (100, 2), (299, 2), (300, 3), (4499, 9), (4500, 10), (-5, 1)],
)
def test_the_level_follows_the_curve(xp: int, level: int) -> None:
    assert level_for_xp(xp) == level


@pytest.mark.parametrize("level", range(2, 60))
def test_every_level_boundary_is_exact(level: int) -> None:
    """total(L) = 50 * L * (L - 1): the boundary XP is the first of level L, the XP before it the last of L - 1."""
    boundary = 50 * level * (level - 1)

    assert level_for_xp(boundary) == level
    assert level_for_xp(boundary - 1) == level - 1


def test_an_award_adds_xp_and_raises_the_level() -> None:
    change = awarded(xp=50, level=1, delta=50)

    assert (change.new_xp, change.old_level, change.new_level, change.leveled_up) == (100, 1, 2, True)


def test_an_award_can_skip_levels() -> None:
    assert awarded(xp=0, level=1, delta=4500).new_level == 10


def test_an_award_that_stays_in_the_level_is_not_a_level_up() -> None:
    change = awarded(xp=0, level=1, delta=50)

    assert (change.new_level, change.leveled_up) == (1, False)


def test_a_level_above_the_curve_is_kept() -> None:
    assert awarded(xp=0, level=5, delta=1).new_level == 5


def test_a_negative_award_is_refused() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        _ = awarded(xp=10, level=1, delta=-1)
