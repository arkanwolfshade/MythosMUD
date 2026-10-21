# ItemFactory

> 66 nodes · cohesion 0.04

## Key Concepts

- **get_async_session()** (68 connections) — `server/database.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **asyncio** (12 connections)
- **init_db()** (10 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database.py`
- **close_db()** (8 connections) — `server/database.py`
- **test_database_manager_close_dispose_error()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_with_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_close_without_engine()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_unsupported()** (6 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_database_path_postgresql()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_event_loop_check()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_no_running_loop()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_engine_reinitializes_if_none()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_manager_get_session_maker_initializes()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_async_session_rollback_on_error()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_engine_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_get_session_maker_initializes_database()** (5 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **ensure_database_directory()** (4 connections) — `server/database.py`
- **test_close_db_error()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_close_db_success()** (4 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- *... and 41 more nodes in this community*

## Relationships

- [resolve_lazy_attr](resolve_lazy_attr.md) (26 shared connections)
- [InventoryPanel.tsx](InventoryPanel.tsx.md) (13 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (12 shared connections)
- [test_check_coverage_thresholds.py](test_check_coverage_thresholds.py.md) (6 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (4 shared connections)
- [endpoints.py](endpoints.py.md) (3 shared connections)
- [reset_database](reset_database.md) (3 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (3 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/database.py`
- `server/tests/unit/infrastructure/test_database_extended.py`

## Audit Trail

- EXTRACTED: 203 (93%)
- INFERRED: 16 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*