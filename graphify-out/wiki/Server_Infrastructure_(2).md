# Server Infrastructure (2)

> 224 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **Path** (6 connections)
- **get_database_url()** (6 connections) — `server/database.py`
- **.get_engine()** (5 connections) — `server/database.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_os_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 199 more nodes in this community*

## Relationships

- [Server Utils](Server_Utils.md) (28 shared connections)
- [Server Admin](Server_Admin.md) (22 shared connections)
- [Server Infrastructure (5)](Server_Infrastructure_%285%29.md) (20 shared connections)
- [Server Persistence](Server_Persistence.md) (11 shared connections)
- [Server Tools](Server_Tools.md) (6 shared connections)
- [Server App (2)](Server_App_%282%29.md) (5 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (3 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (3 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Game (8)](Server_Game_%288%29.md) (1 shared connections)
- [Server Services (81)](Server_Services_%2881%29.md) (1 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 894 (95%)
- INFERRED: 45 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*