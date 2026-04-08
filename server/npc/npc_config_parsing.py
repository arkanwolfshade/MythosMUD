"""Parsing and normalization of NPC config (stats, behavior, AI) to keep npc_base NLOC under limit."""

import json
from typing import cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)


def parse_stats(stats_json: str, npc_id: str) -> dict[str, object]:
    """Parse stats from JSON string. Returns default stats on parse error."""
    try:
        return json.loads(stats_json) if stats_json else {}
    except json.JSONDecodeError:
        logger.warning("Invalid stats JSON, using defaults", npc_id=npc_id)
        return {
            "determination_points": 20,
            "max_dp": 20,
            "strength": 50,
            "intelligence": 40,
            "charisma": 30,
        }


def apply_dp_from_source(stats: dict[str, object], source_key: str, max_dp_from: str | None = None) -> bool:
    """Set determination_points from source_key; optionally set max_dp. Returns True if applied."""
    if source_key not in stats:
        return False
    stats["determination_points"] = stats[source_key]
    if "max_dp" not in stats and max_dp_from:
        if max_dp_from == "max_hp" and "max_hp" in stats:
            stats["max_dp"] = stats["max_hp"]
        elif max_dp_from == "health" and "max_hp" not in stats:
            stats["max_dp"] = stats[source_key]
    return True


def normalize_determination_points(stats: dict[str, object]) -> None:
    """Ensure stats has determination_points; support hp/dp backward compat. Mutates stats."""
    if "determination_points" in stats:
        return
    if (
        apply_dp_from_source(stats, "dp")
        or apply_dp_from_source(stats, "hp", "max_hp")
        or apply_dp_from_source(stats, "health", "health")
    ):
        return
    stats["determination_points"] = 20  # Default DP


def apply_idle_movement_defaults(config: dict[str, object], npc_type: str) -> None:
    """Apply default idle movement config based on NPC type. Mutates config."""
    if "idle_movement_enabled" not in config:
        config["idle_movement_enabled"] = npc_type in ["passive_mob", "aggressive_mob"]
    if "idle_movement_interval" not in config:
        config["idle_movement_interval"] = 100
    if "idle_movement_probability" not in config:
        config["idle_movement_probability"] = 0.25
    if "idle_movement_weighted_home" not in config:
        config["idle_movement_weighted_home"] = True


def parse_behavior_config(config_json: str, npc_id: str, npc_type: str) -> dict[str, object]:
    """Parse behavior configuration from JSON string. Applies idle movement defaults."""
    try:
        config = cast(
            dict[str, object],
            json.loads(config_json) if config_json else {},
        )
        apply_idle_movement_defaults(config, npc_type)
        return config
    except json.JSONDecodeError:
        logger.warning("Invalid behavior config JSON, using defaults", npc_id=npc_id)
        config = cast(dict[str, object], {})
        apply_idle_movement_defaults(config, npc_type)
        return config


def parse_ai_config(ai_json: str, npc_id: str) -> dict[str, object]:
    """Parse AI integration configuration from JSON string."""
    try:
        return json.loads(ai_json) if ai_json else {}
    except json.JSONDecodeError:
        logger.warning("Invalid AI config JSON, using defaults", npc_id=npc_id)
        return {"ai_enabled": False, "ai_model": None}


def to_int_or_default(val: object, default: int) -> int:
    """Coerce value to int; return default if not numeric."""
    if isinstance(val, int | float):
        return int(val)
    if isinstance(val, str) and val.isdigit():
        return int(val)
    return default


def _safe_stat_int(stats: dict[str, object], key: str, default: int = 50) -> int:
    """Return stats[key] as int, or default if missing/None."""
    return to_int_or_default(stats.get(key), default)


def _compute_max_dp(stats: dict[str, object]) -> int:
    """Compute max_dp from stats when max_dp/max_hp not explicitly set."""
    max_dp_raw = stats.get("max_dp")
    max_hp_raw = stats.get("max_hp")
    if max_dp_raw is not None or max_hp_raw is not None:
        if max_dp_raw is not None:
            return _safe_stat_int(stats, "max_dp", 100)
        return _safe_stat_int(stats, "max_hp", 100)
    if "constitution" in stats and "size" in stats:
        return (_safe_stat_int(stats, "constitution") + _safe_stat_int(stats, "size")) // 5
    return 100


def get_combat_stats_dict(stats: dict[str, object]) -> dict[str, int]:
    """Return current_dp, max_dp, dexterity for CombatParticipantData."""
    current_dp = stats.get("determination_points", stats.get("dp", stats.get("hp", 100)))
    current_dp_int = to_int_or_default(current_dp, 100)
    max_dp = _compute_max_dp(stats)
    dexterity_int = _safe_stat_int(stats, "dexterity", 10)
    return {
        "current_dp": current_dp_int,
        "max_dp": max_dp,
        "dexterity": dexterity_int,
    }
