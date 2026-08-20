# PeriodicOrphanAuditor

> 47 nodes

## Key Concepts

- **PeriodicOrphanAuditor** (23 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_memory_lifespan_coordinator.py** (19 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **asyncio** (11 connections)
- **create_lifespan_memory_service()** (5 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
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
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_stop_audit_scheduler_not_running()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (3 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/tests/unit/app/test_memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 69 (85%)
- INFERRED: 12 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*