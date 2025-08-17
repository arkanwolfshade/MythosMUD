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
    logger.debug("Processing alias command", player=player_name, args=args)

    if not args:
        logger.warning("Alias command with no arguments", player=player_name)
        return {"result": "Usage: alias <name> <command> or alias <name> to view"}

    alias_name = args[0]

    # If only one argument, show the alias details
    if len(args) == 1:
        logger.debug("Viewing alias", player=player_name, alias_name=alias_name)
        alias = alias_storage.get_alias(player_name, alias_name)
        if alias:
            logger.debug("Alias found", player=player_name, alias_name=alias_name, command=alias.command)
            return {"result": f"Alias '{alias_name}' -> '{alias.command}'"}
        else:
            logger.debug("Alias not found", player=player_name, alias_name=alias_name)
            return {"result": f"No alias found with name '{alias_name}'"}

    # Create or update alias
    command = " ".join(args[1:])
    logger.debug("Creating/updating alias", player=player_name, alias_name=alias_name, command=command)

    # Validate alias name
    if not alias_storage.validate_alias_name(alias_name):
        logger.warning("Invalid alias name", player=player_name, alias_name=alias_name)
        return {
            "result": "Invalid alias name. Must start with a letter and contain only alphanumeric characters and underscores."
        }

    # Validate command
    if not alias_storage.validate_alias_command(command):
        logger.warning("Invalid alias command", player=player_name, alias_name=alias_name, command=command)
        return {"result": "Invalid command. Cannot alias reserved commands or empty commands."}

    # Check alias count limit
    if alias_storage.get_alias_count(player_name) >= 50:
        existing_alias = alias_storage.get_alias(player_name, alias_name)
        if not existing_alias:
            logger.warning(
                "Alias limit reached", player=player_name, alias_count=alias_storage.get_alias_count(player_name)
            )
            return {"result": "Maximum number of aliases (50) reached. Remove some aliases before creating new ones."}

    # Create the alias
    alias = alias_storage.create_alias(player_name, alias_name, command)
    if alias:
        logger.info("Alias created", player=player_name, alias_name=alias_name, command=command)
        return {"result": f"Alias '{alias_name}' created: '{command}'"}
    else:
        logger.error("Failed to create alias", player=player_name, alias_name=alias_name, command=command)
        return {"result": "Failed to create alias. Please check your input."}


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
        dict: Command result
    """
    logger.debug("Listing aliases", player=player_name)
    aliases = alias_storage.get_player_aliases(player_name)

    if not aliases:
        logger.debug("No aliases found", player=player_name)
        return {"result": "You have no aliases defined."}

    # Format alias list
    alias_list = []
    for alias in aliases:
        alias_list.append(f"  {alias.name} -> {alias.command}")

    result = f"You have {len(aliases)} alias(es):\n" + "\n".join(alias_list)
    logger.debug("Aliases listed", player=player_name, alias_count=len(aliases))
    return {"result": result}


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
        dict: Command result
    """
    logger.debug("Processing unalias command", player=player_name, args=args)

    if not args:
        logger.warning("Unalias command with no arguments", player=player_name)
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0]
    logger.debug("Removing alias", player=player_name, alias_name=alias_name)

    # Check if alias exists
    existing_alias = alias_storage.get_alias(player_name, alias_name)
    if not existing_alias:
        logger.debug("Alias not found for removal", player=player_name, alias_name=alias_name)
        return {"result": f"No alias found with name '{alias_name}'"}

    # Remove the alias
    if alias_storage.remove_alias(player_name, alias_name):
        logger.info("Alias removed", player=player_name, alias_name=alias_name)
        return {"result": f"Alias '{alias_name}' removed."}
    else:
        logger.error("Failed to remove alias", player=player_name, alias_name=alias_name)
        return {"result": f"Failed to remove alias '{alias_name}'."}
