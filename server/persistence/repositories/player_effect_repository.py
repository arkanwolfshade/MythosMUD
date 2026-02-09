"""
Player effect repository for the effects system (ADR-009).

Async persistence for player_effects table: add, delete, get active, has_effect,
remaining_ticks, and expire effects by current tick.
"""

from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_effect import PlayerEffect
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class PlayerEffectRepository:
    """Repository for player_effects table (tick-based persistent effects)."""

    async def add_effect(
        self,
        player_id: UUID | str,
        effect_type: str,
        category: str,
        duration: int,
        applied_at_tick: int,
        intensity: int = 1,
        source: str | None = None,
        visibility_level: str = "visible",
    ) -> str:
        """
        Add a player effect. Returns the effect id (UUID string).

        Args:
            player_id: Player UUID
            effect_type: Effect type (e.g. login_warded)
            category: Category (e.g. entry_ward)
            duration: Duration in ticks
            applied_at_tick: Tick when effect was applied
            intensity: Intensity (default 1)
            source: Optional source string
            visibility_level: visible, hidden, or detailed

        Returns:
            Effect id (UUID string)

        Raises:
            DatabaseError: If insert fails
        """
        context = create_error_context()
        context.metadata["operation"] = "add_effect"
        context.metadata["player_id"] = str(player_id)
        context.metadata["effect_type"] = effect_type

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                effect = PlayerEffect(
                    player_id=str(player_id),
                    effect_type=effect_type,
                    category=category,
                    duration=duration,
                    applied_at_tick=applied_at_tick,
                    intensity=intensity,
                    source=source,
                    visibility_level=visibility_level,
                )
                session.add(effect)
                await session.commit()
                await session.refresh(effect)
                effect_id = effect.id
                logger.debug(
                    "Added player effect",
                    player_id=str(player_id),
                    effect_type=effect_type,
                    effect_id=effect_id,
                )
                return effect_id
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error adding player effect: {e}",
                context=context,
                details={"player_id": str(player_id), "effect_type": effect_type, "error": str(e)},
                user_friendly="Failed to add player effect",
            )

    async def delete_effect(self, effect_id: UUID | str) -> None:
        """Delete an effect by id. No-op if not found."""
        context = create_error_context()
        context.metadata["operation"] = "delete_effect"
        context.metadata["effect_id"] = str(effect_id)

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(delete(PlayerEffect).where(PlayerEffect.id == str(effect_id)))
                await session.commit()
                logger.debug("Deleted player effect", effect_id=str(effect_id))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player effect: {e}",
                context=context,
                details={"effect_id": str(effect_id), "error": str(e)},
                user_friendly="Failed to delete player effect",
            )

    def _remaining_ticks(self, duration: int, applied_at_tick: int, current_tick: int) -> int:
        """Compute remaining ticks. Effect is active when result > 0."""
        return duration - (current_tick - applied_at_tick)

    async def get_active_effects_for_player(self, player_id: UUID | str, current_tick: int) -> list[PlayerEffect]:
        """Return effects where remaining_ticks > 0. Order by applied_at_tick."""
        context = create_error_context()
        context.metadata["operation"] = "get_active_effects_for_player"
        context.metadata["player_id"] = str(player_id)

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    select(PlayerEffect)
                    .where(PlayerEffect.player_id == str(player_id))
                    .order_by(PlayerEffect.applied_at_tick)
                )
                rows = list(result.scalars().all())
                # Filter by remaining > 0
                active = [r for r in rows if self._remaining_ticks(r.duration, r.applied_at_tick, current_tick) > 0]
                return active
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting active effects: {e}",
                context=context,
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to get active effects",
            )

    async def get_effects_expiring_this_tick(self, current_tick: int) -> list[tuple[str, str]]:
        """
        Find effects that expire this tick (remaining <= 0), return (player_id, effect_type).
        Caller should then delete/expire them (we delete in expire_effects_for_tick).
        """
        context = create_error_context()
        context.metadata["operation"] = "get_effects_expiring_this_tick"
        context.metadata["current_tick"] = current_tick

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(select(PlayerEffect))
                rows = result.scalars().all()
                expiring = [
                    (r.player_id, r.effect_type)
                    for r in rows
                    if self._remaining_ticks(r.duration, r.applied_at_tick, current_tick) <= 0
                ]
                return expiring
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting expiring effects: {e}",
                context=context,
                details={"current_tick": current_tick, "error": str(e)},
                user_friendly="Failed to get expiring effects",
            )

    async def expire_effects_for_tick(self, current_tick: int) -> list[tuple[str, str]]:
        """
        Delete all effects that have expired at current_tick and return their (player_id, effect_type).
        """
        expiring = await self.get_effects_expiring_this_tick(current_tick)
        if not expiring:
            return []

        context = create_error_context()
        context.metadata["operation"] = "expire_effects_for_tick"
        context.metadata["current_tick"] = current_tick

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # Delete rows where applied_at_tick + duration <= current_tick
                stmt = delete(PlayerEffect).where(PlayerEffect.applied_at_tick + PlayerEffect.duration <= current_tick)
                await session.execute(stmt)
                await session.commit()
                logger.debug(
                    "Expired player effects for tick",
                    current_tick=current_tick,
                    count=len(expiring),
                    expired=expiring,
                )
                return expiring
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error expiring effects: {e}",
                context=context,
                details={"current_tick": current_tick, "error": str(e)},
                user_friendly="Failed to expire effects",
            )

    async def has_effect(self, player_id: UUID | str, effect_type: str, current_tick: int) -> bool:
        """Return True if player has an active effect of the given type."""
        active = await self.get_active_effects_for_player(player_id, current_tick)
        return any(e.effect_type == effect_type for e in active)

    async def get_effect_remaining_ticks(
        self, player_id: UUID | str, effect_type: str, current_tick: int
    ) -> int | None:
        """
        Return remaining ticks for the first matching active effect, or None if none.
        """
        active = await self.get_active_effects_for_player(player_id, current_tick)
        for e in active:
            if e.effect_type == effect_type:
                return self._remaining_ticks(e.duration, e.applied_at_tick, current_tick)
        return None
