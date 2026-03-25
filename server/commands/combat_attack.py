"""
Attack command flow: validation and execution.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from typing import Any, cast

from server.config import get_config
from server.game.weapons import resolve_weapon_attack_from_equipped
from server.npc.combat_integration import NPCCombatIntegration
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def _validate_attack_player_and_room(
    handler: Any,
    request_app: Any,
    current_user: dict[str, Any],
    target_name: str | None,
) -> tuple[Any, Any, dict[str, str] | None]:
    """
    Validate target name, load player/room, check DP and no_combat.
    Returns (player, room_id, None) or (None, None, error_dict).
    """
    target_validation_error = handler.validate_target_name(target_name)
    if target_validation_error:
        return None, None, target_validation_error
    if target_name is None:
        return None, None, {"result": "Target name is required for attack command."}
    player, _, player_error = await handler.get_player_and_room(request_app, current_user)
    if player_error:
        return None, None, player_error
    current_dp = (player.get_stats() or {}).get("current_dp", 1)
    if current_dp <= 0:
        return None, None, {"result": "You are incapacitated and cannot attack."}
    room_id = player.current_room_id
    if handler.room_forbids_combat(room_id):
        return None, None, {"result": "The cosmic forces forbid violence in this place."}
    return player, room_id, None


async def _validate_attack_target_and_action(
    handler: Any,
    player: Any,
    target_name: str,
    player_name: str,
    command: str,
) -> tuple[Any, Any, dict[str, str] | None]:
    """
    Resolve combat target and validate action; return (target_match, npc_instance, None) or (None, None, error_dict).
    """
    target_match, target_error = await handler.resolve_combat_target(player, target_name)
    if target_error:
        return None, None, target_error
    npc_id = target_match.target_id
    npc_instance = handler.get_npc_instance(npc_id)
    validation_result = await handler.validate_combat_action(player_name, npc_id, command)
    if not validation_result.get("valid", False):
        return None, None, {"result": validation_result.get("message", "Invalid combat action.")}
    return target_match, npc_instance, None


async def _validate_attack_preconditions(
    handler: Any,
    request_app: Any,
    current_user: dict[str, Any],
    player_name: str,
    command: str,
    target_name: str | None,
) -> tuple[Any, Any, Any, Any, dict[str, str] | None]:
    """
    Run all attack pre-checks; return (player, room_id, target_match, npc_instance, None) or error 5-tuple.
    """
    player, room_id, err = await _validate_attack_player_and_room(handler, request_app, current_user, target_name)
    if err:
        return None, None, None, None, err
    if target_name is None:
        raise RuntimeError("target_name must be set when _validate_attack_player_and_room returns no error")
    target_match, npc_instance, action_err = await _validate_attack_target_and_action(
        handler, player, target_name, player_name, command
    )
    if action_err:
        return None, None, None, None, action_err
    return player, room_id, target_match, npc_instance, None


async def _get_combat_action_context(
    handler: Any, player_name: str, npc_id: str, npc_instance: Any | None
) -> tuple[Any, Any, str, dict[str, str] | None]:
    """
    Load player and resolve NPC instance/name for combat action.
    Returns (player, npc_instance, npc_name, None) or (None, None, "", error_dict).
    """
    player = await handler.persistence.get_player_by_name(player_name)
    if not player:
        logger.error("Player not found for combat action", player_name=player_name)
        return None, None, "", {"result": "You are not recognized by the cosmic forces."}
    if npc_instance is None:
        npc_instance = handler.get_npc_instance(npc_id)
    npc_name = npc_instance.name if npc_instance else "unknown target"
    return player, npc_instance, npc_name, None


def _resolve_combat_damage(handler: Any, player: Any) -> int:
    """Resolve damage from equipped weapon or fall back to config unarmed damage."""
    config = get_config()
    damage = config.game.basic_unarmed_damage
    if not handler.item_prototype_registry:
        return damage
    main_hand = (player.get_equipped_items() or {}).get("main_hand")
    weapon_info = resolve_weapon_attack_from_equipped(main_hand, handler.item_prototype_registry)
    if not weapon_info:
        return damage
    integration = NPCCombatIntegration(async_persistence=handler.persistence)
    attacker_stats = player.get_stats() if hasattr(player, "get_stats") else {}
    return integration.calculate_damage(
        attacker_stats=attacker_stats,
        target_stats={},
        weapon_damage=weapon_info.base_damage,
        damage_type=weapon_info.damage_type,
    )


async def _execute_combat_action(
    handler: Any,
    player_name: str,
    npc_id: str,
    command: str,
    room_id: str,
    npc_instance: Any | None = None,
) -> dict[str, str]:
    """Execute combat action using the proper combat service."""
    try:
        player, npc_instance, npc_name, ctx_error = await _get_combat_action_context(
            handler, player_name, npc_id, npc_instance
        )
        if ctx_error:
            return ctx_error
        player_id = str(player.player_id)
        damage = _resolve_combat_damage(handler, player)
        logger.info(
            "Executing combat action",
            player_name=player_name,
            player_id=player_id,
            command=command,
            npc_id=npc_id,
            damage=damage,
            npc_instance_provided=npc_instance is not None,
        )
        combat_success = await handler.npc_combat_service.handle_player_attack_on_npc(
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat action errors unpredictable
        logger.error("Error executing combat action", error=str(e), exc_info=True)
        return {"result": f"Error executing {command} command"}


async def run_handle_attack_command(
    handler: Any,
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: Any,
    player_name: str,
) -> dict[str, str]:
    """Handle attack commands (attack, punch, kick, etc.)."""
    _ = alias_storage
    request_app = request.app if request else None
    rest_check_result = await handler.check_and_interrupt_rest(request_app, player_name, current_user)
    if rest_check_result:
        return cast(dict[str, str], rest_check_result)
    command, target_name = handler.extract_combat_command_data(command_data)
    logger.debug(
        "Processing attack command",
        command=command,
        player_name=player_name,
        target_name=target_name,
    )
    try:
        _player, room_id, target_match, npc_instance, err = await _validate_attack_preconditions(
            handler, request_app, current_user, player_name, command, target_name
        )
        if err:
            return err
        combat_result = await _execute_combat_action(
            handler, player_name, target_match.target_id, command, room_id, npc_instance=npc_instance
        )
        return combat_result
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Combat errors unpredictable
        logger.error("ERROR: Exception in combat handler", error=str(e), exc_info=True)
        return {"result": f"An error occurred during combat: {str(e)}"}
