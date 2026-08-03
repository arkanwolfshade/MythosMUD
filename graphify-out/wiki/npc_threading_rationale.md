# npc threading rationale

> 17 nodes

## Key Concepts

- **Any** (11 connections)
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **Add a message to an NPC's pending message queue.          Args:             npc_** (1 connections) — `server/npc/threading.py`
- **Bridge for communication between NPC threads and main game thread.      This cla** (1 connections) — `server/npc/threading.py`
- **Initialize the communication bridge.** (1 connections) — `server/npc/threading.py`
- **Send a message to a specific NPC.          Args:             npc_id: The NPC's I** (1 connections) — `server/npc/threading.py`
- **Receive a message from a specific NPC.          Args:             npc_id: The NP** (1 connections) — `server/npc/threading.py`
- **Broadcast a message to all NPCs.          Args:             message: The message** (1 connections) — `server/npc/threading.py`
- **Get all pending outgoing messages from NPCs.** (1 connections) — `server/npc/threading.py`
- **Get pending messages for a specific NPC.** (1 connections) — `server/npc/threading.py`

## Relationships

- [combat services initialization](combat_services_initialization.md) (2 shared connections)
- [combat service services](combat_service_services.md) (2 shared connections)
- [services combat sync](services_combat_sync.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*