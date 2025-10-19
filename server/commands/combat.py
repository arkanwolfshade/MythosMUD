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
from server.validators.combat_validator import CombatValidator

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
        self.combat_validator = CombatValidator()

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
        command_type = command_data.get("command_type", "attack")
        # Convert enum to string if needed
        if hasattr(command_type, "value"):
            command = command_type.value
        else:
            command = str(command_type)
        target_name = command_data.get("target_player")

        logger.info(f"Processing attack command '{command}' from {player_name} targeting '{target_name}'")
        logger.debug(f"DEBUG: command_data keys: {list(command_data.keys())}")
        logger.debug(f"DEBUG: current_user keys: {list(current_user.keys()) if current_user else 'None'}")
        logger.debug(f"DEBUG: request type: {type(request)}")
        logger.debug(f"DEBUG: alias_storage type: {type(alias_storage)}")

        # Add more debug logging to trace execution
        try:
            logger.debug("DEBUG: Starting target validation", player_name=player_name)
            if not target_name:
                logger.debug("DEBUG: No target name provided", player_name=player_name)
                # Return a thematic error message for no target
                error_messages = [
                    "You must focus your wrath upon a specific target, lest your fury be wasted.",
                    "The void stares back at you, demanding a name to direct your hatred.",
                    "Your anger needs direction - who shall bear the brunt of your assault?",
                    "The cosmic forces require a target for your destructive intent.",
                ]
                import random

                return {"result": random.choice(error_messages)}

            logger.debug(f"DEBUG: Target name: '{target_name}'")

            # Get player's current room
            logger.debug("DEBUG: Getting player's current room", player_name=player_name)
            room_id = current_user.get("room_id")
            if not room_id:
                logger.debug("DEBUG: No room_id found in current_user", player_name=player_name)
                return {"result": "You are not in a room."}

            logger.debug(f"DEBUG: Player room_id: {room_id}")

            # Get room data
            logger.debug("DEBUG: Getting room data", player_name=player_name)
            room = self._get_room_data(room_id)
            if not room:
                logger.debug("DEBUG: Room data not found", player_name=player_name)
                return {"result": "You are in an unknown room."}

            logger.debug(f"DEBUG: Room data found: {room}")

            # Look for NPCs in the room
            logger.debug("DEBUG: Looking for NPCs in room", player_name=player_name)
            npc_found = None
            npc_id = None
            available_targets = []
            logger.debug(f"DEBUG: Looking for NPCs in room {room_id}, room.get_npcs() = {room.get_npcs()}")
            for current_npc_id in room.get_npcs():
                # Try to get NPC instance
                logger.debug(f"DEBUG: Processing NPC ID: {current_npc_id}")
                npc_instance = self._get_npc_instance(current_npc_id)
                logger.debug(f"DEBUG: Got NPC instance for {current_npc_id}: {npc_instance}")
                if npc_instance:
                    available_targets.append(npc_instance.name)
                    logger.debug(f"DEBUG: Comparing '{npc_instance.name.lower()}' with '{target_name.lower()}'")
                    if npc_instance.name.lower() == target_name.lower():
                        npc_found = npc_instance
                        npc_id = current_npc_id
                        logger.debug(f"DEBUG: Found matching NPC: npc_found={npc_found}, npc_id={npc_id}")
                        break

            logger.debug(
                f"DEBUG: After loop - npc_found={npc_found}, npc_id={npc_id}, available_targets={available_targets}"
            )

            if not npc_found:
                logger.debug("DEBUG: No matching NPC found", player_name=player_name)
                available_list = ", ".join(available_targets) if available_targets else "none"
                return {"result": f"No target named '{target_name}' found. Available targets: {available_list}"}

            logger.debug(f"DEBUG: Found target NPC: {npc_found.name} (ID: {npc_id})")

            # Validate combat action
            logger.debug("DEBUG: Validating combat action", player_name=player_name)
            validation_result = await self._validate_combat_action(player_name, npc_id, command)
            if not validation_result.get("valid", False):
                logger.debug(f"DEBUG: Combat validation failed: {validation_result}")
                return {"result": validation_result.get("message", "Invalid combat action.")}

            logger.debug("DEBUG: Combat validation passed", player_name=player_name)

            # Execute combat action
            logger.debug("DEBUG: Executing combat action", player_name=player_name)
            combat_result = await self._execute_combat_action(player_name, npc_id, command)
            logger.debug(f"DEBUG: Combat action executed: {combat_result}")

            return combat_result

        except Exception as e:
            logger.error(f"DEBUG: Exception in combat handler: {e}", exc_info=True)
            return {"result": f"An error occurred during combat: {str(e)}"}

    def _get_room_data(self, room_id: str) -> Any | None:
        """Get room data from persistence."""
        try:
            return self.persistence.get_room(room_id)
        except Exception as e:
            logger.error(f"Error getting room data for {room_id}: {e}")
            return None

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

    async def _validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict:
        """Validate combat action."""
        # Simple validation for now
        if not player_name or not npc_id or not command:
            return {"valid": False, "message": "Invalid combat parameters"}
        return {"valid": True}

    async def _execute_combat_action(self, player_name: str, npc_id: str, command: str) -> dict[str, str]:
        """Execute combat action."""
        try:
            # Simple combat execution for now
            return {"result": f"You {command} the target!"}
        except Exception as e:
            logger.error(f"Error executing combat action: {e}")
            return {"result": f"Error executing {command} command"}


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
