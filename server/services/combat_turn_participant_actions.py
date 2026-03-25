"""
NPC and player turn execution for combat auto-progression.

Extracted from combat_turn_processor to keep module size under limit.
Handles process_npc_turn, process_player_turn, and damage resolution helpers.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, cast
from uuid import UUID

from fastapi import FastAPI
from structlog.stdlib import BoundLogger

from server.async_persistence import AsyncPersistenceLayer
from server.config import AppConfig, get_config
from server.container.main import ApplicationContainer
from server.game.items.prototype_registry import PrototypeRegistry
from server.game.player_service import PlayerService
from server.game.weapons import resolve_weapon_attack_from_equipped
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.aggro_threat import get_npc_current_target, update_aggro
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


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


def _get_combat_container_services(
    config: AppConfig,
) -> tuple[PlayerService | None, PrototypeRegistry | None, AsyncPersistenceLayer | None]:
    """Return (player_service, registry, async_persistence) from app container, or (None, None, None)."""
    app_candidate = getattr(config, "_app_instance", None)
    if app_candidate is None:
        return None, None, None
    app = cast(FastAPI, app_candidate)
    container_candidate = getattr(app.state, "container", None)
    if container_candidate is None:
        return None, None, None
    container = cast(ApplicationContainer, container_candidate)
    return (
        cast(PlayerService | None, container.player_service),
        cast(PrototypeRegistry | None, container.item_prototype_registry),
        cast(AsyncPersistenceLayer | None, container.async_persistence),
    )


async def _get_target_stats_for_damage(
    target: CombatParticipant, async_persistence: AsyncPersistenceLayer | None
) -> dict[str, object]:
    """Resolve target stats dict for damage calculation (player or default)."""
    if target.participant_type != CombatParticipantType.PLAYER or not async_persistence:
        return {"constitution": 50}
    try:
        target_player = await async_persistence.get_player_by_id(target.participant_id)
        stats_candidate: object
        if target_player and hasattr(target_player, "get_stats"):
            # Widen for type checker: get_stats() is typed as dict but may not be at runtime.
            stats_candidate = cast(object, target_player.get_stats())
        else:
            stats_candidate = cast(object, {})
    except (TypeError, ValueError, AttributeError):
        return {"constitution": 50}
    if isinstance(stats_candidate, dict):
        return cast(dict[str, object], stats_candidate)
    return {"constitution": 50}


def _strength_modifier_from_attacker_stats(attacker_stats: dict[str, object]) -> int:
    """Parse strength from attacker stats dict; default 50 when missing or invalid."""
    strength_mod_raw = attacker_stats.get("strength", 50)
    if isinstance(strength_mod_raw, int | float):
        return int(strength_mod_raw)
    if isinstance(strength_mod_raw, str) and strength_mod_raw.isdigit():
        return int(strength_mod_raw)
    return 50


def _apply_physical_strength_bonus(base_damage: int, damage_type: str, attacker_stats: dict[str, object]) -> int:
    """Add CoC-style strength bonus for physical attacks (same formula as NPC combat integration)."""
    if damage_type != "physical":
        return base_damage
    strength_mod = _strength_modifier_from_attacker_stats(attacker_stats)
    strength_bonus = max(0, (strength_mod - 50) // 2)
    return base_damage + strength_bonus


def _attacker_stats_dict_from_full_player(full_player: object) -> dict[str, object]:
    """Normalize full_player.get_stats() to a dict for damage math."""
    get_stats_attr: object = cast(object, getattr(full_player, "get_stats", None))
    if not callable(get_stats_attr):
        return {}
    get_stats_fn = cast(Callable[[], object], get_stats_attr)
    raw_stats: object = get_stats_fn()
    if isinstance(raw_stats, dict):
        return cast(dict[str, object], raw_stats)
    return {}


async def _weapon_damage_from_equipped_player(
    full_player: object,
    registry: PrototypeRegistry,
    target: CombatParticipant,
    async_persistence: AsyncPersistenceLayer | None,
    unarmed_damage: int,
    default_damage_type: str,
) -> tuple[int, str]:
    """Resolve rolled damage and type from main-hand weapon, or unarmed fallback."""
    get_equipped_attr: object = cast(object, getattr(full_player, "get_equipped_items", None))
    if not callable(get_equipped_attr):
        return unarmed_damage, default_damage_type
    get_equipped_fn = cast(Callable[[], object], get_equipped_attr)
    equipped_raw: object = get_equipped_fn()
    equipped: dict[str, object] = cast(dict[str, object], equipped_raw) if isinstance(equipped_raw, dict) else {}
    main_hand_candidate = equipped.get("main_hand")
    main_hand_stack: dict[str, object] | None = (
        cast(dict[str, object], main_hand_candidate) if isinstance(main_hand_candidate, dict) else None
    )
    weapon_info = resolve_weapon_attack_from_equipped(main_hand_stack, registry)
    if not weapon_info:
        return unarmed_damage, default_damage_type

    attacker_stats = _attacker_stats_dict_from_full_player(full_player)
    # Target stats are currently unused for damage math but may be used in future balancing.
    target_stats = await _get_target_stats_for_damage(target, async_persistence)
    _ = target_stats

    damage_type = weapon_info.damage_type
    base_damage = _apply_physical_strength_bonus(int(weapon_info.base_damage), damage_type, attacker_stats)
    return max(1, base_damage), damage_type


async def resolve_player_attack_damage(
    _combat_service: CombatService,
    player: CombatParticipant,
    target: CombatParticipant,
    config: AppConfig,
) -> tuple[int, str]:
    """
    Resolve damage and damage_type for a player auto-attack from equipped main_hand or unarmed fallback.

    _combat_service: Unused; kept first so call sites match process_* (same positional shape as process_attack).

    Returns:
        (damage, damage_type) for use with process_attack.
    """
    damage = config.game.basic_unarmed_damage
    damage_type = "physical"

    player_service, registry, async_persistence = _get_combat_container_services(config)
    if not player_service or not registry:
        return damage, damage_type

    # PlayerService.persistence is typed as Any on the service; AsyncPersistenceLayer has a typed API.
    persistence_layer = cast(AsyncPersistenceLayer, player_service.persistence)
    full_player = await persistence_layer.get_player_by_id(player.participant_id)
    if not full_player:
        return damage, damage_type

    return await _weapon_damage_from_equipped_player(
        full_player, registry, target, async_persistence, damage, damage_type
    )


def _should_continue_npc_turn(combat: CombatInstance, npc: CombatParticipant, current_tick: int) -> bool:
    """Return False if we should return early (missing participant_id or cannot act)."""
    if not hasattr(npc, "participant_id"):
        logger.error("NPC object missing participant_id attribute", npc=npc)
        return False
    logger.debug("NPC participant_id", participant_id=npc.participant_id, id_type=type(npc.participant_id).__name__)
    if not npc.can_act_in_combat():
        logger.info(
            "NPC cannot act (dead or inactive)",
            npc_name=npc.name,
            current_dp=npc.current_dp,
            combat_id=combat.combat_id,
        )
        npc.last_action_tick = current_tick
        return False
    return True


async def _resolve_npc_target(
    combat: CombatInstance, npc: CombatParticipant, combat_service: CombatService
) -> CombatParticipant | None:
    """Resolve target via aggro (ADR-016), then fallback to _select_npc_target."""
    new_target_id, did_switch = update_aggro(combat, npc, combat.room_id, combat.participants)
    if did_switch and new_target_id:
        new_target = combat.participants.get(new_target_id)
        new_target_name = new_target.name if new_target else "someone"
        await combat_service.broadcast_aggro_target_switches(
            combat.room_id, combat.combat_id, [(npc.participant_id, npc.name, new_target_name)]
        )
    target_id = get_npc_current_target(combat, npc.participant_id)
    if target_id is not None:
        target = combat.participants.get(target_id)
        if target is not None and not target.is_dead():
            return target
    return _select_npc_target(combat, npc.participant_id)


async def _execute_npc_attack(
    combat_service: CombatService, npc: CombatParticipant, target: CombatParticipant, current_tick: int
) -> None:
    """Perform NPC attack and update last_action_tick."""
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


async def process_npc_turn(
    combat_service: CombatService, combat: CombatInstance, npc: CombatParticipant, current_tick: int
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
        if not _should_continue_npc_turn(combat, npc, current_tick):
            return
        target = await _resolve_npc_target(combat, npc, combat_service)
        if not target:
            logger.warning("No target found for NPC", npc_name=npc.name, combat_id=combat.combat_id)
            return
        logger.debug("NPC performing automatic attack", npc_name=npc.name, target_name=target.name)
        await _execute_npc_attack(combat_service, npc, target, current_tick)
    except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
        logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)


def _should_continue_player_turn(combat: CombatInstance, player: CombatParticipant, current_tick: int) -> bool:
    """Return False if we should return early (missing participant_id or cannot act)."""
    if not hasattr(player, "participant_id"):
        logger.error("Player object missing participant_id attribute", player=player)
        return False
    logger.debug(
        "Player participant_id",
        participant_id=player.participant_id,
        participant_id_type=type(player.participant_id),
    )
    if not player.can_act_in_combat():
        logger.info(
            "Player cannot act (unconscious or inactive)",
            player_name=player.name,
            current_dp=player.current_dp,
            combat_id=combat.combat_id,
        )
        player.last_action_tick = current_tick
        return False
    return True


def _select_player_target(combat: CombatInstance, player: CombatParticipant) -> CombatParticipant | None:
    """Select first non-self participant as target."""
    for participant in combat.participants.values():
        if participant.participant_id != player.participant_id:
            return participant
    return None


def _should_skip_for_casting(combat_service: CombatService, player: CombatParticipant, current_tick: int) -> bool:
    """Return True if player is casting (and we should skip autoattack); sets last_action_tick when skipping."""
    try:
        # Use attribute access (not getattr): CombatService.magic_service is typed; getattr erases to Any.
        magic_service = combat_service.magic_service
        if magic_service and magic_service.casting_state_manager.is_casting(player.participant_id):
            casting_state = magic_service.casting_state_manager.get_casting_state(player.participant_id)
            logger.debug(
                "Player is casting, skipping autoattack",
                player_name=player.name,
                spell_name=casting_state.spell_name if casting_state else "unknown",
            )
            player.last_action_tick = current_tick
            return True
    except (AttributeError, TypeError, KeyError) as e:
        logger.debug("Could not check casting state for autoattack", player_name=player.name, error=str(e))
    return False


async def _execute_player_attack(
    combat_service: CombatService,
    player: CombatParticipant,
    target: CombatParticipant,
    current_tick: int,
) -> None:
    """Resolve damage, process attack, log, and update last_action_tick."""
    config = get_config()
    damage, damage_type = await resolve_player_attack_damage(combat_service, player, target, config)
    combat_result = await combat_service.process_attack(
        attacker_id=player.participant_id,
        target_id=target.participant_id,
        damage=damage,
        damage_type=damage_type,
    )
    if combat_result.success:
        logger.info("Player automatically attacked", player_name=player.name, target_name=target.name, damage=damage)
    else:
        logger.warning("Player automatic attack failed", player_name=player.name, message=combat_result.message)
    player.last_action_tick = current_tick


async def process_player_turn(
    combat_service: CombatService, combat: CombatInstance, player: CombatParticipant, current_tick: int
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
        if not _should_continue_player_turn(combat, player, current_tick):
            return
        target = _select_player_target(combat, player)
        if not target:
            logger.warning("No target found for player", player_name=player.name, combat_id=combat.combat_id)
            return
        if _should_skip_for_casting(combat_service, player, current_tick):
            return
        logger.info(
            "Executing default attack (no queued action)",
            combat_id=combat.combat_id,
            attacker_id=player.participant_id,
            target_id=target.participant_id,
            participant_ids=[str(pid) for pid in combat.participants.keys()],
        )
        logger.debug("Player performing automatic attack", player_name=player.name, target_name=target.name)
        await _execute_player_attack(combat_service, player, target, current_tick)
    except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
        player_type = type(player)
        player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
        logger.error("Error processing player turn", player_name=player_name, error=str(e), exc_info=True)
