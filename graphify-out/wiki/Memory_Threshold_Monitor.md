# Memory Threshold Monitor

> 17 nodes · cohesion 0.13

## Key Concepts

- **PeriodicOrphanAuditor** (9 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **create_lifespan_memory_service()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **.__init__()** (3 connections) — `server/app/memory_lifespan_coordinator.py`
- **.stop_audit_scheduler()** (2 connections) — `server/app/memory_lifespan_coordinator.py`
- **Any** (1 connections)
- **Core capability for granular investigation cycles.          Repeated universal a** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Execute a single investigation loop synchronously producing operator summary.** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Stop the periodic orphan auditor background enforcement.** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Create a centralized memory operations coordinator instance targeted for     app** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Periodic background auditor that investigates orphanage patterns and memory cond** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Initialize the periodic orphan auditor.          Args:             check_interva** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Start the background auditing scheduler responsible for identifying orphan vecto** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Primary background cycle consuming auditor implementation.          Executes per** (1 connections) — `server/app/memory_lifespan_coordinator.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*