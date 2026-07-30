# .validate message()

> 29 nodes

## Key Concepts

- **__init__.py** (18 connections) — `server/tests/fixtures/integration/__init__.py`
- **session_factory()** (17 connections) — `server/tests/fixtures/integration/__init__.py`
- **db_cleanup()** (10 connections) — `server/tests/fixtures/integration/__init__.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **_assert_allowed_integration_test_db()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_engine()** (6 connections) — `server/tests/fixtures/integration/__init__.py`
- **db.py** (6 connections) — `server/tests/fixtures/integration/db.py`
- **_delete_mutable_integration_test_rows()** (5 connections) — `server/tests/fixtures/integration/__init__.py`
- **_get_db_name_from_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **_is_allowed_integration_test_db()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **integration_db_url()** (4 connections) — `server/tests/fixtures/integration/__init__.py`
- **FixtureRequest** (3 connections)
- **AsyncSession** (3 connections)
- **_should_preserve_table_on_cleanup()** (3 connections) — `server/tests/fixtures/integration/__init__.py`
- **_IntegrationState** (2 connections) — `server/tests/fixtures/integration/__init__.py`
- **async_sessionmaker** (2 connections)
- **Build connect_args for asyncpg when POSTGRES_SEARCH_PATH is set.      Used so un** (1 connections) — `server/database_config_helpers.py`
- **AsyncEngine** (1 connections)
- **Integration-tier fixtures with real database connections.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse failu** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Return True only if the URL points to an allowed test-only database (mythos_unit** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev.** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an isolated PostgreSQL database URL for integration tests.      Reads fr** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide a SQLAlchemy async engine bound to the integration DB URL.      CRITICAL** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Provide an async session factory for integration tests.      CRITICAL: This fixt** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- *... and 4 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (4 shared connections)
- [Tests for get profession service](Tests_for_get_profession_service.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (3 shared connections)
- [world](world.md) (3 shared connections)
- [test admin commands](test_admin_commands.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [bench cache npc](bench_cache_npc.md) (2 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [occupation slots 9()](occupation_slots_9%28%29.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/fixtures/integration/db.py`

## Audit Trail

- EXTRACTED: 104 (90%)
- INFERRED: 11 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*