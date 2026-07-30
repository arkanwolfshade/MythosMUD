# close db()

> 272 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (7 connections) — `server/database_helpers.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **_reset_database_url_state()** (5 connections) — `server/database.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_value_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 247 more nodes in this community*

## Relationships

- [real time](real_time.md) (65 shared connections)
- [.initialize()](initialize%28%29.md) (34 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [.use invite()](use_invite%28%29.md) (1 shared connections)
- [metrics](metrics.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1034 (96%)
- INFERRED: 47 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*