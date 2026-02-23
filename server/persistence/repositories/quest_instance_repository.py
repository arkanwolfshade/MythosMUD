"""
QuestInstance repository for quest subsystem.

CRUD for quest_instances: create, get by player+quest, update state/progress,
list active and completed by player.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import select, update
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
                instance = QuestInstance(
                    player_id=pid,
                    quest_id=quest_id,
                    state=state,
                    progress=progress,
                )
                session.add(instance)
                await session.commit()
                await session.refresh(instance)
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
                stmt = select(QuestInstance).where(
                    QuestInstance.player_id == pid,
                    QuestInstance.quest_id == quest_id,
                )
                result = await session.execute(stmt)
                return result.unique().scalars().first()
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
                values: dict[str, Any] = {}
                if state is not None:
                    values["state"] = state
                if progress is not None:
                    values["progress"] = progress
                if completed_at is not None:
                    values["completed_at"] = completed_at
                if not values:
                    return
                stmt = update(QuestInstance).where(QuestInstance.id == iid).values(**values)
                await session.execute(stmt)
                await session.commit()
                self._logger.debug(
                    "Updated quest instance",
                    instance_id=str(iid),
                    updated_keys=list(values.keys()),
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
                stmt = (
                    select(QuestInstance)
                    .where(
                        QuestInstance.player_id == pid,
                        QuestInstance.state == "active",
                    )
                    .order_by(QuestInstance.accepted_at)
                )
                result = await session.execute(stmt)
                return list(result.unique().scalars().all())
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
                stmt = (
                    select(QuestInstance)
                    .where(
                        QuestInstance.player_id == pid,
                        QuestInstance.state == "completed",
                    )
                    .order_by(QuestInstance.completed_at.desc().nullslast())
                )
                result = await session.execute(stmt)
                return list(result.unique().scalars().all())
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing completed quests: {e}",
                operation="list_completed_by_player",
                details={"player_id": pid, "error": str(e)},
                user_friendly="Failed to load quest log",
            )
