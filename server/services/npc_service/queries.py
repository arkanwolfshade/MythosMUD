"""NPC query operations for NPCService."""

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ...exceptions import DatabaseError
from ...models.npc import NPCDefinition
from ...structured_logging.enhanced_logging_config import get_logger
from ..npc_service_models import _row_to_npc_definition

logger = get_logger("services.npc_service")


class NPCQueryMixin:
    """Mixin providing NPC query operations."""

    async def get_npc_definitions_by_type(self, session: AsyncSession, npc_type: str) -> list[NPCDefinition]:
        """Get NPC definitions by type."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, name, description, npc_type, sub_zone_id, room_id,
                        required_npc, max_population, spawn_probability,
                        base_stats, behavior_config, ai_integration_stub,
                        created_at, updated_at
                    FROM get_npc_definitions_by_type(:npc_type)
                    """
                ),
                {"npc_type": npc_type},
            )
            rows = result.mappings().all()
            definitions = [_row_to_npc_definition(row) for row in rows]
            logger.info("Retrieved NPC definitions by type", npc_type=npc_type, count=len(definitions))
            return definitions

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error retrieving NPC definitions by type", error=str(e), npc_type=npc_type)
            raise

    async def get_npc_definitions_by_sub_zone(self, session: AsyncSession, sub_zone_id: str) -> list[NPCDefinition]:
        """Get NPC definitions by sub-zone."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, name, description, npc_type, sub_zone_id, room_id,
                        required_npc, max_population, spawn_probability,
                        base_stats, behavior_config, ai_integration_stub,
                        created_at, updated_at
                    FROM get_npc_definitions_by_sub_zone(:sub_zone_id)
                    """
                ),
                {"sub_zone_id": sub_zone_id},
            )
            rows = result.mappings().all()
            definitions = [_row_to_npc_definition(row) for row in rows]
            logger.info("Retrieved NPC definitions by sub-zone", sub_zone_id=sub_zone_id, count=len(definitions))
            return definitions

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error retrieving NPC definitions by sub-zone", error=str(e), sub_zone_id=sub_zone_id)
            raise

    async def get_system_statistics(self, session: AsyncSession) -> dict[str, Any]:
        """Get system-wide NPC statistics."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT total_npc_definitions, npc_definitions_by_type, total_spawn_rules
                    FROM get_npc_system_statistics()
                    """
                )
            )
            rows = result.mappings().all()
            if not rows:
                raise DatabaseError("get_npc_system_statistics returned no row")
            row = rows[0]
            by_type = row.npc_definitions_by_type
            if isinstance(by_type, str):
                by_type = json.loads(by_type) if by_type else {}
            elif by_type is None:
                by_type = {}
            stats = {
                "total_npc_definitions": row.total_npc_definitions,
                "npc_definitions_by_type": dict(by_type) if by_type else {},
                "total_spawn_rules": row.total_spawn_rules,
                "generated_at": datetime.now(UTC).isoformat(),
            }
            logger.info("Generated NPC system statistics", **stats)
            return stats

        except SQLAlchemyError as e:
            logger.error("Database error generating NPC system statistics", error=str(e), error_type=type(e).__name__)
            raise DatabaseError(f"Failed to generate NPC system statistics: {e}") from e
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Unexpected error generating NPC system statistics", error=str(e), error_type=type(e).__name__)
            raise
