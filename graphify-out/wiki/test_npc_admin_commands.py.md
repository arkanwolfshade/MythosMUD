# test_npc_admin_commands.py

> 75 nodes

## Key Concepts

- **test_npc_admin_commands.py** (23 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **asyncio** (21 connections)
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_spawn_command()** (13 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_params()** (7 connections) — `server/commands/npc_admin/instance.py`
- **Any** (6 connections)
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections)
- **_execute_spawn_loop()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_normalize_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_parse_npc_spawn_numeric()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_definition_id_from_name()** (4 connections) — `server/commands/npc_admin/instance.py`
- **_resolve_spawn_room_id()** (4 connections) — `server/commands/npc_admin/instance.py`
- **test_handle_npc_command_no_args()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_permission()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_command_unknown_subcommand()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_invalid_type()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **test_handle_npc_create_command_no_args()** (4 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- *... and 50 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (40 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/router.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`

## Audit Trail

- EXTRACTED: 140 (86%)
- INFERRED: 23 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*