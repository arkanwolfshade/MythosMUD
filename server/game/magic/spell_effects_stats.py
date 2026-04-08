"""
Stat modification helpers for spell effects.

This module contains utility functions extracted from spell_effects to
keep the main spell effects engine focused and within module size limits.
"""

from structlog.stdlib import BoundLogger

from server.structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)

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
    stats: dict[str, object],
    stat_modifications: dict[str, object],
    mastery_modifier: float,
    spell_id: str,
) -> tuple[dict[str, object], dict[str, int], list[str]]:
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
        if isinstance(change_amount, (int, float)):
            coerced = float(change_amount)
        elif isinstance(change_amount, str) and change_amount.strip():
            try:
                coerced = float(change_amount)
            except ValueError:
                continue
        else:
            continue
        adjusted_change = int(coerced * mastery_modifier)
        cur_raw = stats.get(stat_name, 50)
        current_value = int(cur_raw) if isinstance(cur_raw, (int, float)) else 50
        new_value = max(1, min(100, current_value + adjusted_change))
        stats[stat_name] = new_value
        stat_changes[stat_name] = adjusted_change
        modified_stats.append(f"{stat_name} ({adjusted_change:+d})")
    return (stats, stat_changes, modified_stats)
