# Lock

> 9 nodes

## Key Concepts

- **Lock** (8 connections)
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **HolidayResolver** (1 connections)
- **Initialize metrics collector. AI: Uses Lock for thread-safety in async context.** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize the communication bridge.** (1 connections) — `server/npc/threading.py`
- **Get or create the async lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`

## Relationships

- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 14 (70%)
- INFERRED: 6 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*