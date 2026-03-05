"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick,
strike, and other combat-related actions.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Combat command handlers require multiple return statements for early validation returns (target validation, combat state checks, error handling). Module size is necessary for comprehensive combat command handling.

import secrets
import uuid
from typing import TYPE_CHECKING, Any

from server.alias_storage import AliasStorage
from server.commands.rest_command import _cancel_rest_countdown, is_player_resting
from server.config import get_config
from server.game.player_service import PlayerService
from server.game.weapons import resolve_weapon_attack_from_equipped
from server.npc.combat_integration import NPCCombatIntegration
from server.realtime.login_grace_period import is_player_in_login_grace_period

# Removed: from server.persistence import get_persistence - now using async_persistence parameter
from server.schemas.shared import TargetType
from server.services.combat_flee_handler import execute_voluntary_flee
from server.services.npc_combat_integration_service import (
    NPCCombatIntegrationService,
)
from server.services.npc_instance_service import get_npc_instance_service
from server.services.target_resolution_service import TargetResolutionService
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user
from server.validators.combat_validator import CombatValidator

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer
    from server.events.event_bus import EventBus
    from server.realtime.connection_manager import ConnectionManager
    from server.services.combat_service import CombatService
    from server.services.player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class FleePreconditionError(Exception):
    """Raised when flee preconditions fail; carries the error dict to return to the client."""

    def __init__(self, error_result: dict[str, str]) -> None:
        super().__init__(str(error_result))
        self.error_result = error_result


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
        event_bus: "EventBus | None" = None,
        player_combat_service: "PlayerCombatService | None" = None,
        connection_manager: "ConnectionManager | None" = None,
        async_persistence: "AsyncPersistenceLayer | None" = None,
        item_prototype_registry: Any | None = None,
        party_service: Any = None,
        movement_service: Any = None,
        player_position_service: Any = None,
    ) -> None:
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
            party_service: Optional PartyService for same-party attack checks (hook).
            movement_service: Optional MovementService for flee movement.
            player_position_service: Optional PlayerPositionService for standing check on flee.
        """
        self._combat_service = combat_service
        self._movement_service = movement_service
        self._player_position_service = player_position_service
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
        self._item_prototype_registry = item_prototype_registry
        self.combat_validator = CombatValidator(party_service=party_service)
        # Initialize target resolution service
        # Use async persistence for target resolution and player service
        # Type ignore: TargetResolutionService accepts PersistenceProtocol (sync methods),
        # but AsyncPersistenceLayer has async methods. The service handles both at runtime
        # by checking if methods are coroutines (see _get_player_from_persistence).
        self.target_resolution_service = TargetResolutionService(
            async_persistence,  # type: ignore[arg-type]
            PlayerService(async_persistence),
        )

    async def _check_and_interrupt_rest(
        self, request_app: Any, player_name: str, current_user: dict[str, Any]
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

    def _extract_combat_command_data(self, command_data: dict[str, Any]) -> tuple[str, str | None]:
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

    def _get_persistence_from_app(self, request_app: Any) -> Any:
        """Resolve persistence from app (container preferred, then app.state). Returns None if unavailable."""
        if not request_app:
            return None
        if hasattr(request_app.state, "container") and request_app.state.container:
            return getattr(request_app.state.container, "async_persistence", None)
        return getattr(request_app.state, "persistence", None)

    async def _get_player_and_room(
        self, request_app: Any, current_user: dict[str, Any]
    ) -> tuple[Any, Any, dict[str, str] | None]:
        """Get player data and room, returning error dict if any step fails."""
        persistence = self._get_persistence_from_app(request_app)
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

    def _validate_combat_target_match(self, target_result: Any, player: Any) -> tuple[Any, dict[str, str] | None]:
        """
        Validate target_result and resolve to a live NPC target_match.

        Returns (target_match, None) on success, or (None, error_dict) on failure.
        """
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
        if not npc_instance.is_alive:
            npc_name = getattr(npc_instance, "name", "target")
            logger.warning(
                "Player attempted to attack dead NPC",
                player_name=getattr(player, "player_name", "unknown"),
                npc_id=target_match.target_id,
                npc_name=npc_name,
            )
            return None, {"result": f"{npc_name} is already dead."}
        return target_match, None

    async def _resolve_combat_target(self, player: Any, target_name: str) -> tuple[Any, dict[str, str] | None]:
        """Resolve combat target using target resolution service."""
        target_result = await self.target_resolution_service.resolve_target(player.player_id, target_name)
        return self._validate_combat_target_match(target_result, player)

    def _room_forbids_combat(self, room_id: Any) -> bool:
        """True if the room has no_combat attribute set."""
        room = self._get_room_data(room_id)
        return bool(room and getattr(room, "attributes", {}) and room.attributes.get("no_combat"))

    async def _validate_attack_player_and_room(
        self,
        request_app: Any,
        current_user: dict[str, Any],
        target_name: str | None,
    ) -> tuple[Any, Any, dict[str, str] | None]:
        """
        Validate target name, load player/room, check DP and no_combat.
        Returns (player, room_id, None) or (None, None, error_dict).
        """
        target_validation_error = self._validate_target_name(target_name)
        if target_validation_error:
            return None, None, target_validation_error
        if target_name is None:
            return None, None, {"result": "Target name is required for attack command."}
        player, _, player_error = await self._get_player_and_room(request_app, current_user)
        if player_error:
            return None, None, player_error
        current_dp = (player.get_stats() or {}).get("current_dp", 1)
        if current_dp <= 0:
            return None, None, {"result": "You are incapacitated and cannot attack."}
        room_id = player.current_room_id
        if self._room_forbids_combat(room_id):
            return None, None, {"result": "The cosmic forces forbid violence in this place."}
        return player, room_id, None

    async def _validate_attack_target_and_action(
        self,
        player: Any,
        target_name: str,
        player_name: str,
        command: str,
    ) -> tuple[Any, Any, dict[str, str] | None]:
        """
        Resolve combat target and validate action; return (target_match, npc_instance, None) or (None, None, error_dict).
        """
        target_match, target_error = await self._resolve_combat_target(player, target_name)
        if target_error:
            return None, None, target_error
        npc_id = target_match.target_id
        npc_instance = self._get_npc_instance(npc_id)
        validation_result = await self._validate_combat_action(player_name, npc_id, command)
        if not validation_result.get("valid", False):
            return None, None, {"result": validation_result.get("message", "Invalid combat action.")}
        return target_match, npc_instance, None

    async def _validate_attack_preconditions(
        self,
        request_app: Any,
        current_user: dict[str, Any],
        player_name: str,
        command: str,
        target_name: str | None,
    ) -> tuple[Any, Any, Any, Any, dict[str, str] | None]:
        """
        Run all attack pre-checks; return (player, room_id, target_match, npc_instance, None) or (None, None, None, None, error_dict).
        """
        player, room_id, err = await self._validate_attack_player_and_room(request_app, current_user, target_name)
        if err:
            return None, None, None, None, err
        if target_name is None:
            raise RuntimeError("target_name must be set when _validate_attack_player_and_room returns no error")
        target_match, npc_instance, action_err = await self._validate_attack_target_and_action(
            player, target_name, player_name, command
        )
        if action_err:
            return None, None, None, None, action_err
        return player, room_id, target_match, npc_instance, None

    async def handle_attack_command(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat command handler interface
        self,
        command_data: dict[str, Any],
        current_user: dict[str, Any],
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
        rest_check_result = await self._check_and_interrupt_rest(request_app, player_name, current_user)
        if rest_check_result:
            return rest_check_result

        command, target_name = self._extract_combat_command_data(command_data)
        logger.debug(
            "Processing attack command",
            command=command,
            player_name=player_name,
            target_name=target_name,
        )
        try:
            _player, room_id, target_match, npc_instance, err = await self._validate_attack_preconditions(
                request_app, current_user, player_name, command, target_name
            )
            if err:
                return err
            combat_result = await self._execute_combat_action(
                player_name, target_match.target_id, command, room_id, npc_instance=npc_instance
            )
            return combat_result
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat errors unpredictable, must return error message
            logger.error("ERROR: Exception in combat handler", error=str(e), exc_info=True)
            return {"result": f"An error occurred during combat: {str(e)}"}

    async def _ensure_flee_standing(self, player: Any, player_name: str) -> dict[str, str] | None:
        """If not standing, stand and return error message; else return None."""
        stats = player.get_stats() if hasattr(player, "get_stats") else {}
        position = (stats or {}).get("position", "standing")
        if position != "standing":
            if self._player_position_service:
                await self._player_position_service.change_position(player_name, "standing")
            return {"result": "You scrabble to your feet! Try /flee again to escape."}
        return None

    def _get_flee_player_uuid(self, player: Any) -> tuple[uuid.UUID | None, dict[str, str] | None]:
        """Resolve player_id to UUID; return (uuid, None) or (None, error_dict)."""
        player_id = player.player_id
        if not isinstance(player_id, str):
            return (player_id, None)
        try:
            return (uuid.UUID(player_id), None)
        except (ValueError, TypeError):
            return (None, {"result": "You are not recognized by the cosmic forces."})

    def _get_flee_room_id(self, room_id: str) -> tuple[str | None, dict[str, str] | None]:
        """Ensure room exists and has exits; return (room_id, None) or (None, error_dict)."""
        room_data = self._get_room_data(room_id)
        if not room_data:
            return None, {"result": "You are in an unknown room."}
        exits = getattr(room_data, "exits", None) or {}
        if not exits:
            return None, {"result": "There is no escape!"}
        return room_id, None

    async def _validate_flee_combat_and_room(
        self, player_id: uuid.UUID, player: Any
    ) -> tuple[Any, str | None, dict[str, str] | None]:
        """
        Resolve combat, room, exits, and movement service for flee.
        Returns (combat, room_id, None) or (None, None, error_dict).
        """
        if not self._combat_service:
            return None, None, {"result": "Combat is not available."}
        combat = await self._combat_service.get_combat_by_participant(player_id)
        if not combat:
            return None, None, {"result": "You are not in combat."}
        room_id_raw = player.current_room_id or combat.room_id
        if not room_id_raw:
            return None, None, {"result": "You are not in a room."}
        room_id = str(room_id_raw)
        resolved_room_id, room_err = self._get_flee_room_id(room_id)
        if room_err:
            return None, None, room_err
        assert resolved_room_id is not None  # _get_flee_room_id returns (str, None) when room_err is None
        if not self._movement_service:
            return None, None, {"result": "Movement is not available."}
        return combat, resolved_room_id, None

    async def _resolve_flee_preconditions(
        self,
        request_app: Any,
        current_user: dict[str, Any],
        player_name: str,
    ) -> tuple[Any, uuid.UUID, Any, str]:
        """
        Resolve player, player_id, combat, and room_id for flee.

        Returns (player, player_id, combat, room_id).
        Raises FleePreconditionError with error_result dict on any precondition failure.
        """
        player, _room, player_error = await self._get_player_and_room(request_app, current_user)
        if player_error:
            raise FleePreconditionError(player_error)
        standing_error = await self._ensure_flee_standing(player, player_name)
        if standing_error:
            raise FleePreconditionError(standing_error)
        player_id, uuid_error = self._get_flee_player_uuid(player)
        if uuid_error:
            raise FleePreconditionError(uuid_error)
        if player_id is None:
            raise FleePreconditionError({"result": "You are not recognized by the cosmic forces."})
        combat, room_id, combat_error = await self._validate_flee_combat_and_room(player_id, player)
        if combat_error:
            raise FleePreconditionError(combat_error)
        if room_id is None:
            raise RuntimeError("room_id must be set when _validate_flee_combat_and_room returns no error")
        return (player, player_id, combat, room_id)

    async def handle_flee_command(
        self,
        _command_data: dict[str, Any],
        current_user: dict[str, Any],
        request: Any,
        alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /flee command: leave combat and move to random adjacent room.

        Standing check (players must stand first), success roll; on failure you remain in combat
        and lose your attack for this round, on success end combat and move.
        """
        _ = alias_storage
        request_app = request.app if request else None
        rest_check_result = await self._check_and_interrupt_rest(request_app, player_name, current_user)
        if rest_check_result:
            return rest_check_result
        try:
            _, player_id, combat, _ = await self._resolve_flee_preconditions(request_app, current_user, player_name)
        except FleePreconditionError as e:
            return e.error_result
        success = await execute_voluntary_flee(
            self._combat_service,
            self._get_room_data,
            self._movement_service,
            combat,
            player_id,
        )
        if not success:
            return {"result": "You try to flee but fail, losing your attack for this round."}
        return {"result": "You flee to safety!"}

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

    async def _validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict[str, Any]:
        """Validate combat action."""
        # Simple validation for now
        if not player_name or not npc_id or not command:
            return {"valid": False, "message": "Invalid combat parameters"}
        return {"valid": True}

    async def _get_combat_action_context(
        self, player_name: str, npc_id: str, npc_instance: Any | None
    ) -> tuple[Any, Any, str, dict[str, str] | None]:
        """
        Load player and resolve NPC instance/name for combat action.
        Returns (player, npc_instance, npc_name, None) or (None, None, "", error_dict).
        """
        player = await self.persistence.get_player_by_name(player_name)
        if not player:
            logger.error("Player not found for combat action", player_name=player_name)
            return None, None, "", {"result": "You are not recognized by the cosmic forces."}
        if npc_instance is None:
            npc_instance = self._get_npc_instance(npc_id)
        npc_name = npc_instance.name if npc_instance else "unknown target"
        return player, npc_instance, npc_name, None

    def _resolve_combat_damage(self, player: Any) -> int:
        """Resolve damage from equipped weapon or fall back to config unarmed damage."""
        config = get_config()
        damage = config.game.basic_unarmed_damage
        if not self._item_prototype_registry:
            return damage
        main_hand = (player.get_equipped_items() or {}).get("main_hand")
        weapon_info = resolve_weapon_attack_from_equipped(main_hand, self._item_prototype_registry)
        if not weapon_info:
            return damage
        integration = NPCCombatIntegration(async_persistence=self.persistence)
        attacker_stats = player.get_stats() if hasattr(player, "get_stats") else {}
        return integration.calculate_damage(
            attacker_stats=attacker_stats,
            target_stats={},  # CON does not affect damage
            weapon_damage=weapon_info.base_damage,
            damage_type=weapon_info.damage_type,
        )

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
            player, npc_instance, npc_name, ctx_error = await self._get_combat_action_context(
                player_name, npc_id, npc_instance
            )
            if ctx_error:
                return ctx_error
            player_id = str(player.player_id)
            damage = self._resolve_combat_damage(player)
            logger.info(
                "Executing combat action",
                player_name=player_name,
                player_id=player_id,
                command=command,
                npc_id=npc_id,
                damage=damage,
                npc_instance_provided=npc_instance is not None,
            )
            combat_success = await self.npc_combat_service.handle_player_attack_on_npc(
                player_id=player_id,
                npc_id=npc_id,
                room_id=room_id,
                action_type=command,
                damage=damage,
                npc_instance=npc_instance,
            )
            if not combat_success:
                logger.warning(
                    "Combat initiation failed",
                    player_name=player_name,
                    player_id=player_id,
                    npc_id=npc_id,
                    npc_name=npc_name,
                )
                return {"result": f"You cannot attack {npc_name} right now."}
            return {"result": f"You {command} {npc_name}!"}
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat action errors unpredictable, must return error message
            logger.error("Error executing combat action", error=str(e), exc_info=True)
            return {"result": f"Error executing {command} command"}


