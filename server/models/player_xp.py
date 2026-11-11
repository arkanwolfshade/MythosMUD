"""
Experience point (XP) and level rules, as pure functions (ADR-029 step 7b).

The curve is total(L) = 50 * L * (L - 1): level 1 at 0 XP, level 2 at 100, level 3 at 300, level 10 at 4,500. It is a
placeholder (see docs/subsystems/SUBSYSTEM_SKILLS_LEVEL_DESIGN.md). The same curve is the SQL function
``level_for_xp``; an integration test checks that the two agree for every level boundary and the XP either side of it,
so the registry (which grants XP now) and the database cannot drift apart. A level never goes down.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True, slots=True)
class XpChange:
    """One XP award: the totals after it and the level before and after."""

    new_xp: int
    old_level: int
    new_level: int

    @property
    def leveled_up(self) -> bool:
        """True if the award raised the player's level."""
        return self.new_level > self.old_level


def level_for_xp(xp: int) -> int:
    """The level a total of ``xp`` implies: the largest L with 50 * L * (L - 1) <= xp, and at least 1.

    Inverting the curve gives (2L - 1)^2 <= 1 + xp / 12.5, which is done in integers so that a level boundary is exact
    rather than a floating-point near miss.
    """
    odd = isqrt((25 + 2 * max(xp, 0)) // 25)  # the largest 2L - 1 the XP reaches
    return max(1, (odd + 1) // 2)


def awarded(xp: int, level: int, delta: int) -> XpChange:
    """Add ``delta`` XP to a player at ``xp`` and ``level``; the level rises with the curve and never falls."""
    if delta < 0:
        raise ValueError(f"XP delta must be non-negative, got {delta}")
    new_xp = xp + delta
    return XpChange(new_xp, level, max(level, level_for_xp(new_xp)))
