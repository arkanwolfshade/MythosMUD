# resolve_lazy_attr

> 76 nodes · cohesion 0.05

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **asyncio** (7 connections)
- **test_close_handles_attribute_error_during_dispose()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_value_error()** (7 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_closed_event_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_dispose_timeout()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_generic_exception_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_no_running_loop()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_none_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_close_handles_runtime_error_during_dispose()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_none_url_raises()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_unsupported_raises()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_runtime_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_config_validation_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_connection_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_generic_exception()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_none_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_os_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_type_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_initialize_database_unsupported_url()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_reset_database_resets_singleton()** (6 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_manager_init_raises_when_instance_exists()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_get_database_path_postgresql_returns_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- *... and 51 more nodes in this community*

## Relationships

- [InventoryPanel.tsx](InventoryPanel.tsx.md) (82 shared connections)
- [ItemFactory](ItemFactory.md) (26 shared connections)
- [RateLimiter](RateLimiter.md) (11 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [test_check_coverage_thresholds.py](test_check_coverage_thresholds.py.md) (7 shared connections)
- [intersection_schema.json](intersection_schema.json.md) (7 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [endpoints.py](endpoints.py.md) (1 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 263 (85%)
- INFERRED: 47 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*