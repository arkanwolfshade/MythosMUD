# server alias storage aliasstorage

> 113 nodes

## Key Concepts

- **AliasStorage** (250 connections) — `server/alias_storage.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **test_occupants.py** (14 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_test_occupants_command()** (13 connections) — `server/commands/npc_admin/test_occupants.py`
- **handle_npc_react_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_population_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- *... and 88 more nodes in this community*

## Relationships

- [server tests unit test alias](server_tests_unit_test_alias.md) (57 shared connections)
- [server commands npc admin router](server_commands_npc_admin_router.md) (53 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (28 shared connections)
- [aliasrecord](aliasrecord.md) (17 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (14 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (12 shared connections)
- [server alias storage aliasstorage add](server_alias_storage_aliasstorage_add.md) (10 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (9 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (9 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (8 shared connections)
- [aliaspayload](aliaspayload.md) (8 shared connections)
- [draft7validator](draft7validator.md) (8 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin/test_occupants.py`
- `server/commands/npc_admin_commands.py`
- `server/models/npc.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 538 (84%)
- INFERRED: 106 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*