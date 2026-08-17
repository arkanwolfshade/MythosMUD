# Any

> 23 nodes

## Key Concepts

- **Any** (14 connections)
- **._execute_wander_movement()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (6 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (5 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (4 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.get_messages()** (3 connections) — `server/npc/threading.py`
- **Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…** (1 connections) — `server/npc/threading.py`
- **Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…** (1 connections) — `server/npc/threading.py`
- **Resolve active NPC instance and definition for a WANDER action.** (1 connections) — `server/npc/threading.py`
- **Parse NPC behavior config from instance attribute (dict or JSON string).** (1 connections) — `server/npc/threading.py`
- **Run idle movement for a resolved wander NPC.** (1 connections) — `server/npc/threading.py`
- **Process a WANDER action for idle movement. Args: npc_id: ID of the NPC to move…** (1 connections) — `server/npc/threading.py`
- **Send a message to a specific NPC. Args: npc_id: The NPC's ID message: The…** (1 connections) — `server/npc/threading.py`
- **Receive a message from a specific NPC. Args: npc_id: The NPC's ID message: The…** (1 connections) — `server/npc/threading.py`
- **Broadcast a message to all NPCs. Args: message: The message to broadcast…** (1 connections) — `server/npc/threading.py`
- **Get all pending outgoing messages from NPCs.** (1 connections) — `server/npc/threading.py`
- **Get pending messages for a specific NPC.** (1 connections) — `server/npc/threading.py`

## Relationships

- [NPCThreadManager](NPCThreadManager.md) (13 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*