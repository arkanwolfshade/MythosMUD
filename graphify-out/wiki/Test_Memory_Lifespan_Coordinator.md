# Test Memory Lifespan Coordinator

> 36 nodes

## Key Concepts

- **PeriodicOrphanAuditor** (23 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_memory_lifespan_coordinator.py** (19 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **asyncio** (11 connections)
- **create_lifespan_memory_service()** (5 connections) — `server/app/memory_lifespan_coordinator.py`
- **auditor()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_background_audit_cycle_cancelled()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_create_lifespan_memory_service()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_handles_errors()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_no_cleanup()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_with_cleanup()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_force_single_audit_cycle_no_orphans()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_force_single_audit_cycle_with_cleanup()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_already_running()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_init_failure()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_success()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_stop_audit_scheduler_cancels_task()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_stop_audit_scheduler_not_running()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **fixture** (1 connections)
- **Stop the periodic orphan auditor background enforcement.** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Create a centralized memory operations coordinator instance targeted for…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Periodic background auditor that investigates orphanage patterns and memory…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Unit tests for periodic orphan auditing and lifespan memory coordination.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **No orphans and no threshold breach skips cleanup.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Audit cycle errors are logged without propagating.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- *... and 11 more nodes in this community*

## Relationships

- [Memory Lifespan Coordinator](Memory_Lifespan_Coordinator.md) (8 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/tests/unit/app/test_memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 57 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*