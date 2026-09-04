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


def _core_stat_values_by_field(stats: Stats) -> dict[str, int | None]:
    """Map core stat field names to current values (typed access, no getattr)."""
    return {
        "strength": stats.strength,
        "dexterity": stats.dexterity,
        "constitution": stats.constitution,
        "size": stats.size,
        "intelligence": stats.intelligence,
        "power": stats.power,
        "education": stats.education,
        "charisma": stats.charisma,
        "luck": stats.luck,
    }


def _build_attribute_summary(stats: Stats, core_values: dict[str, int | None]) -> dict[str, object]:
    """Build per-attribute value and modifier entries for stat summary."""
    return {
        field: {
            "value": core_values[field],
            "modifier": stats.get_attribute_modifier(attr_type),
        }
        for attr_type, field in _ATTRIBUTE_SUMMARY_SPECS
    }


def build_stat_summary(stats: Stats) -> dict[str, object]:
    """Build full stat summary dict including modifiers, derived stats, and totals."""
    core_values = _core_stat_values_by_field(stats)
    summary: dict[str, object] = {
        "attributes": _build_attribute_summary(stats, core_values),
        "derived_stats": {
            "max_dp": stats.max_dp,
            "max_magic_points": stats.max_magic_points,
            "max_lucidity": stats.max_lucidity,
        },
    }

    stat_values = np.array(
        [_stat_value_for_summary(core_values[field]) for _, field in _ATTRIBUTE_SUMMARY_SPECS],
        dtype=np.int32,
    )
    summary["total_points"] = int(np.sum(stat_values))
    summary["average_stat"] = float(np.mean(stat_values))
    return summary
