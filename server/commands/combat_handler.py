"""
Combat command handler class and shared helpers.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

import uuid
from typing import TYPE_CHECKING, Any

from server.alias_storage import AliasStorage
from server.commands.combat_attack import run_handle_attack_command
from server.commands.combat_flee import run_handle_flee_command
from server.commands.combat_taunt import run_handle_taunt_command
from server.commands.rest_command import _cancel_rest_countdown, is_player_resting
from server.game.player_service import PlayerService
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.schemas.shared import TargetType
from server.services.npc_combat_integration_service import NPCCombatIntegrationService
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


class CombatCommandHandler:  # pylint: disable=too-few-public-methods  # Reason: Command handler class
    """
    Handler for combat-related commands.
    Processes combat commands and integrates with the command system and combat service.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Many deps
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
        if async_persistence is None:
            raise ValueError("async_persistence is required for CombatCommandHandler")
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
        self.target_resolution_service = TargetResolutionService(
            async_persistence,  # type: ignore[arg-type]
            PlayerService(async_persistence),
        )

    # Public API for combat command modules (avoid W0212 protected-access outside tests).
    @property
    def combat_service(self) -> Any:
        """Combat service for command modules."""
        return self._combat_service

    @property
    def movement_service(self) -> Any:
        """Movement service for command modules."""
        return self._movement_service

    @property
    def player_position_service(self) -> Any:
        """Player position service for command modules."""
        return self._player_position_service

    @property
    def item_prototype_registry(self) -> Any | None:
        """Item prototype registry for command modules."""
        return self._item_prototype_registry

    async def check_and_interrupt_rest(
        self, request_app: Any, player_name: str, current_user: dict[str, Any]
    ) -> dict[str, str] | None:
        """Check if player is resting or in login grace period, interrupt rest if needed. Public API."""
        return await self._check_and_interrupt_rest(request_app, player_name, current_user)

    def extract_combat_command_data(self, command_data: dict[str, Any]) -> tuple[str, str | None]:
        """Extract command type and target name from command_data. Public API."""
        return self._extract_combat_command_data(command_data)

    def validate_target_name(self, target_name: str | None) -> dict[str, str] | None:
        """Validate that target name is provided. Public API."""
        return self._validate_target_name(target_name)

    async def get_player_and_room(
        self, request_app: Any, current_user: dict[str, Any]
    ) -> tuple[Any, Any, dict[str, str] | None]:
        """Get player data and room, returning error dict if any step fails. Public API."""
        return await self._get_player_and_room(request_app, current_user)

    def room_forbids_combat(self, room_id: Any) -> bool:
        """True if the room has no_combat attribute set. Public API."""
        return self._room_forbids_combat(room_id)

    async def resolve_combat_target(self, player: Any, target_name: str) -> tuple[Any, dict[str, str] | None]:
        """Resolve combat target using target resolution service. Public API."""
        return await self._resolve_combat_target(player, target_name)

    def get_room_data(self, room_id: str) -> Any | None:
        """Get room data from persistence. Public API."""
        return self._get_room_data(room_id)

    def get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service. Public API."""
        return self._get_npc_instance(npc_id)

    async def validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict[str, Any]:
        """Validate combat action. Public API."""
        return await self._validate_combat_action(player_name, npc_id, command)

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
        command = command_type.value if hasattr(command_type, "value") else str(command_type)
        target_name = command_data.get("target_player")
        return command, target_name

    def _validate_target_name(self, target_name: str | None) -> dict[str, str] | None:
        """Validate that target name is provided."""
        if not target_name:
            import secrets

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
        room = persistence.get_room_by_id(room_id)
        if not room:
            return None, None, {"result": "You are in an unknown room."}
        return player, room, None

    def _validate_combat_target_match(self, target_result: Any, player: Any) -> tuple[Any, dict[str, str] | None]:
        """Validate target_result and resolve to a live NPC target_match. Returns (target_match, None) or (None, error_dict)."""
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

    async def handle_attack_command(
        self,
        command_data: dict[str, Any],
        current_user: dict[str, Any],
        request: Any,
        alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """Handle attack commands (attack, punch, kick, etc.)."""
        return await run_handle_attack_command(self, command_data, current_user, request, alias_storage, player_name)

    async def handle_flee_command(
        self,
        command_data: dict[str, Any],
        current_user: dict[str, Any],
        request: Any,
        alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """Handle /flee command: leave combat and move to random adjacent room."""
        return await run_handle_flee_command(self, command_data, current_user, request, alias_storage, player_name)

    async def handle_taunt_command(
        self,
        command_data: dict[str, Any],
        current_user: dict[str, Any],
        request: Any,
        alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """Handle taunt command: draw NPC aggro (ADR-016). Room-local only."""
        return await run_handle_taunt_command(self, command_data, current_user, request, alias_storage, player_name)

    def _get_room_data(self, room_id: str) -> Any | None:
        """Get room data from persistence."""
        try:
            return self.persistence.get_room_by_id(room_id)
        except (AttributeError, TypeError) as e:
            logger.error("Error getting room data", room_id=room_id, error=str(e))
            return None

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lm = npc_instance_service.lifecycle_manager
                if lm and npc_id in lm.active_npcs:
                    return lm.active_npcs[npc_id]
            return None
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC lookup errors
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    async def _validate_combat_action(self, player_name: str, npc_id: str, command: str) -> dict[str, Any]:
        """Validate combat action."""
        if not player_name or not npc_id or not command:
            return {"valid": False, "message": "Invalid combat parameters"}
        return {"valid": True}
