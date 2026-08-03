# combat service services

> 20 nodes

## Key Concepts

- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.clear_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading.py`
- **Thread-safe message queue for NPC actions.      This queue handles pending actio** (1 connections) — `server/npc/threading.py`
- **Initialize the NPC message queue.          Args:             max_messages_per_np** (1 connections) — `server/npc/threading.py`
- **Get all pending messages for an NPC.          Args:             npc_id: The NPC'** (1 connections) — `server/npc/threading.py`
- **Clear all pending messages for an NPC.          Args:             npc_id: The NP** (1 connections) — `server/npc/threading.py`
- **Get the number of pending messages for an NPC.** (1 connections) — `server/npc/threading.py`
- **Get the total number of pending messages across all NPCs.** (1 connections) — `server/npc/threading.py`
- **Initialize the NPC thread manager.** (1 connections) — `server/npc/threading.py`
- **Stop the NPC thread manager and all active threads.          Returns:** (1 connections) — `server/npc/threading.py`
- **Stop a specific NPC thread.          Args:             npc_id: Unique identifier** (1 connections) — `server/npc/threading.py`
- **Internal method to stop an NPC thread.** (1 connections) — `server/npc/threading.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*