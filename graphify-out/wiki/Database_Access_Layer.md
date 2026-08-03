# Database Access Layer

> 446 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (76 connections) — `server/database.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **npc_database.py** (27 connections) — `server/npc_database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **init_db()** (11 connections) — `server/database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- *... and 421 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (85 shared connections)
- [npc populate databases](npc_populate_databases.md) (24 shared connections)
- [Database Config](Database_Config.md) (15 shared connections)
- [NATS Messaging](NATS_Messaging.md) (14 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (13 shared connections)
- [auth users rationale](auth_users_rationale.md) (12 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (8 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (6 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 1795 (96%)
- INFERRED: 84 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*