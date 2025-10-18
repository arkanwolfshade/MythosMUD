"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick, strike,
and other combat-related actions.
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.logging_config import get_logger
from server.persistence import get_persistence
from server.services.npc_combat_integration_service import NPCCombatIntegrationService

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
        self.npc_combat_service = NPCCombatIntegrationService()
        self.persistence = get_persistence()

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

        # Get player information
        player_id = current_user.get("player_id")
        if not player_id:
            return {"result": "You must be logged in to attack."}

        # Get player's current room
        player = self.persistence.get_player(player_id)
        if not player:
            return {"result": "Player not found."}

        room_id = player.current_room
        if not room_id:
            return {"result": "You are not in a room."}

        # Get room to check for NPCs
        room = self.persistence.get_room(room_id)
        if not room:
            return {"result": "You are in an invalid room."}

        # Look for NPCs in the room
        npc_found = None
        for npc_id in room.npcs:
            # Try to get NPC instance
            npc_instance = self._get_npc_instance(npc_id)
            if npc_instance and npc_instance.name.lower() == target_name.lower():
                npc_found = npc_instance
                break

        if not npc_found:
            return {"result": f"You don't see {target_name} here."}

        # Check if NPC is alive
        if not npc_found.is_alive:
            return {"result": f"{target_name} is already dead."}

        # Execute the attack
        try:
            success = self.npc_combat_service.handle_player_attack_on_npc(
                player_id=player_id,
                npc_id=npc_id,
                room_id=room_id,
                action_type=command,
                damage=1,  # MVP: all attacks do 1 damage
            )

            if success:
                return {"result": f"You {command} {target_name}!"}
            else:
                return {"result": f"Your attack on {target_name} failed."}

        except Exception as e:
            logger.error(f"Error in combat: {str(e)}")
            return {"result": "An error occurred during combat."}

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            # Try to get from spawning service if available
            if hasattr(self.persistence, "get_npc_spawning_service"):
                spawning_service = self.persistence.get_npc_spawning_service()
                if spawning_service and npc_id in spawning_service.active_npc_instances:
                    return spawning_service.active_npc_instances[npc_id]

            return None

        except Exception as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None


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
