# effect player repository

> 26 nodes

## Key Concepts

- **NPCCommunicationBridge** (14 connections) — `server/npc/threading.py`
- **Any** (11 connections)
- **Lock** (9 connections)
- **.__init__()** (3 connections) — `server/container/main.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/services/inventory_mutation_guard.py`
- **test_npc_communication_bridge_messages()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_receive_message_failure()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_broadcast_failure()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Initialize the container. Services are NOT initialized here - use initialize().** (1 connections) — `server/container/main.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Add a message to an NPC's pending message queue.          Args:             npc_** (1 connections) — `server/npc/threading.py`
- **Bridge for communication between NPC threads and main game thread.      This cla** (1 connections) — `server/npc/threading.py`
- **Initialize the communication bridge.** (1 connections) — `server/npc/threading.py`
- **Send a message to a specific NPC.          Args:             npc_id: The NPC's I** (1 connections) — `server/npc/threading.py`
- **Receive a message from a specific NPC.          Args:             npc_id: The NP** (1 connections) — `server/npc/threading.py`
- **Broadcast a message to all NPCs.          Args:             message: The message** (1 connections) — `server/npc/threading.py`
- **Get all pending outgoing messages from NPCs.** (1 connections) — `server/npc/threading.py`
- *... and 1 more nodes in this community*

## Relationships

- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (9 shared connections)
- [services npc startup](services_npc_startup.md) (2 shared connections)
- [room cache services](room_cache_services.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [command player state](command_player_state.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 69 (87%)
- INFERRED: 10 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*