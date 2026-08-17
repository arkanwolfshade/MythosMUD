# server app memory lifespan coordinator

> 31 nodes

## Key Concepts

- **PeriodicOrphanAuditor** (23 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_memory_lifespan_coordinator.py** (19 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **asyncio** (11 connections)
- **create_lifespan_memory_service()** (5 connections) — `server/app/memory_lifespan_coordinator.py`
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
- **Create a centralized memory operations coordinator instance targeted for…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Periodic background auditor that investigates orphanage patterns and memory…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Unit tests for periodic orphan auditing and lifespan memory coordination.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **No orphans and no threshold breach skips cleanup.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Audit cycle errors are logged without propagating.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Manual audit returns summary and cleans detected orphans.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Manual audit skips cleanup when no orphans are found.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Stopping when idle is a no-op.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **Running scheduler cancels its coordinator task.** (1 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- *... and 6 more nodes in this community*

## Relationships

- [server app memory lifespan coordinator](server_app_memory_lifespan_coordinator.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server tests unit app test](server_tests_unit_app_test.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/tests/unit/app/test_memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 53 (80%)
- INFERRED: 13 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*