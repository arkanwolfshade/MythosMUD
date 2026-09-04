"""NPC definition CRUD operations for NPCService."""

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ...exceptions import DatabaseError
from ...models.npc import NPCDefinition, NPCDefinitionType
from ...structured_logging.enhanced_logging_config import get_logger
from ..npc_service_models import (
    CreateNPCDefinitionInput,
    NPCDefinitionCreateParams,
    NPCDefinitionUpdateParams,
    _row_to_npc_definition,
)

logger = get_logger("services.npc_service")


class NPCDefinitionCRUDMixin:
    """Mixin providing NPC definition CRUD operations."""

    async def get_npc_definitions(self, session: AsyncSession) -> list[NPCDefinition]:
        """Get all NPC definitions."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, name, description, npc_type, sub_zone_id, room_id,
                        required_npc, max_population, spawn_probability,
                        base_stats, behavior_config, ai_integration_stub,
                        created_at, updated_at
                    FROM get_npc_definitions()
                    """
                )
            )
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Unexpected error retrieving NPC definitions", error=str(e), error_type=type(e).__name__)
            raise

    async def get_npc_definition(self, session: AsyncSession, definition_id: int) -> NPCDefinition | None:
        """Get a specific NPC definition by ID."""
        try:
            result = await session.execute(
                text(
                    """
                    SELECT id, name, description, npc_type, sub_zone_id, room_id,
                        required_npc, max_population, spawn_probability,
                        base_stats, behavior_config, ai_integration_stub,
                        created_at, updated_at
                    FROM get_npc_definition(:definition_id)
                    """
                ),
                {"definition_id": definition_id},
            )
            rows = result.mappings().all()
            if not rows:
                logger.warning("NPC definition not found", definition_id=definition_id)
                return None
            definition = _row_to_npc_definition(rows[0])
            logger.info("Retrieved NPC definition", definition_id=definition_id, name=definition.name)
            return definition

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error retrieving NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def get_npc_definition_by_name(self, session: AsyncSession, name: str) -> NPCDefinition | None:
        """Get an NPC definition by name (case-insensitive)."""
        definitions = await self.get_npc_definitions(session)
        name_lower = name.lower()
        for definition in definitions:
            if definition.name.lower() == name_lower:
                return definition
        return None

    async def create_npc_definition(self, session: AsyncSession, data: CreateNPCDefinitionInput) -> NPCDefinition:
        """Create a new NPC definition."""
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
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
                """
                SELECT id, name, description, npc_type, sub_zone_id, room_id,
                    required_npc, max_population, spawn_probability,
                    base_stats, behavior_config, ai_integration_stub,
                    created_at, updated_at
                FROM create_npc_definition(
                    :name, :description, :npc_type, :sub_zone_id, :room_id,
                    :required_npc, :max_population, :spawn_probability,
                    :base_stats, :behavior_config, :ai_integration_stub
                )
                """
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
                """
                SELECT id, name, description, npc_type, sub_zone_id, room_id,
                    required_npc, max_population, spawn_probability,
                    base_stats, behavior_config, ai_integration_stub,
                    created_at, updated_at
                FROM update_npc_definition(
                    :id, :name, :description, :npc_type, :sub_zone_id, :room_id,
                    :required_npc, :max_population, :spawn_probability,
                    :base_stats, :behavior_config, :ai_integration_stub
                )
                """
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

    async def update_npc_definition(
        self,
        session: AsyncSession,
        definition_id: int,
        params: NPCDefinitionUpdateParams,
    ) -> NPCDefinition | None:
        """Update an existing NPC definition."""
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error updating NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def delete_npc_definition(self, session: AsyncSession, definition_id: int) -> bool:
        """Delete an NPC definition."""
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error deleting NPC definition", error=str(e), definition_id=definition_id)
            raise
