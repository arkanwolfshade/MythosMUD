"""
Level and XP curve for MythosMUD.

Placeholder implementation: XP required for next level grows logarithmically so the
increase flattens at higher levels. The exact formula will be tuned later; see
character creation revamp plan and ADR.

As noted in the Pnakotic Manuscripts, progression curves that resist simple
extrapolation keep the cosmos from collapsing into predictability.
"""

import math

# Placeholder constants; document in code/ADR that the curve will be tuned later.
# Total XP to reach level N: BASE * log(1 + N * SCALE). Level 1 = 0 XP.
_BASE_XP = 100.0
_SCALE = 10.0


def total_xp_for_level(level: int) -> int:
    """
    Total XP required to reach a given level (cumulative).

    Level 1 requires 0 XP. Level 2+ uses a log-style curve so each level
    requires more than the last but the increase flattens.

    Args:
        level: Target level (1-based).

    Returns:
        Cumulative XP needed to be at that level (minimum).

    Raises:
        ValueError: If level < 1.
    """
    if level < 1:
        raise ValueError("level must be >= 1")
    if level == 1:
        return 0
    # Placeholder: BASE * log(1 + level * SCALE). Curve will be tuned later.
    return int(_BASE_XP * math.log(1.0 + level * _SCALE))


def xp_required_for_level(level: int) -> int:
    """
    XP required to go from (level - 1) to level.

    Args:
        level: Target level (2-based for "XP to reach this level").

    Returns:
        XP needed for that level only (marginal).

    Raises:
        ValueError: If level < 2.
    """
    if level < 2:
        raise ValueError("level must be >= 2 for xp_required_for_level")
    return total_xp_for_level(level) - total_xp_for_level(level - 1)


def level_from_total_xp(total_xp: int) -> int:
    """
    Compute character level from total experience points.

    Uses the same curve as total_xp_for_level; inverts by finding the
    largest level whose total XP <= total_xp.

    Args:
        total_xp: Total experience points (non-negative).

    Returns:
        Level (1-based). Minimum 1.
    """
    if total_xp <= 0:
        return 1
    # Binary search or linear scan. Levels are small; linear is fine.
    level = 1
    while total_xp_for_level(level + 1) <= total_xp:
        level += 1
        # Cap at a reasonable max to avoid infinite loop if curve flattens
        if level >= 1000:
            return 1000
    return level
