"""
Alias management commands for MythosMUD.

This module contains handlers for alias-related commands.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_alias_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the alias command for creating and viewing aliases.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Command result
    """
    logger.debug("Processing alias command", player_name=player_name, args=args)

    if not args:
        logger.warning("Alias command with no arguments", player_name=player_name)
        return {"result": "Usage: alias <name> [command] or alias <name> to view"}

    alias_name = args[0].lower()

    # View existing alias
    if len(args) == 1:
        logger.debug("Viewing alias", player_name=player_name, alias_name=alias_name)
        alias = alias_storage.get_alias(alias_name)
        if alias:
            logger.debug("Alias found", player_name=player_name, alias_name=alias_name, command=alias.command)
            return {"result": f"Alias '{alias_name}' = '{alias.command}'"}
        else:
            logger.debug("Alias not found", player_name=player_name, alias_name=alias_name)
            return {"result": f"No alias found for '{alias_name}'"}

    # Create/update alias
    command = " ".join(args[1:])
    logger.debug("Creating/updating alias", player_name=player_name, alias_name=alias_name, command=command)

    # Validate alias name
    if not alias_name or len(alias_name) > 20:
        logger.warning("Invalid alias name", player_name=player_name, alias_name=alias_name)
        return {"result": "Alias name must be 1-20 characters long."}

    # Validate command
    if not command or len(command) > 200:
        logger.warning("Invalid alias command", player_name=player_name, alias_name=alias_name, command=command)
        return {"result": "Alias command must be 1-200 characters long."}

    try:
        # Check for circular references
        if alias_name in command.lower():
            return {"result": "Alias cannot reference itself."}

        # Create the alias
        alias_storage.create_alias(alias_name, command)
        logger.info("Alias created", player_name=player_name, alias_name=alias_name, command=command)
        return {"result": f"Alias '{alias_name}' created successfully."}

    except Exception as e:
        logger.error(
            "Failed to create alias", player_name=player_name, alias_name=alias_name, command=command, error=str(e)
        )
        return {"result": f"Failed to create alias: {str(e)}"}


async def handle_aliases_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the aliases command for listing all aliases.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Aliases command result
    """
    logger.debug("Listing aliases", player_name=player_name)

    try:
        aliases = alias_storage.list_aliases()
        if not aliases:
            logger.debug("No aliases found", player_name=player_name)
            return {"result": "You have no aliases defined."}

        # Format alias list
        alias_lines = []
        for alias in aliases:
            alias_lines.append(f"{alias.name}: {alias.command}")

        result = "Your aliases:\n" + "\n".join(alias_lines)
        logger.debug("Aliases listed", player_name=player_name, alias_count=len(aliases))
        return {"result": result}

    except Exception as e:
        logger.error("Failed to list aliases", player_name=player_name, error=str(e))
        return {"result": f"Failed to list aliases: {str(e)}"}


async def handle_unalias_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the unalias command for removing aliases.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unalias command result
    """
    logger.debug("Processing unalias command", player_name=player_name, args=args)

    if not args:
        logger.warning("Unalias command with no arguments", player_name=player_name)
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0].lower()
    logger.debug("Removing alias", player_name=player_name, alias_name=alias_name)

    try:
        # Check if alias exists
        existing_alias = alias_storage.get_alias(alias_name)
        if not existing_alias:
            logger.debug("Alias not found for removal", player_name=player_name, alias_name=alias_name)
            return {"result": f"No alias found for '{alias_name}'"}

        # Remove the alias
        alias_storage.delete_alias(alias_name)
        logger.info("Alias removed", player_name=player_name, alias_name=alias_name)
        return {"result": f"Alias '{alias_name}' removed successfully."}

    except Exception as e:
        logger.error("Failed to remove alias", player_name=player_name, alias_name=alias_name, error=str(e))
        return {"result": f"Failed to remove alias: {str(e)}"}
