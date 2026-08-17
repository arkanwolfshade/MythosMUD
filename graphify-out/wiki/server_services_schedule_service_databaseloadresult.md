# server services schedule service databaseloadresult

> 14 nodes

## Key Concepts

- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MonkeyPatch** (3 connections)
- **TypedDict** (1 connections)
- **asyncio** (1 connections)
- **Async helper to load schedules from PostgreSQL database.** (1 connections) — `server/services/schedule_service.py`
- **Return asyncpg-compatible DATABASE_URL from the environment.** (1 connections) — `server/services/schedule_service.py`
- **DATABASE_URL is converted to asyncpg-compatible form.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Missing DATABASE_URL raises ValueError.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Regression: tables live in schema mythos_e2e; raw asyncpg must set search_path…** (1 connections) — `server/tests/unit/services/test_schedule_service.py`

## Relationships

- [scripts validate calendar](scripts_validate_calendar.md) (4 shared connections)
- [scripts validate calendar load and](scripts_validate_calendar_load_and.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*