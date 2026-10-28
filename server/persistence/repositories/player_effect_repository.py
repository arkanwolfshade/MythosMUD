"""
Player effect repository for the effects system (ADR-019, ADR-029 step 3b-i).

Async persistence for the player_effects table via PostgreSQL stored procedures: add, delete (by id, by type, the
instance-scoped ones), list a player's active effects, update an effect's payload, and advance one game second for a
set of online players (expiring the effects that run out).
"""

import json
from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import Required, TypedDict, cast
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_effect import PlayerEffect
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class AddEffectInput(TypedDict, total=False):
    """Input for add_effect: effect_type and category, plus optional fields.

    remaining_seconds: game seconds the effect lasts (counted down while the player is online); absent or None means
    until removed. payload: the effect's parameters and mutable state.
    """

    effect_type: Required[str]
    category: Required[str]
    remaining_seconds: int | None
    payload: Mapping[str, object]
    instance_scoped: bool
    intensity: int
    source: str | None
    visibility_level: str


def _row_to_player_effect(row: Mapping[str, object]) -> PlayerEffect:
    """Map a get_active_effects_for_player row to a PlayerEffect."""
    remaining = row.get("remaining_seconds")
    payload = row.get("payload")
    return PlayerEffect(
        id=str(row["id"]),
        player_id=str(row["player_id"]),
        effect_type=str(row.get("effect_type") or ""),
        category=str(row.get("category") or ""),
        remaining_seconds=int(cast(int, remaining)) if remaining is not None else None,
        payload=dict(cast(Mapping[str, object], payload)) if isinstance(payload, Mapping) else {},
        instance_scoped=bool(row.get("instance_scoped")),
        intensity=int(cast(int, row.get("intensity") or 1)),
        source=cast(str | None, row.get("source")),
        visibility_level=str(row.get("visibility_level") or "visible"),
        created_at=cast(datetime | None, row.get("created_at")),
    )


def _add_effect_params(player_id: UUID | str, data: AddEffectInput) -> dict[str, object]:
    """Build params dict for add_player_effect procedure."""
    return {
        "player_id": str(player_id),
        "effect_type": data["effect_type"],
        "category": data["category"],
        "remaining_seconds": data.get("remaining_seconds"),
        "payload": json.dumps(dict(data.get("payload", {}))),
        "instance_scoped": data.get("instance_scoped", False),
        "intensity": data.get("intensity", 1),
        "source": data.get("source"),
        "visibility_level": data.get("visibility_level", "visible"),
    }


class PlayerEffectRepository:
    """Repository for the player_effects table."""

    async def _scalar(self, statement: str, params: Mapping[str, object], operation: str) -> object:
        """Run one procedure call that returns a scalar, commit, and return the scalar. Raises DatabaseError."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(text(statement), dict(params))
                value = cast(object, result.scalar())
                await session.commit()
                return value
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error in {operation}: {e}",
                operation=operation,
                details={**{k: str(v) for k, v in params.items()}, "error": str(e)},
                user_friendly="Failed to update player effects",
            )

    async def _rows(
        self, statement: str, params: Mapping[str, object], operation: str
    ) -> Sequence[Mapping[str, object]]:
        """Run one procedure call that returns rows, commit, and return them. Raises DatabaseError."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(text(statement), dict(params))
                rows = cast(Sequence[Mapping[str, object]], result.mappings().all())
                await session.commit()
                return rows
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error in {operation}: {e}",
                operation=operation,
                details={**{k: str(v) for k, v in params.items()}, "error": str(e)},
                user_friendly="Failed to read player effects",
            )

    async def add_effect(self, player_id: UUID | str, data: AddEffectInput) -> str:
        """Add a player effect; returns its id. Raises DatabaseError if the insert fails."""
        effect_id = await self._scalar(
            "SELECT add_player_effect(:player_id, :effect_type, :category, :remaining_seconds, CAST(:payload AS jsonb),"
            + " :instance_scoped, :intensity, :source, :visibility_level)",
            _add_effect_params(player_id, data),
            "add_effect",
        )
        logger.debug("Added player effect", player_id=str(player_id), effect_type=data["effect_type"])
        return str(effect_id)

    async def delete_effect(self, effect_id: UUID | str) -> None:
        """Delete an effect by id. No-op if not found."""
        _ = await self._scalar(
            "SELECT delete_player_effect(:effect_id)", {"effect_id": str(effect_id)}, "delete_effect"
        )

    async def delete_effects_by_type(self, player_id: UUID | str, effect_type: str) -> int:
        """Delete every effect of one type on a player; returns how many were deleted."""
        deleted = await self._scalar(
            "SELECT delete_player_effects_by_type(:player_id, :effect_type)",
            {"player_id": str(player_id), "effect_type": effect_type},
            "delete_effects_by_type",
        )
        return int(cast(int, deleted or 0))

    async def delete_instance_scoped_effects(self, player_id: UUID | str) -> int:
        """Delete a player's instance-scoped effects (their instance was lost); returns how many were deleted."""
        deleted = await self._scalar(
            "SELECT delete_instance_scoped_effects(:player_id)",
            {"player_id": str(player_id)},
            "delete_instance_scoped_effects",
        )
        return int(cast(int, deleted or 0))

    async def get_active_effects_for_player(self, player_id: UUID | str) -> list[PlayerEffect]:
        """A player's effects with time left (or no limit), oldest first."""
        rows = await self._rows(
            """
            SELECT
                id,
                player_id,
                effect_type,
                category,
                remaining_seconds,
                payload,
                instance_scoped,
                intensity,
                source,
                visibility_level,
                created_at
            FROM get_active_effects_for_player(:player_id)
            """,
            {"player_id": str(player_id)},
            "get_active_effects_for_player",
        )
        return [_row_to_player_effect(row) for row in rows]

    async def update_effect_payload(self, effect_id: UUID | str, payload: Mapping[str, object]) -> None:
        """Replace an effect's payload (its mutable state)."""
        _ = await self._scalar(
            "SELECT update_player_effect_payload(:effect_id, CAST(:payload AS jsonb))",
            {"effect_id": str(effect_id), "payload": json.dumps(dict(payload))},
            "update_effect_payload",
        )

    async def advance_effects(self, player_ids: Sequence[UUID]) -> list[tuple[str, str]]:
        """One game second passes for these online players: timed effects lose a second, and the ones that run out
        are deleted and returned as (player_id, effect_type)."""
        if not player_ids:
            return []
        rows = await self._rows(
            "SELECT player_id, effect_type FROM advance_player_effects(CAST(:player_ids AS uuid[]))",
            {"player_ids": list(player_ids)},
            "advance_effects",
        )
        return [(str(row["player_id"]), str(row["effect_type"])) for row in rows]
