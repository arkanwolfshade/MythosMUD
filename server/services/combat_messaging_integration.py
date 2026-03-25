"""
Combat messaging integration with real-time messaging system.

Re-exports from combat_messaging package for backward compatibility.
"""

from server.services.combat_messaging import CombatMessagingIntegration, combat_messaging_integration

__all__ = ["CombatMessagingIntegration", "combat_messaging_integration"]
