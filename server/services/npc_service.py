"""
NPC management service for MythosMUD.

This module provides comprehensive NPC management including CRUD operations
for NPC definitions, spawn rules, relationships, and instance management.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: NPC service requires many parameters and intermediate variables for complex NPC management logic. NPC service requires extensive NPC management operations for comprehensive NPC system management.

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import delete, func, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError
from ..models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("services.npc_service")


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
            result = await session.execute(
                select(NPCDefinition)
                # .options(selectinload(NPCDefinition.spawn_rules))  # Disabled - spawn_rules relationship removed
                .order_by(NPCDefinition.name, NPCDefinition.sub_zone_id)
            )
            definitions = result.scalars().all()

            logger.info("Retrieved NPC definitions")
            return list(definitions)

        except SQLAlchemyError as e:
            logger.error("Database error retrieving NPC definitions", error=str(e), error_type=type(e).__name__)
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
                select(NPCDefinition)
                # .options(selectinload(NPCDefinition.spawn_rules))  # Disabled - spawn_rules relationship removed
                .where(NPCDefinition.id == definition_id)
            )
            definition = result.scalar_one_or_none()

            if definition:
                logger.info("Retrieved NPC definition", definition_id=definition_id, name=definition.name)
            else:
                logger.warning("NPC definition not found", definition_id=definition_id)

            return definition

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition retrieval errors unpredictable, must re-raise
            logger.error("Error retrieving NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def create_npc_definition(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: NPC definition creation requires many parameters for complete NPC setup
        self,
        session: AsyncSession,
        name: str,
        description: str | None,
        npc_type: str,
        sub_zone_id: str,
        room_id: str | None = None,
        required_npc: bool = False,
        max_population: int = 1,
        spawn_probability: float = 1.0,
        base_stats: dict[str, Any] | None = None,
        behavior_config: dict[str, Any] | None = None,
        ai_integration_stub: dict[str, Any] | None = None,
    ) -> NPCDefinition:
        """
        Create a new NPC definition.

        Args:
            session: Database session
            name: NPC name
            description: NPC description
            npc_type: NPC type (shopkeeper, quest_giver, passive_mob, aggressive_mob)
            sub_zone_id: Sub-zone ID where NPC can spawn
            room_id: Specific room ID (optional)
            required_npc: Whether NPC is required to spawn
            max_population: Maximum population for this NPC type
            spawn_probability: Spawn probability (0.0 to 1.0)
            base_stats: Base statistics dictionary
            behavior_config: Behavior configuration dictionary
            ai_integration_stub: AI integration configuration dictionary

        Returns:
            Created NPC definition

        Raises:
            ValueError: If validation fails
        """
        try:
            # Validate NPC type
            if npc_type not in [t.value for t in NPCDefinitionType]:
                raise ValueError(f"Invalid NPC type: {npc_type}")

            # Validate spawn probability
            if not 0.0 <= spawn_probability <= 1.0:
                raise ValueError(f"Spawn probability must be between 0.0 and 1.0, got: {spawn_probability}")

            # Validate max population
            if max_population < 1:
                raise ValueError(f"Max population must be at least 1, got: {max_population}")

            # Create NPC definition
            definition = NPCDefinition(
                name=name,
                description=description,
                npc_type=npc_type,
                sub_zone_id=sub_zone_id,
                room_id=room_id,
                required_npc=required_npc,
                max_population=max_population,
                spawn_probability=spawn_probability,
                base_stats=json.dumps(base_stats or {}),
                behavior_config=json.dumps(behavior_config or {}),
                ai_integration_stub=json.dumps(ai_integration_stub or {}),
            )

            session.add(definition)
            await session.flush()  # Get the ID
            await session.refresh(definition)

            logger.info(
                "Created NPC definition",
                definition_id=definition.id,
                name=name,
                npc_type=npc_type,
                sub_zone_id=sub_zone_id,
            )

            return definition

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC definition creation errors unpredictable, must re-raise
            logger.error("Error creating NPC definition", error=str(e), name=name, npc_type=npc_type)
            raise

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

    def _build_npc_update_data(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: NPC update data building requires many parameters for complete update context
        self,
        name: str | None,
        description: str | None,
        npc_type: str | None,
        sub_zone_id: str | None,
        room_id: str | None,
        required_npc: bool | None,
        max_population: int | None,
        spawn_probability: float | None,
        base_stats: dict[str, Any] | None,
        behavior_config: dict[str, Any] | None,
        ai_integration_stub: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """Build update data dictionary from provided parameters."""
        update_data: dict[str, Any] = {}
        self._add_simple_field(update_data, "name", name)
        self._add_simple_field(update_data, "description", description)
        self._add_simple_field(update_data, "npc_type", npc_type)
        self._add_simple_field(update_data, "sub_zone_id", sub_zone_id)
        self._add_simple_field(update_data, "room_id", room_id)
        self._add_simple_field(update_data, "required_npc", required_npc)
        self._add_simple_field(update_data, "max_population", max_population)
        self._add_simple_field(update_data, "spawn_probability", spawn_probability)
        self._add_json_field(update_data, "base_stats", base_stats)
        self._add_json_field(update_data, "behavior_config", behavior_config)
        self._add_json_field(update_data, "ai_integration_stub", ai_integration_stub)
        update_data["updated_at"] = datetime.now(UTC).replace(tzinfo=None)
        return update_data

    async def _execute_npc_update(
        self, session: AsyncSession, definition_id: int, update_data: dict[str, Any], definition: NPCDefinition
    ) -> NPCDefinition:
        """Execute the database update and refresh the definition."""
        await session.execute(update(NPCDefinition).where(NPCDefinition.id == definition_id).values(**update_data))
        await session.refresh(definition)
        logger.info("Updated NPC definition", definition_id=definition_id, updated_fields=list(update_data.keys()))
        return definition

    async def update_npc_definition(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: NPC definition update requires many parameters and intermediate variables for complex update logic
        self,
        session: AsyncSession,
        definition_id: int,
        name: str | None = None,
        description: str | None = None,
        npc_type: str | None = None,
        sub_zone_id: str | None = None,
        room_id: str | None = None,
        required_npc: bool | None = None,
        max_population: int | None = None,
        spawn_probability: float | None = None,
        base_stats: dict[str, Any] | None = None,
        behavior_config: dict[str, Any] | None = None,
        ai_integration_stub: dict[str, Any] | None = None,
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

            self._validate_npc_update_params(npc_type, spawn_probability, max_population)

            update_data = self._build_npc_update_data(
                name,
                description,
                npc_type,
                sub_zone_id,
                room_id,
                required_npc,
                max_population,
                spawn_probability,
                base_stats,
                behavior_config,
                ai_integration_stub,
            )

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
            # Check if definition exists
            definition = await self.get_npc_definition(session, definition_id)
            if not definition:
                return False

            # Delete the definition (cascade will handle related records)
            await session.execute(delete(NPCDefinition).where(NPCDefinition.id == definition_id))

            logger.info("Deleted NPC definition", definition_id=definition_id, name=definition.name)

            return True

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
            result = await session.execute(
                select(NPCSpawnRule).order_by(NPCSpawnRule.sub_zone_id, NPCSpawnRule.min_population)
            )
            rules = result.scalars().all()

            logger.info("Retrieved NPC spawn rules", count=len(rules))
            return list(rules)

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
            result = await session.execute(select(NPCSpawnRule).where(NPCSpawnRule.id == rule_id))
            rule = result.scalar_one_or_none()

            if rule:
                logger.info("Retrieved NPC spawn rule", rule_id=rule_id, npc_definition_id=rule.npc_definition_id)
            else:
                logger.warning("NPC spawn rule not found", rule_id=rule_id)

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
            # Validate NPC definition exists
            definition = await self.get_npc_definition(session, npc_definition_id)
            if not definition:
                raise ValueError(f"NPC definition not found: {npc_definition_id}")

            # Validate population counts
            if min_population < 0:
                raise ValueError(f"Min population must be non-negative, got: {min_population}")
            if max_population < min_population:
                raise ValueError(f"Max population must be >= min population, got: {max_population} < {min_population}")

            # Create spawn rule
            rule = NPCSpawnRule(
                npc_definition_id=npc_definition_id,
                sub_zone_id=sub_zone_id,
                min_population=min_population,
                max_population=max_population,
                spawn_conditions=json.dumps(spawn_conditions or {}),
            )

            session.add(rule)
            await session.flush()  # Get the ID
            await session.refresh(rule)

            logger.info(
                "Created NPC spawn rule",
                rule_id=rule.id,
                npc_definition_id=npc_definition_id,
                sub_zone_id=sub_zone_id,
            )

            return rule

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn rule creation errors unpredictable, must re-raise
            logger.error("Error creating NPC spawn rule", error=str(e), npc_definition_id=npc_definition_id)
            raise

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
            # Check if rule exists
            rule = await self.get_spawn_rule(session, rule_id)
            if not rule:
                return False

            # Delete the rule
            await session.execute(delete(NPCSpawnRule).where(NPCSpawnRule.id == rule_id))

            logger.info("Deleted NPC spawn rule", rule_id=rule_id, npc_definition_id=rule.npc_definition_id)

            return True

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
                select(NPCDefinition)
                # .options(selectinload(NPCDefinition.spawn_rules))  # Disabled - spawn_rules relationship removed
                .where(NPCDefinition.npc_type == npc_type)
                .order_by(NPCDefinition.name, NPCDefinition.sub_zone_id)
            )
            definitions = result.scalars().all()

            logger.info("Retrieved NPC definitions by type", npc_type=npc_type, count=len(definitions))
            return list(definitions)

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
                select(NPCDefinition)
                # .options(selectinload(NPCDefinition.spawn_rules))  # Disabled - spawn_rules relationship removed
                .where(NPCDefinition.sub_zone_id == sub_zone_id)
                .order_by(NPCDefinition.name)
            )
            definitions = result.scalars().all()

            logger.info("Retrieved NPC definitions by sub-zone", sub_zone_id=sub_zone_id, count=len(definitions))
            return list(definitions)

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
            # Count NPC definitions by type
            definitions_result = await session.execute(
                select(NPCDefinition.npc_type, func.count(NPCDefinition.id)).group_by(NPCDefinition.npc_type)  # pylint: disable=not-callable  # Reason: SQLAlchemy func is callable at runtime, pylint cannot detect this statically
            )
            definitions_by_type: dict[str, int] = dict(definitions_result.all())  # type: ignore[arg-type]  # Reason: SQLAlchemy result.all() returns Row tuples, dict() constructor handles the conversion correctly at runtime

            # Count total definitions
            total_definitions_result = await session.execute(select(func.count(NPCDefinition.id)))  # pylint: disable=not-callable  # Reason: SQLAlchemy func is callable at runtime, pylint cannot detect this statically
            total_definitions = total_definitions_result.scalar()

            # Count spawn rules
            spawn_rules_result = await session.execute(select(func.count(NPCSpawnRule.id)))  # pylint: disable=not-callable  # Reason: SQLAlchemy func is callable at runtime, pylint cannot detect this statically
            total_spawn_rules = spawn_rules_result.scalar()

            stats = {
                "total_npc_definitions": total_definitions,
                "npc_definitions_by_type": definitions_by_type,
                "total_spawn_rules": total_spawn_rules,
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
