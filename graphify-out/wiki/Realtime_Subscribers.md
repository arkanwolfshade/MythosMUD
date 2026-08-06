# Realtime Subscribers

> 150 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **test_combat_schema.py** (20 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **CombatSchemaValidationError** (17 connections) — `server/schemas/combat/combat_schema.py`
- **migrate_combat_data.py** (15 connections) — `server/scripts/migrate_combat_data.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- **migrate_npc_combat_data()** (10 connections) — `server/scripts/migrate_combat_data.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **validate_behavior_config_combat_data()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **add_default_combat_data_to_config()** (8 connections) — `server/schemas/combat/combat_schema.py`
- **validate_migration_results()** (8 connections) — `server/scripts/migrate_combat_data.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **rollback_migration()** (7 connections) — `server/scripts/migrate_combat_data.py`
- *... and 125 more nodes in this community*

## Relationships

- [add used user](add_used_user.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [room look commands](room_look_commands.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (2 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/database.py`
- `server/npc_database.py`
- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/tests/unit/infrastructure/test_npc_database.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 553 (93%)
- INFERRED: 42 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*