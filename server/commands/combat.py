"""
Combat command handlers for the MUD.

This module implements the combat commands including attack, punch, kick, strike,
and other combat-related actions.
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.logging.combat_audit import combat_audit_logger
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
        command = command_data.get("command_type", "attack")
        args = command_data.get("args", [])
        target_name = args[0] if args else None

        logger.info(f"Processing attack command '{command}' from {player_name} targeting '{target_name}'")

        # Use combat validator for enhanced validation
        player_context = {
            "player_id": current_user.get("player_id"),
            "player_name": player_name,
            "room_id": None,  # Will be set later
        }

        is_valid, error_msg, warning_msg = self.combat_validator.validate_combat_command(command_data, player_context)

        if not is_valid:
            # Log validation failure for security monitoring
            combat_audit_logger.log_combat_validation_failure(
                player_id=current_user.get("player_id", "unknown"),
                player_name=player_name,
                validation_type="command_validation",
                failure_reason=error_msg,
                command_data=command_data,
            )
            return {"result": error_msg}

        if warning_msg:
            logger.warning(f"Combat validation warning: {warning_msg}")
            # Log security warning
            combat_audit_logger.log_combat_security_event(
                event_type="validation_warning",
                player_id=current_user.get("player_id", "unknown"),
                player_name=player_name,
                security_level="medium",
                description=warning_msg,
            )

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
        available_targets = []
        for npc_id in room.npcs:
            # Try to get NPC instance
            npc_instance = self._get_npc_instance(npc_id)
            if npc_instance:
                available_targets.append(npc_instance.name)
                if npc_instance.name.lower() == target_name.lower():
                    npc_found = npc_instance
                    break

        # Use combat validator for target validation
        target_exists, target_error = self.combat_validator.validate_target_exists(target_name, available_targets)

        if not target_exists:
            return {"result": target_error}

        # Check if NPC is alive
        if not npc_found.is_alive:
            alive_check, alive_error = self.combat_validator.validate_target_alive(target_name, npc_found.is_alive)
            if not alive_check:
                return {"result": alive_error}

        # Validate attack strength
        player_level = player.level if hasattr(player, "level") else 1
        npc_level = getattr(npc_found, "level", 1) if hasattr(npc_found, "level") else 1

        can_attack, strength_error, strength_warning = self.combat_validator.validate_attack_strength(
            player_level, npc_level, weapon_power=1
        )

        if not can_attack:
            return {"result": strength_error}

        if strength_warning:
            logger.warning(f"Attack strength warning: {strength_warning}")

        # Log combat start
        combat_audit_logger.log_combat_start(
            player_id=player_id,
            player_name=player_name,
            target_id=npc_id,
            target_name=target_name,
            room_id=room_id,
            action_type=command,
        )

        # Execute the attack
        try:
            success = self.npc_combat_service.handle_player_attack_on_npc(
                player_id=player_id,
                npc_id=npc_id,
                room_id=room_id,
                action_type=command,
                damage=1,  # MVP: all attacks do 1 damage
            )

            # Log attack execution
            combat_audit_logger.log_combat_attack(
                player_id=player_id,
                player_name=player_name,
                target_id=npc_id,
                target_name=target_name,
                action_type=command,
                damage_dealt=1 if success else 0,
                target_hp_before=50,  # Placeholder - would get from NPC
                target_hp_after=49 if success else 50,  # Placeholder
                success=success,
            )

            if success:
                result_msg = self.combat_validator.get_combat_result_message(command, target_name, True, 1)
                return {"result": result_msg}
            else:
                result_msg = self.combat_validator.get_combat_result_message(command, target_name, False, 0)
                return {"result": result_msg}

        except Exception as e:
            logger.error(f"Error in combat: {str(e)}")
            # Log combat error for security monitoring
            combat_audit_logger.log_combat_security_event(
                event_type="combat_error",
                player_id=player_id,
                player_name=player_name,
                security_level="high",
                description=f"Combat execution error: {str(e)}",
                additional_data={
                    "target_id": npc_id,
                    "target_name": target_name,
                    "action_type": command,
                    "error_type": type(e).__name__,
                },
            )
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
