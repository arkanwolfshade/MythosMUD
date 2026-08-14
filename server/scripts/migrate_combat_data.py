"""
Combat data migration script.

This script adds default combat data to existing NPC definitions,
including base stats and behavior configuration.
"""

from typing import Protocol, TypedDict, cast

from anyio import run
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.npc import NPCDefinition
from server.npc_database import get_npc_session
from server.schemas.combat import (
    CombatSchemaValidationError,
    add_default_combat_data_to_config,
    add_default_combat_data_to_stats,
    validate_npc_combat_data,
)
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

_COMBAT_STATS_KEYS = ("xp_value", "dexterity", "strength", "constitution")
_COMBAT_CONFIG_KEYS = ("combat_messages", "combat_behavior")
_REQUIRED_VALIDATION_STATS = ("xp_value", "dexterity")
_MIGRATION_ERRORS = (
    CombatSchemaValidationError,
    SQLAlchemyError,
    ValueError,
    TypeError,
    KeyError,
    AttributeError,
)


class MigrationResults(TypedDict):
    """Counts and error strings from combat data migration."""

    total_npcs: int
    updated_npcs: int
    skipped_npcs: int
    error_npcs: int
    errors: list[str]


class ValidationResults(TypedDict):
    """Counts and error strings from combat data validation."""

    total_npcs: int
    valid_npcs: int
    invalid_npcs: int
    validation_errors: list[str]


class RollbackResults(TypedDict):
    """Counts and error strings from combat data rollback."""

    total_npcs: int
    rolled_back_npcs: int
    skipped_npcs: int
    rollback_errors: list[str]


class _MigrationArgs(Protocol):
    """argparse namespace for this script."""

    dry_run: bool
    validate: bool
    rollback: bool


def _npc_has_full_combat_data(stats: dict[str, object], config: dict[str, object]) -> bool:
    has_stats = any(key in stats for key in _COMBAT_STATS_KEYS)
    return has_stats and "combat_messages" in config and "combat_behavior" in config


def _record_npc_error(errors: list[str], npc: NPCDefinition, exc: Exception) -> None:
    error_msg = f"Failed for NPC {npc.name} (ID: {npc.id}): {exc}"
    logger.error("NPC operation error", npc_name=npc.name, npc_id=npc.id, error=str(exc))
    errors.append(error_msg)


async def _migrate_one_npc(npc: NPCDefinition, session: AsyncSession, dry_run: bool, results: MigrationResults) -> None:
    current_stats = npc.get_base_stats()
    current_config = npc.get_behavior_config()
    if _npc_has_full_combat_data(current_stats, current_config):
        logger.debug("NPC already has combat data, skipping", npc_name=npc.name, npc_id=npc.id)
        results["skipped_npcs"] += 1
        return

    updated_stats = add_default_combat_data_to_stats(current_stats)
    updated_config = add_default_combat_data_to_config(current_config)
    if not dry_run:
        npc.set_base_stats(updated_stats)
        npc.set_behavior_config(updated_config)
        validate_npc_combat_data(npc)
        await session.commit()
        logger.info(
            "Updated NPC with combat data",
            npc_name=npc.name,
            npc_id=npc.id,
            added_stats=list(set(updated_stats.keys()) - set(current_stats.keys())),
            added_config=list(set(updated_config.keys()) - set(current_config.keys())),
        )
    results["updated_npcs"] += 1


def _validate_one_npc(npc: NPCDefinition, results: ValidationResults) -> None:
    validate_npc_combat_data(npc)
    stats = npc.get_base_stats()
    config = npc.get_behavior_config()
    has_required = all(key in stats for key in _REQUIRED_VALIDATION_STATS) and "combat_messages" in config
    if has_required:
        results["valid_npcs"] += 1
        logger.debug("NPC combat data validation passed", npc_name=npc.name, npc_id=npc.id)
        return
    error_msg = f"NPC {npc.name} missing required combat data"
    results["validation_errors"].append(error_msg)
    results["invalid_npcs"] += 1
    logger.warning("NPC missing required combat data", npc_name=npc.name, npc_id=npc.id)


def _npc_has_combat_data(stats: dict[str, object], config: dict[str, object]) -> bool:
    return any(key in stats for key in _COMBAT_STATS_KEYS) or any(key in config for key in _COMBAT_CONFIG_KEYS)


