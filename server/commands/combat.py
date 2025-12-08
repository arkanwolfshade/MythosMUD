"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick,
strike, and other combat-related actions.
"""

from typing import TYPE_CHECKING, Any

from server.alias_storage import AliasStorage
from server.config import get_config
from server.logging.enhanced_logging_config import get_logger

# Removed: from server.persistence import get_persistence - now using async_persistence parameter
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

    def __init__(
        self,
        combat_service: "CombatService | None" = None,
        event_bus=None,
        player_combat_service=None,
        connection_manager=None,
        async_persistence=None,
    ):
        """
        Initialize the combat command handler.

        Args:
            combat_service: Optional CombatService instance to use.
                If None, NPCCombatIntegrationService will create its own.
            event_bus: Optional EventBus instance to use.
                If None, NPCCombatIntegrationService will create its own.
            player_combat_service: Optional PlayerCombatService instance to use.
                If None, NPCCombatIntegrationService will create its own.
            connection_manager: Optional ConnectionManager instance to use.
                If None, NPCCombatIntegrationService will try to lazy-load from container.
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
        # Use async_persistence directly (now the only persistence layer)
        if async_persistence is None:
            raise ValueError("async_persistence is required for CombatCommandHandler")
        self.npc_combat_service = NPCCombatIntegrationService(
            combat_service=combat_service,
            event_bus=event_bus,
            player_combat_service=player_combat_service,
            connection_manager=connection_manager,
            async_persistence=async_persistence,
        )
        self.persistence = async_persistence
        self.combat_validator = CombatValidator()
        # Initialize target resolution service
        from server.game.player_service import PlayerService

        # Use async persistence for target resolution and player service
        self.target_resolution_service = TargetResolutionService(async_persistence, PlayerService(async_persistence))

    async def handle_attack_command(
        self,
        command_data: dict,
        current_user: dict,
        request: Any,
        alias_storage: AliasStorage | None,
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
            "🚨 COMBAT DEBUG: Processing attack command",
            command=command,
            player_name=player_name,
            target_name=target_name,
        )
        logger.debug("DEBUG: command_data keys", keys=list(command_data.keys()))
        logger.debug("DEBUG: current_user type", user_type=type(current_user))
        logger.debug("DEBUG: current_user value", user_value=current_user)
        logger.debug(
            "DEBUG: current_user keys",
            keys=list(current_user.keys()) if hasattr(current_user, "keys") else "No keys method",
        )
        logger.debug("DEBUG: request type", request_type=type(request))
        logger.debug("DEBUG: alias_storage type", alias_storage_type=type(alias_storage))

        # Add more debug logging to trace execution
        try:
            logger.debug("DEBUG: Starting target validation", player_name=player_name)
            logger.debug("DEBUG: About to check target_name", target_name=target_name)
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

            logger.debug("DEBUG: Target name", target_name=target_name)

            # Get persistence layer and player data (following the same pattern as look command)
            logger.debug("DEBUG: Getting persistence layer", player_name=player_name)
            app = request.app if request else None
            persistence = app.state.persistence if app else None

            if not persistence:
                logger.debug("DEBUG: No persistence layer found", player_name=player_name)
                return {"result": "The cosmic forces are unreachable."}

            logger.debug("DEBUG: Getting player data", player_name=player_name)
            from ..utils.command_parser import get_username_from_user

            player = persistence.get_player_by_name(get_username_from_user(current_user))
            if not player:
                logger.debug("DEBUG: Player not found", player_name=player_name)
                return {"result": "You are not recognized by the cosmic forces."}

            logger.debug("DEBUG: Player found", player=player)

            # Get player's current room
            logger.debug("DEBUG: Getting player's current room", player_name=player_name)
            room_id = player.current_room_id
            if not room_id:
                logger.debug("DEBUG: No room_id found in player data", player_name=player_name)
                return {"result": "You are not in a room."}

            logger.debug("DEBUG: Player room_id", room_id=room_id)

            # Get room data
            logger.debug("DEBUG: Getting room data", player_name=player_name)
            room = persistence.get_room(room_id)
            if not room:
                logger.debug("DEBUG: Room data not found", player_name=player_name)
                return {"result": "You are in an unknown room."}

            logger.debug("DEBUG: Room data found", room=room)

            # Use target resolution service to find targets
            logger.debug("DEBUG: Using target resolution service", player_name=player_name, player_room_id=room_id)
            target_result = await self.target_resolution_service.resolve_target(player.player_id, target_name)

            if not target_result.success:
                logger.debug("DEBUG: Target resolution failed", error_message=target_result.error_message)
                # AI Agent: Provide fallback for None case
                return {"result": target_result.error_message or "Target not found"}

            # Get the single match
            target_match = target_result.get_single_match()
            if not target_match:
                logger.debug("DEBUG: No single match found", player_name=player_name)
                # AI Agent: Provide fallback for None case
                return {"result": target_result.error_message or "No valid target found"}

            # Check if target is an NPC (combat only works on NPCs for now)
            if target_match.target_type != TargetType.NPC:
                logger.debug("DEBUG: Target is not an NPC", target_type=target_match.target_type)
                return {"result": f"You can only attack NPCs, not {target_match.target_type}s."}

            # Get NPC instance for combat
            npc_instance = self._get_npc_instance(target_match.target_id)
            if not npc_instance:
                logger.debug("DEBUG: Could not get NPC instance", target_id=target_match.target_id)
                return {"result": "Target not found."}

            # BUGFIX: Validate NPC is alive before proceeding
            # This prevents passing dead NPCs to the combat service
            # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
            if not getattr(npc_instance, "is_alive", True):
                npc_name = getattr(npc_instance, "name", "target")
                logger.warning(
                    "Player attempted to attack dead NPC",
                    player_name=player_name,
                    npc_id=target_match.target_id,
                    npc_name=npc_name,
                )
                return {"result": f"{npc_name} is already dead."}

            logger.debug("DEBUG: Found target NPC", npc_name=npc_instance.name, target_id=target_match.target_id)

            # Validate combat action
            logger.debug("DEBUG: Validating combat action", player_name=player_name)
            npc_id = target_match.target_id
            validation_result = await self._validate_combat_action(player_name, npc_id, command)
            if not validation_result.get("valid", False):
                logger.debug("DEBUG: Combat validation failed", validation_result=validation_result)
                return {"result": validation_result.get("message", "Invalid combat action.")}

            logger.debug("DEBUG: Combat validation passed", player_name=player_name)

            # Execute combat action - pass validated NPC instance to avoid redundant lookup
            logger.debug("DEBUG: Executing combat action", player_name=player_name)
            combat_result = await self._execute_combat_action(
                player_name, npc_id, command, room_id, npc_instance=npc_instance
            )
            logger.debug("DEBUG: Combat action executed", combat_result=combat_result)

            return combat_result

        except Exception as e:
            logger.error("ERROR: Exception in combat handler", error=str(e), exc_info=True)
            return {"result": f"An error occurred during combat: {str(e)}"}

    def _get_room_data(self, room_id: str) -> Any | None:
        """Get room data from persistence."""
        try:
            return self.persistence.get_room(room_id)
        except Exception as e:
            logger.error("Error getting room data", room_id=room_id, error=str(e))
            return None

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            # Use the same approach as websocket handler
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

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

    async def _execute_combat_action(
        self, player_name: str, npc_id: str, command: str, room_id: str, npc_instance: Any | None = None
    ) -> dict[str, str]:
        """
        Execute combat action using the proper combat service.

        Args:
            player_name: Name of the attacking player
            npc_id: ID of the target NPC
            command: Attack command type
            room_id: ID of the room where combat occurs
            npc_instance: Optional pre-validated NPC instance to pass to combat service
        """
        try:
            # Get player ID from the persistence layer
            # We need to get the player object to get the player ID
            player = self.persistence.get_player_by_name(player_name)
            if not player:
                logger.error("Player not found for combat action", player_name=player_name)
                return {"result": "You are not recognized by the cosmic forces."}

            player_id = str(player.player_id)

            # Get NPC instance if not provided, or get NPC name
            if npc_instance is None:
                npc_instance = self._get_npc_instance(npc_id)
            npc_name = npc_instance.name if npc_instance else "unknown target"

            # Calculate basic damage using configured value
            # TODO: Implement proper damage calculation based on player stats, weapon, etc.
            config = get_config()
            damage = config.game.basic_unarmed_damage

            logger.info(
                "Executing combat action",
                player_name=player_name,
                player_id=player_id,
                command=command,
                npc_id=npc_id,
                damage=damage,
                npc_instance_provided=npc_instance is not None,
            )

            # BUGFIX: Use the proper combat service and check return value
            # Pass validated NPC instance to avoid redundant lookup and race conditions
            # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
            combat_success = await self.npc_combat_service.handle_player_attack_on_npc(
                player_id=player_id,
                npc_id=npc_id,
                room_id=room_id,
                action_type=command,
                damage=damage,
                npc_instance=npc_instance,
            )

            # BUGFIX: Return proper error message if combat initiation failed
            # Previously returned success message even when combat didn't start (silent failure)
            if not combat_success:
                logger.warning(
                    "Combat initiation failed",
                    player_name=player_name,
                    player_id=player_id,
                    npc_id=npc_id,
                    npc_name=npc_name,
                )
                return {"result": f"You cannot attack {npc_name} right now."}

            # Return simple acknowledgment since detailed message is sent via broadcast system
            return {"result": f"You {command} {npc_name}!"}

        except Exception as e:
            logger.error("Error executing combat action", error=str(e), exc_info=True)
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
        event_bus = getattr(app.state, "event_bus", None)
        player_combat_service = getattr(app.state, "player_combat_service", None)
        # CRITICAL FIX: Get connection_manager from container to pass to CombatMessagingIntegration
        connection_manager = None
        async_persistence = None
        container = getattr(app.state, "container", None)
        if container:
            connection_manager = getattr(container, "connection_manager", None)
            async_persistence = getattr(container, "async_persistence", None)
        _combat_command_handler = CombatCommandHandler(
            combat_service=combat_service,
            event_bus=event_bus,
            player_combat_service=player_combat_service,
            connection_manager=connection_manager,
            async_persistence=async_persistence,
        )
    return _combat_command_handler


# Individual command handler functions for the command service
async def handle_attack_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_punch_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
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
    alias_storage: AliasStorage | None,
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
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle strike command (alias for attack)."""
    # Set command type to strike for proper messaging
    command_data = command_data.copy()
    command_data["command_type"] = "strike"
    handler = get_combat_command_handler()
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)
