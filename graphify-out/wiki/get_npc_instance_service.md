# get_npc_instance_service

> 228 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **test_npc_admin_commands.py** (55 connections) — `server/tests/unit/commands/test_npc_admin_commands.py`
- **asyncio** (41 connections)
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **npc_database.py** (29 connections) — `server/npc_database.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **instance.py** (23 connections) — `server/commands/npc_admin/instance.py`
- **test_npc_database.py** (23 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **npc_startup_service.py** (21 connections) — `server/services/npc_startup_service.py`
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
- **handle_npc_delete_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- **handle_npc_list_command()** (11 connections) — `server/commands/npc_admin/definition.py`
- *... and 203 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (32 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [NPCDefinition](NPCDefinition.md) (15 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (9 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (7 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [NPCStartupService](NPCStartupService.md) (6 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin/test_occupants.py`
- `server/commands/npc_admin_commands.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/scripts/verify_npc_occupants.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/commands/test_npc_admin_commands.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 663 (94%)
- INFERRED: 40 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*