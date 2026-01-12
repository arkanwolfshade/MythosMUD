"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick,
strike, and other combat-related actions.
"""

# pylint: disable=too-many-return-statements  # Reason: Combat command handlers require multiple return statements for early validation returns (target validation, combat state checks, error handling)

import secrets
import uuid
from typing import TYPE_CHECKING, Any

from server.alias_storage import AliasStorage
from server.commands.rest_command import _cancel_rest_countdown, is_player_resting
from server.config import get_config
from server.game.player_service import PlayerService
from server.realtime.login_grace_period import is_player_in_login_grace_period

# Removed: from server.persistence import get_persistence - now using async_persistence parameter
from server.schemas.target_resolution import TargetType
from server.services.npc_combat_integration_service import (
    NPCCombatIntegrationService,
)
from server.services.npc_instance_service import get_npc_instance_service
from server.services.target_resolution_service import TargetResolutionService
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user
from server.validators.combat_validator import CombatValidator

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger = get_logger(__name__)


def _format_combat_status(player: Any, combat_instance: Any | None) -> str:
    """
    Produce a human-readable combat status string.

    This helper is retained for backward compatibility with tests that validate
    status reporting in isolation from the command handler.
    """
    if getattr(player, "in_combat", False) and combat_instance is not None:
        status = getattr(combat_instance, "status", "") or "active"
        return f"Combat status: {status}"
    return "You are not in combat."


def _get_combat_target(_player: Any, target_name: str | None) -> Any | None:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future player-based target resolution
    """
    Resolve a combat target by name.

    The current implementation is intentionally minimal for unit tests that only
    verify callable presence and basic return semantics. In production code the
    target resolution is delegated to TargetResolutionService.
    """
    if not target_name:
        return None
    # Real resolution is handled elsewhere; return None to indicate no local match
    return None


class CombatCommandHandler:  # pylint: disable=too-few-public-methods  # Reason: Command handler class with focused responsibility, minimal public interface
    """
    Handler for combat-related commands.

    This class processes combat commands and integrates with the existing
    command system and combat service.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Command handler initialization requires many service dependencies
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
        # Use async persistence for target resolution and player service
        self.target_resolution_service = TargetResolutionService(async_persistence, PlayerService(async_persistence))

    async def _check_and_interrupt_rest(
        self, request_app: Any, player_name: str, current_user: dict
    ) -> dict[str, str] | None:
        """Check if player is resting or in login grace period, interrupt rest if needed."""
        if not request_app:
            return None

        connection_manager = getattr(request_app.state, "connection_manager", None)
        persistence = getattr(request_app.state, "persistence", None)
        if not (connection_manager and persistence):
            return None

        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return None

        player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id

        # Check if player is in login grace period - block combat commands
        if is_player_in_login_grace_period(player_id, connection_manager):
            logger.info(
                "Combat command blocked - player in login grace period",
                player_id=player_id,
                player_name=player_name,
            )
            return {"result": "You are still warded by protective energies. You cannot engage in combat yet."}

        if is_player_resting(player_id, connection_manager):
            await _cancel_rest_countdown(player_id, connection_manager)
            logger.info("Rest interrupted by combat command", player_id=player_id, player_name=player_name)

        return None

    def _extract_combat_command_data(self, command_data: dict) -> tuple[str, str | None]:
        """Extract command type and target name from command_data."""
        command_type = command_data.get("command_type", "attack")
        # Convert enum to string if needed
        if hasattr(command_type, "value"):
            command = command_type.value
        else:
            command = str(command_type)
        target_name = command_data.get("target_player")
        return command, target_name

    def _validate_target_name(self, target_name: str | None) -> dict[str, str] | None:
        """Validate that target name is provided."""
        if not target_name:
            error_messages = [
                "You must focus your wrath upon a specific target, lest your fury be wasted.",
                "The void stares back at you, demanding a name to direct your hatred.",
                "Your anger needs direction - who shall bear the brunt of your assault?",
                "The cosmic forces require a target for your destructive intent.",
            ]
            return {"result": secrets.choice(error_messages)}
        return None

    async def _get_player_and_room(
        self, request_app: Any, current_user: dict
    ) -> tuple[Any, Any, dict[str, str] | None]:
        """Get player data and room, returning error dict if any step fails."""
        persistence = request_app.state.persistence if request_app else None
        if not persistence:
            return None, None, {"result": "The cosmic forces are unreachable."}

        player = await persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return None, None, {"result": "You are not recognized by the cosmic forces."}

        room_id = player.current_room_id
        if not room_id:
            return None, None, {"result": "You are not in a room."}

        room = persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if not room:
            return None, None, {"result": "You are in an unknown room."}

        return player, room, None

    async def _resolve_combat_target(self, player: Any, target_name: str) -> tuple[Any, dict[str, str] | None]:
        """Resolve combat target using target resolution service."""
        target_result = await self.target_resolution_service.resolve_target(player.player_id, target_name)

        if not target_result.success:
            return None, {"result": target_result.error_message or "Target not found"}

        target_match = target_result.get_single_match()
        if not target_match:
            return None, {"result": target_result.error_message or "No valid target found"}

        if target_match.target_type != TargetType.NPC:
            return None, {"result": f"You can only attack NPCs, not {target_match.target_type}s."}

        npc_instance = self._get_npc_instance(target_match.target_id)
        if not npc_instance:
            return None, {"result": "Target not found."}

        # Validate NPC is alive before proceeding
        if not getattr(npc_instance, "is_alive", True):
            npc_name = getattr(npc_instance, "name", "target")
            logger.warning(
                "Player attempted to attack dead NPC",
                player_name=player.player_name if hasattr(player, "player_name") else "unknown",
                npc_id=target_match.target_id,
                npc_name=npc_name,
            )
            return None, {"result": f"{npc_name} is already dead."}

        return target_match, None

    async def handle_attack_command(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Combat command handling requires many parameters and intermediate variables for complex combat logic
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
        _ = alias_storage  # Intentionally unused - part of standard command handler interface

        request_app = request.app if request else None

        # Check if player is resting and interrupt rest
        rest_check_result = await self._check_and_interrupt_rest(request_app, player_name, current_user)
        if rest_check_result:
            return rest_check_result

        # Extract command data
        command, target_name = self._extract_combat_command_data(command_data)

        logger.debug(
            "🚨 COMBAT DEBUG: Processing attack command",
            command=command,
            player_name=player_name,
            target_name=target_name,
        )

        try:
            # Validate target name
            target_validation_error = self._validate_target_name(target_name)
            if target_validation_error:
                return target_validation_error

            # After validation, target_name is guaranteed to be non-None
            if target_name is None:
                return {"result": "Target name is required for attack command."}

            assert target_name is not None, "target_name should not be None after validation"

            # Get player and room
            player, _, player_error = await self._get_player_and_room(request_app, current_user)
            if player_error:
                return player_error

            room_id = player.current_room_id

            # Resolve combat target
            target_match, target_error = await self._resolve_combat_target(player, target_name)
            if target_error:
                return target_error

            npc_id = target_match.target_id
            npc_instance = self._get_npc_instance(npc_id)

            # Validate combat action
            validation_result = await self._validate_combat_action(player_name, npc_id, command)
            if not validation_result.get("valid", False):
                return {"result": validation_result.get("message", "Invalid combat action.")}

            # Execute combat action
            combat_result = await self._execute_combat_action(
                player_name, npc_id, command, room_id, npc_instance=npc_instance
            )

            return combat_result

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat errors unpredictable, must return error message
            logger.error("ERROR: Exception in combat handler", error=str(e), exc_info=True)
            return {"result": f"An error occurred during combat: {str(e)}"}

    def _get_room_data(self, room_id: str) -> Any | None:
        """Get room data from persistence."""
        try:
            return self.persistence.get_room_by_id(room_id)  # Sync method, uses cache
        except (AttributeError, TypeError) as e:
            logger.error("Error getting room data", room_id=room_id, error=str(e))
            return None

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            # Use the same approach as websocket handler
            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

            return None

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC lookup errors unpredictable, must return None
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    async def _validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict:
        """Validate combat action."""
        # Simple validation for now
        if not player_name or not npc_id or not command:
            return {"valid": False, "message": "Invalid combat parameters"}
        return {"valid": True}

    async def _execute_combat_action(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat action execution requires many parameters for context and state
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
            player = await self.persistence.get_player_by_name(player_name)
            if not player:
                logger.error("Player not found for combat action", player_name=player_name)
                return {"result": "You are not recognized by the cosmic forces."}

            player_id = str(player.player_id)

            # Get NPC instance if not provided, or get NPC name
            if npc_instance is None:
                npc_instance = self._get_npc_instance(npc_id)
            npc_name = npc_instance.name if npc_instance else "unknown target"

            # Calculate basic damage using configured value
            # TODO: Implement proper damage calculation based on player stats, weapon, etc.  # pylint: disable=fixme  # Reason: Enhancement for more sophisticated damage system
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat action errors unpredictable, must return error message
            logger.error("Error executing combat action", error=str(e), exc_info=True)
            return {"result": f"Error executing {command} command"}


# Global combat command handler instance (initialized lazily)
_combat_command_handler: CombatCommandHandler | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_combat_command_handler(app: Any = None) -> CombatCommandHandler:
    """
    Get the global combat command handler instance, creating it if needed.

    This uses lazy initialization to ensure that the combat_service from
    app.state is properly initialized before we create the handler.

    Args:
        app: Optional FastAPI app instance. If None, uses cached handler if available.
    """
    global _combat_command_handler  # pylint: disable=global-statement  # Reason: Singleton pattern for combat handler
    if _combat_command_handler is None:
        if app is None:
            raise RuntimeError("Cannot initialize combat command handler without app instance")
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
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
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
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
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
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
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
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)
