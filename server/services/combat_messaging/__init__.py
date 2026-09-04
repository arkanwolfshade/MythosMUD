"""
Combat messaging integration with real-time messaging system.

This package integrates combat messages with the existing real-time messaging
infrastructure to broadcast combat events to all players in a room.
"""

from server.services.combat_messaging.integration import (
    CombatMessagingIntegration,
    combat_messaging_integration,
)

__all__ = ["CombatMessagingIntegration", "combat_messaging_integration"]
