"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick, strike,
and other combat-related actions.
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.logging_config import get_logger

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
        command_data: dict,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle attack commands (attack, punch, kick, etc.).

        Args:
            command_data: Command data dictionary containing validated command
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name for logging

        Returns:
            dict: Attack command result with 'result' key
        """
        command = command_data.get("command_type", "attack")
        args = command_data.get("args", [])
        target_name = args[0] if args else None

        logger.info(f"Processing attack command '{command}' from {player_name} targeting '{target_name}'")

        # Validate command
        if command not in self.attack_aliases:
            return {"result": f"You can't {command} in combat. Try 'attack', 'punch', 'kick', or 'strike'."}

        # Check if target is specified
        if not target_name:
            return {"result": f"{command} who?"}

        # For now, return a placeholder response
        # This will be integrated with the room service and NPC service
        return {
            "result": f"You attempt to {command} {target_name}, but the "
            f"combat system is not yet fully integrated with the room and "
            f"NPC systems."
        }


# Global combat command handler instance
combat_command_handler = CombatCommandHandler()


# Individual command handler functions for the command service
async def handle_attack_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    return await combat_command_handler.handle_attack_command(
        command_data, current_user, request, alias_storage, player_name
    )


async def handle_punch_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, str]:
    """Handle punch command (alias for attack)."""
    # Set command type to punch for proper messaging
    command_data = command_data.copy()
    command_data["command_type"] = "punch"
    return await combat_command_handler.handle_attack_command(
        command_data, current_user, request, alias_storage, player_name
    )


async def handle_kick_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, str]:
    """Handle kick command (alias for attack)."""
    # Set command type to kick for proper messaging
    command_data = command_data.copy()
    command_data["command_type"] = "kick"
    return await combat_command_handler.handle_attack_command(
        command_data, current_user, request, alias_storage, player_name
    )


async def handle_strike_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, str]:
    """Handle strike command (alias for attack)."""
    # Set command type to strike for proper messaging
    command_data = command_data.copy()
    command_data["command_type"] = "strike"
    return await combat_command_handler.handle_attack_command(
        command_data, current_user, request, alias_storage, player_name
    )


# Global combat command handler instance
combat_command_handler = CombatCommandHandler()
