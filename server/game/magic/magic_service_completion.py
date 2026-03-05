"""
Casting completion flow for spellcasting.

Mixin that handles completing a casting: get player/room, recreate target,
apply costs/effects, queue for combat or execute immediately. Used by MagicService.
"""

import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from server.schemas.shared import TargetMatch, TargetType
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.magic.casting_state_manager import CastingStateManager
    from server.game.magic.spell_costs import SpellCostsService
    from server.game.magic.spell_effects import SpellEffects
    from server.game.magic.spell_learning_service import SpellLearningService
    from server.game.player_service import PlayerService
    from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
    from server.services.combat_service import CombatService


logger = get_logger(__name__)


class MagicServiceCompletionMixin:
    """Mixin for MagicService: complete casting (player/room, target, costs/effects, combat or immediate)."""

    # These attributes are provided by the concrete MagicService implementation.
    player_service: "PlayerService"
    casting_state_manager: "CastingStateManager"
    spell_costs_service: "SpellCostsService"
    spell_effects: "SpellEffects"
    player_spell_repository: "PlayerSpellRepository"
    spell_learning_service: "SpellLearningService | None"
    combat_service: "CombatService | None"

    if TYPE_CHECKING:

        async def _send_spell_completion_message(  # pragma: no cover - typing stub only  # pylint: disable=unused-argument
            self,
            player_id: uuid.UUID,
            spell_id: str,
            effect_result: dict[str, Any],
        ) -> None: ...

        def _is_heal_other_target(  # pragma: no cover - typing stub only  # pylint: disable=unused-argument
            self,
            effect_result: dict[str, Any],
            spell: Any,
            target: Any,
            player_id: uuid.UUID,
        ) -> bool: ...

        async def _send_healing_update_event(  # pragma: no cover - typing stub only  # pylint: disable=unused-argument
            self,
            player_id: uuid.UUID,
            effect_result: dict[str, Any],
            spell_id: str,
            room_id: str,
            healed_player_id: uuid.UUID | None = None,
        ) -> None: ...

    async def _get_player_and_room(self, player_id: uuid.UUID) -> tuple[Any, str] | None:
        """
        Get player and room_id for casting completion.

        Returns:
            Tuple of (player, room_id) if successful, None otherwise
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            logger.error("Player not found when completing casting", player_id=player_id)
            self.casting_state_manager.complete_casting(player_id)
            return None

        room_id = player.current_room_id or ""
        return player, room_id

    def _recreate_target_from_state(
        self, casting_state: Any, player_id: uuid.UUID, player: Any, room_id: str
    ) -> TargetMatch:
        """
        Recreate target from stored casting state.

        Args:
            casting_state: The casting state
            player_id: Player ID
            player: Player object
            room_id: Room ID

        Returns:
            TargetMatch object
        """
        target_type_str = casting_state.target_type or "player"
        try:
            target_type = TargetType(target_type_str)
        except ValueError:
            target_type = TargetType.PLAYER

        return TargetMatch(
            target_id=casting_state.target_id or str(player_id),
            target_name=casting_state.target_name or player.name,
            target_type=target_type,
            room_id=room_id,
        )

    async def _apply_spell_costs_and_effects(
        self, player_id: uuid.UUID, spell: Any, target: Any, casting_state: Any
    ) -> dict[str, Any]:
        """
        Apply spell costs and process effects.

        Args:
            player_id: Player ID
            spell: Spell object
            target: TargetMatch object
            casting_state: Casting state

        Returns:
            Effect result dictionary
        """
        await self.spell_costs_service.apply_costs(player_id, spell)
        effect_result = await self.spell_effects.process_effect(spell, target, player_id, casting_state.mastery)
        await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

        if self.spell_learning_service:
            await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, True)

        return effect_result

    def _parse_casting_target_id(self, casting_state: Any) -> uuid.UUID | None:
        """Parse target_id from casting state. Returns None if missing or invalid."""
        if not casting_state.target_id:
            return None
        try:
            raw = casting_state.target_id
            return uuid.UUID(raw) if isinstance(raw, str) else raw
        except (ValueError, TypeError):
            logger.warning("Invalid target_id in casting state", target_id=casting_state.target_id)
            return None

    async def _try_queue_spell_for_combat(
        self, player_id: uuid.UUID, spell: Any, casting_state: Any, combat: Any
    ) -> bool:
        """Apply costs and queue spell for next combat round. Returns True if queued, False to run immediately."""
        if self.combat_service is None:
            raise RuntimeError("combat_service must be set when invoking _try_queue_spell_for_combat")
        await self.spell_costs_service.apply_costs(player_id, spell)
        target_id = self._parse_casting_target_id(casting_state)
        queued = await self.combat_service.queue_combat_action(
            combat_id=combat.combat_id,
            participant_id=player_id,
            action_type="spell",
            target_id=target_id,
            spell_id=spell.spell_id,
            spell_name=spell.name,
        )
        if queued:
            logger.info(
                "Spell queued for combat round (costs paid, effects queued)",
                player_id=player_id,
                spell_id=spell.spell_id,
                spell_name=spell.name,
                combat_id=combat.combat_id,
                round=combat.combat_round + 1,
            )
            return True
        logger.warning(
            "Failed to queue spell, executing immediately",
            player_id=player_id,
            spell_id=spell.spell_id,
        )
        return False

    async def _execute_casting_immediately(
        self,
        player_id: uuid.UUID,
        spell: Any,
        target: Any,
        casting_state: Any,
        room_id: str,
    ) -> None:
        """Apply spell costs/effects, send completion message and healing event."""
        effect_result = await self._apply_spell_costs_and_effects(player_id, spell, target, casting_state)
        logger.info(
            "Completed casting",
            player_id=player_id,
            spell_id=spell.spell_id,
            effect_success=effect_result.get("success", False),
        )
        await self._send_spell_completion_message(player_id, spell.spell_id, effect_result)
        healed_player_id = None
        if self._is_heal_other_target(effect_result, spell, target, player_id):
            healed_player_id = uuid.UUID(target.target_id) if isinstance(target.target_id, str) else target.target_id
        await self._send_healing_update_event(
            player_id,
            effect_result,
            spell.spell_id,
            room_id,
            healed_player_id=healed_player_id,
        )

    async def _try_complete_casting_via_combat(self, player_id: uuid.UUID, spell: Any, casting_state: Any) -> bool:
        """If in combat, try to queue spell for next round. Return True if queued, False otherwise."""
        if not self.combat_service:
            return False
        combat = await self.combat_service.get_combat_by_participant(player_id)
        if not combat:
            return False
        return await self._try_queue_spell_for_combat(player_id, spell, casting_state, combat)

    async def _complete_casting(self, player_id: uuid.UUID, casting_state: Any) -> None:
        """
        Complete a casting and apply spell effects.

        In combat, spells are queued for execution in the next round.
        Outside combat, spells execute immediately.

        Args:
            player_id: Player ID
            casting_state: The casting state to complete
        """
        spell = casting_state.spell
        try:
            player_result = await self._get_player_and_room(player_id)
            if player_result is None:
                return
            player, room_id = player_result
            target = self._recreate_target_from_state(casting_state, player_id, player, room_id)
            self.casting_state_manager.complete_casting(player_id)

            if await self._try_complete_casting_via_combat(player_id, spell, casting_state):
                return

            await self._execute_casting_immediately(player_id, spell, target, casting_state, room_id)
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError) as e:
            logger.error(
                "Error completing casting - clearing stuck state",
                player_id=player_id,
                spell_id=spell.spell_id if spell else None,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
        finally:
            if self.casting_state_manager.is_casting(player_id):
                self.casting_state_manager.complete_casting(player_id)
