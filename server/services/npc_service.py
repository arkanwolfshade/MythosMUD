"""
NPC management service for MythosMUD.

This module provides comprehensive NPC management including CRUD operations
for NPC definitions, spawn rules, relationships, and instance management.
"""

import json
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..logging_config import get_logger
from ..models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule

logger = get_logger("services.npc_service")


class NPCService:
    """
    Comprehensive NPC management service.

    Handles CRUD operations for NPC definitions, spawn rules, relationships,
    and provides integration with the NPC subsystem.
    """

    def __init__(self):
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

            logger.info("Retrieved NPC definitions", context={"count": len(definitions)})
            return list(definitions)

        except Exception as e:
            logger.error("Error retrieving NPC definitions", context={"error": str(e)})
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
                logger.info(
                    "Retrieved NPC definition", context={"definition_id": definition_id, "name": definition.name}
                )
            else:
                logger.warning("NPC definition not found", definition_id=definition_id)

            return definition

        except Exception as e:
            logger.error("Error retrieving NPC definition", error=str(e), definition_id=definition_id)
            raise

    async def create_npc_definition(
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

        except Exception as e:
            logger.error("Error creating NPC definition", error=str(e), name=name, npc_type=npc_type)
            raise

    async def update_npc_definition(
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
            # Get existing definition
            definition = await self.get_npc_definition(session, definition_id)
            if not definition:
                return None

            # Validate NPC type if provided
            if npc_type is not None and npc_type not in [t.value for t in NPCDefinitionType]:
                raise ValueError(f"Invalid NPC type: {npc_type}")

            # Validate spawn probability if provided
            if spawn_probability is not None and not 0.0 <= spawn_probability <= 1.0:
                raise ValueError(f"Spawn probability must be between 0.0 and 1.0, got: {spawn_probability}")

            # Validate max population if provided
            if max_population is not None and max_population < 1:
                raise ValueError(f"Max population must be at least 1, got: {max_population}")

            # Update fields
            update_data = {}
            if name is not None:
                update_data["name"] = name
            if description is not None:
                update_data["description"] = description
            if npc_type is not None:
                update_data["npc_type"] = npc_type
            if sub_zone_id is not None:
                update_data["sub_zone_id"] = sub_zone_id
            if room_id is not None:
                update_data["room_id"] = room_id
            if required_npc is not None:
                update_data["required_npc"] = required_npc
            if max_population is not None:
                update_data["max_population"] = max_population
            if spawn_probability is not None:
                update_data["spawn_probability"] = spawn_probability
            if base_stats is not None:
                update_data["base_stats"] = json.dumps(base_stats)
            if behavior_config is not None:
                update_data["behavior_config"] = json.dumps(behavior_config)
            if ai_integration_stub is not None:
                update_data["ai_integration_stub"] = json.dumps(ai_integration_stub)

            # Update timestamp
            update_data["updated_at"] = datetime.now(UTC).replace(tzinfo=None)

            # Perform update
            await session.execute(update(NPCDefinition).where(NPCDefinition.id == definition_id).values(**update_data))

            # Refresh the definition
            await session.refresh(definition)

            logger.info("Updated NPC definition", definition_id=definition_id, updated_fields=list(update_data.keys()))

            return definition

        except Exception as e:
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

            logger.info("Deleted NPC definition", context={"definition_id": definition_id, "name": definition.name})

            return True

        except Exception as e:
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
                select(NPCSpawnRule).order_by(NPCSpawnRule.sub_zone_id, NPCSpawnRule.min_players)
            )
            rules = result.scalars().all()

            logger.info("Retrieved NPC spawn rules", count=len(rules))
            return list(rules)

        except Exception as e:
            logger.error("Error retrieving NPC spawn rules", context={"error": str(e)})
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

        except Exception as e:
            logger.error("Error retrieving NPC spawn rule", error=str(e), rule_id=rule_id)
            raise

    async def create_spawn_rule(
        self,
        session: AsyncSession,
        npc_definition_id: int,
        sub_zone_id: str,
        min_players: int = 0,
        max_players: int = 999,
        spawn_conditions: dict[str, Any] | None = None,
    ) -> NPCSpawnRule:
        """
        Create a new NPC spawn rule.

        Args:
            session: Database session
            npc_definition_id: NPC definition ID
            sub_zone_id: Sub-zone ID
            min_players: Minimum player count
            max_players: Maximum player count
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

            # Validate player counts
            if min_players < 0:
                raise ValueError(f"Min players must be non-negative, got: {min_players}")
            if max_players < min_players:
                raise ValueError(f"Max players must be >= min players, got: {max_players} < {min_players}")

            # Create spawn rule
            rule = NPCSpawnRule(
                npc_definition_id=npc_definition_id,
                sub_zone_id=sub_zone_id,
                min_players=min_players,
                max_players=max_players,
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

        except Exception as e:
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

        except Exception as e:
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

            logger.info("Retrieved NPC definitions by type", npc_type=npc_type, context={"count": len(definitions)})
            return list(definitions)

        except Exception as e:
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

            logger.info(
                "Retrieved NPC definitions by sub-zone", sub_zone_id=sub_zone_id, context={"count": len(definitions)}
            )
            return list(definitions)

        except Exception as e:
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
                select(NPCDefinition.npc_type, session.query(NPCDefinition.id).count()).group_by(NPCDefinition.npc_type)
            )
            definitions_by_type = dict(definitions_result.all())

            # Count total definitions
            total_definitions_result = await session.execute(select(session.query(NPCDefinition.id).count()))
            total_definitions = total_definitions_result.scalar()

            # Count spawn rules
            spawn_rules_result = await session.execute(select(session.query(NPCSpawnRule.id).count()))
            total_spawn_rules = spawn_rules_result.scalar()

            stats = {
                "total_npc_definitions": total_definitions,
                "npc_definitions_by_type": definitions_by_type,
                "total_spawn_rules": total_spawn_rules,
                "generated_at": datetime.now(UTC).isoformat(),
            }

            logger.info("Generated NPC system statistics", **stats)
            return stats

        except Exception as e:
            logger.error("Error generating NPC system statistics", context={"error": str(e)})
            raise


# Global NPC service instance
npc_service = NPCService()
