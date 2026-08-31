# get_npc_instance_service

> 177 nodes

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
- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_behavior_command()** (14 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_create_command()** (14 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_spawn_command()** (14 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_edit_command()** (13 connections) — `server/commands/npc_admin/definition.py`
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
- *... and 152 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (29 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [event_types.py](event_types.py.md) (12 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [test_occupants.py](test_occupants.py.md) (7 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (3 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
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

- EXTRACTED: 468 (93%)
- INFERRED: 36 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*