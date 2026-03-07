"""
Shared helpers and exceptions for combat commands.

Extracted from combat.py to reduce file nloc (Lizard limit 500).
"""

from typing import Any


class FleePreconditionError(Exception):
    """Raised when flee preconditions fail; carries the error dict to return to the client."""

    def __init__(self, error_result: dict[str, str]) -> None:
        super().__init__(str(error_result))
        self.error_result = error_result


def _format_combat_status(player: Any, combat_instance: Any | None) -> str:
    """
    Produce a human-readable combat status string.

    This helper is retained for backward compatibility with tests that validate
    status reporting in isolation from the command handler.
    """
    if getattr(player, "in_combat", False) and combat_instance is not None:
        status = getattr(combat_instance, "status", "") or "active"
        return f"Combat status: {status}"
    return "You are not in combat."


def _get_combat_target(_player: Any, target_name: str | None) -> Any | None:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future player-based target resolution
    """
    Resolve a combat target by name.

    The current implementation is intentionally minimal for unit tests that only
    verify callable presence and basic return semantics. In production code the
    target resolution is delegated to TargetResolutionService.
    """
    if not target_name:
        return None
    # Real resolution is handled elsewhere; return None to indicate no local match
    return None
