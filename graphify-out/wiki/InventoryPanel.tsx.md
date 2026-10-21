# InventoryPanel.tsx

> 50 nodes · cohesion 0.06

## Key Concepts

- **DatabaseManager** (113 connections) — `server/database.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_connection_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_generic_exception()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_os_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_value_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_none_url_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_postgresql_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_database_path_unsupported_raises()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_handles_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_get_engine_reinitializes_if_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_runtime_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_config_validation_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_converts_postgresql_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_import_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_keeps_asyncpg_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_none_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_skip_if_already_initialized()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_type_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_unsupported_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_module_level_url()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_nullpool_for_test()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **test_initialize_database_uses_pool_config_for_production()** (5 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **.__init__()** (2 connections) — `server/database.py`
- *... and 25 more nodes in this community*

## Relationships

- [resolve_lazy_attr](resolve_lazy_attr.md) (82 shared connections)
- [RateLimiter](RateLimiter.md) (13 shared connections)
- [ItemFactory](ItemFactory.md) (13 shared connections)
- [test_check_coverage_thresholds.py](test_check_coverage_thresholds.py.md) (10 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (8 shared connections)
- [intersection_schema.json](intersection_schema.json.md) (5 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (5 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [4. Common Fix Patterns](4._Common_Fix_Patterns.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 122 (56%)
- INFERRED: 96 (44%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*