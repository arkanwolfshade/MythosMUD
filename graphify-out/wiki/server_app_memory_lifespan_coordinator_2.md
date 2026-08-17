# server app memory lifespan coordinator

> 6 nodes

## Key Concepts

- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **Core capability for granular investigation cycles. Repeated universal analysis…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Start the background auditing scheduler responsible for identifying orphan…** (1 connections) — `server/app/memory_lifespan_coordinator.py`
- **Primary background cycle consuming auditor implementation. Executes periodic…** (1 connections) — `server/app/memory_lifespan_coordinator.py`

## Relationships

- [server app memory lifespan coordinator](server_app_memory_lifespan_coordinator.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*