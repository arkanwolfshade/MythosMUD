# server app task registry get

> 28 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (25 connections) — `server/tests/unit/app/test_task_registry.py`
- **asyncio** (14 connections)
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_module_level_helpers()** (6 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_task_by_name()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_info_and_metrics()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_list_active_tasks_and_stats_by_type()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_clears_active_tasks()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_task_metadata_repr()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **_hang_until_cancelled()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **registry()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_missing_task_returns_false()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_get_registry_returns_global_instance()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_idempotent_warning()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_unregister_missing_task_returns_false()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **.__init__()** (2 connections) — `server/app/task_registry.py`
- **fixture** (1 connections)
- **MonkeyPatch** (1 connections)
- **Access the global TaskRegistry.** (1 connections) — `server/app/task_registry.py`
- *... and 3 more nodes in this community*

## Relationships

- [server app task registry py](server_app_task_registry_py.md) (10 shared connections)
- [server app task registry](server_app_task_registry.md) (8 shared connections)
- [server app task registry rationale](server_app_task_registry_rationale.md) (8 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app tracked task manager](server_app_tracked_task_manager.md) (3 shared connections)
- [server api monitoring](server_api_monitoring.md) (3 shared connections)
- [holidayresolver](holidayresolver.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (1 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 90 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*