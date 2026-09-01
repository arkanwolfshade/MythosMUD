"""Stat summary helpers for StatsGenerator (keeps stats_generator under module line limit)."""

from __future__ import annotations

import numpy as np

from ..models.game import AttributeType, Stats

_ATTRIBUTE_SUMMARY_SPECS: tuple[tuple[AttributeType, str], ...] = (
    (AttributeType.STR, "strength"),
    (AttributeType.DEX, "dexterity"),
    (AttributeType.CON, "constitution"),
    (AttributeType.SIZ, "size"),
    (AttributeType.INT, "intelligence"),
    (AttributeType.POW, "power"),
    (AttributeType.EDU, "education"),
    (AttributeType.CHA, "charisma"),
    (AttributeType.LUCK, "luck"),
)


def _stat_value_for_summary(value: int | None) -> int:
    """Coerce optional stat ints for summary totals (matches legacy ``or 50`` fallback)."""
    return value if value is not None else 50


def _read_core_stat_value(stats: Stats, field: str) -> int | None:
    """Read a core stat field from Stats without getattr (avoids reportAny)."""
    match field:
        case "strength":
            return stats.strength
        case "dexterity":
            return stats.dexterity
        case "constitution":
            return stats.constitution
        case "size":
            return stats.size
        case "intelligence":
            return stats.intelligence
        case "power":
            return stats.power
        case "education":
            return stats.education
        case "charisma":
            return stats.charisma
        case "luck":
            return stats.luck
        case _:
            return None


def _build_attribute_summary(stats: Stats) -> dict[str, object]:
    """Build per-attribute value and modifier entries for stat summary."""
    return {
        field: {
            "value": _read_core_stat_value(stats, field),
            "modifier": stats.get_attribute_modifier(attr_type),
        }
        for attr_type, field in _ATTRIBUTE_SUMMARY_SPECS
    }


def build_stat_summary(stats: Stats) -> dict[str, object]:
    """Build full stat summary dict including modifiers, derived stats, and totals."""
    summary: dict[str, object] = {
        "attributes": _build_attribute_summary(stats),
        "derived_stats": {
            "max_dp": stats.max_dp,
            "max_magic_points": stats.max_magic_points,
            "max_lucidity": stats.max_lucidity,
        },
    }

    stat_values = np.array(
        [_stat_value_for_summary(_read_core_stat_value(stats, field)) for _, field in _ATTRIBUTE_SUMMARY_SPECS],
        dtype=np.int32,
    )
    summary["total_points"] = int(np.sum(stat_values))
    summary["average_stat"] = float(np.mean(stat_values))
    return summary
