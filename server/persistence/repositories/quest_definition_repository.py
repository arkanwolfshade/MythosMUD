"""
QuestDefinition repository for quest subsystem.

Provides get_by_id, get_by_name (resolve common name to quest), and list for offer checks.
Uses PostgreSQL stored procedures.
"""

from __future__ import annotations

from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.quest import QuestDefinition
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _row_to_quest_definition(row: Any) -> QuestDefinition:
    """Map procedure result row to QuestDefinition model."""
    return QuestDefinition(
        id=row.id or "",
        definition=dict(row.definition) if row.definition else {},
        created_at=row.created_at,
        updated_at=row.updated_at,
    )


class QuestDefinitionRepository:
    """Repository for quest_definitions and quest_offers (read-only for offers)."""

    def __init__(self) -> None:
        self._logger = get_logger(__name__)

    async def get_by_id(self, quest_id: str) -> QuestDefinition | None:
        """Load a quest definition by id. Returns None if not found."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_quest_definition_by_id(:quest_id)"),
                    {"quest_id": quest_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_quest_definition(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading quest definition: {e}",
                operation="get_by_id",
                details={"quest_id": quest_id, "error": str(e)},
                user_friendly="Failed to load quest",
            )

    async def get_by_name(self, name: str) -> QuestDefinition | None:
        """Load a quest definition by common name (definition->>'name'). Returns None if not found."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_quest_definition_by_name(:name)"),
                    {"name": name},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_quest_definition(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading quest by name: {e}",
                operation="get_by_name",
                details={"name": name, "error": str(e)},
                user_friendly="Failed to load quest",
            )

    async def list_quest_ids_offered_by(self, entity_type: str, entity_id: str) -> list[str]:
        """Return quest IDs offered by the given entity (npc or room)."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM list_quest_ids_offered_by(:entity_type, :entity_id)"),
                    {"entity_type": entity_type, "entity_id": entity_id},
                )
                return [row.quest_id for row in result.mappings().all()]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing quests offered by entity: {e}",
                operation="list_quest_ids_offered_by",
                details={
                    "entity_type": entity_type,
                    "entity_id": entity_id,
                    "error": str(e),
                },
                user_friendly="Failed to load offered quests",
            )
