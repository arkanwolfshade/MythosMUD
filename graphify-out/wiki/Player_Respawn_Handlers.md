# Player Respawn Handlers

> 38 nodes

## Key Concepts

- **test_npc_admin_commands.py** (23 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_player_service()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_permission()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_not_admin()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_admin()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_list_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_not_found()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_spawn_command_name_success()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_spawn_command_regression_routing_via_npc_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_despawn_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_move_command_no_args()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_stats_command()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_validate_npc_admin_permission_exception()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_unknown_subcommand()** (3 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Unit tests for NPC admin command handlers.  Tests the NPC admin command function** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player service is not available.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player is not found.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() when player lacks admin permission.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test handle_npc_command() with no arguments.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **Test validate_npc_admin_permission() with no player.** (1 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- *... and 13 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (11 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (6 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (5 shared connections)

## Source Files

- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 78 (81%)
- INFERRED: 18 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*