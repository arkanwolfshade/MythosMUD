# DatabaseManager

> 108 nodes

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- *... and 83 more nodes in this community*

## Relationships

- [.get_instance](get_instance.md) (88 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [ValidationError](ValidationError.md) (9 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [models/player.py](models-player.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (2 shared connections)
- [Invite](Invite.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 228 (71%)
- INFERRED: 95 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*