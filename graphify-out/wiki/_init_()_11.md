# . init ()

> 33 nodes

## Key Concepts

- **Any** (11 connections)
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading.py`
- **Convert message to JSON string.** (1 connections) — `server/npc/threading.py`
- **Thread-safe message queue for NPC actions.      This queue handles pending actio** (1 connections) — `server/npc/threading.py`
- **Initialize the NPC message queue.          Args:             max_messages_per_np** (1 connections) — `server/npc/threading.py`
- **Add a message to an NPC's pending message queue.          Args:             npc_** (1 connections) — `server/npc/threading.py`
- **Get all pending messages for an NPC.          Args:             npc_id: The NPC'** (1 connections) — `server/npc/threading.py`
- **Get the number of pending messages for an NPC.** (1 connections) — `server/npc/threading.py`
- **Get the total number of pending messages across all NPCs.** (1 connections) — `server/npc/threading.py`
- *... and 8 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (5 shared connections)
- [. repr ()](_repr_%28%29.md) (5 shared connections)
- [cfg float()](cfg_float%28%29.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [Lock](Lock.md) (2 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 86 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*