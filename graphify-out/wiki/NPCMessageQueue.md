# NPCMessageQueue

> 21 nodes

## Key Concepts

- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **Lock** (8 connections)
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.get_messages()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **.clear_messages()** (2 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/npc/threading.py`
- **Initialize metrics collector. AI: Uses Lock for thread-safety in async context.** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…** (1 connections) — `server/npc/threading.py`
- **Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…** (1 connections) — `server/npc/threading.py`
- **Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…** (1 connections) — `server/npc/threading.py`
- **Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:…** (1 connections) — `server/npc/threading.py`
- **Get the number of pending messages for an NPC.** (1 connections) — `server/npc/threading.py`
- **Get the total number of pending messages across all NPCs.** (1 connections) — `server/npc/threading.py`
- **Initialize the NPC thread manager.** (1 connections) — `server/npc/threading.py`
- **Thread-safe message queue for NPC actions. This queue handles pending actions…** (1 connections) — `server/npc/threading.py`
- **Get or create the async lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`

## Relationships

- [EventBus](EventBus.md) (5 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 26 (79%)
- INFERRED: 7 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*