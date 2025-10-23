"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick,
strike, and other combat-related actions.
"""

from typing import TYPE_CHECKING, Any

from server.alias_storage import AliasStorage
from server.config import get_config
from server.logging.enhanced_logging_config import get_logger
from server.persistence import get_persistence
from server.schemas.target_resolution import TargetType
from server.services.npc_combat_integration_service import (
    NPCCombatIntegrationService,
)
from server.services.target_resolution_service import TargetResolutionService
from server.validators.combat_validator import CombatValidator

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger = get_logger(__name__)


class CombatCommandHandler:
    """
    Handler for combat-related commands.

    This class processes combat commands and integrates with the existing
    command system and combat service.
    """

    def __init__(self, combat_service: "CombatService | None" = None):
        """
        Initialize the combat command handler.

        Args:
            combat_service: Optional CombatService instance to use.
                If None, NPCCombatIntegrationService will create its own.
        """
        self.attack_aliases = {
            "attack",
            "punch",
            "kick",
            "strike",
            "hit",
            "smack",
            "thump",
        }
        self.npc_combat_service = NPCCombatIntegrationService(combat_service=combat_service)
        self.persistence = get_persistence()
        self.combat_validator = CombatValidator()
        # Initialize target resolution service
        from server.game.player_service import PlayerService

        self.target_resolution_service = TargetResolutionService(self.persistence, PlayerService(self.persistence))

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

        logger.debug(
            f"🚨 COMBAT DEBUG: Processing attack command '{command}' from {player_name} targeting '{target_name}'"
        )
        logger.debug(f"DEBUG: command_data keys: {list(command_data.keys())}")
        logger.debug(f"DEBUG: current_user type: {type(current_user)}")
        logger.debug(f"DEBUG: current_user value: {current_user}")
        logger.debug(
            f"DEBUG: current_user keys: {list(current_user.keys()) if hasattr(current_user, 'keys') else 'No keys method'}"
        )
        logger.debug(f"DEBUG: request type: {type(request)}")
        logger.debug(f"DEBUG: alias_storage type: {type(alias_storage)}")

        # Add more debug logging to trace execution
        try:
            logger.debug(f"DEBUG: Starting target validation for {player_name}")
            logger.debug(f"DEBUG: About to check target_name: '{target_name}'")
            if not target_name:
                logger.debug(f"DEBUG: No target name provided for {player_name}")
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

            # Get persistence layer and player data (following the same pattern as look command)
            logger.debug(f"DEBUG: Getting persistence layer for {player_name}")
            app = request.app if request else None
            persistence = app.state.persistence if app else None

            if not persistence:
                logger.debug(f"DEBUG: No persistence layer found for {player_name}")
                return {"result": "The cosmic forces are unreachable."}

            logger.debug(f"DEBUG: Getting player data for {player_name}")
            from ..utils.command_parser import get_username_from_user

            player = persistence.get_player_by_name(get_username_from_user(current_user))
            if not player:
                logger.debug(f"DEBUG: Player not found for {player_name}")
                return {"result": "You are not recognized by the cosmic forces."}

            logger.debug(f"DEBUG: Player found: {player}")

            # Get player's current room
            logger.debug(f"DEBUG: Getting player's current room for {player_name}")
            room_id = player.current_room_id
            if not room_id:
                logger.debug(f"DEBUG: No room_id found in player data for {player_name}")
                return {"result": "You are not in a room."}

            logger.debug(f"DEBUG: Player room_id: {room_id}")

            # Get room data
            logger.debug(f"DEBUG: Getting room data for {player_name}")
            room = persistence.get_room(room_id)
            if not room:
                logger.debug(f"DEBUG: Room data not found for {player_name}")
                return {"result": "You are in an unknown room."}

            logger.debug(f"DEBUG: Room data found: {room}")

            # Use target resolution service to find targets
            logger.debug(f"DEBUG: Using target resolution service for {player_name}")
            target_result = await self.target_resolution_service.resolve_target(str(player.player_id), target_name)

            if not target_result.success:
                logger.debug(f"DEBUG: Target resolution failed: {target_result.error_message}")
                return {"result": target_result.error_message}

            # Get the single match
            target_match = target_result.get_single_match()
            if not target_match:
                logger.debug(f"DEBUG: No single match found for {player_name}")
                return {"result": target_result.error_message}

            # Check if target is an NPC (combat only works on NPCs for now)
            if target_match.target_type != TargetType.NPC:
                logger.debug(f"DEBUG: Target is not an NPC: {target_match.target_type}")
                return {"result": f"You can only attack NPCs, not {target_match.target_type}s."}

            # Get NPC instance for combat
            npc_instance = self._get_npc_instance(target_match.target_id)
            if not npc_instance:
                logger.debug(f"DEBUG: Could not get NPC instance for {target_match.target_id}")
                return {"result": "Target not found."}

            logger.debug(f"DEBUG: Found target NPC: {npc_instance.name} (ID: {target_match.target_id})")

            # Validate combat action
            logger.debug(f"DEBUG: Validating combat action for {player_name}")
            npc_id = target_match.target_id
            validation_result = await self._validate_combat_action(player_name, npc_id, command)
            if not validation_result.get("valid", False):
                logger.debug(f"DEBUG: Combat validation failed: {validation_result}")
                return {"result": validation_result.get("message", "Invalid combat action.")}

            logger.debug(f"DEBUG: Combat validation passed for {player_name}")

            # Execute combat action
            logger.debug(f"DEBUG: Executing combat action for {player_name}")
            combat_result = await self._execute_combat_action(player_name, npc_id, command, room_id)
            logger.debug(f"DEBUG: Combat action executed: {combat_result}")

            return combat_result

        except Exception as e:
            logger.error(f"ERROR: Exception in combat handler: {e}", exc_info=True)
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
            # Use the same approach as websocket handler
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "spawning_service"):
                spawning_service = npc_instance_service.spawning_service
                if npc_id in spawning_service.active_npc_instances:
                    return spawning_service.active_npc_instances[npc_id]

            return None

        except Exception as e:
            logger.error(f"Error getting NPC instance for {npc_id}: {e}")
            return None

    async def _validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict:
        """Validate combat action."""
        # Simple validation for now
        if not player_name or not npc_id or not command:
            return {"valid": False, "message": "Invalid combat parameters"}
        return {"valid": True}

    async def _execute_combat_action(self, player_name: str, npc_id: str, command: str, room_id: str) -> dict[str, str]:
        """Execute combat action using the proper combat service."""
        try:
            # Get player ID from the persistence layer
            # We need to get the player object to get the player ID
            player = self.persistence.get_player_by_name(player_name)
            if not player:
                logger.error(f"Player not found for combat action: {player_name}")
                return {"result": "You are not recognized by the cosmic forces."}

            player_id = str(player.player_id)

            # Get NPC instance to get the NPC name for the message
            npc_instance = self._get_npc_instance(npc_id)
            npc_name = npc_instance.name if npc_instance else "unknown target"

            # Calculate basic damage using configured value
            # TODO: Implement proper damage calculation based on player stats, weapon, etc.
            config = get_config()
            damage = config.game.basic_unarmed_damage

            logger.info(f"Executing combat action: {player_name} ({player_id}) {command}s {npc_id} for {damage} damage")

            # Use the proper combat service to handle the attack with auto-progression
            await self.npc_combat_service.handle_player_attack_on_npc(
                player_id=player_id, npc_id=npc_id, room_id=room_id, action_type=command, damage=damage
            )

            # Return simple acknowledgment since detailed message is sent via broadcast system
            return {"result": f"You {command} {npc_name}!"}

        except Exception as e:
            logger.error(f"Error executing combat action: {e}")
            return {"result": f"Error executing {command} command"}


# Global combat command handler instance (initialized lazily)
_combat_command_handler: CombatCommandHandler | None = None


def get_combat_command_handler() -> CombatCommandHandler:
    """
    Get the global combat command handler instance, creating it if needed.

    This uses lazy initialization to ensure that the combat_service from
    app.state is properly initialized before we create the handler.
    """
    global _combat_command_handler
    if _combat_command_handler is None:
        # Import here to avoid circular dependency
        from server.main import app

        combat_service = getattr(app.state, "combat_service", None)
        _combat_command_handler = CombatCommandHandler(combat_service=combat_service)
    return _combat_command_handler


# Individual command handler functions for the command service
async def handle_attack_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


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
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


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
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


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
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)
