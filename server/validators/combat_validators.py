"""
Combat system data validators.

This module provides validation functions for combat data stored in
NPC definition JSON fields, including schema validation and business logic validation.
"""

from typing import Any

from server.exceptions import ValidationError
from server.logging_config import get_logger
from server.schemas.combat_schema import (
    CombatSchemaValidationError,
    validate_base_stats_combat_data,
    validate_behavior_config_combat_data,
    validate_combat_messages,
    validate_message_template_variables,
)

logger = get_logger(__name__)


class CombatDataValidator:
    """Validator for combat data in NPC definitions."""

    @staticmethod
    def validate_npc_combat_stats(stats: dict[str, Any]) -> None:
        """
        Validate NPC combat stats.

        Args:
            stats: Base stats dictionary to validate

        Raises:
            ValidationError: If stats fail validation
        """
        try:
            validate_base_stats_combat_data(stats)
        except CombatSchemaValidationError as e:
            raise ValidationError(f"Invalid combat stats: {str(e)}") from e

    @staticmethod
    def validate_npc_combat_config(config: dict[str, Any]) -> None:
        """
        Validate NPC combat configuration.

        Args:
            config: Behavior config dictionary to validate

        Raises:
            ValidationError: If config fails validation
        """
        try:
            validate_behavior_config_combat_data(config)
        except CombatSchemaValidationError as e:
            raise ValidationError(f"Invalid combat config: {str(e)}") from e

    @staticmethod
    def validate_combat_message_templates(messages: dict[str, str]) -> None:
        """
        Validate combat message templates.

        Args:
            messages: Combat messages dictionary to validate

        Raises:
            ValidationError: If messages fail validation
        """
        try:
            validate_combat_messages(messages)
            validate_message_template_variables(messages)
        except CombatSchemaValidationError as e:
            raise ValidationError(f"Invalid combat messages: {str(e)}") from e

    @staticmethod
    def validate_combat_data_integrity(stats: dict[str, Any], config: dict[str, Any]) -> None:
        """
        Validate combat data integrity across stats and config.

        Args:
            stats: Base stats dictionary
            config: Behavior config dictionary

        Raises:
            ValidationError: If data integrity validation fails
        """
        # Check that HP values are consistent
        hp = stats.get("hp", 0)
        max_hp = stats.get("max_hp", 0)

        if hp > max_hp:
            raise ValidationError(f"Current HP ({hp}) cannot exceed max HP ({max_hp})")

        if max_hp <= 0:
            raise ValidationError(f"Max HP must be positive, got {max_hp}")

        # Check that XP value is reasonable
        xp_value = stats.get("xp_value", 0)
        if xp_value < 0:
            raise ValidationError(f"XP value must be non-negative, got {xp_value}")

        # Check that attributes are within valid ranges
        for attr in ["dexterity", "strength", "constitution"]:
            value = stats.get(attr, 10)
            if not (1 <= value <= 20):
                raise ValidationError(f"{attr} must be between 1 and 20, got {value}")

        # Check combat behavior configuration
        if "combat_behavior" in config:
            behavior = config["combat_behavior"]

            # Check retreat threshold
            retreat_threshold = behavior.get("retreat_threshold", 0.2)
            if not (0 <= retreat_threshold <= 1):
                raise ValidationError(f"Retreat threshold must be between 0 and 1, got {retreat_threshold}")

            # Check combat timeout
            combat_timeout = behavior.get("combat_timeout", 300)
            if combat_timeout < 60:
                raise ValidationError(f"Combat timeout must be at least 60 seconds, got {combat_timeout}")


class CombatMessageValidator:
    """Validator for combat message templates."""

    @staticmethod
    def validate_message_template(template: str, required_variables: list[str]) -> None:
        """
        Validate a single message template.

        Args:
            template: Message template string
            required_variables: List of required variable names

        Raises:
            ValidationError: If template validation fails
        """
        if not template or not isinstance(template, str):
            raise ValidationError("Message template must be a non-empty string")

        # Check for required variables
        for var in required_variables:
            if var not in template:
                raise ValidationError(f"Message template missing required variable '{var}': {template}")

        # Check for balanced braces
        open_braces = template.count("{")
        close_braces = template.count("}")
        if open_braces != close_braces:
            raise ValidationError(f"Message template has unbalanced braces: {template}")

    @staticmethod
    def validate_combat_message_set(messages: dict[str, str]) -> None:
        """
        Validate a complete set of combat messages.

        Args:
            messages: Dictionary of combat messages

        Raises:
            ValidationError: If message set validation fails
        """
        required_messages = ["attack_attacker", "attack_defender", "attack_other", "death_message"]

        # Check that all required messages are present
        for msg_type in required_messages:
            if msg_type not in messages:
                raise ValidationError(f"Missing required message type: {msg_type}")

        # Validate each message template
        message_requirements = {
            "attack_attacker": ["{target_name}", "{damage}"],
            "attack_defender": ["{attacker_name}", "{damage}"],
            "attack_other": ["{attacker_name}", "{target_name}", "{damage}"],
            "death_message": ["{npc_name}"],
        }

        for msg_type, template in messages.items():
            if msg_type in message_requirements:
                CombatMessageValidator.validate_message_template(template, message_requirements[msg_type])


