# Test Memory Cleanup Service

> 31 nodes

## Key Concepts

- **MemoryThresholdMonitor** (25 connections) — `server/app/memory_cleanup_service.py`
- **test_memory_cleanup_service.py** (22 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **asyncio** (9 connections)
- **get_managed_task_cleanup_implementation_for_task_four_spec_compliance()** (6 connections) — `server/app/memory_cleanup_service.py`
- **test_task_four_spec_factory()** (5 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_active_task_count_with_loop()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_memory_status_report()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_execution_failure()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_skips_on_cooldown()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_skips_when_below_threshold()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_success()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_managed_task_cleanup_timeout()** (4 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_flush_memory_indexes_cache_error()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_active_task_count_no_loop()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_current_memory_usage_failure()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **test_get_current_memory_usage_success()** (3 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Factory function returning implementation conforming to Task 4.3 Specified…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Runtime monitor for detecting memory threshold violations requiring cleanup.…** (1 connections) — `server/app/memory_cleanup_service.py`
- **Unit tests for memory threshold monitoring and managed task cleanup.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Threshold breach triggers orphan cleanup via tracked manager.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Cleanup timeout returns -1.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Unexpected cleanup errors return -2.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Legacy factory delegates to monitor.managed_task_cleanup.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Process memory query returns a positive byte count.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **Memory query failures return zero instead of raising.** (1 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [Memory Lifespan Coordinator](Memory_Lifespan_Coordinator.md) (8 shared connections)
- [Memory Cleanup Service](Memory_Cleanup_Service.md) (6 shared connections)
- [Test Memory Cleanup Service](Test_Memory_Cleanup_Service.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/tests/unit/app/test_memory_cleanup_service.py`

## Audit Trail

- EXTRACTED: 58 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*