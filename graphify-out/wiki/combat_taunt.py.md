# combat_taunt.py

> 76 nodes · cohesion 0.04

## Key Concepts

- **database.py** (89 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **fixtures/integration/__init__.py** (23 connections) — `server/tests/fixtures/integration/__init__.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **db_cleanup()** (13 connections) — `server/tests/fixtures/integration/__init__.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **_delete_mutable_integration_test_rows()** (8 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_cleanup_deletes_rows_from_mutable_tables()** (8 connections) — `server/tests/integration/test_integration_cleanup.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **_assert_allowed_integration_test_db()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (7 connections) — `server/tests/fixtures/integration/__init__.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **integration_db_url()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **configure_pool_settings()** (5 connections) — `server/database_config_helpers.py`
- **.get_session_maker()** (5 connections) — `server/database.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **fresh_database_manager()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 51 more nodes in this community*

## Relationships

- [endpoints.py](endpoints.py.md) (23 shared connections)
- [ItemFactory](ItemFactory.md) (12 shared connections)
- [AttributeError](AttributeError.md) (9 shared connections)
- [CombatBroadcastMixin](CombatBroadcastMixin.md) (8 shared connections)
- [RateLimiter](RateLimiter.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (6 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [InventoryPanel.tsx](InventoryPanel.tsx.md) (5 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (4 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (4 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`
- `server/tests/integration/test_integration_cleanup.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 263 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*