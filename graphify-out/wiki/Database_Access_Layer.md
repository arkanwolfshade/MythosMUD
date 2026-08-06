# Database Access Layer

> 324 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **close_db()** (9 connections) — `server/database.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (7 connections) — `server/database_helpers.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database.py`
- *... and 299 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (53 shared connections)
- [add used user](add_used_user.md) (39 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [scripts worktree ops](scripts_worktree_ops.md) (2 shared connections)
- [game models enums](game_models_enums.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (1 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1223 (96%)
- INFERRED: 53 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*