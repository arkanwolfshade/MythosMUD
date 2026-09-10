"""Unit tests for the corruption tier model (#804)."""

import pytest

from server.models.corruption import CorruptionTier, compute_tier


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, CorruptionTier.PURE),
        (24, CorruptionTier.PURE),
        (25, CorruptionTier.MARKED),
        (49, CorruptionTier.MARKED),
        (50, CorruptionTier.CORRUPTED),
        (74, CorruptionTier.CORRUPTED),
        (75, CorruptionTier.WARPED),
        (100, CorruptionTier.WARPED),
    ],
)
def test_compute_tier_boundaries(value: int, expected: CorruptionTier) -> None:
    """Every tier boundary from SUBSYSTEM_CORRUPTION_DESIGN.md's table, both edges."""
    assert compute_tier(value) is expected


def test_compute_tier_corrupted_floor_matches_is_corrupted() -> None:
    """The `corrupted` tier's floor MUST stay at 50 -- Stats.is_corrupted() depends on it."""
    assert compute_tier(49) is not CorruptionTier.CORRUPTED
    assert compute_tier(50) is CorruptionTier.CORRUPTED


if __name__ == "__main__":
    # ponytail: smallest runnable check for the tier-boundary math, per house convention.
    for value, expected in [(0, "pure"), (25, "marked"), (50, "corrupted"), (75, "warped")]:
        tier = compute_tier(value)
        assert tier == expected, f"compute_tier({value}) = {tier}, expected {expected}"
    print("compute_tier boundary demo OK")
