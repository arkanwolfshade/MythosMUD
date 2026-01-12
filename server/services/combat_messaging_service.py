"""
Combat messaging service for thematic combat messages.

This service handles the generation and formatting of combat messages
with proper perspective (attacker, defender, others) and variable substitution.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Messaging service requires many parameters for context and message formatting

from typing import Any

from server.exceptions import MythosMUDError
from server.schemas.combat_schema import validate_combat_messages
from server.structured_logging.enhanced_logging_config import get_logger

# Type aliases for better readability
ErrorMessages = dict[str, str]
CombatMessages = dict[str, str]

logger = get_logger(__name__)


class CombatMessagingService:
    """
    Service for generating combat messages.

    This service creates thematic, perspective-based combat messages
    using templates stored in NPC behavior configuration.
    """

    def __init__(self) -> None:
        """Initialize the combat messaging service."""
        # Default message templates for when NPCs don't have custom ones
        self.default_messages: CombatMessages = {
            "attack_attacker": "You {action_type} {target_name} for {damage} damage.",
            "attack_defender": "{attacker_name} {action_type}s you for {damage} damage.",
            "attack_other": "{attacker_name} {action_type}s {target_name} for {damage} damage.",
            "death_message": "{npc_name} dies.",
        }

    async def get_attack_message(
        self,
        attacker_name: str,
        target_name: str,
        damage: int,
        action_type: str = "attack",
        npc_messages: CombatMessages | None = None,
        perspective: str = "attacker",
    ) -> str:
        """
        Generate an attack message based on perspective and NPC configuration.

        Args:
            attacker_name: Name of the attacker
            target_name: Name of the target
            damage: Amount of damage dealt
            action_type: Type of attack (attack, punch, kick, etc.)
            npc_messages: NPC-specific message templates
            perspective: Message perspective (attacker, defender, other)

        Returns:
            Formatted combat message
        """
        # Use NPC messages if available, otherwise use defaults
        messages = npc_messages or self.default_messages

        # Get the appropriate message template based on perspective
        if perspective == "attacker":
            template = messages.get("attack_attacker", self.default_messages["attack_attacker"])
        elif perspective == "defender":
            template = messages.get("attack_defender", self.default_messages["attack_defender"])
        else:  # other
            template = messages.get("attack_other", self.default_messages["attack_other"])

        # Substitute variables in the template
        message = template.format(
            attacker_name=attacker_name, target_name=target_name, damage=damage, action_type=action_type
        )

        logger.debug("Generated attack message", perspective=perspective, message=message)
        return message

    async def get_death_message(self, npc_name: str, npc_messages: CombatMessages | None = None) -> str:
        """
        Generate a death message for an NPC.

        Args:
            npc_name: Name of the NPC that died
            npc_messages: NPC-specific message templates

        Returns:
            Formatted death message
        """
        # Use NPC messages if available, otherwise use defaults
        messages = npc_messages or self.default_messages

        # Get death message template
        template = messages.get("death_message", self.default_messages["death_message"])

        # Substitute variables in the template
        message = template.format(npc_name=npc_name)

        logger.debug("Generated death message", message=message)
        return message

    async def get_combat_start_messages(
        self, attacker_name: str, target_name: str, room_occupants: list[str]
    ) -> CombatMessages:
        """
        Generate combat start messages for all room occupants.

        Args:
            attacker_name: Name of the attacker
            target_name: Name of the target
            room_occupants: List of all occupant names in the room

        Returns:
            Dictionary mapping occupant names to their perspective messages
        """
        messages = {}

        for occupant in room_occupants:
            if occupant == attacker_name:
                messages[occupant] = f"You attack {target_name}!"
            elif occupant == target_name:
                messages[occupant] = f"{attacker_name} attacks you!"
            else:
                messages[occupant] = f"{attacker_name} attacks {target_name}!"

        logger.debug("Generated combat start messages", occupant_count=len(room_occupants))
        return messages

    async def get_combat_end_messages(
        self, winner_name: str, loser_name: str, room_occupants: list[str]
    ) -> CombatMessages:
        """
        Generate combat end messages for all room occupants.

        Args:
            winner_name: Name of the winner
            loser_name: Name of the loser
            room_occupants: List of all occupant names in the room

        Returns:
            Dictionary mapping occupant names to their perspective messages
        """
        messages = {}

        for occupant in room_occupants:
            if occupant == winner_name:
                messages[occupant] = f"You defeat {loser_name}!"
            elif occupant == loser_name:
                messages[occupant] = f"You are defeated by {winner_name}!"
            else:
                messages[occupant] = f"{winner_name} defeats {loser_name}!"

        logger.debug("Generated combat end messages", occupant_count=len(room_occupants))
        return messages

    async def get_error_message(self, error_type: str, player_name: str, target_name: str | None = None) -> str:
        """
        Generate thematic error messages for combat actions.

        Args:
            error_type: Type of error (no_target, not_in_combat, etc.)
            player_name: Name of the player
            target_name: Name of the target (if applicable)

        Returns:
            Thematic error message
        """
        error_messages: ErrorMessages = {
            "no_target": f"{player_name}, you must specify a target to attack.",
            "target_not_found": f"{player_name}, you don't see '{target_name}' here.",
            "not_in_combat": f"{player_name}, you are not currently in combat.",
            "wrong_turn": f"{player_name}, it is not your turn to act.",
            "target_dead": f"{player_name}, {target_name} is already dead.",
            "target_not_in_combat": f"{player_name}, {target_name} is not in this combat.",
            "invalid_target": f"{player_name}, you cannot attack {target_name}.",
            "combat_not_active": f"{player_name}, this combat is no longer active.",
        }

        message = error_messages.get(error_type, f"{player_name}, something goes wrong with your attack.")
        logger.debug("Generated error message", error_type=error_type, message=message)
        return message

    async def validate_npc_messages(self, messages_data: dict[str, Any]) -> CombatMessages:
        """
        Validate NPC message templates against the schema.

        Args:
            messages_data: NPC message data to validate

        Returns:
            Validated message data

        Raises:
            MythosValidationError: If messages are invalid
        """
        try:
            validate_combat_messages(messages_data)
            return messages_data
        except Exception as e:
            raise MythosMUDError(
                message="Invalid combat message templates",
                details={"validation_error": str(e), "messages_data": messages_data},
                user_friendly="The combat message templates for this NPC are invalid.",
            ) from e


# Global combat messaging service instance
combat_messaging_service = CombatMessagingService()
