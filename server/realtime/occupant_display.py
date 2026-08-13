"""Shared occupant display names for look text and Occupants panel events."""

from __future__ import annotations

import uuid
from typing import Any

from .disconnect_grace_period import is_player_in_grace_period
from .login_grace_period import is_player_in_login_grace_period


def _parse_occupant_player_id(player_id: uuid.UUID | str | None) -> uuid.UUID | None:
    if player_id is None:
        return None
    try:
        return player_id if isinstance(player_id, uuid.UUID) else uuid.UUID(str(player_id))
    except (ValueError, AttributeError, TypeError):
        return None


def _apply_grace_badges(name: str, player_id: uuid.UUID, connection_manager: Any) -> str:
    display = name
    if is_player_in_grace_period(player_id, connection_manager) and "(linkdead)" not in display:
        display = f"{name} (linkdead)"
    if is_player_in_login_grace_period(player_id, connection_manager) and "(warded)" not in display:
        display = f"{display} (warded)"
    return display


def format_occupant_display_name(
    name: str,
    player_id: uuid.UUID | str | None,
    connection_manager: Any | None,
) -> str:
    """Format an in-room player's Occupants/look name. Always list; grace badges only."""
    if not name or connection_manager is None:
        return name
    resolved = _parse_occupant_player_id(player_id)
    if resolved is None:
        return name
    try:
        return _apply_grace_badges(name, resolved, connection_manager)
    except (ValueError, AttributeError, ImportError, TypeError):
        return name
