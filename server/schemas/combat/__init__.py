"""Combat domain schemas: combat JSON schema validation and defaults."""

from .combat_schema import (
    CombatSchemaValidationError,
    add_default_combat_data_to_config,
    add_default_combat_data_to_stats,
    get_combat_stats_summary,
    validate_base_stats_combat_data,
    validate_behavior_config_combat_data,
    validate_combat_messages,
    validate_npc_combat_data,
)

__all__ = [
    "CombatSchemaValidationError",
    "add_default_combat_data_to_config",
    "add_default_combat_data_to_stats",
    "get_combat_stats_summary",
    "validate_base_stats_combat_data",
    "validate_behavior_config_combat_data",
    "validate_combat_messages",
    "validate_npc_combat_data",
]
