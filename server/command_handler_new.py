"""
Refactored command handler for MythosMUD.

This is the new, modular command handler that replaces the massive
command_handler.py file with a clean, organized structure.
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user
from .commands.command_service import CommandService
from .logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])

# Global command service instance
command_service = CommandService()


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    else:
        raise ValueError("User object must have username attribute or key")


class CommandRequest(BaseModel):
    command: str


@router.post("/")
async def handle_command(
    request_data: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """
    Handle a command request.

    This is the main entry point for command processing, using the new
    modular command service architecture.
    """
    try:
        player_name = get_username_from_user(current_user)
        logger.debug("Command request received", player=player_name, command=request_data.command)

        # Get alias storage from request app state
        app = request.app if request else None
        alias_storage = app.state.alias_storage if app else None

        if not alias_storage:
            logger.error("No alias storage available")
            raise HTTPException(status_code=500, detail="Internal server error")

        # Process command using the new service
        result = await command_service.process_command(
            request_data.command,
            current_user,
            request,
            alias_storage,
            player_name,
        )

        logger.debug("Command processed successfully", player=player_name, result=result)
        return result

    except Exception as e:
        logger.error("Command processing error", error=str(e))
        raise HTTPException(status_code=500, detail=f"Error processing command: {str(e)}") from e


async def handle_expanded_command(
    command: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
) -> dict:
    """
    Handle command expansion for aliases.

    This function handles the recursive expansion of aliases and
    processes the final command.
    """
    MAX_ALIAS_DEPTH = 10

    if depth >= MAX_ALIAS_DEPTH:
        logger.warning("Maximum alias depth exceeded", player=player_name, depth=depth)
        return {"result": "Alias chain too deep. Possible circular alias."}

    # Check for alias
    alias = alias_storage.get_alias(player_name, command)
    if alias:
        logger.debug("Alias found, expanding", player=player_name, alias=command, expanded=alias.command)

        # Recursively expand the alias
        expanded_result = await handle_expanded_command(
            alias.command,
            current_user,
            request,
            alias_storage,
            player_name,
            depth + 1,
        )

        # Add alias chain information
        if "alias_chain" not in expanded_result:
            expanded_result["alias_chain"] = []
        expanded_result["alias_chain"].append(command)

        return expanded_result

    # No alias found, process as regular command
    return await command_service.process_command(
        command,
        current_user,
        request,
        alias_storage,
        player_name,
    )


def get_help_content(command_name: str | None = None) -> str:
    """
    Get help content for commands.

    This is a compatibility function that delegates to the new help system.
    """
    from .help.help_content import get_help_content as get_help_content_new

    return get_help_content_new(command_name)
