"""
Spell learning service for handling spell acquisition.

This module provides services for learning spells from various sources:
spellbooks, NPC teachers, and quest rewards.
"""

import uuid
from typing import Any

from server.game.magic.spell_registry import SpellRegistry
from server.game.player_service import PlayerService
from server.models.spell import Spell
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SpellLearningService:
    """
    Service for handling spell learning from various sources.

    Manages spell acquisition, prerequisite validation, and corruption
    application for Mythos spells.
    """

    def __init__(
        self,
        spell_registry: SpellRegistry,
        player_service: PlayerService,
        player_spell_repository: PlayerSpellRepository | None = None,
    ) -> None:
        """
        Initialize the spell learning service.

        Args:
            spell_registry: Registry for spell lookups
            player_service: Player service for stat modifications
            player_spell_repository: Optional repository for spell learning
        """
        self.spell_registry = spell_registry
        self.player_service = player_service
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        logger.info("SpellLearningService initialized")

    def _resolve_spell(self, spell_id: str) -> Spell | None:
        spell = self.spell_registry.get_spell(spell_id)
        if spell:
            return spell
        return self.spell_registry.get_spell_by_name(spell_id)

    async def _apply_mythos_corruption_on_learn(self, player: Any, spell: Spell) -> int:
        if not spell.is_mythos() or spell.corruption_on_learn <= 0:
            return 0
        stats = player.get_stats()
        current_corruption = stats.get("corruption", 0)
        stats["corruption"] = current_corruption + spell.corruption_on_learn
        await self.player_service.persistence.save_player(player)
        logger.info(
            "Applied corruption on spell learning",
            player_id=player.player_id,
            spell_id=spell.spell_id,
            corruption=spell.corruption_on_learn,
        )
        return spell.corruption_on_learn

    async def _persist_spell_learning(
        self, player_id: uuid.UUID, spell: Spell, initial_mastery: int
    ) -> dict[str, Any] | None:
        try:
            await self.player_spell_repository.learn_spell(player_id, spell.spell_id, initial_mastery)
        except OSError as e:
            logger.error("Error learning spell", player_id=player_id, spell_id=spell.spell_id, error=str(e))
            return {"success": False, "message": f"Failed to learn spell: {str(e)}"}
        return None

    def _spell_learn_success_response(self, spell: Spell, corruption_applied: int, source: str) -> dict[str, Any]:
        return {
            "success": True,
            "message": f"You have learned {spell.name}!",
            "spell_name": spell.name,
            "spell_id": spell.spell_id,
            "corruption_applied": corruption_applied,
            "source": source,
        }

    async def _load_spell_learn_context(
        self, player_id: uuid.UUID, spell_id: str
    ) -> tuple[Spell, Any] | dict[str, Any]:
        spell = self._resolve_spell(spell_id)
        if not spell:
            return {"success": False, "message": f"Spell '{spell_id}' not found."}

        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "You are not recognized by the cosmic forces."}

        existing = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        if existing:
            return {
                "success": False,
                "message": f"You already know {spell.name}.",
                "already_known": True,
            }

        return spell, player

    async def learn_spell(
        self,
        player_id: uuid.UUID,
        spell_id: str,
        source: str = "unknown",
        initial_mastery: int = 0,
    ) -> dict[str, Any]:
        """Learn a spell for a player."""
        logger.info("Learning spell", player_id=player_id, spell_id=spell_id, source=source)

        context = await self._load_spell_learn_context(player_id, spell_id)
        if isinstance(context, dict):
            return context
        spell, player = context

        validation_result = await self._validate_prerequisites(player_id, spell)
        if not validation_result["valid"]:
            return {
                "success": False,
                "message": validation_result["error_message"],
                "prerequisite_failed": True,
            }

        learn_error = await self._persist_spell_learning(player_id, spell, initial_mastery)
        if learn_error:
            return learn_error

        corruption_applied = await self._apply_mythos_corruption_on_learn(player, spell)
        return self._spell_learn_success_response(spell, corruption_applied, source)

    def _check_power_requirement(self, stats: dict[str, Any], spell: Spell) -> dict[str, Any] | None:
        required_power = spell.effect_data.get("required_power", 0)
        if required_power <= 0:
            return None
        current_power = stats.get("power", 50)
        if current_power >= required_power:
            return None
        return {
            "valid": False,
            "error_message": (f"{spell.name} requires Power {required_power}, but you only have {current_power}."),
        }

    def _check_intelligence_requirement(self, stats: dict[str, Any], spell: Spell) -> dict[str, Any] | None:
        required_intelligence = spell.effect_data.get("required_intelligence", 0)
        if required_intelligence <= 0:
            return None
        current_intelligence = stats.get("intelligence", 50)
        if current_intelligence >= required_intelligence:
            return None
        return {
            "valid": False,
            "error_message": (
                f"{spell.name} requires Intelligence {required_intelligence}, but you only have {current_intelligence}."
            ),
        }

    async def _check_required_spell_prerequisites(self, player_id: uuid.UUID, spell: Spell) -> dict[str, Any] | None:
        required_spells = spell.effect_data.get("required_spells", [])
        if not required_spells:
            return None

        player_spells = await self.player_spell_repository.get_player_spells(player_id)
        known_spell_ids = {player_spell.spell_id for player_spell in player_spells}
        missing_spells = [spell_id for spell_id in required_spells if spell_id not in known_spell_ids]
        if not missing_spells:
            return None

        missing_names = []
        for missing_spell_id in missing_spells:
            required_spell = self.spell_registry.get_spell(missing_spell_id)
            missing_names.append(required_spell.name if required_spell else missing_spell_id)

        return {
            "valid": False,
            "error_message": (
                f"{spell.name} requires knowledge of: {', '.join(missing_names)}. You must learn these spells first."
            ),
        }

    async def _validate_prerequisites(self, player_id: uuid.UUID, spell: Spell) -> dict[str, Any]:
        """
        Validate prerequisites for learning a spell.

        Args:
            player_id: Player ID
            spell: Spell to validate

        Returns:
            dict: Validation result with 'valid' bool and optional 'error_message'
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"valid": False, "error_message": "Player not found"}

        stats = player.get_stats()
        for check in (
            self._check_power_requirement(stats, spell),
            self._check_intelligence_requirement(stats, spell),
        ):
            if check:
                return check

        spell_check = await self._check_required_spell_prerequisites(player_id, spell)
        if spell_check:
            return spell_check

        return {"valid": True}

    async def learn_spell_from_book(
        self, player_id: uuid.UUID, spellbook_item_id: str, spell_id: str | None = None
    ) -> dict[str, Any]:
        """
        Learn a spell from a spellbook item.

        Args:
            player_id: Player ID
            spellbook_item_id: ID of the spellbook item
            spell_id: Optional specific spell ID (if book contains multiple spells)

        Returns:
            dict: Result with success, message, and details
        """
        # TODO: Integrate with item system to get spellbook data  # pylint: disable=fixme  # Reason: Feature placeholder for item system integration
        # For now, this is a placeholder that can be called when item interaction is implemented
        logger.debug("Learning spell from book", player_id=player_id, item_id=spellbook_item_id, spell_id=spell_id)

        if not spell_id:
            # If no spell_id specified, get first spell from book
            # This would come from item metadata in the future
            return {"success": False, "message": "No spell specified. Use: /read <spellbook> <spell_name>"}

        return await self.learn_spell(player_id, spell_id, source="spellbook")

    async def learn_spell_from_npc(self, player_id: uuid.UUID, npc_id: str, spell_id: str) -> dict[str, Any]:
        """
        Learn a spell from an NPC teacher.

        Args:
            player_id: Player ID
            npc_id: ID of the NPC teacher
            spell_id: Spell ID to learn

        Returns:
            dict: Result with success, message, and details
        """
        # TODO: Integrate with NPC system to validate teacher status  # pylint: disable=fixme  # Reason: Feature placeholder for NPC system integration
        # For now, this is a placeholder that can be called when NPC interaction is implemented
        logger.debug("Learning spell from NPC", player_id=player_id, npc_id=npc_id, spell_id=spell_id)

        return await self.learn_spell(player_id, spell_id, source=f"npc_teacher:{npc_id}")

    async def learn_spell_from_quest(self, player_id: uuid.UUID, quest_id: str, spell_id: str) -> dict[str, Any]:
        """
        Learn a spell as a quest reward.

        Args:
            player_id: Player ID
            quest_id: ID of the quest
            spell_id: Spell ID to learn

        Returns:
            dict: Result with success, message, and details
        """
        # TODO: Integrate with quest system to validate quest completion  # pylint: disable=fixme  # Reason: Feature placeholder for quest system integration
        # For now, this is a placeholder that can be called when quest system is implemented
        logger.debug("Learning spell from quest", player_id=player_id, quest_id=quest_id, spell_id=spell_id)

        return await self.learn_spell(player_id, spell_id, source=f"quest_reward:{quest_id}")

    async def increase_mastery_on_cast(self, player_id: uuid.UUID, spell_id: str, cast_success: bool) -> None:
        """
        Increase mastery level after casting a spell.

        Args:
            player_id: Player ID
            spell_id: Spell ID that was cast
            cast_success: Whether the cast was successful
        """
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell_id)
        if not player_spell:
            return

        # Only increase mastery on successful casts
        if not cast_success:
            return

        # Small mastery increase (1-2 points per successful cast)
        # Mastery increases faster at lower levels, slower at higher levels
        current_mastery: int = int(player_spell.mastery)
        if current_mastery >= 100:
            return  # Already at max mastery

        # Calculate mastery gain (more at lower levels)
        if current_mastery < 50:
            mastery_gain = 2
        elif current_mastery < 80:
            mastery_gain = 1
        else:
            # Very slow progress at high mastery
            import random

            mastery_gain = 1 if random.random() < 0.5 else 0  # nosec B311: Game mechanics probability, not cryptographic

        # Calculate new mastery and ensure it's an int
        new_mastery = int(min(100, current_mastery + mastery_gain))
        await self.player_spell_repository.update_mastery(player_id, spell_id, new_mastery)

        logger.debug(
            "Increased spell mastery",
            player_id=player_id,
            spell_id=spell_id,
            old_mastery=current_mastery,
            new_mastery=new_mastery,
            gain=mastery_gain,
        )
