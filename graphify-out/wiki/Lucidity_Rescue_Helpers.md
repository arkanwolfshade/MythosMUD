# Lucidity Rescue Helpers

> 57 nodes · cohesion 0.05

## Key Concepts

- **NPCThreadManager** (22 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **Any** (11 connections)
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.clear_messages()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.get_npc_definition()** (3 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- *... and 32 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (15 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (3 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (2 shared connections)
- [App Router Integration](App_Router_Integration.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 167 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*