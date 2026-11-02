"""
NPC Combat Lucidity Effects.

This module handles lucidity (sanity) effects when players encounter NPCs,
applying appropriate lucidity loss based on NPC type and characteristics.
"""

# pylint: disable=too-few-public-methods  # Reason: Lucidity effects class with focused responsibility, minimal public interface

from typing import TYPE_CHECKING, Any, NamedTuple

from sqlalchemy.exc import SQLAlchemyError

from ..structured_logging.enhanced_logging_config import get_logger
from .active_lucidity_service import ActiveLucidityService, UnknownEncounterCategoryError
from .lucidity_helpers import PlayerGoneError

if TYPE_CHECKING:
    from ..game.player_registry import PlayerRegistry

logger = get_logger(__name__)

_SOFT_ERRORS = (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError, PlayerGoneError)


class _EncounterCtx(NamedTuple):
    """Context for applying encounter lucidity loss."""

    player_id: str
    npc_id: str
    archetype: str
    category: str
    room_id: str


class NPCCombatLucidity:  # pylint: disable=too-few-public-methods  # Reason: Lucidity effects class with focused responsibility, minimal public interface
    """Manages lucidity effects for NPC encounters."""

    def __init__(self, player_registry: PlayerRegistry | None = None) -> None:
        self._player_registry: PlayerRegistry | None = player_registry

    @staticmethod
    def _archetype_from_definition(npc_definition: Any | None, npc_id: str) -> str:
        """Resolve encounter archetype name from NPC definition or id."""
        if npc_definition is not None:
            potential_name = getattr(npc_definition, "name", None)
            if isinstance(potential_name, str) and potential_name.strip():
                return potential_name
        return npc_id

    @staticmethod
    async def _apply_loss(service: ActiveLucidityService, ctx: _EncounterCtx, category: str) -> None:
        """Apply one encounter lucidity loss for the given category (one registry unit, committed by it)."""
        _ = await service.apply_encounter_lucidity_loss(
            player_id=str(ctx.player_id),
            entity_archetype=str(ctx.archetype),
            category=category,
            location_id=ctx.room_id,
        )

    async def _apply_disturbing_fallback(self, service: ActiveLucidityService, ctx: _EncounterCtx) -> None:
        """Retry encounter loss with the disturbing category after unknown-category failure."""
        logger.warning(
            "Encounter SAN category unavailable, defaulting to disturbing",
            npc_id=ctx.npc_id,
            provided_category=ctx.category,
        )
        try:
            await self._apply_loss(service, ctx, "disturbing")
        except _SOFT_ERRORS as nested_exc:  # pragma: no cover - defensive logging
            logger.error(
                "Failed to apply fallback encounter lucidity loss",
                npc_id=ctx.npc_id,
                player_id=ctx.player_id,
                error=str(nested_exc),
            )

    async def _apply_loss_with_fallback(self, service: ActiveLucidityService, ctx: _EncounterCtx) -> None:
        """Apply encounter lucidity loss, falling back to disturbing on unknown category."""
        try:
            await self._apply_loss(service, ctx, ctx.category)
        except UnknownEncounterCategoryError:
            await self._apply_disturbing_fallback(service, ctx)
            return
        except _SOFT_ERRORS as exc:  # pragma: no cover - defensive logging
            logger.error(
                "Active encounter lucidity adjustment failed",
                npc_id=ctx.npc_id,
                player_id=ctx.player_id,
                room_id=ctx.room_id,
                error=str(exc),
            )
            return
        logger.info(
            "Applied encounter lucidity loss",
            npc_id=ctx.npc_id,
            player_id=ctx.player_id,
            archetype=ctx.archetype,
            category=ctx.category,
        )

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
        ctx = _EncounterCtx(
            player_id=player_id,
            npc_id=npc_id,
            archetype=self._archetype_from_definition(npc_definition, npc_id),
            category=self._resolve_lucidity_category(npc_definition),
            room_id=room_id,
        )
        if self._player_registry is None:
            logger.warning("Encounter lucidity loss skipped: no player registry", npc_id=npc_id, player_id=player_id)
            return
        await self._apply_loss_with_fallback(ActiveLucidityService(self._player_registry), ctx)

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
        except ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError:
            base_stats = {}

        try:
            behavior_config = npc_definition.get_behavior_config()
        except ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError:
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
