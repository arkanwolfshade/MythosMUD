"""
Combat system JSON schema validation.

This module provides JSON schema validation for combat data stored in
NPC definition JSON fields (base_stats and behavior_config).
"""

from typing import Any

from jsonschema import Draft7Validator
from jsonschema import ValidationError as JSONSchemaValidationError


class CombatSchemaValidationError(Exception):
    """Raised when combat data fails schema validation."""


# JSON Schema for base_stats combat data
BASE_STATS_COMBAT_SCHEMA = {
    "type": "object",
    "properties": {
        "hp": {
            "type": "integer",
            "minimum": 0,
            "description": "Current hit points",
        },
        "max_hp": {
            "type": "integer",
            "minimum": 1,
            "description": "Maximum hit points",
        },
        "xp_value": {
            "type": "integer",
            "minimum": 0,
            "description": "Experience points awarded when NPC is defeated",
        },
        "dexterity": {
            "type": "integer",
            "minimum": 1,
            "maximum": 20,
            "description": "NPC dexterity for turn order calculation",
        },
        "strength": {
            "type": "integer",
            "minimum": 1,
            "maximum": 20,
            "description": "NPC strength (for future expansion)",
        },
        "constitution": {
            "type": "integer",
            "minimum": 1,
            "maximum": 20,
            "description": "NPC constitution (for future expansion)",
        },
    },
    "required": ["hp", "max_hp", "xp_value"],
    "additionalProperties": True,
}

# JSON Schema for behavior_config combat messages
COMBAT_MESSAGES_SCHEMA = {
    "type": "object",
    "properties": {
        "attack_attacker": {
            "type": "string",
            "minLength": 1,
            "description": "Message template for attacker perspective",
        },
        "attack_defender": {
            "type": "string",
            "minLength": 1,
            "description": "Message template for defender perspective",
        },
        "attack_other": {
            "type": "string",
            "minLength": 1,
            "description": "Message template for other players perspective",
        },
        "death_message": {
            "type": "string",
            "minLength": 1,
            "description": "Message template for NPC death",
        },
    },
    "required": [
        "attack_attacker",
        "attack_defender",
        "attack_other",
        "death_message",
    ],
    "additionalProperties": False,
}

# JSON Schema for behavior_config combat behavior
COMBAT_BEHAVIOR_SCHEMA = {
    "type": "object",
    "properties": {
        "aggression_level": {
            "type": "string",
            "enum": ["passive", "aggressive"],
            "description": "NPC aggression level",
        },
        "retreat_threshold": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "HP percentage threshold for retreat",
        },
        "combat_timeout": {
            "type": "integer",
            "minimum": 60,
            "description": "Combat timeout in seconds",
        },
    },
    "additionalProperties": False,
}

# JSON Schema for behavior_config with combat data
BEHAVIOR_CONFIG_COMBAT_SCHEMA = {
    "type": "object",
    "properties": {
        "combat_messages": COMBAT_MESSAGES_SCHEMA,
        "combat_behavior": COMBAT_BEHAVIOR_SCHEMA,
    },
    "additionalProperties": True,
}

# Default combat data templates
DEFAULT_COMBAT_STATS = {
    "hp": 50,
    "max_hp": 50,
    "xp_value": 1,
    "dexterity": 10,
    "strength": 10,
    "constitution": 8,
}

DEFAULT_COMBAT_MESSAGES = {
    "attack_attacker": ("You swing your fist at {target_name} and hit for {damage} damage"),
    "attack_defender": ("{attacker_name} swings their fist at you and hits you for {damage} damage"),
    "attack_other": ("{attacker_name} swings their fist at {target_name} and hits for {damage} damage"),
    "death_message": "The {npc_name} collapses, dead",
}

DEFAULT_COMBAT_BEHAVIOR = {
    "aggression_level": "passive",
    "retreat_threshold": 0.2,
    "combat_timeout": 300,
}


def validate_base_stats_combat_data(data: dict[str, Any]) -> None:
    """
    Validate base_stats combat data against schema.

    Args:
        data: Base stats dictionary to validate

    Raises:
        CombatSchemaValidationError: If data fails validation
    """
    try:
        validator = Draft7Validator(BASE_STATS_COMBAT_SCHEMA)
        validator.validate(data)
    except JSONSchemaValidationError as e:
        raise CombatSchemaValidationError(f"Base stats combat data validation failed: {e.message}") from e


