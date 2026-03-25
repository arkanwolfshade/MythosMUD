"""
NPC Admin Commands for MythosMUD.

This module provides administrative slash commands for managing NPCs,
including CRUD operations for NPC definitions, instance management,
population monitoring, and relationship management.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.

Implementation is split across the npc_admin subpackage for maintainability.
"""

from .npc_admin import (
    handle_npc_behavior_command,
    handle_npc_command,
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_despawn_command,
    handle_npc_edit_command,
    handle_npc_list_command,
    handle_npc_move_command,
    handle_npc_population_command,
    handle_npc_react_command,
    handle_npc_spawn_command,
    handle_npc_stats_command,
    handle_npc_status_command,
    handle_npc_stop_command,
    handle_npc_test_occupants_command,
    handle_npc_zone_command,
    validate_npc_admin_permission,
)

__all__ = [
    "handle_npc_command",
    "validate_npc_admin_permission",
    "handle_npc_create_command",
    "handle_npc_edit_command",
    "handle_npc_delete_command",
    "handle_npc_list_command",
    "handle_npc_spawn_command",
    "handle_npc_despawn_command",
    "handle_npc_move_command",
    "handle_npc_stats_command",
    "handle_npc_population_command",
    "handle_npc_zone_command",
    "handle_npc_status_command",
    "handle_npc_behavior_command",
    "handle_npc_react_command",
    "handle_npc_stop_command",
    "handle_npc_test_occupants_command",
]
