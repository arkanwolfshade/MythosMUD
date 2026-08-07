# command parser rationale

> 36 nodes

## Key Concepts

- **reset_database()** (16 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **test_reset_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **test_reset_database_resets_singleton()** (4 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **reset_db_state()** (3 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **reset_db()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_reset_database_resets_module_url()** (3 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **datetime** (3 connections)
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **Reset the database connection state (for testing).      This resets the Database** (1 connections) — `server/database.py`
- **Set test override database URL.** (1 connections) — `server/database_config_helpers.py`
- **Normalize database URL for asyncpg.      Args:         database_url: Original da** (1 connections) — `server/database_config_helpers.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Test reset_database resets module-level _database_url.** (1 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 11 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (12 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (7 shared connections)
- [manager subject services](manager_subject_services.md) (4 shared connections)
- [game models player](game_models_player.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 122 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*