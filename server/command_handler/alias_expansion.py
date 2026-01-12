"""
Alias Expansion Logic for MythosMUD.

This module handles alias resolution, expansion, and safety checks
including cycle detection to prevent infinite loops.
"""

# pylint: disable=too-many-arguments  # Reason: Alias expansion requires many parameters for context and expansion logic

from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.alias_graph import AliasGraph
from ..utils.audit_logger import audit_logger
from ..validators.command_validator import CommandValidator

if TYPE_CHECKING:
    from fastapi import Request

    from ..alias_storage import AliasStorage

logger = get_logger(__name__)

# Maximum expanded command length
MAX_EXPANDED_COMMAND_LENGTH = CommandValidator.MAX_EXPANDED_COMMAND_LENGTH


async def check_alias_safety(
    alias_storage: "AliasStorage",
    player_name: str,
    alias_name: str,
) -> tuple[bool, str | None, int]:
    """
    Check if an alias is safe to expand.

    Builds an alias dependency graph and checks for cycles and excessive depth.

    Args:
        alias_storage: The alias storage instance
        player_name: The player's name
        alias_name: The alias to check

    Returns:
        Tuple of (is_safe, error_message, expansion_depth)
    """
    alias_graph = AliasGraph(alias_storage)
    alias_graph.build_graph(player_name)

    if not alias_graph.is_safe_to_expand(alias_name):
        cycle = alias_graph.detect_cycle(alias_name)
        cycle_path = " -> ".join(cycle) if cycle else "unknown"

        logger.warning(
            "Circular alias dependency detected - expansion blocked",
            player=player_name,
            alias=alias_name,
            cycle=cycle,
        )

        # Log security event
        audit_logger.log_alias_expansion(
            player_name=player_name,
            alias_name=alias_name,
            expanded_command="[BLOCKED - Circular dependency]",
            cycle_detected=True,
            expansion_depth=0,
        )

        error_msg = (
            f"Alias '{alias_name}' contains circular dependency: {cycle_path}\n"
            f"Please remove the circular reference using 'unalias {alias_name}'"
        )
        return False, error_msg, 0

    # Check expansion depth
    expansion_depth = alias_graph.get_expansion_depth(alias_name)
    if expansion_depth > 10:  # Reasonable depth limit
        logger.warning(
            "Alias expansion depth too deep",
            player=player_name,
            alias=alias_name,
            depth=expansion_depth,
        )
        error_msg = (
            f"Alias '{alias_name}' has excessive expansion depth ({expansion_depth} levels). Maximum allowed is 10."
        )
        return False, error_msg, expansion_depth

    return True, None, expansion_depth


def validate_expanded_command(
    expanded_command: str,
    player_name: str,
    alias_name: str,
    expansion_depth: int,
) -> tuple[bool, str | None]:
    """
    Validate an expanded command for length and content.

    Args:
        expanded_command: The expanded command string
        player_name: The player's name
        alias_name: The alias that was expanded
        expansion_depth: The depth of expansion

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check length
    if len(expanded_command) > MAX_EXPANDED_COMMAND_LENGTH:
        logger.warning(
            "Expanded command exceeds length limit",
            player=player_name,
            alias=alias_name,
            length=len(expanded_command),
            max_length=MAX_EXPANDED_COMMAND_LENGTH,
        )
        # Log security event
        audit_logger.log_alias_expansion(
            player_name=player_name,
            alias_name=alias_name,
            expanded_command="[BLOCKED - Too long]",
            cycle_detected=False,
            expansion_depth=expansion_depth,
        )
        error_msg = f"Expanded command too long ({len(expanded_command)} chars, max {MAX_EXPANDED_COMMAND_LENGTH})"
        return False, error_msg

    # Validate content
    is_valid_expanded, expanded_error = CommandValidator.validate_expanded_command(expanded_command)
    if not is_valid_expanded:
        logger.warning(
            "Expanded command validation failed",
            player=player_name,
            alias=alias_name,
            error=expanded_error,
        )
        # Log security event
        audit_logger.log_security_event(
            event_type="malicious_alias_detected",
            player_name=player_name,
            description=f"Alias expands to dangerous content: {expanded_error}",
            severity="high",
            metadata={"alias": alias_name},
        )
        return False, f"Alias expansion blocked: {expanded_error}"

    return True, None


async def handle_expanded_command(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Alias expansion requires many parameters for context and expansion logic
    command_line: str,
    current_user: dict,
    request: "Request",
    alias_storage: "AliasStorage",
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Handle command processing with alias expansion and loop detection.

    This function processes an expanded command, with protection against
    infinite recursion via depth limiting.

    Args:
        command_line: The command line to process
        current_user: Current user information
        request: FastAPI request object
        alias_storage: The alias storage instance
        player_name: The player's name
        depth: Current recursion depth
        alias_chain: Chain of alias expansions for debugging

    Returns:
        dict: Command result with 'result' key and optional metadata
    """
    # Import here to avoid circular imports between alias_expansion and processing modules
    from .processing import (
        process_command_with_validation,  # pylint: disable=import-outside-toplevel  # Reason: Circular import avoidance - processing imports from this module's parent package
    )

    logger.debug(
        "Handling expanded command",
        player=player_name,
        command_line=command_line,
        depth=depth,
    )

    # Prevent infinite loops
    if depth > 10:
        logger.warning("Alias expansion depth limit exceeded", player=player_name, depth=depth)
        return {"result": "Alias expansion too deep - possible loop detected"}

    # Initialize alias chain if not provided
    if alias_chain is None:
        alias_chain = []

    # Process the expanded command
    return await process_command_with_validation(command_line, current_user, request, alias_storage, player_name)
