# RateLimiter

> 85 nodes · cohesion 0.04

## Key Concepts

- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **get_database_path()** (17 connections) — `server/database_helpers.py`
- **asyncio** (14 connections)
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **get_session_maker()** (10 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **get_database_url()** (7 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- **test_get_engine_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker_raises_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_engine_initialization_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_close_db_raises_runtime_error_on_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_failure()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_on_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_rollback_success()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_database_url_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_engine()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_session_maker()** (5 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **_get_database_url_state()** (4 connections) — `server/database.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_get_async_session_finally_block_executes()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- *... and 60 more nodes in this community*

## Relationships

- [InventoryPanel.tsx](InventoryPanel.tsx.md) (13 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (11 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (7 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (5 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`

## Audit Trail

- EXTRACTED: 181 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*