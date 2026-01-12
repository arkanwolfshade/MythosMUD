"""
Global state management for CombatService.

This module provides functions for managing the global CombatService instance,
allowing access to the service from anywhere in the application.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from server.services.combat_service import CombatService

# Using a dict container to avoid global statement warnings
_combat_service_state: dict[str, CombatService | None] = {"service": None}


def get_combat_service() -> CombatService | None:
    """Get the global combat service instance."""
    return _combat_service_state["service"]


def set_combat_service(service: CombatService | None) -> None:
    """Set the global combat service instance."""
    _combat_service_state["service"] = service


# For backward compatibility
COMBAT_SERVICE = None  # pylint: disable=invalid-name  # Reason: Legacy backward compatibility variable
