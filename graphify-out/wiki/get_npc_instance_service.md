# get_npc_instance_service

> 157 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **test_npc_admin_commands.py** (55 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **asyncio** (41 connections)
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (17 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_react_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (12 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_despawn_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_move_command()** (11 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_population_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **npc_admin/monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **validate_npc_admin_permission()** (9 connections) — `server/commands/npc_admin/router.py`
- *... and 132 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (19 shared connections)
- [definition.py](definition.py.md) (17 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [test_occupants.py](test_occupants.py.md) (8 shared connections)
- [command_service.py](command_service.py.md) (8 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [test_npc_instances_api.py](test_npc_instances_api.py.md) (5 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (5 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin_commands.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 432 (92%)
- INFERRED: 36 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*