"""
Combat data migration script.

This script adds default combat data to existing NPC definitions,
including base stats and behavior configuration.
"""

import asyncio
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.database import get_async_session
from server.logging_config import get_logger
from server.models.npc import NPCDefinition
from server.schemas.combat_schema import (
    add_default_combat_data_to_config,
    add_default_combat_data_to_stats,
    validate_npc_combat_data,
)

logger = get_logger(__name__)


async def migrate_npc_combat_data(session: AsyncSession, dry_run: bool = False) -> dict[str, Any]:
    """
    Migrate combat data for all NPC definitions.

    Args:
        session: Database session
        dry_run: If True, don't actually update the database

    Returns:
        Migration results summary
    """
    logger.info("Starting combat data migration", dry_run=dry_run)

    # Get all NPC definitions
    result = await session.execute(select(NPCDefinition))
    npcs = result.scalars().all()

    migration_results = {"total_npcs": len(npcs), "updated_npcs": 0, "skipped_npcs": 0, "error_npcs": 0, "errors": []}

    for npc in npcs:
        try:
            # Get current data
            current_stats = npc.get_base_stats()
            current_config = npc.get_behavior_config()

            # Check if combat data already exists
            has_combat_stats = any(
                key in current_stats for key in ["xp_value", "dexterity", "strength", "constitution"]
            )
            has_combat_messages = "combat_messages" in current_config
            has_combat_behavior = "combat_behavior" in current_config

            if has_combat_stats and has_combat_messages and has_combat_behavior:
                logger.debug("NPC already has combat data, skipping", npc_name=npc.name, npc_id=npc.id)
                migration_results["skipped_npcs"] += 1
                continue

            # Add default combat data
            updated_stats = add_default_combat_data_to_stats(current_stats)
            updated_config = add_default_combat_data_to_config(current_config)

            if not dry_run:
                # Update the NPC definition
                npc.set_base_stats(updated_stats)
                npc.set_behavior_config(updated_config)

                # Validate the updated data
                validate_npc_combat_data(npc)

                await session.commit()

                logger.info(
                    "Updated NPC with combat data",
                    npc_name=npc.name,
                    npc_id=npc.id,
                    added_stats=list(set(updated_stats.keys()) - set(current_stats.keys())),
                    added_config=list(set(updated_config.keys()) - set(current_config.keys())),
                )

            migration_results["updated_npcs"] += 1

        except Exception as e:
            error_msg = f"Failed to migrate NPC {npc.name} (ID: {npc.id}): {str(e)}"
            logger.error("NPC migration error", npc_name=npc.name, npc_id=npc.id, error=str(e))
            migration_results["errors"].append(error_msg)
            migration_results["error_npcs"] += 1

    logger.info("Combat data migration completed", **migration_results)
    return migration_results


async def validate_migration_results(session: AsyncSession) -> dict[str, Any]:
    """
    Validate that migration was successful.

    Args:
        session: Database session

    Returns:
        Validation results
    """
    logger.info("Validating combat data migration results")

    # Get all NPC definitions
    result = await session.execute(select(NPCDefinition))
    npcs = result.scalars().all()

    validation_results = {"total_npcs": len(npcs), "valid_npcs": 0, "invalid_npcs": 0, "validation_errors": []}

    for npc in npcs:
        try:
            # Validate combat data
            validate_npc_combat_data(npc)

            # Check that required combat data is present
            stats = npc.get_base_stats()
            config = npc.get_behavior_config()

            has_required_stats = all(key in stats for key in ["xp_value", "dexterity"])
            has_required_messages = "combat_messages" in config

            if has_required_stats and has_required_messages:
                validation_results["valid_npcs"] += 1
                logger.debug("NPC combat data validation passed", npc_name=npc.name, npc_id=npc.id)
            else:
                error_msg = f"NPC {npc.name} missing required combat data"
                validation_results["validation_errors"].append(error_msg)
                validation_results["invalid_npcs"] += 1
                logger.warning("NPC missing required combat data", npc_name=npc.name, npc_id=npc.id)

        except Exception as e:
            error_msg = f"NPC {npc.name} validation failed: {str(e)}"
            validation_results["validation_errors"].append(error_msg)
            validation_results["invalid_npcs"] += 1
            logger.error("NPC validation error", npc_name=npc.name, npc_id=npc.id, error=str(e))

    logger.info("Combat data migration validation completed", **validation_results)
    return validation_results


async def rollback_migration(session: AsyncSession) -> dict[str, Any]:
    """
    Rollback combat data migration by removing combat fields.

    Args:
        session: Database session

    Returns:
        Rollback results
    """
    logger.info("Starting combat data migration rollback")

    # Get all NPC definitions
    result = await session.execute(select(NPCDefinition))
    npcs = result.scalars().all()

    rollback_results = {"total_npcs": len(npcs), "rolled_back_npcs": 0, "skipped_npcs": 0, "rollback_errors": []}

    combat_stats_keys = ["xp_value", "dexterity", "strength", "constitution"]
    combat_config_keys = ["combat_messages", "combat_behavior"]

    for npc in npcs:
        try:
            # Get current data
            current_stats = npc.get_base_stats()
            current_config = npc.get_behavior_config()

            # Check if combat data exists
            has_combat_stats = any(key in current_stats for key in combat_stats_keys)
            has_combat_config = any(key in current_config for key in combat_config_keys)

            if not has_combat_stats and not has_combat_config:
                logger.debug("NPC has no combat data to rollback", npc_name=npc.name, npc_id=npc.id)
                rollback_results["skipped_npcs"] += 1
                continue

            # Remove combat data
            updated_stats = {k: v for k, v in current_stats.items() if k not in combat_stats_keys}
            updated_config = {k: v for k, v in current_config.items() if k not in combat_config_keys}

            # Update the NPC definition
            npc.set_base_stats(updated_stats)
            npc.set_behavior_config(updated_config)

            await session.commit()

            logger.info(
                "Rolled back NPC combat data",
                npc_name=npc.name,
                npc_id=npc.id,
                removed_stats=[k for k in combat_stats_keys if k in current_stats],
                removed_config=[k for k in combat_config_keys if k in current_config],
            )

            rollback_results["rolled_back_npcs"] += 1

        except Exception as e:
            error_msg = f"Failed to rollback NPC {npc.name} (ID: {npc.id}): {str(e)}"
            logger.error("NPC rollback error", npc_name=npc.name, npc_id=npc.id, error=str(e))
            rollback_results["rollback_errors"].append(error_msg)

    logger.info("Combat data migration rollback completed", **rollback_results)
    return rollback_results


async def main():
    """Main migration function."""
    import argparse

    parser = argparse.ArgumentParser(description="Combat data migration script")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making changes")
    parser.add_argument("--validate", action="store_true", help="Validate migration results")
    parser.add_argument("--rollback", action="store_true", help="Rollback migration")
    args = parser.parse_args()

    async with get_async_session() as session:
        if args.rollback:
            results = await rollback_migration(session)
            print(f"Rollback completed: {results}")
        elif args.validate:
            results = await validate_migration_results(session)
            print(f"Validation completed: {results}")
        else:
            results = await migrate_npc_combat_data(session, dry_run=args.dry_run)
            print(f"Migration completed: {results}")

            if not args.dry_run:
                # Validate after migration
                validation_results = await validate_migration_results(session)
                print(f"Validation results: {validation_results}")


if __name__ == "__main__":
    asyncio.run(main())
