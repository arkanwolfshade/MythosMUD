# commands npc admin

> 36 nodes

## Key Concepts

- **test_npc_admin_commands.py** (23 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **validate_npc_admin_permission()** (9 connections) — `server/commands/npc_admin/router.py`
- **test_handle_npc_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_success()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_spawn_command_regression_routing_via_npc_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_despawn_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_move_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_stats_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_exception()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_unknown_subcommand()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Validate that a player has NPC admin permissions.      Args:         player: Pla** (1 connections) — `server/commands/npc_admin/router.py`
- **Unit tests for NPC admin command handlers.  Tests the NPC admin command function** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test validate_npc_admin_permission() with no player.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- *... and 11 more nodes in this community*

## Relationships

- [combat attack handler](combat_attack_handler.md) (8 shared connections)
- [npc commands admin](npc_commands_admin.md) (7 shared connections)
- [help content websocket](help_content_websocket.md) (3 shared connections)
- [container schemas containers](container_schemas_containers.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)

## Source Files

- `server/commands/npc_admin/router.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 78 (80%)
- INFERRED: 20 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*