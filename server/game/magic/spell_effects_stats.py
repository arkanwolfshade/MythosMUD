"""
Stat modification helpers for spell effects.

This module contains utility functions extracted from spell_effects to
keep the main spell effects engine focused and within module size limits.
"""

from typing import Any

from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

_VALID_STAT_NAMES = (
    "strength",
    "dexterity",
    "constitution",
    "size",
    "intelligence",
    "power",
    "education",
    "charisma",
    "luck",
)


def apply_stat_modifications(
    stats: dict[str, Any],
    stat_modifications: dict[str, Any],
    mastery_modifier: float,
    spell_id: str,
) -> tuple[dict[str, Any], dict[str, int], list[str]]:
    """
    Apply stat modification dict to stats.

    Returns (updated stats, stat_changes, modified_stats list).
    """
    stat_changes: dict[str, int] = {}
    modified_stats: list[str] = []
    for stat_name, change_amount in stat_modifications.items():
        if stat_name not in _VALID_STAT_NAMES:
            logger.warning("Invalid stat name in spell effect", stat_name=stat_name, spell_id=spell_id)
            continue
        adjusted_change = int(change_amount * mastery_modifier)
        current_value = stats.get(stat_name, 50)
        new_value = max(1, min(100, current_value + adjusted_change))
        stats[stat_name] = new_value
        stat_changes[stat_name] = adjusted_change
        modified_stats.append(f"{stat_name} ({adjusted_change:+d})")
    return (stats, stat_changes, modified_stats)
