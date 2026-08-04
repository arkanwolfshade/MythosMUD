# idle npc movement

> 22 nodes

## Key Concepts

- **NPCCommunicationBridge** (14 connections) — `server/npc/threading.py`
- **Any** (11 connections)
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **test_npc_communication_bridge_messages()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_receive_message_failure()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_broadcast_failure()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Add a message to an NPC's pending message queue.          Args:             npc_** (1 connections) — `server/npc/threading.py`
- **Process a message for an NPC.** (1 connections) — `server/npc/threading.py`
- **Process a WANDER action for idle movement.          Args:             npc_id: ID** (1 connections) — `server/npc/threading.py`
- **Bridge for communication between NPC threads and main game thread.      This cla** (1 connections) — `server/npc/threading.py`
- **Send a message to a specific NPC.          Args:             npc_id: The NPC's I** (1 connections) — `server/npc/threading.py`
- **Receive a message from a specific NPC.          Args:             npc_id: The NP** (1 connections) — `server/npc/threading.py`
- **Broadcast a message to all NPCs.          Args:             message: The message** (1 connections) — `server/npc/threading.py`
- **Get all pending outgoing messages from NPCs.** (1 connections) — `server/npc/threading.py`
- **Get pending messages for a specific NPC.** (1 connections) — `server/npc/threading.py`

## Relationships

- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (9 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (2 shared connections)
- [idle movement npc](idle_movement_npc.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [logging setup structured](logging_setup_structured.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*