class CombatStatsValidator:
    """Validator for combat statistics."""

    @staticmethod
    def validate_hp_values(hp: int, max_hp: int) -> None:
        """
        Validate HP values.

        Args:
            hp: Current HP
            max_hp: Maximum HP

        Raises:
            ValidationError: If HP values are invalid
        """
        if max_hp <= 0:
            raise ValidationError(f"Max HP must be positive, got {max_hp}")

        if hp < 0:
            raise ValidationError(f"Current HP cannot be negative, got {hp}")

        if hp > max_hp:
            raise ValidationError(f"Current HP ({hp}) cannot exceed max HP ({max_hp})")

    @staticmethod
    def validate_attribute_value(attribute: str, value: int) -> None:
        """
        Validate attribute values.

        Args:
            attribute: Attribute name
            value: Attribute value

        Raises:
            ValidationError: If attribute value is invalid
        """
        if not isinstance(value, int):
            raise ValidationError(f"{attribute} must be an integer, got {type(value).__name__}")

        if not (1 <= value <= 20):
            raise ValidationError(f"{attribute} must be between 1 and 20, got {value}")

    @staticmethod
    def validate_xp_value(xp_value: int) -> None:
        """
        Validate XP value.

        Args:
            xp_value: XP value to validate

        Raises:
            ValidationError: If XP value is invalid
        """
        if not isinstance(xp_value, int):
            raise ValidationError(f"XP value must be an integer, got {type(xp_value).__name__}")

        if xp_value < 0:
            raise ValidationError(f"XP value must be non-negative, got {xp_value}")


class CombatBehaviorValidator:
    """Validator for combat behavior configuration."""

    @staticmethod
    def validate_aggression_level(level: str) -> None:
        """
        Validate aggression level.

        Args:
            level: Aggression level to validate

        Raises:
            ValidationError: If aggression level is invalid
        """
        valid_levels = ["passive", "aggressive"]
        if level not in valid_levels:
            raise ValidationError(f"Aggression level must be one of {valid_levels}, got {level}")

    @staticmethod
    def validate_retreat_threshold(threshold: float) -> None:
        """
        Validate retreat threshold.

        Args:
            threshold: Retreat threshold to validate

        Raises:
            ValidationError: If retreat threshold is invalid
        """
        if not isinstance(threshold, (int, float)):
            raise ValidationError(f"Retreat threshold must be a number, got {type(threshold).__name__}")

        if not (0 <= threshold <= 1):
            raise ValidationError(f"Retreat threshold must be between 0 and 1, got {threshold}")

    @staticmethod
    def validate_combat_timeout(timeout: int) -> None:
        """
        Validate combat timeout.

        Args:
            timeout: Combat timeout to validate

        Raises:
            ValidationError: If combat timeout is invalid
        """
        if not isinstance(timeout, int):
            raise ValidationError(f"Combat timeout must be an integer, got {type(timeout).__name__}")

        if timeout < 60:
            raise ValidationError(f"Combat timeout must be at least 60 seconds, got {timeout}")


def validate_npc_combat_data_complete(npc_definition) -> dict[str, Any]:
    """
    Perform complete validation of NPC combat data.

    Args:
        npc_definition: NPCDefinition instance to validate

    Returns:
        Validation results dictionary

    Raises:
        ValidationError: If validation fails
    """
    validation_results = {
        "npc_name": npc_definition.name,
        "npc_id": npc_definition.id,
        "validation_passed": True,
        "errors": [],
        "warnings": [],
    }

    try:
        # Get combat data
        stats = npc_definition.get_base_stats()
        config = npc_definition.get_behavior_config()

        # Validate base stats
        try:
            CombatDataValidator.validate_npc_combat_stats(stats)
        except ValidationError as e:
            validation_results["errors"].append(f"Base stats validation failed: {str(e)}")
            validation_results["validation_passed"] = False

        # Validate behavior config
        try:
            CombatDataValidator.validate_npc_combat_config(config)
        except ValidationError as e:
            validation_results["errors"].append(f"Behavior config validation failed: {str(e)}")
            validation_results["validation_passed"] = False

        # Validate combat messages if present
        if "combat_messages" in config:
            try:
                CombatMessageValidator.validate_combat_message_set(config["combat_messages"])
            except ValidationError as e:
                validation_results["errors"].append(f"Combat messages validation failed: {str(e)}")
                validation_results["validation_passed"] = False

        # Validate data integrity
        try:
            CombatDataValidator.validate_combat_data_integrity(stats, config)
        except ValidationError as e:
            validation_results["errors"].append(f"Data integrity validation failed: {str(e)}")
            validation_results["validation_passed"] = False

        # Check for missing combat data
        if "xp_value" not in stats:
            validation_results["warnings"].append("Missing XP value in base stats")

        if "dexterity" not in stats:
            validation_results["warnings"].append("Missing dexterity in base stats")

        if "combat_messages" not in config:
            validation_results["warnings"].append("Missing combat messages in behavior config")

    except Exception as e:
        validation_results["errors"].append(f"Unexpected validation error: {str(e)}")
        validation_results["validation_passed"] = False
        logger.error(
            "Unexpected validation error", npc_name=npc_definition.name, npc_id=npc_definition.id, error=str(e)
        )

    return validation_results
