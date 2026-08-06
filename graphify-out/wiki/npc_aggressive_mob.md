# npc aggressive mob

> 49 nodes

## Key Concepts

- **MemoryThresholdMonitor** (25 connections) — `server/app/memory_cleanup_service.py`
- **test_memory_cleanup_service.py** (20 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **create_memory_cleanup_monitor()** (8 connections) — `server/app/memory_cleanup_service.py`
- **.get_memory_status_report()** (6 connections) — `server/app/memory_cleanup_service.py`
- **get_managed_task_cleanup_implementation_for_task_four_spec_compliance()** (6 connections) — `server/app/memory_cleanup_service.py`
- **.managed_task_cleanup()** (4 connections) — `server/app/memory_cleanup_service.py`
- **test_create_memory_cleanup_monitor()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_task_four_spec_factory()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **.__init__()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_current_memory_usage()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._get_active_task_count()** (3 connections) — `server/app/memory_cleanup_service.py`
- **._flush_memory_indexes_cache()** (3 connections) — `server/app/memory_cleanup_service.py`
- **monitor()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_current_memory_usage_success()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_current_memory_usage_failure()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_active_task_count_no_loop()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_active_task_count_with_loop()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_flush_memory_indexes_cache_error()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_memory_status_report()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_skips_on_cooldown()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_skips_when_below_threshold()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_success()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_timeout()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_execution_failure()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Any** (1 connections)
- *... and 24 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/tests/unit/app/test_memory_cleanup_service.py`

## Audit Trail

- EXTRACTED: 148 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*