"""Shared occupant display names for look text and Occupants panel events."""

from __future__ import annotations

import uuid
from typing import Any

from ..models.corruption import CorruptionTier
from ..services.corruption_tier_cache import corruption_tier_cache
from .disconnect_grace_period import is_player_in_grace_period
from .login_grace_period import is_player_in_login_grace_period

# #815: same vocabulary as look_helpers._CORRUPTION_LABELS for marked+ -- gated at `marked` so the
# permanent `touched` scar stays private (found only by a deliberate look), while real corruption
# is ambient and unhideable. This is the single chokepoint for per-player adornment visible to
# OTHER players -- it feeds both the room's "Also here:" line and the client Occupants panel.
_CORRUPTION_BADGE_LABELS: dict[CorruptionTier, str] = {
    CorruptionTier.MARKED: "marked",
    CorruptionTier.CORRUPTED: "defiled",
    CorruptionTier.WARPED: "warped",
}


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


def _apply_corruption_badge(name: str, player_id: uuid.UUID) -> str:
    """Append a corruption badge for a `marked`-or-worse tier. Cache-only (#815's connect-time
    warming keeps it correct) -- no persistence lookup on this hot, always-rendered path."""
    label = _CORRUPTION_BADGE_LABELS.get(corruption_tier_cache.get_tier(player_id))
    if label and f"({label})" not in name:
        return f"{name} ({label})"
    return name


def format_occupant_display_name(
    name: str,
    player_id: uuid.UUID | str | None,
    connection_manager: Any | None,
) -> str:
    """Format an in-room player's Occupants/look name: grace badges plus a corruption badge."""
    if not name or connection_manager is None:
        return name
    resolved = _parse_occupant_player_id(player_id)
    if resolved is None:
        return name
    try:
        display = _apply_grace_badges(name, resolved, connection_manager)
        return _apply_corruption_badge(display, resolved)
    except (ValueError, AttributeError, ImportError, TypeError):
        return name
