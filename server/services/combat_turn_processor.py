"""
Combat turn processing logic.

Handles round-based combat where all participants act each round in initiative order.
Processes queued actions and generates default actions for automatic combat progression.
"""

# pylint: disable=too-few-public-methods  # Reason: Turn processor class with focused responsibility, minimal public interface

import uuid
from typing import Any

from server.config import get_config
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatTurnProcessor:
    """Handles combat turn processing and auto-progression."""

    def __init__(self, combat_service: Any) -> None:
        """
        Initialize the turn processor.

        Args:
            combat_service: Reference to the parent CombatService for attack processing
        """
        self._combat_service = combat_service

    async def process_game_tick(
        self, current_tick: int, active_combats: dict[uuid.UUID, CombatInstance], auto_progression_enabled: bool
    ) -> None:
        """
        Process game tick for combat auto-progression.

        Args:
            current_tick: Current game tick number
            active_combats: Dictionary of active combat instances
            auto_progression_enabled: Whether auto-progression is enabled
        """
        logger.info(
            "Combat tick processing",
            tick=current_tick,
            auto_progression_enabled=auto_progression_enabled,
            active_combats_count=len(active_combats),
        )
        if not auto_progression_enabled:
            logger.info("[COMBAT TICK] Auto-progression is disabled, returning early")
            return

        # Check all active combats for auto-progression
        for combat_id, combat in list(active_combats.items()):
            if combat.status != CombatStatus.ACTIVE:
                continue

            if not combat.auto_progression_enabled:
                continue

            logger.debug(
                "Combat auto-progression check",
                combat_id=combat_id,
                current_tick=current_tick,
                next_turn_tick=combat.next_turn_tick,
                auto_progression_enabled=combat.auto_progression_enabled,
            )

            # Check if it's time for the next round (all participants act each round)
            if current_tick >= combat.next_turn_tick:
                logger.debug(
                    "Round progression triggered", combat_id=combat_id, tick=current_tick, round=combat.combat_round
                )
                await self._execute_round(combat, current_tick)

    async def _execute_round(self, combat: CombatInstance, current_tick: int) -> None:
        """
        Execute all actions for a round - all participants act sequentially in initiative order.

        Args:
            combat: Combat instance to process
            current_tick: Current game tick
        """
        # Update activity
        combat.update_activity(current_tick)

        # Load queued actions into round_actions for this round
        # Actions are queued with round = combat.combat_round + 1 (the round they should execute)
        # When we're executing a round, combat.combat_round hasn't been incremented yet,
        # so we check for actions queued for combat.combat_round + 1
        next_round = combat.combat_round + 1
        combat.round_actions.clear()
        for participant_id, queued_actions_list in combat.queued_actions.items():
            # Get actions queued for this round (next_round)
            for action in queued_actions_list:
                if action.round == next_round:
                    combat.round_actions[participant_id] = action
                    break  # Only one action per participant per round

        # Get all alive participants sorted by initiative (dexterity, highest first)
        participants_by_initiative = combat.get_participants_by_initiative()

        if not participants_by_initiative:
            logger.warning("No alive participants in combat", combat_id=combat.combat_id)
            await self._combat_service.end_combat(combat.combat_id, "No alive participants")
            return

        logger.debug(
            "Executing round",
            combat_id=combat.combat_id,
            round=combat.combat_round + 1,
            participants_count=len(participants_by_initiative),
            queued_actions_count=len(combat.round_actions),
        )

        # Execute actions for all participants in initiative order
        for participant in participants_by_initiative:
            if not participant.is_alive():
                continue

            # Check if participant has a queued action for this round
            if participant.participant_id in combat.round_actions:
                action = combat.round_actions[participant.participant_id]
                await self._execute_queued_action(combat, participant, action, current_tick)
                # Clear only this specific queued action (may have others queued for future rounds)
                combat.clear_queued_actions(participant.participant_id, round_number=next_round)
            else:
                # Generate and execute default action (basic attack)
                await self._execute_default_action(combat, participant, current_tick)

        # Advance to next round
        combat.advance_turn(current_tick)

    async def _execute_queued_action(  # pylint: disable=too-many-locals,too-many-branches,too-many-nested-blocks  # Reason: Method handles complex spell execution with multiple nested conditions - refactoring would reduce clarity of action flow
        self, combat: CombatInstance, participant: CombatParticipant, action: CombatAction, current_tick: int
    ) -> None:
        """
        Execute a queued action for a participant.

        Args:
            combat: Combat instance
            participant: Participant executing the action
            action: The queued action to execute
            current_tick: Current game tick
        """
        logger.debug(
            "Executing queued action",
            combat_id=combat.combat_id,
            participant_id=participant.participant_id,
            participant_name=participant.name,
            action_type=action.action_type,
        )

        # Handle different action types
        if action.action_type == "attack":
            # Process attack - result is not used as process_attack has side effects (updates combat state)
            await self._combat_service.process_attack(
                attacker_id=participant.participant_id, target_id=action.target_id, damage=action.damage
            )
        elif action.action_type == "spell":
            # Execute queued spell action via magic service
            # Note: Spell costs were already paid when casting started, we just apply effects here
            if hasattr(self._combat_service, "magic_service") and self._combat_service.magic_service:
                magic_service = self._combat_service.magic_service
                try:
                    # Get spell from registry
                    spell = magic_service.spell_registry.get_spell(action.spell_id) if action.spell_id else None
                    if not spell:
                        logger.warning(
                            "Spell not found for execution", spell_id=action.spell_id, spell_name=action.spell_name
                        )
                        participant.last_action_tick = current_tick
                        return

                    # Get player and room for target recreation
                    config = get_config()
                    app = getattr(config, "_app_instance", None)
                    if app and hasattr(app.state, "container"):
                        player_service = getattr(app.state.container, "player_service", None)
                        if player_service:
                            player = await player_service.persistence.get_player_by_id(participant.participant_id)
                            if player:
                                room_id = player.current_room_id or combat.room_id
                                # Recreate target from action data
                                from server.schemas.target_resolution import (  # noqa: PLC0415  # Reason: Local import
                                    TargetMatch,
                                    TargetType,
                                )

                                target_type = TargetType.NPC if action.target_id else TargetType.PLAYER
                                target_name = action.spell_name or "target"
                                target = TargetMatch(
                                    target_id=str(action.target_id)
                                    if action.target_id
                                    else str(participant.participant_id),
                                    target_name=target_name,
                                    target_type=target_type,
                                    room_id=room_id,
                                )

                                # Get mastery from player spell
                                player_spell = await magic_service.player_spell_repository.get_player_spell(
                                    participant.participant_id, spell.spell_id
                                )
                                mastery = int(player_spell.mastery) if player_spell else 0

                                # Apply spell effects only (costs already paid when casting completed)
                                # Use spell_effects directly to avoid applying costs again
                                effect_result = await magic_service.spell_effects.process_effect(
                                    spell, target, participant.participant_id, mastery
                                )

                                # Record spell cast and increase mastery (if not already done)
                                await magic_service.player_spell_repository.record_spell_cast(
                                    participant.participant_id, spell.spell_id
                                )
                                if magic_service.spell_learning_service:
                                    await magic_service.spell_learning_service.increase_mastery_on_cast(
                                        participant.participant_id, spell.spell_id, True
                                    )

                                # Send completion messages and healing events
                                await magic_service.send_spell_execution_notifications(
                                    participant.participant_id, spell.spell_id, effect_result, room_id
                                )

                                logger.info(
                                    "Queued spell executed",
                                    participant_id=participant.participant_id,
                                    spell_id=action.spell_id,
                                    spell_name=action.spell_name,
                                    success=effect_result.get("success", False),
                                )
                            else:
                                logger.warning(
                                    "Player not found for spell execution", participant_id=participant.participant_id
                                )
                        else:
                            logger.warning("Player service not available for spell execution")
                    else:
                        logger.warning("App/container not available for spell execution")
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Spell execution errors unpredictable
                    logger.error(
                        "Error executing queued spell",
                        participant_id=participant.participant_id,
                        spell_id=action.spell_id,
                        error=str(e),
                        exc_info=True,
                    )
            else:
                logger.warning("Spell action queued but magic service not available", spell_name=action.spell_name)
        else:
            logger.warning("Unknown action type", action_type=action.action_type)

        participant.last_action_tick = current_tick

    async def _execute_default_action(
        self, combat: CombatInstance, participant: CombatParticipant, current_tick: int
    ) -> None:
        """
        Execute default action (basic attack) for a participant.

        Args:
            combat: Combat instance
            participant: Participant executing the action
            current_tick: Current game tick
        """
        # Find target (other participant in combat)
        target = None
        for p in combat.participants.values():
            if p.participant_id != participant.participant_id and p.is_alive():
                target = p
                break

        if not target:
            logger.warning("No target found for default action", participant_id=participant.participant_id)
            participant.last_action_tick = current_tick
            return

        # Execute based on participant type
        if participant.participant_type == CombatParticipantType.NPC:
            await self._process_npc_turn(combat, participant, current_tick)
        else:
            await self._process_player_turn(combat, participant, current_tick)

    async def _process_npc_turn(self, combat: CombatInstance, npc: CombatParticipant, current_tick: int) -> None:
        """
        Process NPC turn with actual combat attack.

        Args:
            combat: Combat instance
            npc: NPC participant
            current_tick: Current game tick
        """
        try:
            # Debug logging to understand what we're receiving
            logger.debug("_process_npc_turn called", npc_type=type(npc).__name__, npc=npc)
            if hasattr(npc, "participant_id"):
                logger.debug(
                    "NPC participant_id", participant_id=npc.participant_id, id_type=type(npc.participant_id).__name__
                )
            else:
                logger.error("NPC object missing participant_id attribute", npc=npc)
                return

            # BUGFIX: Check if NPC can act (DP > 0) before allowing actions
            # NPCs die at DP <= 0; use domain model method
            if not npc.can_act_in_combat():
                logger.info(
                    "NPC cannot act (dead or inactive)",
                    npc_name=npc.name,
                    current_dp=npc.current_dp,
                    combat_id=combat.combat_id,
                )
                npc.last_action_tick = current_tick
                return

            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != npc.participant_id:
                    target = participant
                    break
            if not target:
                logger.warning("No target found for NPC", npc_name=npc.name, combat_id=combat.combat_id)
                return

            # Perform automatic basic attack
            logger.debug("NPC performing automatic attack", npc_name=npc.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage
            # Process the attack
            combat_result = await self._combat_service.process_attack(
                attacker_id=npc.participant_id, target_id=target.participant_id, damage=damage
            )
            if combat_result.success:
                logger.info("NPC automatically attacked", npc_name=npc.name, target_name=target.name, damage=damage)
            else:
                logger.warning("NPC automatic attack failed", npc_name=npc.name, message=combat_result.message)

            # Update NPC's last action tick
            npc.last_action_tick = current_tick

        except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
            logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)

    async def _process_player_turn(self, combat: CombatInstance, player: CombatParticipant, current_tick: int) -> None:
        """
        Process player turn with automatic basic attack.

        Args:
            combat: Combat instance
            player: Player participant
            current_tick: Current game tick
        """
        try:
            # Debug logging to understand what we're receiving
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

            # BUGFIX #243: Check if player can act (DP > 0) before allowing actions
            # Unconscious entities (DP <= 0) cannot perform voluntary actions
            if not player.can_act_in_combat():
                logger.info(
                    "Player cannot act (unconscious or inactive)",
                    player_name=player.name,
                    current_dp=player.current_dp,
                    combat_id=combat.combat_id,
                )
                player.last_action_tick = current_tick
                return

            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != player.participant_id:
                    target = participant
                    break

            if not target:
                logger.warning("No target found for player", player_name=player.name, combat_id=combat.combat_id)
                return

            # Note: Players in grace period (disconnected but still in-game) can still auto-attack.
            # Commands are blocked for grace period players, but combat auto-attack continues normally.
            # Grace period players use normal auto-attack (with weapons, no special abilities).

            # Check if player is casting a spell - if so, skip autoattack
            # Casting spells takes priority over autoattacks
            try:
                # Access magic_service through combat_service
                magic_service = getattr(self._combat_service, "magic_service", None)
                if magic_service and magic_service.casting_state_manager.is_casting(player.participant_id):
                    casting_state = magic_service.casting_state_manager.get_casting_state(player.participant_id)
                    logger.debug(
                        "Player is casting, skipping autoattack",
                        player_name=player.name,
                        spell_name=casting_state.spell_name if casting_state else "unknown",
                    )
                    # Update player's last action tick but don't attack
                    player.last_action_tick = current_tick
                    return
            except (AttributeError, TypeError, KeyError) as e:
                # If we can't check casting state, allow autoattack to proceed
                logger.debug("Could not check casting state for autoattack", player_name=player.name, error=str(e))

            # Perform automatic basic attack
            logger.debug("Player performing automatic attack", player_name=player.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage

            # Process the attack
            combat_result = await self._combat_service.process_attack(
                attacker_id=player.participant_id, target_id=target.participant_id, damage=damage
            )

            if combat_result.success:
                logger.info(
                    "Player automatically attacked", player_name=player.name, target_name=target.name, damage=damage
                )
            else:
                logger.warning("Player automatic attack failed", player_name=player.name, message=combat_result.message)

            # Update player's last action tick
            player.last_action_tick = current_tick

        except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
            # Handle case where player might not be a CombatParticipant
            player_type = type(player)
            player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
            logger.error("Error processing player turn", player_name=player_name, error=str(e), exc_info=True)
