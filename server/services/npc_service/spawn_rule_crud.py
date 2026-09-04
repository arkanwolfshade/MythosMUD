"""NPC spawn rule CRUD operations for NPCService."""

import json
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ...exceptions import DatabaseError
from ...models.npc import NPCSpawnRule
from ...structured_logging.enhanced_logging_config import get_logger
from ..npc_service_models import _row_to_npc_spawn_rule

logger = get_logger("services.npc_service")


class NPCSpawnRuleCRUDMixin:
    """Mixin providing NPC spawn rule CRUD operations."""

    async def get_spawn_rules(self, session: AsyncSession) -> list[NPCSpawnRule]:
        """Get all NPC spawn rules."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, npc_definition_id, sub_zone_id, min_population,
                        max_population, spawn_conditions
                    FROM get_spawn_rules()
                    """
                )
            )
            rows = result.mappings().all()
            rules = [_row_to_npc_spawn_rule(row) for row in rows]
            logger.info("Retrieved NPC spawn rules", count=len(rules))
            return rules

        except SQLAlchemyError as e:
            logger.error("Database error retrieving NPC spawn rules", error=str(e), error_type=type(e).__name__)
            raise DatabaseError(f"Failed to retrieve NPC spawn rules: {e}") from e
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Unexpected error retrieving NPC spawn rules", error=str(e), error_type=type(e).__name__)
            raise

    async def get_spawn_rule(self, session: AsyncSession, rule_id: int) -> NPCSpawnRule | None:
        """Get a specific NPC spawn rule by ID."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, npc_definition_id, sub_zone_id, min_population,
                        max_population, spawn_conditions
                    FROM get_spawn_rule(:rule_id)
                    """
                ),
                {"rule_id": rule_id},
            )
            rows = result.mappings().all()
            if not rows:
                logger.warning("NPC spawn rule not found", rule_id=rule_id)
                return None
            rule = _row_to_npc_spawn_rule(rows[0])
            logger.info("Retrieved NPC spawn rule", rule_id=rule_id, npc_definition_id=rule.npc_definition_id)
            return rule

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error retrieving NPC spawn rule", error=str(e), rule_id=rule_id)
            raise

    async def create_spawn_rule(
        self,
        session: AsyncSession,
        npc_definition_id: int,
        sub_zone_id: str,
        min_population: int = 0,
        max_population: int = 999,
        spawn_conditions: dict[str, Any] | None = None,
    ) -> NPCSpawnRule:
        """Create a new NPC spawn rule."""
        try:
            await self._validate_spawn_rule_inputs(session, npc_definition_id, min_population, max_population)
            return await self._execute_create_spawn_rule(
                session,
                npc_definition_id,
                sub_zone_id,
                min_population,
                max_population,
                spawn_conditions or {},
            )

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error creating NPC spawn rule", error=str(e), npc_definition_id=npc_definition_id)
            raise

    async def _validate_spawn_rule_inputs(
        self,
        session: AsyncSession,
        npc_definition_id: int,
        min_population: int,
        max_population: int,
    ) -> None:
        """Validate NPC definition existence and population counts for spawn rule creation."""
        # Mixin used with NPCDefinitionCRUDMixin in NPCService; get_npc_definition provided by that mixin
        definition = await self.get_npc_definition(session, npc_definition_id)  # type: ignore[attr-defined]
        if not definition:
            raise ValueError(f"NPC definition not found: {npc_definition_id}")
        if min_population < 0:
            raise ValueError(f"Min population must be non-negative, got: {min_population}")
        if max_population < min_population:
            raise ValueError(f"Max population must be >= min population, got: {max_population} < {min_population}")

    async def _execute_create_spawn_rule(
        self,
        session: AsyncSession,
        npc_definition_id: int,
        sub_zone_id: str,
        min_population: int,
        max_population: int,
        spawn_conditions: dict[str, Any],
    ) -> NPCSpawnRule:
        """Execute create_spawn_rule stored procedure and return the created spawn rule."""
        result = await session.execute(
            text(
                """
                SELECT id, npc_definition_id, sub_zone_id, min_population,
                    max_population, spawn_conditions
                FROM create_spawn_rule(
                    :npc_definition_id, :sub_zone_id, :min_population, :max_population, :spawn_conditions
                )
                """
            ),
            {
                "npc_definition_id": npc_definition_id,
                "sub_zone_id": sub_zone_id,
                "min_population": min_population,
                "max_population": max_population,
                "spawn_conditions": json.dumps(spawn_conditions),
            },
        )
        rows = result.mappings().all()
        if not rows:
            raise DatabaseError("create_spawn_rule returned no row")
        rule = _row_to_npc_spawn_rule(rows[0])

        logger.info(
            "Created NPC spawn rule",
            rule_id=rule.id,
            npc_definition_id=npc_definition_id,
            sub_zone_id=sub_zone_id,
        )
        return rule

    async def delete_spawn_rule(self, session: AsyncSession, rule_id: int) -> bool:
        """Delete an NPC spawn rule."""
        try:
            rule = await self.get_spawn_rule(session, rule_id)
            if not rule:
                return False

            result = await session.execute(
                text("SELECT delete_spawn_rule(:id)"),
                {"id": rule_id},
            )
            deleted = result.scalar()
            if deleted:
                logger.info("Deleted NPC spawn rule", rule_id=rule_id, npc_definition_id=rule.npc_definition_id)
            return bool(deleted)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error deleting NPC spawn rule", error=str(e), rule_id=rule_id)
            raise
