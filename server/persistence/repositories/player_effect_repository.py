"""
Player effect repository for the effects system (ADR-009).

Async persistence for player_effects table via PostgreSQL stored procedures:
add, delete, get active, has_effect, remaining_ticks, and expire effects by current tick.
"""

from typing import Any, TypedDict
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_effect import PlayerEffect
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _str_opt(val: Any) -> str:
    """Return str(val) or empty string if val is None."""
    return str(val) if val is not None else ""


def _int_opt(val: Any, default: int = 0) -> int:
    """Return int value or default if val is None."""
    return int(val) if val is not None else default


def _opt_str(val: Any, default: str = "") -> str:
    """Return str value or default if val is None."""
    return str(val) if val is not None else default


def _row_to_player_effect(row: Any) -> PlayerEffect:
    """Map procedure result row to PlayerEffect model."""
    return PlayerEffect(
        id=_str_opt(row.id),
        player_id=_str_opt(row.player_id),
        effect_type=_opt_str(row.effect_type, ""),
        category=_opt_str(row.category, ""),
        duration=_int_opt(row.duration, 0),
        applied_at_tick=_int_opt(row.applied_at_tick, 0),
        intensity=_int_opt(row.intensity, 1),
        source=row.source,
        visibility_level=_opt_str(row.visibility_level, "visible"),
        created_at=row.created_at,
    )


class AddEffectInput(TypedDict, total=False):
    """Input for add_effect. effect_type, category, duration, applied_at_tick required; rest optional."""

    effect_type: str
    category: str
    duration: int
    applied_at_tick: int
    intensity: int
    source: str | None
    visibility_level: str


def _add_effect_params(player_id: UUID | str, data: AddEffectInput) -> dict[str, Any]:
    """Build params dict for add_player_effect procedure."""
    return {
        "player_id": str(player_id),
        "effect_type": data["effect_type"],
        "category": data["category"],
        "duration": data["duration"],
        "applied_at_tick": data["applied_at_tick"],
        "intensity": data.get("intensity", 1),
        "source": data.get("source"),
        "visibility_level": data.get("visibility_level", "visible"),
    }


class PlayerEffectRepository:
    """Repository for player_effects table (tick-based persistent effects)."""

    async def _execute_add_effect(self, params: dict[str, Any]) -> str:
        """Run add_player_effect procedure and return effect id. Raises on DB error."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            result = await session.execute(
                text(
                    "SELECT add_player_effect("
                    ":player_id, :effect_type, :category, :duration, :applied_at_tick,"
                    " :intensity, :source, :visibility_level)"
                ),
                params,
            )
            effect_id = result.scalar()
            await session.commit()
            logger.debug(
                "Added player effect",
                player_id=params.get("player_id"),
                effect_type=params.get("effect_type"),
                effect_id=str(effect_id),
            )
            return str(effect_id)

    async def add_effect(self, player_id: UUID | str, data: AddEffectInput) -> str:
        """
        Add a player effect. Returns the effect id (UUID string).

        Args:
            player_id: Player UUID
            data: Must include effect_type, category, duration, applied_at_tick.
                May include intensity (default 1), source, visibility_level (default "visible").

        Returns:
            Effect id (UUID string)

        Raises:
            DatabaseError: If insert fails
        """
        effect_type = data["effect_type"]
        try:
            params = _add_effect_params(player_id, data)
            return await self._execute_add_effect(params)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error adding player effect: {e}",
                operation="add_effect",
                player_id=str(player_id),
                effect_type=effect_type,
                details={"player_id": str(player_id), "effect_type": effect_type, "error": str(e)},
                user_friendly="Failed to add player effect",
            )

    async def delete_effect(self, effect_id: UUID | str) -> None:
        """Delete an effect by id. No-op if not found."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(
                    text("SELECT delete_player_effect(:effect_id)"),
                    {"effect_id": str(effect_id)},
                )
                await session.commit()
                logger.debug("Deleted player effect", effect_id=str(effect_id))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player effect: {e}",
                operation="delete_effect",
                effect_id=str(effect_id),
                details={"effect_id": str(effect_id), "error": str(e)},
                user_friendly="Failed to delete player effect",
            )

    def _remaining_ticks(self, duration: int, applied_at_tick: int, current_tick: int) -> int:
        """Compute remaining ticks. Effect is active when result > 0."""
        return duration - (current_tick - applied_at_tick)

    async def get_active_effects_for_player(self, player_id: UUID | str, current_tick: int) -> list[PlayerEffect]:
        """Return effects where remaining_ticks > 0. Order by applied_at_tick."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            player_id,
                            effect_type,
                            category,
                            duration,
                            applied_at_tick,
                            intensity,
                            source,
                            visibility_level,
                            created_at
                        FROM get_active_effects_for_player(:player_id, :current_tick)
                        """
                    ),
                    {"player_id": str(player_id), "current_tick": current_tick},
                )
                rows = result.mappings().all()
                return [_row_to_player_effect(row) for row in rows]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting active effects: {e}",
                operation="get_active_effects_for_player",
                player_id=str(player_id),
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to get active effects",
            )

    async def get_effects_expiring_this_tick(self, current_tick: int) -> list[tuple[str, str]]:
        """
        Find effects that expire this tick (remaining <= 0), return (player_id, effect_type).
        Caller should then delete/expire them (we delete in expire_effects_for_tick).
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            player_id,
                            effect_type
                        FROM get_effects_expiring_this_tick(:current_tick)
                        """
                    ),
                    {"current_tick": current_tick},
                )
                rows = result.mappings().all()
                return [(str(row.player_id), str(row.effect_type)) for row in rows]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting expiring effects: {e}",
                operation="get_effects_expiring_this_tick",
                current_tick=current_tick,
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

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(
                    text("SELECT expire_effects_for_tick(:current_tick)"),
                    {"current_tick": current_tick},
                )
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
                operation="expire_effects_for_tick",
                current_tick=current_tick,
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
