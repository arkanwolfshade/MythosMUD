"""
NPC and player turn execution for combat auto-progression.

Extracted from combat_turn_processor to keep module size under limit.
Handles process_npc_turn, process_player_turn, and damage resolution helpers.
"""

from typing import Any
from uuid import UUID

from server.config import get_config
from server.game.weapons import resolve_weapon_attack_from_equipped
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.npc.combat_integration import NPCCombatIntegration
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _select_npc_target(combat: CombatInstance, npc_participant_id: UUID) -> CombatParticipant | None:
    """
    Select target for NPC attack.

    Prefers participants that are not dead (includes mortally wounded players at 0 DP).
    CRITICAL: Players at 0 DP are mortally wounded but NOT dead - they should still be attackable.
    Use is_dead() instead of is_alive() to ensure we can target mortally wounded players.

    Args:
        combat: Combat instance
        npc_participant_id: ID of the NPC selecting target

    Returns:
        Target participant or None if no valid target found
    """
    # Prefer participants that are not dead (includes mortally wounded players at 0 DP)
    for participant in combat.participants.values():
        if participant.participant_id != npc_participant_id:
            # Check if target is not dead (for players: DP > -10, for NPCs: DP > 0)
            # This includes mortally wounded players at 0 DP who are still attackable
            if not participant.is_dead():
                return participant

    # Fallback: if no non-dead target found, try any participant (shouldn't happen but defensive)
    for participant in combat.participants.values():
        if participant.participant_id != npc_participant_id:
            return participant

    return None


def _get_combat_container_services(config: Any) -> tuple[Any, Any, Any]:
    """Return (player_service, registry, async_persistence) from app container, or (None, None, None)."""
    app = getattr(config, "_app_instance", None)
    if not app or not hasattr(app.state, "container"):
        return None, None, None
    container = app.state.container
    return (
        getattr(container, "player_service", None),
        getattr(container, "item_prototype_registry", None),
        getattr(container, "async_persistence", None),
    )


async def _get_target_stats_for_damage(target: CombatParticipant, async_persistence: Any) -> dict[str, Any]:
    """Resolve target stats dict for damage calculation (player or default)."""
    if target.participant_type != CombatParticipantType.PLAYER or not async_persistence:
        return {"constitution": 50}
    try:
        target_player = await async_persistence.get_player_by_id(target.participant_id)
        stats = target_player.get_stats() if target_player and hasattr(target_player, "get_stats") else {}
    except (TypeError, ValueError, AttributeError):
        return {"constitution": 50}
    return stats if isinstance(stats, dict) else {"constitution": 50}


async def resolve_player_attack_damage(
    combat_service: Any,  # pylint: disable=unused-argument  # Reason: API consistency with process_*; not needed for damage resolution
    player: CombatParticipant,
    target: CombatParticipant,
    config: Any,
) -> tuple[int, str]:
    """
    Resolve damage and damage_type for a player auto-attack from equipped main_hand or unarmed fallback.

    Returns:
        (damage, damage_type) for use with process_attack.
    """
    damage = config.game.basic_unarmed_damage
    damage_type = "physical"

    player_service, registry, async_persistence = _get_combat_container_services(config)
    if not player_service or not registry:
        return damage, damage_type

    full_player = await player_service.persistence.get_player_by_id(player.participant_id)
    if not full_player:
        return damage, damage_type

    main_hand_stack = (full_player.get_equipped_items() or {}).get("main_hand")
    weapon_info = resolve_weapon_attack_from_equipped(main_hand_stack, registry)

    if not weapon_info:
        return damage, damage_type

    damage_type = weapon_info.damage_type
    attacker_stats = full_player.get_stats() if hasattr(full_player, "get_stats") else {}
    if not isinstance(attacker_stats, dict):
        attacker_stats = {}

    target_stats = await _get_target_stats_for_damage(target, async_persistence)
    integration = NPCCombatIntegration(async_persistence=async_persistence)
    damage = integration.calculate_damage(
        attacker_stats=attacker_stats,
        target_stats=target_stats,
        weapon_damage=weapon_info.base_damage,
        damage_type=damage_type,
    )
    return damage, damage_type


