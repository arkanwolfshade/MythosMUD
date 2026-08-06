# dialogue definitions admin

> 46 nodes

## Key Concepts

- **PeriodicOrphanAuditor** (23 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_memory_lifespan_coordinator.py** (17 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **memory_lifespan_coordinator.py** (11 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_lifespan_memory_service()** (5 connections) — `server/app/memory_lifespan_coordinator.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **test_create_lifespan_memory_service()** (4 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **auditor()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_success()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_already_running()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_schedule_periodic_auditing_init_failure()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_with_cleanup()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_no_cleanup()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_do_full_cleanup_audit_handles_errors()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_force_single_audit_cycle_with_cleanup()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_force_single_audit_cycle_no_orphans()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_stop_audit_scheduler_not_running()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_stop_audit_scheduler_cancels_task()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **test_background_audit_cycle_cancelled()** (3 connections) — `server/tests/unit/app/test_memory_lifespan_coordinator.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **Any** (1 connections)
- **Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task Pr** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Periodic background auditor that investigates orphanage patterns and memory cond** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- *... and 21 more nodes in this community*

## Relationships

- [schemas player rationale](schemas_player_rationale.md) (6 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/tests/unit/app/test_memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 136 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*