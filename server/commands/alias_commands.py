"""
Alias management commands for MythosMUD.

This module contains handlers for alias-related commands.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger

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
    logger.debug(f"Processing alias command for {player_name} with args: {args}")

    if not args:
        logger.warning(f"Alias command with no arguments for {player_name}")
        return {"result": "Usage: alias <name> [command] or alias <name> to view"}

    alias_name = args[0].lower()

    # View existing alias
    if len(args) == 1:
        logger.debug(f"Viewing alias for {player_name}: {alias_name}")
        alias = alias_storage.get_alias(alias_name)
        if alias:
            logger.debug(f"Alias found for {player_name}: {alias_name} = {alias.command}")
            return {"result": f"Alias '{alias_name}' = '{alias.command}'"}
        else:
            logger.debug(f"Alias not found for {player_name}: {alias_name}")
            return {"result": f"No alias found for '{alias_name}'"}

    # Create/update alias
    command = " ".join(args[1:])
    logger.debug(f"Creating/updating alias for {player_name}: {alias_name} = {command}")

    # Validate alias name
    if not alias_name or len(alias_name) > 20:
        logger.warning(f"Invalid alias name for {player_name}: {alias_name}")
        return {"result": "Alias name must be 1-20 characters long."}

    # Validate command
    if not command or len(command) > 200:
        logger.warning(f"Invalid alias command for {player_name}: {alias_name} = {command}")
        return {"result": "Alias command must be 1-200 characters long."}

    try:
        # Check for circular references
        if alias_name in command.lower():
            return {"result": "Alias cannot reference itself."}

        # Create the alias
        alias_storage.create_alias(alias_name, command)
        logger.info(f"Alias created for {player_name}: {alias_name} = {command}")
        return {"result": f"Alias '{alias_name}' created successfully."}

    except Exception as e:
        logger.error(f"Failed to create alias for {player_name}: {alias_name} = {command}, error: {str(e)}")
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
    logger.debug(f"Listing aliases for {player_name}")

    try:
        aliases = alias_storage.list_aliases()
        if not aliases:
            logger.debug(f"No aliases found for {player_name}")
            return {"result": "You have no aliases defined."}

        # Format alias list
        alias_lines = []
        for alias in aliases:
            alias_lines.append(f"{alias.name}: {alias.command}")

        result = "Your aliases:\n" + "\n".join(alias_lines)
        logger.debug(f"Aliases listed for {player_name}, alias_count: {len(aliases)}")
        return {"result": result}

    except Exception as e:
        logger.error(f"Failed to list aliases for {player_name}: {str(e)}")
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
    logger.debug(f"Processing unalias command for {player_name} with args: {args}")

    if not args:
        logger.warning(f"Unalias command with no arguments for {player_name}")
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0].lower()
    logger.debug(f"Removing alias for {player_name}: {alias_name}")

    try:
        # Check if alias exists
        existing_alias = alias_storage.get_alias(alias_name)
        if not existing_alias:
            logger.debug(f"Alias not found for removal for {player_name}: {alias_name}")
            return {"result": f"No alias found for '{alias_name}'"}

        # Remove the alias
        alias_storage.delete_alias(alias_name)
        logger.info(f"Alias removed for {player_name}: {alias_name}")
        return {"result": f"Alias '{alias_name}' removed successfully."}

    except Exception as e:
        logger.error(f"Failed to remove alias for {player_name}: {alias_name}, error: {str(e)}")
        return {"result": f"Failed to remove alias: {str(e)}"}