def _strip_combat_data_from_npc(
    npc: NPCDefinition,
) -> tuple[dict[str, object], dict[str, object], list[str], list[str]]:
    current_stats = npc.get_base_stats()
    current_config = npc.get_behavior_config()
    updated_stats = {k: v for k, v in current_stats.items() if k not in _COMBAT_STATS_KEYS}
    updated_config = {k: v for k, v in current_config.items() if k not in _COMBAT_CONFIG_KEYS}
    removed_stats = [k for k in _COMBAT_STATS_KEYS if k in current_stats]
    removed_config = [k for k in _COMBAT_CONFIG_KEYS if k in current_config]
    return updated_stats, updated_config, removed_stats, removed_config


async def _rollback_one_npc(npc: NPCDefinition, session: AsyncSession, results: RollbackResults) -> None:
    current_stats = npc.get_base_stats()
    current_config = npc.get_behavior_config()
    if not _npc_has_combat_data(current_stats, current_config):
        logger.debug("NPC has no combat data to rollback", npc_name=npc.name, npc_id=npc.id)
        results["skipped_npcs"] += 1
        return

    updated_stats, updated_config, removed_stats, removed_config = _strip_combat_data_from_npc(npc)
    npc.set_base_stats(updated_stats)
    npc.set_behavior_config(updated_config)
    await session.commit()
    logger.info(
        "Rolled back NPC combat data",
        npc_name=npc.name,
        npc_id=npc.id,
        removed_stats=removed_stats,
        removed_config=removed_config,
    )
    results["rolled_back_npcs"] += 1


async def migrate_npc_combat_data(session: AsyncSession, dry_run: bool = False) -> MigrationResults:
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

    # AI Agent: Explicit type annotation to help mypy understand dict structure
    migration_results: MigrationResults = {
        "total_npcs": len(npcs),
        "updated_npcs": 0,
        "skipped_npcs": 0,
        "error_npcs": 0,
        "errors": [],
    }

    for npc in npcs:
        try:
            await _migrate_one_npc(npc, session, dry_run, migration_results)
        except _MIGRATION_ERRORS as exc:
            _record_npc_error(migration_results["errors"], npc, exc)
            migration_results["error_npcs"] += 1

    logger.info("Combat data migration completed", **migration_results)
    return migration_results


async def validate_migration_results(session: AsyncSession) -> ValidationResults:
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

    # AI Agent: Explicit type annotation to help mypy understand dict structure
    validation_results: ValidationResults = {
        "total_npcs": len(npcs),
        "valid_npcs": 0,
        "invalid_npcs": 0,
        "validation_errors": [],
    }

    for npc in npcs:
        try:
            _validate_one_npc(npc, validation_results)
        except _MIGRATION_ERRORS as exc:
            validation_results["validation_errors"].append(f"NPC {npc.name} validation failed: {exc}")
            validation_results["invalid_npcs"] += 1
            logger.error("NPC validation error", npc_name=npc.name, npc_id=npc.id, error=str(exc))

    logger.info("Combat data migration validation completed", **validation_results)
    return validation_results


async def rollback_migration(session: AsyncSession) -> RollbackResults:
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

    # AI Agent: Explicit type annotation to help mypy understand dict structure
    rollback_results: RollbackResults = {
        "total_npcs": len(npcs),
        "rolled_back_npcs": 0,
        "skipped_npcs": 0,
        "rollback_errors": [],
    }

    for npc in npcs:
        try:
            await _rollback_one_npc(npc, session, rollback_results)
        except _MIGRATION_ERRORS as exc:
            _record_npc_error(rollback_results["rollback_errors"], npc, exc)

    logger.info("Combat data migration rollback completed", **rollback_results)
    return rollback_results


async def main() -> None:
    """Main migration function."""
    import argparse

    parser = argparse.ArgumentParser(description="Combat data migration script")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without making changes",
    )
    parser.add_argument("--validate", action="store_true", help="Validate migration results")
    parser.add_argument("--rollback", action="store_true", help="Rollback migration")
    args = cast(_MigrationArgs, cast(object, parser.parse_args()))

    async for session in get_npc_session():
        if args.rollback:
            print(f"Rollback completed: {await rollback_migration(session)}")
        elif args.validate:
            print(f"Validation completed: {await validate_migration_results(session)}")
        else:
            results = await migrate_npc_combat_data(session, dry_run=args.dry_run)
            print(f"Migration completed: {results}")

            if not args.dry_run:
                # Validate after migration
                validation_results = await validate_migration_results(session)
                print(f"Validation results: {validation_results}")
        break  # Only process one session


if __name__ == "__main__":
    run(main)
