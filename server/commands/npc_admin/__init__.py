"""
NPC Admin Commands subpackage for MythosMUD.

Splits NPC admin functionality across modules to keep file size manageable.
"""

from .behavior import (
    handle_npc_behavior_command,
    handle_npc_react_command,
    handle_npc_stop_command,
)
from .definition import (
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_edit_command,
    handle_npc_list_command,
)
from .instance import (
    handle_npc_despawn_command,
    handle_npc_move_command,
    handle_npc_spawn_command,
    handle_npc_stats_command,
)
from .monitoring import (
    handle_npc_population_command,
    handle_npc_status_command,
    handle_npc_zone_command,
)
from .router import handle_npc_command, validate_npc_admin_permission
from .test_occupants import handle_npc_test_occupants_command

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
