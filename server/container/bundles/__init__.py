"""
Domain-specific bundles for ApplicationContainer initialization.

Each bundle owns a subset of services and initializes them in dependency order.
Bundles are internal implementation details; consumers use container.* attributes.
"""

from server.container.bundles.chat import ChatBundle
from server.container.bundles.combat import CombatBundle
from server.container.bundles.core import CoreBundle
from server.container.bundles.game import GameBundle
from server.container.bundles.magic import MagicBundle
from server.container.bundles.monitoring import MonitoringBundle
from server.container.bundles.npc import NPCBundle
from server.container.bundles.realtime import RealtimeBundle
from server.container.bundles.time import TimeBundle

__all__ = [
    "ChatBundle",
    "CombatBundle",
    "CoreBundle",
    "GameBundle",
    "MagicBundle",
    "MonitoringBundle",
    "NPCBundle",
    "RealtimeBundle",
    "TimeBundle",
]
