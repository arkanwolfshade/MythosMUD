"""DialogueDefinition repository (#583).

CRUD via PostgreSQL procedures in db/procedures/dialogues.sql.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Protocol, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.dialogue import DialogueDefinition
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class _DialogueRow(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Shape of dialogue procedure result rows (attribute access via mappings)."""

    id: str | None
    definition: object
    npc_definition_id: int | None
    created_at: datetime
    updated_at: datetime


def _definition_dict(value: object) -> dict[str, object]:
    """Coerce JSONB definition cell to a plain string-keyed dict."""
    if not isinstance(value, dict):
        return {}
    mapping = cast(dict[object, object], value)
    return {str(k): v for k, v in mapping.items()}


def _as_dialogue_row(row: object) -> _DialogueRow:
    """Narrow SQLAlchemy RowMapping to the dialogue procedure row shape."""
    return cast(_DialogueRow, row)


def _row_to_dialogue(row: _DialogueRow) -> DialogueDefinition:
    """Map procedure result row to DialogueDefinition model."""
    return DialogueDefinition(
        id=row.id or "",
        definition=_definition_dict(row.definition),
        npc_definition_id=row.npc_definition_id,
        created_at=row.created_at,
        updated_at=row.updated_at,
    )


class DialogueDefinitionRepository:
    """Repository for dialogue_definitions via stored procedures."""

    def __init__(self) -> None:
        self._logger: BoundLogger = get_logger(__name__)

    async def list_all(self) -> list[DialogueDefinition]:
        """Return all dialogue definitions ordered by id."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; SQL literal, no user-built query.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            definition,
                            npc_definition_id,
                            created_at,
                            updated_at
                        FROM list_dialogue_definitions()
                        """
                    )
                )
                return [_row_to_dialogue(_as_dialogue_row(row)) for row in result.mappings().all()]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing dialogue definitions: {e}",
                operation="list_all",
                details={"error": str(e)},
                user_friendly="Failed to list dialogues",
            )

    async def get_by_id(self, dialogue_id: str) -> DialogueDefinition | None:
        """Load a dialogue definition by id. Returns None if not found."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            definition,
                            npc_definition_id,
                            created_at,
                            updated_at
                        FROM get_dialogue_definition_by_id(:dialogue_id)
                        """
                    ),
                    {"dialogue_id": dialogue_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_dialogue(_as_dialogue_row(row))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading dialogue definition: {e}",
                operation="get_by_id",
                details={"dialogue_id": dialogue_id, "error": str(e)},
                user_friendly="Failed to load dialogue",
            )

    async def get_by_npc_definition_id(self, npc_definition_id: int) -> DialogueDefinition | None:
        """Load dialogue linked to an NPC definition id. Returns None if none."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            definition,
                            npc_definition_id,
                            created_at,
                            updated_at
                        FROM get_dialogue_definition_by_npc_definition_id(:npc_definition_id)
                        """
                    ),
                    {"npc_definition_id": npc_definition_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_dialogue(_as_dialogue_row(row))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading dialogue by NPC: {e}",
                operation="get_by_npc_definition_id",
                details={"npc_definition_id": npc_definition_id, "error": str(e)},
                user_friendly="Failed to load dialogue",
            )

    async def upsert(
        self,
        dialogue_id: str,
        definition: dict[str, object],
        npc_definition_id: int | None = None,
    ) -> DialogueDefinition:
        """Insert or update a dialogue definition; return the stored row."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            definition,
                            npc_definition_id,
                            created_at,
                            updated_at
                        FROM upsert_dialogue_definition(
                            :dialogue_id, CAST(:definition AS jsonb), :npc_definition_id
                        )
                        """
                    ),
                    {
                        "dialogue_id": dialogue_id,
                        "definition": json.dumps(definition),
                        "npc_definition_id": npc_definition_id,
                    },
                )
                row = result.mappings().first()
                await session.commit()
                if not row:
                    log_and_raise(
                        DatabaseError,
                        "upsert_dialogue_definition returned no row",
                        operation="upsert",
                        details={"dialogue_id": dialogue_id},
                        user_friendly="Failed to save dialogue",
                    )
                return _row_to_dialogue(_as_dialogue_row(row))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error upserting dialogue definition: {e}",
                operation="upsert",
                details={"dialogue_id": dialogue_id, "error": str(e)},
                user_friendly="Failed to save dialogue",
            )

    async def delete(self, dialogue_id: str) -> bool:
        """Delete by id. Returns True if a row was removed."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text("SELECT delete_dialogue_definition(:dialogue_id) AS deleted"),
                    {"dialogue_id": dialogue_id},
                )
                row = result.mappings().first()
                await session.commit()
                if row is None:
                    return False
                deleted: object = cast(object, row["deleted"])
                return bool(deleted)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting dialogue definition: {e}",
                operation="delete",
                details={"dialogue_id": dialogue_id, "error": str(e)},
                user_friendly="Failed to delete dialogue",
            )
