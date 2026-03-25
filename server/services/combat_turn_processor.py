"""
Combat turn processing logic.

Handles round-based combat where all participants act each round in initiative order.
Processes queued actions and generates default actions for automatic combat progression.
"""

# pylint: disable=too-few-public-methods  # Reason: Turn processor class with focused responsibility, minimal public interface

import uuid
from typing import TYPE_CHECKING, Any, cast

from structlog.stdlib import BoundLogger

from server.config import get_config
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services import combat_turn_participant_actions
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class CombatTurnProcessor:
    """Handles combat turn processing and auto-progression."""

    _combat_service: "CombatService"

    def __init__(self, combat_service: "CombatService") -> None:
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

    def _is_npc_still_in_world(self, participant: CombatParticipant) -> bool:
        """
        Return True if an NPC participant is still in the lifecycle active_npcs (not slain and removed).
        Used to skip turns for NPCs killed outside the combat model (e.g. Steal Life) whose
        CombatParticipant.current_dp was never updated.
        """
        if participant.participant_type != CombatParticipantType.NPC:
            return True
        try:
            npc_id_str = self._resolve_npc_participant_to_string_id(participant)
            # Only string ids are valid for active_npcs lookup; otherwise skip the check.
            if not npc_id_str or not isinstance(npc_id_str, str):
                return True
            return self._npc_id_in_active_npcs(npc_id_str)
        except Exception:  # pylint: disable=broad-exception-caught  # Best-effort; do not break tick
            return True

    def _resolve_npc_participant_to_string_id(self, participant: CombatParticipant) -> str | None:
        """Resolve NPC participant UUID to string npc_id via combat integration service."""
        npc_svc = getattr(self._combat_service, "_npc_combat_integration_service", None)
        if not npc_svc or not hasattr(npc_svc, "get_original_string_id"):
            return None
        return cast(str | None, npc_svc.get_original_string_id(participant.participant_id))

    def _npc_id_in_active_npcs(self, npc_id_str: str) -> bool:
        """Return True if npc_id_str is in the lifecycle manager's active_npcs."""
        from server.services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            return True
        lm = npc_instance_service.lifecycle_manager
        if not lm or not hasattr(lm, "active_npcs"):
            return True
        return npc_id_str in lm.active_npcs

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
            # NPCs slain outside combat model (e.g. Steal Life) are removed from active_npcs
            # but CombatParticipant.current_dp is never updated; skip their turn so they stop attacking.
            if participant.participant_type == CombatParticipantType.NPC and not self._is_npc_still_in_world(
                participant
            ):
                logger.debug(
                    "Skipping slain NPC participant (no longer in active_npcs)",
                    combat_id=combat.combat_id,
                    participant_id=participant.participant_id,
                )
                continue
            await self._execute_participant_action(combat, participant, next_round, current_tick)

        combat.advance_turn(current_tick)

    async def _execute_queued_action(
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

        if action.action_type == "attack":
            await self._execute_attack_action(combat, participant, action)
        elif action.action_type == "spell":
            await self._execute_spell_action(combat, participant, action, current_tick)
        elif action.action_type == "flee_skip":
            self._handle_flee_skip_action(combat, participant)
        else:
            self._log_unknown_action(action)

        participant.last_action_tick = current_tick

    async def _execute_attack_action(
        self, combat: CombatInstance, participant: CombatParticipant, action: CombatAction
    ) -> None:
        """Execute a queued attack action."""
        logger.info(
            "Executing queued attack",
            combat_id=combat.combat_id,
            attacker_id=participant.participant_id,
            target_id=action.target_id,
            participant_ids=[str(pid) for pid in combat.participants.keys()],
        )
        await self._combat_service.process_attack(
            attacker_id=participant.participant_id,
            target_id=action.target_id,
            damage=action.damage,
        )

    async def _execute_spell_action(
        self, combat: CombatInstance, participant: CombatParticipant, action: CombatAction, current_tick: int
    ) -> None:
        """Execute a queued spell action via the magic service."""
        magic_service = getattr(self._combat_service, "magic_service", None)
        if not magic_service:
            logger.warning("Spell action queued but magic service not available", spell_name=action.spell_name)
            return

        spell = self._get_spell_for_action(magic_service, action, participant, current_tick)
        if not spell:
            return

        try:
            player, room_id = await self._get_player_and_room_for_spell(combat, participant)
            if not player or not room_id:
                return

            target = self._build_spell_target(action, participant, room_id)
            effect_result = await self._apply_spell_effects(magic_service, spell, participant, target)
            await self._finalize_spell_execution(magic_service, participant, spell, effect_result, room_id, action)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Spell execution errors unpredictable
            logger.error(
                "Error executing queued spell",
                participant_id=participant.participant_id,
                spell_id=action.spell_id,
                error=str(e),
                exc_info=True,
            )

    def _get_spell_for_action(
        self, magic_service: Any, action: CombatAction, participant: CombatParticipant, current_tick: int
    ) -> Any | None:
        """Resolve the spell object for a queued spell action."""
        spell = magic_service.spell_registry.get_spell(action.spell_id) if action.spell_id else None
        if not spell:
            logger.warning("Spell not found for execution", spell_id=action.spell_id, spell_name=action.spell_name)
            participant.last_action_tick = current_tick
            return None
        return spell

    async def _apply_spell_effects(
        self,
        magic_service: Any,
        spell: Any,
        participant: CombatParticipant,
        target: Any,
    ) -> dict[str, Any]:
        """Apply spell effects and update mastery."""
        player_spell = await magic_service.player_spell_repository.get_player_spell(
            participant.participant_id, spell.spell_id
        )
        mastery = int(player_spell.mastery) if player_spell else 0

        effect_result: dict[str, Any] = await magic_service.spell_effects.process_effect(
            spell, target, participant.participant_id, mastery
        )

        await magic_service.player_spell_repository.record_spell_cast(participant.participant_id, spell.spell_id)
        if magic_service.spell_learning_service:
            await magic_service.spell_learning_service.increase_mastery_on_cast(
                participant.participant_id, spell.spell_id, True
            )

        return effect_result

    async def _finalize_spell_execution(
        self,
        magic_service: Any,
        participant: CombatParticipant,
        spell: Any,
        effect_result: dict[str, Any],
        room_id: str,
        action: CombatAction,
    ) -> None:
        """Send notifications and log completion for a queued spell."""
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

    async def _get_player_and_room_for_spell(
        self, combat: CombatInstance, participant: CombatParticipant
    ) -> tuple[Any | None, str | None]:
        """Resolve the casting player and room_id for spell execution."""
        config = get_config()
        app = getattr(config, "_app_instance", None)
        if not app or not hasattr(app.state, "container"):
            logger.warning("App/container not available for spell execution")
            return None, None

        player_service = getattr(app.state.container, "player_service", None)
        if not player_service:
            logger.warning("Player service not available for spell execution")
            return None, None

        player = await player_service.persistence.get_player_by_id(participant.participant_id)
        if not player:
            logger.warning("Player not found for spell execution", participant_id=participant.participant_id)
            return None, None

        room_id = player.current_room_id or combat.room_id
        return player, room_id

    def _build_spell_target(self, action: CombatAction, participant: CombatParticipant, room_id: str) -> Any:
        """Recreate the spell target from queued action data."""
        from server.schemas.shared import (  # noqa: PLC0415  # Reason: Local import
            TargetMatch,
            TargetType,
        )

        target_type = TargetType.NPC if action.target_id else TargetType.PLAYER
        target_name = action.spell_name or "target"
        return TargetMatch(
            target_id=str(action.target_id) if action.target_id else str(participant.participant_id),
            target_name=target_name,
            target_type=target_type,
            room_id=room_id,
        )

    def _handle_flee_skip_action(self, combat: CombatInstance, participant: CombatParticipant) -> None:
        """Handle a queued flee_skip action by logging and skipping execution."""
        logger.info(
            "Skipping queued action due to previous flee attempt",
            combat_id=combat.combat_id,
            participant_id=participant.participant_id,
        )

    def _log_unknown_action(self, action: CombatAction) -> None:
        """Log unknown action types for diagnostics."""
        logger.warning("Unknown action type", action_type=action.action_type)

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
        """Delegate to participant actions module."""
        await combat_turn_participant_actions.process_npc_turn(self._combat_service, combat, npc, current_tick)

    async def _process_player_turn(self, combat: CombatInstance, player: CombatParticipant, current_tick: int) -> None:
        """Delegate to participant actions module."""
        await combat_turn_participant_actions.process_player_turn(self._combat_service, combat, player, current_tick)
