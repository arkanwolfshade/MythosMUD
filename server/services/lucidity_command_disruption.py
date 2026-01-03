"""
Command disruption utilities for lucidity system.

Implements command misfires and involuntary actions based on lucidity tier
as specified in docs/lucidity-system.md section 5.2.
"""

import random

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Complex commands that can misfire
COMPLEX_COMMANDS = {"cast", "craft", "sneak"}

# Misfire probabilities by tier
MISFIRE_PROBABILITIES = {
    "lucid": 0.0,
    "uneasy": 0.0,
    "fractured": 0.10,  # 10% chance
    "deranged": 0.25,  # 25% chance
    "catatonic": 1.0,  # 100% - motor lock
}

# Involuntary flee probability (Deranged tier)
INVOLUNTARY_FLEE_PROBABILITY = 0.20  # 20% chance
INVOLUNTARY_FLEE_DAMAGE_THRESHOLD = 0.15  # 15% of max HP


def should_misfire_command(command_type: str, tier: str) -> bool:
    """
    Check if a command should misfire based on tier and command type.

    Args:
        command_type: Type of command being executed
        tier: Current lucidity tier

    Returns:
        True if command should misfire, False otherwise
    """
    # Only complex commands can misfire
    if command_type.lower() not in COMPLEX_COMMANDS:
        return False

    # Catatonic tier: motor lock - all commands blocked
    if tier == "catatonic":
        return True

    # Get misfire probability for tier
    probability = MISFIRE_PROBABILITIES.get(tier, 0.0)
    if probability <= 0.0:
        return False

    return random.random() < probability


def get_misfire_message(command_type: str, tier: str) -> str:
    """
    Get the misfire message for a failed command.

    Args:
        command_type: Type of command that misfired
        tier: Current lucidity tier

    Returns:
        Misfire message
    """
    if tier == "catatonic":
        return "Your limbs refuse to respond. The void between thought and action yawns wide."
    elif tier == "deranged":
        return f"Your {command_type} command falters. Reality wavers; the gesture dissolves into meaningless motion."
    else:  # fractured
        return f"The {command_type} command sputters and fails. Your focus fractures, and the ritual collapses."


def should_involuntary_flee(tier: str, damage_percent: float) -> bool:
    """
    Check if player should involuntarily flee.

    Args:
        tier: Current lucidity tier
        damage_percent: Percentage of max HP taken in one hit (0.0 to 1.0)

    Returns:
        True if player should flee, False otherwise
    """
    if tier != "deranged":
        return False

    if damage_percent < INVOLUNTARY_FLEE_DAMAGE_THRESHOLD:
        return False

    return random.random() < INVOLUNTARY_FLEE_PROBABILITY


def can_perform_action(tier: str) -> bool:
    """
    Check if player can perform actions (motor lock check).

    Args:
        tier: Current lucidity tier

    Returns:
        True if player can act, False if motor lock applies
    """
    return tier != "catatonic"


__all__ = [
    "should_misfire_command",
    "get_misfire_message",
    "should_involuntary_flee",
    "can_perform_action",
    "COMPLEX_COMMANDS",
    "MISFIRE_PROBABILITIES",
]
