"""
Alias management commands for MythosMUD.

This module contains handlers for alias-related commands.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _extract_alias_params(command_data: dict, player_name: str) -> tuple[str | None, str | None]:
    """Extract alias_name and command from command_data. Returns (alias_name, command)."""
    alias_name = command_data.get("alias_name")
    command = command_data.get("command")

    if alias_name is None:
        args: list = command_data.get("args", [])
        logger.debug("Processing alias command from args", player_name=player_name, args=args)

        if not args:
            return None, None

        alias_name = args[0].lower()

        if len(args) == 1:
            return alias_name, None

        command = " ".join(args[1:])
    else:
        alias_name = alias_name.lower()

    return alias_name, command


def _view_alias(alias_storage: AliasStorage, player_name: str, alias_name: str) -> dict[str, str]:
    """View an existing alias. Returns result dict."""
    logger.debug("Viewing alias", player_name=player_name, alias_name=alias_name)
    alias = alias_storage.get_alias(player_name, alias_name)
    if alias:
        logger.debug("Alias found", player_name=player_name, alias_name=alias_name, command=alias.command)
        return {"result": f"Alias '{alias_name}' = '{alias.command}'"}

    logger.debug("Alias not found", player_name=player_name, alias_name=alias_name)
    return {"result": f"No alias found for '{alias_name}'"}


def _validate_alias_params(alias_name: str, command: str, player_name: str) -> dict[str, str] | None:
    """Validate alias name and command. Returns error dict if invalid, None if valid."""
    if not alias_name or len(alias_name) > 20:
        logger.warning("Invalid alias name", player_name=player_name, alias_name=alias_name)
        return {"result": "Alias name must be 1-20 characters long."}

    if not command or len(command) > 200:
        logger.warning("Invalid alias command", player_name=player_name, alias_name=alias_name, command=command)
        return {"result": "Alias command must be 1-200 characters long."}

    if alias_name in command.lower():
        return {"result": "Alias cannot reference itself."}

    return None


def _create_alias(alias_storage: AliasStorage, player_name: str, alias_name: str, command: str) -> dict[str, str]:
    """Create or update an alias. Returns result dict."""
    logger.debug("Creating/updating alias", player_name=player_name, alias_name=alias_name, command=command)

    error_result = _validate_alias_params(alias_name, command, player_name)
    if error_result:
        return error_result

    try:
        alias_storage.create_alias(player_name, alias_name, command)
        logger.info("Alias created", player_name=player_name, alias_name=alias_name, command=command)
        return {"result": f"Alias '{alias_name}' created successfully."}
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias creation errors unpredictable, must return error message
        logger.error(
            "Failed to create alias", player_name=player_name, alias_name=alias_name, command=command, error=str(e)
        )
        return {"result": f"Failed to create alias: {str(e)}"}


async def handle_alias_command(
    command_data: dict, _current_user: dict, _request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the alias command for creating and viewing aliases.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Command result
    """
    if alias_storage is None:
        logger.error("Alias storage not available", player_name=player_name)
        return {"result": "Alias system is not available"}

    alias_name, command = _extract_alias_params(command_data, player_name)

    if alias_name is None:
        logger.warning("Alias command with no arguments", player_name=player_name)
        return {"result": "Usage: alias <name> [command] or alias <name> to view"}

    if command is None:
        return _view_alias(alias_storage, player_name, alias_name)

    return _create_alias(alias_storage, player_name, alias_name, command)


async def handle_aliases_command(
    _command_data: dict, _current_user: dict, _request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the aliases command for listing all aliases.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Aliases command result
    """
    logger.debug("Listing aliases", player_name=player_name)

    if alias_storage is None:
        logger.error("Alias storage not available", player_name=player_name)
        return {"result": "Alias system is not available"}

    try:
        # AI Agent: Method is get_player_aliases, not list_aliases
        aliases = alias_storage.get_player_aliases(player_name)
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

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias listing errors unpredictable, must return error message
        logger.error("Failed to list aliases", player_name=player_name, error=str(e))
        return {"result": f"Failed to list aliases: {str(e)}"}


async def handle_unalias_command(
    command_data: dict, _current_user: dict, _request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the unalias command for removing aliases.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unalias command result
    """
    # Extract args from command_data
    args: list = command_data.get("args", [])

    logger.debug("Processing unalias command", player_name=player_name, args=args)

    if alias_storage is None:
        logger.error("Alias storage not available", player_name=player_name)
        return {"result": "Alias system is not available"}

    if not args:
        logger.warning("Unalias command with no arguments", player_name=player_name)
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0].lower()
    logger.debug("Removing alias", player_name=player_name, alias_name=alias_name)

    try:
        # Check if alias exists
        # AI Agent: get_alias requires player_name as first argument
        existing_alias = alias_storage.get_alias(player_name, alias_name)
        if not existing_alias:
            logger.debug("Alias not found for removal", player_name=player_name, alias_name=alias_name)
            return {"result": f"No alias found for '{alias_name}'"}

        # Remove the alias
        # AI Agent: Method is remove_alias, not delete_alias, and requires player_name
        alias_storage.remove_alias(player_name, alias_name)
        logger.info("Alias removed", player_name=player_name, alias_name=alias_name)
        return {"result": f"Alias '{alias_name}' removed successfully."}

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alias removal errors unpredictable, must return error message
        logger.error("Failed to remove alias", player_name=player_name, alias_name=alias_name, error=str(e))
        return {"result": f"Failed to remove alias: {str(e)}"}
