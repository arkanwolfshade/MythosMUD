# Lock

> 9 nodes

## Key Concepts

- **Lock** (8 connections)
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **Initialize metrics collector. AI: Uses Lock for thread-safety in async context.** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize the communication bridge.** (1 connections) — `server/npc/threading.py`
- **Initialize the NPC thread manager.** (1 connections) — `server/npc/threading.py`
- **Get or create the async lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`

## Relationships

- [test_npc_threading_messages.py](test_npc_threading_messages.py.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 11 (65%)
- INFERRED: 6 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*