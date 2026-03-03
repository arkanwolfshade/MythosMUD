"""
NPC management service for MythosMUD.

This module provides comprehensive NPC management including CRUD operations
for NPC definitions, spawn rules, relationships, and instance management.
Uses PostgreSQL stored procedures for all database access.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: NPC service requires many parameters and intermediate variables for complex NPC management logic. NPC service requires extensive NPC management operations for comprehensive NPC system management.

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError
from ..models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from ..structured_logging.enhanced_logging_config import get_logger
from .npc_service_models import (
    CreateNPCDefinitionInput,
    NPCDefinitionCreateParams,
    NPCDefinitionUpdateParams,
    _row_to_npc_definition,
    _row_to_npc_spawn_rule,
)

logger = get_logger("services.npc_service")

__all__ = [
    "NPCService",
    "CreateNPCDefinitionInput",
    "NPCDefinitionCreateParams",
    "NPCDefinitionUpdateParams",
]


class NPCService:
    """
    Comprehensive NPC management service.

    Handles CRUD operations for NPC definitions, spawn rules, relationships,
    and provides integration with the NPC subsystem.
    """

    def __init__(self) -> None:
        """Initialize the NPC service."""
        logger.info("NPCService initialized")

    # NPC Definition CRUD Operations

    async def get_npc_definitions(self, session: AsyncSession) -> list[NPCDefinition]:
        """
        Get all NPC definitions.

        Args:
            session: Database session

        Returns:
            List of NPC definitions
        """
        try:
            result = await session.execute(text("SELECT * FROM get_npc_definitions()"))
            rows = result.mappings().all()
            definitions = [_row_to_npc_definition(row) for row in rows]
            logger.info("Retrieved NPC definitions")
            return definitions

        except SQLAlchemyError as e:
            logger.error("Database error retrieving NPC definitions", error=str(e), error_type=type(e).__name__)
            if "does not exist" in str(e).lower() or "UndefinedTableError" in type(e).__name__:
                logger.warning(
                    "Ensure POSTGRES_SEARCH_PATH is set (e.g. mythos_dev in .env.local) and that "
                    "the schema DDL has been applied (e.g. psql -d mythos_dev -f db/mythos_dev_ddl.sql)",
                )
            raise DatabaseError(f"Failed to retrieve NPC definitions: {e}") from e
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC retrieval errors unpredictable, must re-raise
            logger.error("Unexpected error retrieving NPC definitions", error=str(e), error_type=type(e).__name__)
            raise

    async def get_npc_definition(self, session: AsyncSession, definition_id: int) -> NPCDefinition | None:
        """
        Get a specific NPC definition by ID.

        Args:
            session: Database session
            definition_id: NPC definition ID

        Returns:
            NPC definition or None if not found
        """
        try:
            result = await session.execute(
                text("SELECT * FROM get_npc_definition(:definition_id)"),
                {"definition_id": definition_id},
            )
            rows = result.mappings().all()
            if not rows:
                logger.warning("NPC definition not found", definition_id=definition_id)
                return None
            definition = _row_to_npc_definition(rows[0])
            logger.info("Retrieved NPC definition", definition_id=definition_id, name=definition.name)
            return definition

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition retrieval errors unpredictable, must re-raise
            logger.error("Error retrieving NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def create_npc_definition(self, session: AsyncSession, data: CreateNPCDefinitionInput) -> NPCDefinition:
        """
        Create a new NPC definition.

        Args:
            session: Database session
            data: Must include name, npc_type, sub_zone_id. May include description,
                room_id, required_npc, max_population, spawn_probability,
                base_stats, behavior_config, ai_integration_stub.

        Returns:
            Created NPC definition

        Raises:
            ValueError: If validation fails
        """
        name = data["name"]
        npc_type = data["npc_type"]
        sub_zone_id = data["sub_zone_id"]
        description = data.get("description")
        room_id = data.get("room_id")
        required_npc = data.get("required_npc", False)
        max_population = data.get("max_population", 1)
        spawn_probability = data.get("spawn_probability", 1.0)
        base_stats = data.get("base_stats") or {}
        behavior_config = data.get("behavior_config") or {}
        ai_integration_stub = data.get("ai_integration_stub") or {}

        try:
            self._validate_create_npc_definition_params(npc_type, spawn_probability, max_population)
            params: NPCDefinitionCreateParams = {
                "name": name,
                "description": description,
                "npc_type": npc_type,
                "sub_zone_id": sub_zone_id,
                "room_id": room_id,
                "required_npc": required_npc,
                "max_population": max_population,
                "spawn_probability": spawn_probability,
                "base_stats": base_stats,
                "behavior_config": behavior_config,
                "ai_integration_stub": ai_integration_stub,
            }
            definition = await self._execute_create_npc_definition(session=session, params=params)
            self._log_npc_definition_created(definition, name, npc_type, sub_zone_id)
            return definition

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition creation errors unpredictable, must re-raise
            logger.error("Error creating NPC definition", error=str(e), name=name, npc_type=npc_type)
            raise

    async def _execute_create_npc_definition(
        self,
        session: AsyncSession,
        *,
        params: NPCDefinitionCreateParams,
    ) -> NPCDefinition:
        """Execute create_npc_definition stored procedure and return the created definition."""
        result = await session.execute(
            text(
                "SELECT * FROM create_npc_definition("
                ":name, :description, :npc_type, :sub_zone_id, :room_id,"
                " :required_npc, :max_population, :spawn_probability,"
                " :base_stats, :behavior_config, :ai_integration_stub)"
            ),
            {
                "name": params["name"],
                "description": params["description"],
                "npc_type": params["npc_type"],
                "sub_zone_id": params["sub_zone_id"],
                "room_id": params["room_id"],
                "required_npc": params["required_npc"],
                "max_population": params["max_population"],
                "spawn_probability": params["spawn_probability"],
                "base_stats": json.dumps(params["base_stats"]),
                "behavior_config": json.dumps(params["behavior_config"]),
                "ai_integration_stub": json.dumps(params["ai_integration_stub"]),
            },
        )
        rows = result.mappings().all()
        if not rows:
            raise DatabaseError("create_npc_definition returned no row")
        return _row_to_npc_definition(rows[0])

    @staticmethod
    def _validate_create_npc_definition_params(npc_type: str, spawn_probability: float, max_population: int) -> None:
        """Validate create_npc_definition parameters. Raises ValueError if invalid."""
        if npc_type not in [t.value for t in NPCDefinitionType]:
            raise ValueError(f"Invalid NPC type: {npc_type}")
        if not 0.0 <= spawn_probability <= 1.0:
            raise ValueError(f"Spawn probability must be between 0.0 and 1.0, got: {spawn_probability}")
        if max_population < 1:
            raise ValueError(f"Max population must be at least 1, got: {max_population}")

    @staticmethod
    def _log_npc_definition_created(definition: NPCDefinition, name: str, npc_type: str, sub_zone_id: str) -> None:
        """Log successful NPC definition creation."""
        logger.info(
            "Created NPC definition",
            definition_id=definition.id,
            name=name,
            npc_type=npc_type,
            sub_zone_id=sub_zone_id,
        )

    def _validate_npc_update_params(
        self, npc_type: str | None, spawn_probability: float | None, max_population: int | None
    ) -> None:
        """Validate NPC update parameters."""
        if npc_type is not None and npc_type not in [t.value for t in NPCDefinitionType]:
            raise ValueError(f"Invalid NPC type: {npc_type}")

        if spawn_probability is not None and not 0.0 <= spawn_probability <= 1.0:
            raise ValueError(f"Spawn probability must be between 0.0 and 1.0, got: {spawn_probability}")

        if max_population is not None and max_population < 1:
            raise ValueError(f"Max population must be at least 1, got: {max_population}")

    def _add_simple_field(self, update_data: dict[str, Any], field_name: str, value: Any | None) -> None:
        """Add a simple field to update_data if value is not None."""
        if value is not None:
            update_data[field_name] = value

    def _add_json_field(self, update_data: dict[str, Any], field_name: str, value: dict[str, Any] | None) -> None:
        """Add a JSON-encoded field to update_data if value is not None."""
        if value is not None:
            update_data[field_name] = json.dumps(value)

    def _build_npc_update_data(self, params: NPCDefinitionUpdateParams) -> dict[str, Any]:
        """Build update data dictionary from provided parameters."""
        update_data: dict[str, Any] = {}
        self._add_simple_field(update_data, "name", params.get("name"))
        self._add_simple_field(update_data, "description", params.get("description"))
        self._add_simple_field(update_data, "npc_type", params.get("npc_type"))
        self._add_simple_field(update_data, "sub_zone_id", params.get("sub_zone_id"))
        self._add_simple_field(update_data, "room_id", params.get("room_id"))
        self._add_simple_field(update_data, "required_npc", params.get("required_npc"))
        self._add_simple_field(update_data, "max_population", params.get("max_population"))
        self._add_simple_field(update_data, "spawn_probability", params.get("spawn_probability"))
        self._add_json_field(update_data, "base_stats", params.get("base_stats"))
        self._add_json_field(update_data, "behavior_config", params.get("behavior_config"))
        self._add_json_field(update_data, "ai_integration_stub", params.get("ai_integration_stub"))
        update_data["updated_at"] = datetime.now(UTC).replace(tzinfo=None)
        return update_data

    async def _execute_npc_update(
        self,
        session: AsyncSession,
        definition_id: int,
        update_data: dict[str, Any],
        _definition: NPCDefinition,
    ) -> NPCDefinition:
        """Execute the database update via procedure and return updated definition."""
        result = await session.execute(
            text(
                "SELECT * FROM update_npc_definition("
                ":id, :name, :description, :npc_type, :sub_zone_id, :room_id,"
                " :required_npc, :max_population, :spawn_probability,"
                " :base_stats, :behavior_config, :ai_integration_stub)"
            ),
            {
                "id": definition_id,
                "name": update_data.get("name"),
                "description": update_data.get("description"),
                "npc_type": update_data.get("npc_type"),
                "sub_zone_id": update_data.get("sub_zone_id"),
                "room_id": update_data.get("room_id"),
                "required_npc": update_data.get("required_npc"),
                "max_population": update_data.get("max_population"),
                "spawn_probability": update_data.get("spawn_probability"),
                "base_stats": update_data.get("base_stats"),
                "behavior_config": update_data.get("behavior_config"),
                "ai_integration_stub": update_data.get("ai_integration_stub"),
            },
        )
        rows = result.mappings().all()
        if not rows:
            raise DatabaseError("update_npc_definition returned no row")
        updated = _row_to_npc_definition(rows[0])
        logger.info("Updated NPC definition", definition_id=definition_id, updated_fields=list(update_data.keys()))
        return updated

    async def update_npc_definition(  # pylint: disable=too-many-locals  # Reason: NPC definition update requires intermediate variables for complex update logic
        self,
        session: AsyncSession,
        definition_id: int,
        params: NPCDefinitionUpdateParams,
    ) -> NPCDefinition | None:
        """
        Update an existing NPC definition.

        Args:
            session: Database session
            definition_id: NPC definition ID
            name: New NPC name (optional)
            description: New NPC description (optional)
            npc_type: New NPC type (optional)
            sub_zone_id: New sub-zone ID (optional)
            room_id: New room ID (optional)
            required_npc: New required status (optional)
            max_population: New max population (optional)
            spawn_probability: New spawn probability (optional)
            base_stats: New base stats (optional)
            behavior_config: New behavior config (optional)
            ai_integration_stub: New AI integration stub (optional)

        Returns:
            Updated NPC definition or None if not found

        Raises:
            ValueError: If validation fails
        """
        try:
            definition = await self.get_npc_definition(session, definition_id)
            if not definition:
                return None

            npc_type = params.get("npc_type")
            spawn_probability = params.get("spawn_probability")
            max_population = params.get("max_population")

            self._validate_npc_update_params(npc_type, spawn_probability, max_population)

            update_data = self._build_npc_update_data(params)

            return await self._execute_npc_update(session, definition_id, update_data, definition)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition update errors unpredictable, must re-raise
            logger.error("Error updating NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def delete_npc_definition(self, session: AsyncSession, definition_id: int) -> bool:
        """
        Delete an NPC definition.

        Args:
            session: Database session
            definition_id: NPC definition ID

        Returns:
            True if deleted, False if not found
        """
        try:
            definition = await self.get_npc_definition(session, definition_id)
            if not definition:
                return False

            result = await session.execute(
                text("SELECT delete_npc_definition(:id)"),
                {"id": definition_id},
            )
            deleted = result.scalar()
            if deleted:
                logger.info("Deleted NPC definition", definition_id=definition_id, name=definition.name)
            return bool(deleted)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition deletion errors unpredictable, must re-raise
            logger.error("Error deleting NPC definition", error=str(e), definition_id=definition_id)
            raise

    # NPC Spawn Rule CRUD Operations

    async def get_spawn_rules(self, session: AsyncSession) -> list[NPCSpawnRule]:
        """
        Get all NPC spawn rules.

        Args:
            session: Database session

        Returns:
            List of NPC spawn rules
        """
        try:
            result = await session.execute(text("SELECT * FROM get_spawn_rules()"))
            rows = result.mappings().all()
            rules = [_row_to_npc_spawn_rule(row) for row in rows]
            logger.info("Retrieved NPC spawn rules", count=len(rules))
            return rules

        except SQLAlchemyError as e:
            logger.error("Database error retrieving NPC spawn rules", error=str(e), error_type=type(e).__name__)
            raise DatabaseError(f"Failed to retrieve NPC spawn rules: {e}") from e
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule retrieval errors unpredictable, must re-raise
            logger.error("Unexpected error retrieving NPC spawn rules", error=str(e), error_type=type(e).__name__)
            raise

    async def get_spawn_rule(self, session: AsyncSession, rule_id: int) -> NPCSpawnRule | None:
        """
        Get a specific NPC spawn rule by ID.

        Args:
            session: Database session
            rule_id: NPC spawn rule ID

        Returns:
            NPC spawn rule or None if not found
        """
        try:
            result = await session.execute(
                text("SELECT * FROM get_spawn_rule(:rule_id)"),
                {"rule_id": rule_id},
            )
            rows = result.mappings().all()
            if not rows:
                logger.warning("NPC spawn rule not found", rule_id=rule_id)
                return None
            rule = _row_to_npc_spawn_rule(rows[0])
            logger.info("Retrieved NPC spawn rule", rule_id=rule_id, npc_definition_id=rule.npc_definition_id)
            return rule

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule retrieval errors unpredictable, must re-raise
            logger.error("Error retrieving NPC spawn rule", error=str(e), rule_id=rule_id)
            raise

    async def create_spawn_rule(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Spawn rule creation requires many parameters for complete spawn rule setup
        self,
        session: AsyncSession,
        npc_definition_id: int,
        sub_zone_id: str,
        min_population: int = 0,
        max_population: int = 999,
        spawn_conditions: dict[str, Any] | None = None,
    ) -> NPCSpawnRule:
        """
        Create a new NPC spawn rule.

        Args:
            session: Database session
            npc_definition_id: NPC definition ID
            sub_zone_id: Sub-zone ID
            min_population: Minimum NPC population count
            max_population: Maximum NPC population count
            spawn_conditions: Spawn conditions dictionary

        Returns:
            Created NPC spawn rule

        Raises:
            ValueError: If validation fails
        """
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule creation errors unpredictable, must re-raise
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
        definition = await self.get_npc_definition(session, npc_definition_id)
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
                "SELECT * FROM create_spawn_rule("
                ":npc_definition_id, :sub_zone_id, :min_population, :max_population, :spawn_conditions)"
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
        """
        Delete an NPC spawn rule.

        Args:
            session: Database session
            rule_id: NPC spawn rule ID

        Returns:
            True if deleted, False if not found
        """
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule deletion errors unpredictable, must re-raise
            logger.error("Error deleting NPC spawn rule", error=str(e), rule_id=rule_id)
            raise

    # Utility Methods

    async def get_npc_definitions_by_type(self, session: AsyncSession, npc_type: str) -> list[NPCDefinition]:
        """
        Get NPC definitions by type.

        Args:
            session: Database session
            npc_type: NPC type to filter by

        Returns:
            List of NPC definitions of the specified type
        """
        try:
            result = await session.execute(
                text("SELECT * FROM get_npc_definitions_by_type(:npc_type)"),
                {"npc_type": npc_type},
            )
            rows = result.mappings().all()
            definitions = [_row_to_npc_definition(row) for row in rows]
            logger.info("Retrieved NPC definitions by type", npc_type=npc_type, count=len(definitions))
            return definitions

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition type retrieval errors unpredictable, must re-raise
            logger.error("Error retrieving NPC definitions by type", error=str(e), npc_type=npc_type)
            raise

    async def get_npc_definitions_by_sub_zone(self, session: AsyncSession, sub_zone_id: str) -> list[NPCDefinition]:
        """
        Get NPC definitions by sub-zone.

        Args:
            session: Database session
            sub_zone_id: Sub-zone ID to filter by

        Returns:
            List of NPC definitions in the specified sub-zone
        """
        try:
            result = await session.execute(
                text("SELECT * FROM get_npc_definitions_by_sub_zone(:sub_zone_id)"),
                {"sub_zone_id": sub_zone_id},
            )
            rows = result.mappings().all()
            definitions = [_row_to_npc_definition(row) for row in rows]
            logger.info("Retrieved NPC definitions by sub-zone", sub_zone_id=sub_zone_id, count=len(definitions))
            return definitions

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition sub-zone retrieval errors unpredictable, must re-raise
            logger.error("Error retrieving NPC definitions by sub-zone", error=str(e), sub_zone_id=sub_zone_id)
            raise

    async def get_system_statistics(self, session: AsyncSession) -> dict[str, Any]:
        """
        Get system-wide NPC statistics.

        Args:
            session: Database session

        Returns:
            Dictionary with system statistics
        """
        try:
            result = await session.execute(text("SELECT * FROM get_npc_system_statistics()"))
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC statistics generation errors unpredictable, must re-raise
            logger.error("Unexpected error generating NPC system statistics", error=str(e), error_type=type(e).__name__)
            raise


# Global NPC service instance
npc_service = NPCService()
