"""
Spell targeting service for resolving spell targets.

This module handles target resolution for spells, including auto-selection
of combat targets and validation of target types.
"""

import uuid
from typing import Any

from server.models.spell import Spell, SpellTargetType
from server.schemas.target_resolution import TargetMatch, TargetType
from server.services.combat_service import CombatService
from server.services.player_combat_service import PlayerCombatService
from server.services.target_resolution_service import TargetResolutionService
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SpellTargetingService:  # pylint: disable=too-few-public-methods  # Reason: Utility class with focused responsibility, minimal public interface
    """
    Service for resolving spell targets.

    Handles target resolution based on spell requirements, including
    auto-selection of combat targets and validation.
    """

    def __init__(
        self,
        target_resolution_service: TargetResolutionService,
        combat_service: CombatService | None = None,
        player_combat_service: PlayerCombatService | None = None,
    ):
        """
        Initialize the spell targeting service.

        Args:
            target_resolution_service: Service for resolving target names
            combat_service: Optional combat service for combat target resolution
            player_combat_service: Optional player combat service for combat state checks
        """
        self.target_resolution_service = target_resolution_service
        self.combat_service = combat_service
        self.player_combat_service = player_combat_service
        logger.info("SpellTargetingService initialized")

    async def _resolve_self_target(self, player_id: uuid.UUID) -> tuple[TargetMatch | None, str]:
        """Resolve self-target spell. Returns (target_match, error_message)."""
        player = await self._get_player(player_id)
        if not player:
            return None, "You are not recognized by the cosmic forces."

        return (
            TargetMatch(
                target_id=str(player_id),
                target_name=player.name,
                target_type=TargetType.PLAYER,
                room_id=player.current_room_id,
            ),
            "",
        )

    async def _resolve_area_target(self, player_id: uuid.UUID) -> tuple[TargetMatch | None, str]:
        """Resolve area/all target spell. Returns (target_match, error_message)."""
        player = await self._get_player(player_id)
        if not player:
            return None, "You are not recognized by the cosmic forces."

        return (
            TargetMatch(
                target_id="area",
                target_name="area",
                target_type=TargetType.ROOM,
                room_id=player.current_room_id,
            ),
            "",
        )

    async def _resolve_entity_target(
        self, player_id: uuid.UUID, spell: Spell, target_name: str
    ) -> tuple[TargetMatch | None, str]:
        """Resolve entity/location target spell with explicit target. Returns (target_match, error_message)."""
        target_result = await self.target_resolution_service.resolve_target(player_id, target_name)
        if not target_result.success:
            return None, target_result.error_message or "Target not found."

        target_match = target_result.get_single_match()
        if not target_match:
            return None, target_result.error_message or "No valid target found."

        if spell.target_type == SpellTargetType.ENTITY:
            if target_match.target_type not in (TargetType.PLAYER, TargetType.NPC):
                return None, f"{spell.name} can only target entities, not locations."

        return target_match, ""

    async def resolve_spell_target(
        self, player_id: uuid.UUID, spell: Spell, target_name: str | None = None
    ) -> tuple[TargetMatch | None, str]:
        """
        Resolve the target for a spell cast.

        Args:
            player_id: ID of the player casting the spell
            spell: The spell being cast
            target_name: Optional explicit target name

        Returns:
            tuple[TargetMatch | None, str]: Target match (or None) and error message (if any)
        """
        logger.debug("Resolving spell target", player_id=player_id, spell_id=spell.spell_id, target_name=target_name)

        if spell.target_type == SpellTargetType.SELF:
            if target_name and target_name.strip():
                return None, f"{spell.name} can only be cast on yourself."
            return await self._resolve_self_target(player_id)

        if spell.target_type in (SpellTargetType.AREA, SpellTargetType.ALL):
            return await self._resolve_area_target(player_id)

        if spell.target_type in (SpellTargetType.ENTITY, SpellTargetType.LOCATION):
            if not target_name:
                auto_target = await self._get_combat_target(player_id)
                if auto_target:
                    logger.debug("Using combat auto-target", player_id=player_id, target_id=auto_target.target_id)
                    return auto_target, ""

                return None, f"{spell.name} requires a target."

            return await self._resolve_entity_target(player_id, spell, target_name)

        return None, f"Unknown target type: {spell.target_type}"

    async def _get_player(self, player_id: uuid.UUID) -> Any:
        """Get player object from persistence."""
        # Use target resolution service's persistence
        if hasattr(self.target_resolution_service.persistence, "get_player_by_id"):
            import inspect

            method = self.target_resolution_service.persistence.get_player_by_id
            if inspect.iscoroutinefunction(method):
                return await method(player_id)
            return method(player_id)
        return None

    async def _get_combat_target(self, player_id: uuid.UUID) -> TargetMatch | None:
        """
        Get the combat target for a player if they are in combat.

        Args:
            player_id: Player ID

        Returns:
            TargetMatch | None: Combat target or None if not in combat
        """
        if not self.combat_service or not self.player_combat_service:
            return None

        try:
            # Check if player is in combat
            combat_state = await self.player_combat_service.get_player_combat_state(player_id)
            if not combat_state or not combat_state.is_in_combat:
                return None

            # Get combat instance
            combat = await self.combat_service.get_combat_by_participant(player_id)
            if not combat:
                return None

            # Find the other participant
            for participant in combat.participants.values():
                if participant.participant_id != player_id:
                    # Get participant details
                    if participant.participant_type.value == "npc":
                        # Get NPC name from room
                        player = await self._get_player(player_id)
                        if player:
                            # For now, return a basic match - could be enhanced
                            return TargetMatch(
                                target_id=str(participant.participant_id),
                                target_name="combat target",
                                target_type=TargetType.NPC,
                                room_id=player.current_room_id,
                            )
                    elif participant.participant_type.value == "player":
                        target_player = await self._get_player(participant.participant_id)
                        if target_player:
                            return TargetMatch(
                                target_id=str(participant.participant_id),
                                target_name=target_player.name,
                                target_type=TargetType.PLAYER,
                                room_id=target_player.current_room_id,
                            )

        except OSError as e:
            logger.warning("Error getting combat target", player_id=player_id, error=str(e))

        return None
