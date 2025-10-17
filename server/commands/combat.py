"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick, strike,
and other combat-related actions.
"""

from uuid import UUID

from server.exceptions import MythosMUDError
from server.logging_config import get_logger
from server.services.combat_service import combat_service

logger = get_logger(__name__)


class CombatCommandHandler:
    """
    Handler for combat-related commands.

    This class processes combat commands and integrates with the existing
    command system and combat service.
    """

    def __init__(self):
        """Initialize the combat command handler."""
        self.attack_aliases = {"attack", "punch", "kick", "strike", "hit", "smack", "thump"}

    async def handle_attack_command(
        self,
        player_id: UUID,
        player_name: str,
        command: str,
        target_name: str | None = None,
        room_id: str | None = None,
    ) -> str:
        """
        Handle attack commands (attack, punch, kick, etc.).

        Args:
            player_id: ID of the player issuing the command
            player_name: Name of the player
            command: The command that was issued
            target_name: Name of the target (if specified)
            room_id: ID of the room where the command was issued

        Returns:
            Response message for the player

        Raises:
            MythosValidationError: If the command is invalid
        """
        logger.info(f"Processing attack command '{command}' from {player_name} targeting '{target_name}'")

        # Validate command
        if command not in self.attack_aliases:
            raise MythosMUDError(
                message=f"Unknown combat command: {command}",
                user_friendly=f"You can't {command} in combat. Try 'attack', 'punch', 'kick', or 'strike'.",
            )

        # Check if target is specified
        if not target_name:
            return f"{command} who?"

        # For now, return a placeholder response
        # This will be integrated with the room service and NPC service
        return f"You attempt to {command} {target_name}, but the combat system is not yet fully integrated with the room and NPC systems."

    async def handle_flee_command(self, player_id: UUID, player_name: str) -> str:
        """
        Handle flee command (future implementation).

        Args:
            player_id: ID of the player issuing the command
            player_name: Name of the player
            command: The command that was issued

        Returns:
            Response message for the player
        """
        logger.info(f"Processing flee command from {player_name}")

        # Check if player is in combat
        combat = await combat_service.get_combat_by_participant(player_id)
        if not combat:
            return "You are not in combat."

        # For now, return a placeholder response
        return "You attempt to flee, but the flee command is not yet implemented."

    async def handle_defend_command(self, player_id: UUID, player_name: str) -> str:
        """
        Handle defend command (future implementation).

        Args:
            player_id: ID of the player issuing the command
            player_name: Name of the player
            command: The command that was issued

        Returns:
            Response message for the player
        """
        logger.info(f"Processing defend command from {player_name}")

        # Check if player is in combat
        combat = await combat_service.get_combat_by_participant(player_id)
        if not combat:
            return "You are not in combat."

        # For now, return a placeholder response
        return "You attempt to defend, but the defend command is not yet implemented."


# Global combat command handler instance
combat_command_handler = CombatCommandHandler()