def validate_behavior_config_combat_data(data: dict[str, Any]) -> None:
    """
    Validate behavior_config combat data against schema.

    Args:
        data: Behavior config dictionary to validate

    Raises:
        CombatSchemaValidationError: If data fails validation
    """
    try:
        validator = Draft7Validator(BEHAVIOR_CONFIG_COMBAT_SCHEMA)
        validator.validate(data)
    except JSONSchemaValidationError as e:
        raise CombatSchemaValidationError(f"Behavior config combat data validation failed: {e.message}") from e


def validate_combat_messages(messages: dict[str, str]) -> None:
    """
    Validate combat message templates.

    Args:
        messages: Combat messages dictionary to validate

    Raises:
        CombatSchemaValidationError: If messages fail validation
    """
    try:
        validator = Draft7Validator(COMBAT_MESSAGES_SCHEMA)
        validator.validate(messages)
    except JSONSchemaValidationError as e:
        raise CombatSchemaValidationError(f"Combat messages validation failed: {e.message}") from e


def validate_message_template_variables(messages: dict[str, str]) -> None:
    """
    Validate that message templates contain required variables.

    Args:
        messages: Combat messages dictionary to validate

    Raises:
        CombatSchemaValidationError: If required variables are missing
    """
    required_variables = {
        "attack_attacker": ["{target_name}", "{damage}"],
        "attack_defender": ["{attacker_name}", "{damage}"],
        "attack_other": [
            "{attacker_name}",
            "{target_name}",
            "{damage}",
        ],
        "death_message": ["{npc_name}"],
    }

    for message_type, required_vars in required_variables.items():
        if message_type not in messages:
            continue

        message = messages[message_type]
        for var in required_vars:
            if var not in message:
                raise CombatSchemaValidationError(
                    f"Message template '{message_type}' missing required variable '{var}'"
                )


def add_default_combat_data_to_stats(stats: dict[str, Any]) -> dict[str, Any]:
    """
    Add default combat data to base_stats if not present.

    Args:
        stats: Base stats dictionary to update

    Returns:
        Updated base stats dictionary with default combat data
    """
    updated_stats = stats.copy()

    for key, default_value in DEFAULT_COMBAT_STATS.items():
        if key not in updated_stats:
            updated_stats[key] = default_value

    return updated_stats


def add_default_combat_data_to_config(config: dict[str, Any]) -> dict[str, Any]:
    """
    Add default combat data to behavior_config if not present.

    Args:
        config: Behavior config dictionary to update

    Returns:
        Updated behavior config dictionary with default combat data
    """
    updated_config = config.copy()

    # Add default combat messages if not present
    if "combat_messages" not in updated_config:
        updated_config["combat_messages"] = DEFAULT_COMBAT_MESSAGES.copy()

    # Add default combat behavior if not present
    if "combat_behavior" not in updated_config:
        updated_config["combat_behavior"] = DEFAULT_COMBAT_BEHAVIOR.copy()

    return updated_config


def validate_npc_combat_data(npc_definition) -> None:
    """
    Validate combat data for an NPC definition.

    Args:
        npc_definition: NPCDefinition instance to validate

    Raises:
        CombatSchemaValidationError: If combat data fails validation
    """
    # Validate base stats combat data
    try:
        stats = npc_definition.get_base_stats()
        validate_base_stats_combat_data(stats)
    except Exception as e:
        raise CombatSchemaValidationError(f"NPC {npc_definition.name} base stats validation failed: {e}") from e

    # Validate behavior config combat data
    try:
        config = npc_definition.get_behavior_config()
        validate_behavior_config_combat_data(config)

        # Validate combat messages if present
        if "combat_messages" in config:
            validate_combat_messages(config["combat_messages"])
            validate_message_template_variables(config["combat_messages"])
    except Exception as e:
        raise CombatSchemaValidationError(f"NPC {npc_definition.name} behavior config validation failed: {e}") from e


def get_combat_stats_summary(npc_definition) -> dict[str, Any]:
    """
    Get a summary of combat stats for an NPC definition.

    Args:
        npc_definition: NPCDefinition instance

    Returns:
        Dictionary with combat stats summary
    """
    stats = npc_definition.get_base_stats()
    config = npc_definition.get_behavior_config()

    return {
        "npc_name": npc_definition.name,
        "npc_type": npc_definition.npc_type,
        "combat_stats": {
            "hp": stats.get("hp", 0),
            "max_hp": stats.get("max_hp", 0),
            "xp_value": stats.get("xp_value", 0),
            "dexterity": stats.get("dexterity", 10),
            "strength": stats.get("strength", 10),
            "constitution": stats.get("constitution", 8),
        },
        "has_combat_messages": "combat_messages" in config,
        "has_combat_behavior": "combat_behavior" in config,
    }
