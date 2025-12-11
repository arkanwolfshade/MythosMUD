"""
NPC Combat Lucidity Effects.

This module handles lucidity (sanity) effects when players encounter NPCs,
applying appropriate lucidity loss based on NPC type and characteristics.
"""

from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..database import get_async_session
from ..logging.enhanced_logging_config import get_logger
from .active_lucidity_service import ActiveLucidityService, UnknownEncounterCategoryError

logger = get_logger(__name__)


class NPCCombatLucidity:
    """Manages lucidity effects for NPC encounters."""

    async def apply_encounter_lucidity_effect(
        self,
        player_id: str,
        npc_id: str,
        npc_definition: Any | None,
        room_id: str,
    ) -> None:
        """
        Apply lucidity loss when a player engages an eldritch entity.

        Args:
            player_id: ID of the player
            npc_id: ID of the NPC
            npc_definition: NPC definition object
            room_id: ID of the room where encounter occurs
        """
        definition_name: str | None = None
        if npc_definition is not None:
            potential_name = getattr(npc_definition, "name", None)
            if isinstance(potential_name, str) and potential_name.strip():
                definition_name = potential_name

        archetype = definition_name or npc_id
        category = self._resolve_lucidity_category(npc_definition)

        async for session in get_async_session():
            service = ActiveLucidityService(session)
            try:
                await service.apply_encounter_lucidity_loss(
                    player_id=str(player_id),
                    entity_archetype=str(archetype),
                    category=category,
                    location_id=room_id,
                )
                await session.commit()
            except UnknownEncounterCategoryError:
                await session.rollback()
                logger.warning(
                    "Encounter SAN category unavailable, defaulting to disturbing",
                    npc_id=npc_id,
                    provided_category=category,
                )
                try:
                    await service.apply_encounter_lucidity_loss(
                        player_id=str(player_id),
                        entity_archetype=str(archetype),
                        category="disturbing",
                        location_id=room_id,
                    )
                    await session.commit()
                except (
                    ValueError,
                    AttributeError,
                    ImportError,
                    SQLAlchemyError,
                    TypeError,
                ) as nested_exc:  # pragma: no cover - defensive logging
                    await session.rollback()
                    logger.error(
                        "Failed to apply fallback encounter lucidity loss",
                        npc_id=npc_id,
                        player_id=player_id,
                        error=str(nested_exc),
                    )
            except (
                ValueError,
                AttributeError,
                ImportError,
                SQLAlchemyError,
                TypeError,
            ) as exc:  # pragma: no cover - defensive logging
                await session.rollback()
                logger.error(
                    "Active encounter lucidity adjustment failed",
                    npc_id=npc_id,
                    player_id=player_id,
                    room_id=room_id,
                    error=str(exc),
                )
            else:
                logger.info(
                    "Applied encounter lucidity loss",
                    npc_id=npc_id,
                    player_id=player_id,
                    archetype=archetype,
                    category=category,
                )
            break

    def _resolve_lucidity_category(self, npc_definition: Any | None) -> str:
        """
        Determine encounter category based on NPC definition metadata.

        Args:
            npc_definition: NPC definition object

        Returns:
            Lucidity category string
        """
        if npc_definition is None:
            return "disturbing"

        try:
            base_stats = npc_definition.get_base_stats()
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError):
            base_stats = {}

        try:
            behavior_config = npc_definition.get_behavior_config()
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError):
            behavior_config = {}

        for source in (base_stats, behavior_config):
            if isinstance(source, dict):
                category = source.get("lucidity_category") or source.get("mythos_tier")
                if isinstance(category, str):
                    return category.lower()

        npc_type = getattr(npc_definition, "npc_type", "")
        if npc_type == "aggressive_mob":
            return "horrific"
        if npc_type == "passive_mob":
            return "disturbing"
        return "disturbing"
