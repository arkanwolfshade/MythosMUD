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
from server.services import combat_turn_participant_actions
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

    def _load_round_actions(self, combat: CombatInstance, next_round: int) -> None:
        """
        Load queued actions for the next round into combat.round_actions.

        Actions are queued with round = combat.combat_round + 1. When executing a round,
        combat.combat_round has not been incremented yet, so we match actions for next_round.
        """
        combat.round_actions.clear()
        for participant_id, queued_actions_list in combat.queued_actions.items():
            for action in queued_actions_list:
                if action.round == next_round:
                    combat.round_actions[participant_id] = action
                    break

    def _log_round_start_debug(
        self, combat: CombatInstance, participants_by_initiative: list[CombatParticipant]
    ) -> None:
        """Write debug log when any participant has zero or negative DP at round start (agent hypothesis H6)."""
        try:
            any_zero_or_neg = any(p.current_dp <= 0 for p in combat.participants.values())
            if not any_zero_or_neg:
                return
            import json

            parts = [
                {
                    "id": str(p.participant_id),
                    "type": str(p.participant_type),
                    "current_dp": p.current_dp,
                    "is_alive": p.is_alive(),
                }
                for p in combat.participants.values()
            ]
            by_init = [{"id": str(p.participant_id), "current_dp": p.current_dp} for p in participants_by_initiative]
            with open("e:\\projects\\GitHub\\MythosMUD\\.cursor\\debug.log", "a", encoding="utf-8") as _f:
                _f.write(
                    json.dumps(
                        {
                            "hypothesisId": "H6",
                            "location": "combat_turn_processor:_execute_round",
                            "message": "round start with participant at 0 or below",
                            "data": {
                                "participants": parts,
                                "by_initiative": by_init,
                                "count": len(participants_by_initiative),
                            },
                            "timestamp": __import__("time", fromlist=["time"]).time() * 1000,
                        },
                        ensure_ascii=True,
                    )
                    + "\n"
                )
        except (OSError, TypeError, AttributeError, ValueError):
            # Debug log must never affect combat; absorb file/serialization/attribute errors
            pass

    async def _execute_participant_action(
        self,
        combat: CombatInstance,
        participant: CombatParticipant,
        next_round: int,
        current_tick: int,
    ) -> None:
        """
        Execute one participant's action for the round (queued or default).
        Call only for participants that are alive.
        """
        if participant.participant_id not in combat.round_actions:
            await self._execute_default_action(combat, participant, current_tick)
            return
        action = combat.round_actions[participant.participant_id]
        if action.action_type == "attack":
            target_in_combat = combat.participants.get(action.target_id)
            # CRITICAL: Use is_dead() instead of is_alive() to allow attacking mortally wounded players (0 DP)
            # Players at 0 DP are not dead yet and should still be attackable until -10 DP
            if not target_in_combat or target_in_combat.is_dead():
                logger.warning(
                    "Stale queued attack target (not in combat or dead), using default action",
                    combat_id=combat.combat_id,
                    participant_id=participant.participant_id,
                    queued_target_id=action.target_id,
                    participant_ids=[str(pid) for pid in combat.participants.keys()],
                )
                combat.clear_queued_actions(participant.participant_id, round_number=next_round)
                await self._execute_default_action(combat, participant, current_tick)
                return
        await self._execute_queued_action(combat, participant, action, current_tick)
        combat.clear_queued_actions(participant.participant_id, round_number=next_round)

    async def _execute_round(self, combat: CombatInstance, current_tick: int) -> None:
        """
        Execute all actions for a round - all participants act sequentially in initiative order.

        Args:
            combat: Combat instance to process
            current_tick: Current game tick
        """
        combat.update_activity(current_tick)
        next_round = combat.combat_round + 1
        self._load_round_actions(combat, next_round)
        participants_by_initiative = combat.get_participants_by_initiative()
        self._log_round_start_debug(combat, participants_by_initiative)

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

        for participant in participants_by_initiative:
            # CRITICAL: Use is_dead() instead of is_alive() to ensure mortally wounded players
            # (0 DP) remain in combat and can be attacked until -10 DP
            # is_alive() requires is_active=True, which might be False for incapacitated players
            if participant.is_dead():
                continue
            await self._execute_participant_action(combat, participant, next_round, current_tick)

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
            logger.info(
                "Executing queued attack",
                combat_id=combat.combat_id,
                attacker_id=participant.participant_id,
                target_id=action.target_id,
                participant_ids=[str(pid) for pid in combat.participants.keys()],
            )
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
                                from server.schemas.shared import (  # noqa: PLC0415  # Reason: Local import
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

        # #region agent log
        try:
            import json

            _alive = [
                {"id": str(p.participant_id), "current_dp": p.current_dp, "is_alive": p.is_alive()}
                for p in combat.participants.values()
            ]
            with open("e:\\projects\\GitHub\\MythosMUD\\.cursor\\debug.log", "a", encoding="utf-8") as _f:
                _f.write(
                    json.dumps(
                        {
                            "hypothesisId": "H5",
                            "location": "combat_turn_processor:_execute_default_action",
                            "message": "default action target selection",
                            "data": {
                                "actor_id": str(participant.participant_id),
                                "target_id": str(target.participant_id) if target else None,
                                "target_current_dp": target.current_dp if target else None,
                                "target_is_alive": target.is_alive() if target else None,
                                "participants": _alive,
                            },
                            "timestamp": __import__("time", fromlist=["time"]).time() * 1000,
                        },
                        ensure_ascii=True,
                    )
                    + "\n"
                )
        except (OSError, TypeError, AttributeError, ValueError):
            # Debug log must never affect combat; absorb file/serialization/attribute errors
            pass
        # #endregion

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
        """Delegate to participant actions module."""
        await combat_turn_participant_actions.process_npc_turn(self._combat_service, combat, npc, current_tick)

    async def _process_player_turn(self, combat: CombatInstance, player: CombatParticipant, current_tick: int) -> None:
        """Delegate to participant actions module."""
        await combat_turn_participant_actions.process_player_turn(self._combat_service, combat, player, current_tick)