# Global combat command handler instance (initialized lazily)
_combat_command_handler: CombatCommandHandler | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_combat_command_handler(app: Any | None = None) -> CombatCommandHandler:
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
        # CRITICAL FIX: Get services from container, not app.state (container has the correct instances)
        container = getattr(app.state, "container", None)
        if not container:
            raise RuntimeError("Cannot initialize combat command handler without container")
        combat_service = getattr(container, "combat_service", None)
        event_bus = getattr(container, "event_bus", None)
        player_combat_service = getattr(container, "player_combat_service", None)
        connection_manager = getattr(container, "connection_manager", None)
        async_persistence = getattr(container, "async_persistence", None)
        item_prototype_registry = getattr(container, "item_prototype_registry", None)
        party_service = getattr(container, "party_service", None)
        movement_service = getattr(container, "movement_service", None)
        player_position_service = getattr(container, "player_position_service", None)
        _combat_command_handler = CombatCommandHandler(
            combat_service=combat_service,
            event_bus=event_bus,
            player_combat_service=player_combat_service,
            connection_manager=connection_manager,
            async_persistence=async_persistence,
            item_prototype_registry=item_prototype_registry,
            party_service=party_service,
            movement_service=movement_service,
            player_position_service=player_position_service,
        )
    return _combat_command_handler


# Individual command handler functions for the command service
async def handle_attack_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle attack command."""
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_attack_command(command_data, current_user, request, alias_storage, player_name)


async def handle_punch_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
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
    command_data: dict[str, Any],
    current_user: dict[str, Any],
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


async def handle_flee_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle flee command: leave combat and move to random adjacent room."""
    app = getattr(request, "app", None)
    handler = get_combat_command_handler(app)
    return await handler.handle_flee_command(command_data, current_user, request, alias_storage, player_name)


async def handle_strike_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
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
