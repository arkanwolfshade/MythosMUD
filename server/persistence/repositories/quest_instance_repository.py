"""
QuestInstance repository for quest subsystem.

CRUD for quest_instances via PostgreSQL stored procedures: create, get by player+quest,
update state/progress, list active and completed by player.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.quest import QuestInstance
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _str_player_id(player_id: UUID | str) -> str:
    """Normalize player_id to string for DB (players.player_id is UUID as_uuid=False)."""
    return str(player_id) if isinstance(player_id, UUID) else player_id


def _row_to_quest_instance(row: Any) -> QuestInstance:
    """Map procedure result row to QuestInstance model."""
    return QuestInstance(
        id=row.id,
        player_id=str(row.player_id) if row.player_id else "",
        quest_id=row.quest_id or "",
        state=row.state or "active",
        progress=dict(row.progress) if row.progress else {},
        accepted_at=row.accepted_at,
        completed_at=row.completed_at,
    )


class QuestInstanceRepository:
    """Repository for quest_instances table."""

    def __init__(self) -> None:
        self._logger = get_logger(__name__)

    async def create(
        self,
        player_id: UUID | str,
        quest_id: str,
        state: str = "active",
        progress: dict[str, Any] | None = None,
    ) -> QuestInstance:
        """Create a new quest instance. Returns the created instance (with id set)."""
        pid = _str_player_id(player_id)
        progress = progress if progress is not None else {}
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            player_id,
                            quest_id,
                            state,
                            progress,
                            accepted_at,
                            completed_at
                        FROM create_quest_instance(:player_id, :quest_id, :state, :progress)
                        """
                    ),
                    {
                        "player_id": pid,
                        "quest_id": quest_id,
                        "state": state,
                        "progress": json.dumps(progress),
                    },
                )
                row = result.mappings().first()
                if not row:
                    log_and_raise(
                        DatabaseError,
                        "create_quest_instance returned no row",
                        operation="create",
                        details={"player_id": pid, "quest_id": quest_id},
                        user_friendly="Failed to start quest",
                    )
                await session.commit()
                instance = _row_to_quest_instance(row)
                self._logger.debug(
                    "Created quest instance",
                    player_id=pid,
                    quest_id=quest_id,
                    instance_id=str(instance.id),
                )
                return instance
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error creating quest instance: {e}",
                operation="create",
                details={"player_id": pid, "quest_id": quest_id, "error": str(e)},
                user_friendly="Failed to start quest",
            )

    async def get_by_player_and_quest(
        self,
        player_id: UUID | str,
        quest_id: str,
    ) -> QuestInstance | None:
        """Get the quest instance for this player and quest (any state). Returns None if not found."""
        pid = _str_player_id(player_id)
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            player_id,
                            quest_id,
                            state,
                            progress,
                            accepted_at,
                            completed_at
                        FROM get_quest_instance_by_player_and_quest(:player_id, :quest_id)
                        """
                    ),
                    {"player_id": pid, "quest_id": quest_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_quest_instance(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading quest instance: {e}",
                operation="get_by_player_and_quest",
                details={"player_id": pid, "quest_id": quest_id, "error": str(e)},
                user_friendly="Failed to load quest progress",
            )

    async def update_state_and_progress(
        self,
        instance_id: UUID | str,
        state: str | None = None,
        progress: dict[str, Any] | None = None,
        completed_at: datetime | None = None,
    ) -> None:
        """Update an instance's state and/or progress. Pass only fields to change."""
        iid = instance_id if isinstance(instance_id, UUID) else UUID(instance_id)
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(
                    text(
                        "SELECT update_quest_instance_state_and_progress("
                        ":instance_id, :state, :progress, :completed_at)"
                    ),
                    {
                        "instance_id": str(iid),
                        "state": state,
                        "progress": json.dumps(progress) if progress is not None else None,
                        "completed_at": completed_at,
                    },
                )
                await session.commit()
                updated_keys = [
                    k
                    for k, v in [("state", state), ("progress", progress), ("completed_at", completed_at)]
                    if v is not None
                ]
                self._logger.debug(
                    "Updated quest instance",
                    instance_id=str(iid),
                    updated_keys=updated_keys,
                )
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating quest instance: {e}",
                operation="update_state_and_progress",
                details={"instance_id": str(iid), "error": str(e)},
                user_friendly="Failed to update quest progress",
            )

    async def list_active_by_player(self, player_id: UUID | str) -> list[QuestInstance]:
        """List all active quest instances for the player."""
        pid = _str_player_id(player_id)
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            player_id,
                            quest_id,
                            state,
                            progress,
                            accepted_at,
                            completed_at
                        FROM list_active_quest_instances_by_player(:player_id)
                        """
                    ),
                    {"player_id": pid},
                )
                return [_row_to_quest_instance(row) for row in result.mappings().all()]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing active quests: {e}",
                operation="list_active_by_player",
                details={"player_id": pid, "error": str(e)},
                user_friendly="Failed to load quest log",
            )

    async def list_completed_by_player(self, player_id: UUID | str) -> list[QuestInstance]:
        """List completed quest instances for the player (for quest log or prerequisite checks)."""
        pid = _str_player_id(player_id)
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            player_id,
                            quest_id,
                            state,
                            progress,
                            accepted_at,
                            completed_at
                        FROM list_completed_quest_instances_by_player(:player_id)
                        """
                    ),
                    {"player_id": pid},
                )
                return [_row_to_quest_instance(row) for row in result.mappings().all()]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing completed quests: {e}",
                operation="list_completed_by_player",
                details={"player_id": pid, "error": str(e)},
                user_friendly="Failed to load quest log",
            )
