"""
NPC Admin API endpoints for MythosMUD server.

This module provides the router and shared helpers for administrative NPC APIs.
Route handlers are registered by submodules (definitions, instances, population,
spawn rules, admin mgmt) to keep this file's NLOC under complexity limits.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

# Import for side-effect: each module registers routes on npc_router.
from . import (  # noqa: F401  # pylint: disable=unused-import
    npc_admin_mgmt_api,
    npc_definitions_api,
    npc_instances_api,
    npc_population_api,
    npc_spawn_rules_api,
)
from .npc_router_core import npc_router, validate_admin_permission

__all__ = ["npc_router", "validate_admin_permission"]