async def process_npc_turn(
    combat_service: Any, combat: CombatInstance, npc: CombatParticipant, current_tick: int
) -> None:
    """
    Process NPC turn with actual combat attack.

    Args:
        combat_service: Parent CombatService for process_attack
        combat: Combat instance
        npc: NPC participant
        current_tick: Current game tick
    """
    try:
        logger.debug("_process_npc_turn called", npc_type=type(npc).__name__, npc=npc)
        if hasattr(npc, "participant_id"):
            logger.debug(
                "NPC participant_id", participant_id=npc.participant_id, id_type=type(npc.participant_id).__name__
            )
        else:
            logger.error("NPC object missing participant_id attribute", npc=npc)
            return

        if not npc.can_act_in_combat():
            logger.info(
                "NPC cannot act (dead or inactive)",
                npc_name=npc.name,
                current_dp=npc.current_dp,
                combat_id=combat.combat_id,
            )
            npc.last_action_tick = current_tick
            return

        # Select target: prefer participants that are not dead (includes mortally wounded players at 0 DP)
        target = _select_npc_target(combat, npc.participant_id)
        if not target:
            logger.warning("No target found for NPC", npc_name=npc.name, combat_id=combat.combat_id)
            return

        logger.debug("NPC performing automatic attack", npc_name=npc.name, target_name=target.name)

        config = get_config()
        damage = config.game.basic_unarmed_damage
        combat_result = await combat_service.process_attack(
            attacker_id=npc.participant_id, target_id=target.participant_id, damage=damage
        )
        if combat_result.success:
            logger.info("NPC automatically attacked", npc_name=npc.name, target_name=target.name, damage=damage)
        else:
            logger.warning("NPC automatic attack failed", npc_name=npc.name, message=combat_result.message)

        npc.last_action_tick = current_tick

    except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
        logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)
        logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)


async def process_player_turn(
    combat_service: Any, combat: CombatInstance, player: CombatParticipant, current_tick: int
) -> None:
    """
    Process player turn with automatic basic attack.

    Args:
        combat_service: Parent CombatService for process_attack and magic_service
        combat: Combat instance
        player: Player participant
        current_tick: Current game tick
    """
    try:
        logger.debug("_process_player_turn called", player_type=type(player), player=player)
        if hasattr(player, "participant_id"):
            logger.debug(
                "Player participant_id",
                participant_id=player.participant_id,
                participant_id_type=type(player.participant_id),
            )
        else:
            logger.error("Player object missing participant_id attribute", player=player)
            return

        if not player.can_act_in_combat():
            logger.info(
                "Player cannot act (unconscious or inactive)",
                player_name=player.name,
                current_dp=player.current_dp,
                combat_id=combat.combat_id,
            )
            player.last_action_tick = current_tick
            return

        target = None
        for participant in combat.participants.values():
            if participant.participant_id != player.participant_id:
                target = participant
                break

        if not target:
            logger.warning("No target found for player", player_name=player.name, combat_id=combat.combat_id)
            return

        try:
            magic_service = getattr(combat_service, "magic_service", None)
            if magic_service and magic_service.casting_state_manager.is_casting(player.participant_id):
                casting_state = magic_service.casting_state_manager.get_casting_state(player.participant_id)
                logger.debug(
                    "Player is casting, skipping autoattack",
                    player_name=player.name,
                    spell_name=casting_state.spell_name if casting_state else "unknown",
                )
                player.last_action_tick = current_tick
                return
        except (AttributeError, TypeError, KeyError) as e:
            logger.debug("Could not check casting state for autoattack", player_name=player.name, error=str(e))

        logger.info(
            "Executing default attack (no queued action)",
            combat_id=combat.combat_id,
            attacker_id=player.participant_id,
            target_id=target.participant_id,
            participant_ids=[str(pid) for pid in combat.participants.keys()],
        )
        logger.debug("Player performing automatic attack", player_name=player.name, target_name=target.name)

        config = get_config()
        damage, damage_type = await resolve_player_attack_damage(combat_service, player, target, config)

        combat_result = await combat_service.process_attack(
            attacker_id=player.participant_id,
            target_id=target.participant_id,
            damage=damage,
            damage_type=damage_type,
        )

        if combat_result.success:
            logger.info(
                "Player automatically attacked", player_name=player.name, target_name=target.name, damage=damage
            )
        else:
            logger.warning("Player automatic attack failed", player_name=player.name, message=combat_result.message)

        player.last_action_tick = current_tick

    except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
        player_type = type(player)
        player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
        logger.error("Error processing player turn", player_name=player_name, error=str(e), exc_info=True)
