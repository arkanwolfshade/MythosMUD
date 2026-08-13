# NPCCommunicationIntegration

> 16 nodes

## Key Concepts

- **NPCCommunicationIntegration** (10 connections) — `server/npc/communication_integration.py`
- **.handle_player_message()** (4 connections) — `server/npc/communication_integration.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **._process_message_for_response()** (4 connections) — `server/npc/communication_integration.py`
- **.send_message_to_room()** (4 connections) — `server/npc/communication_integration.py`
- **.send_whisper_to_player()** (3 connections) — `server/npc/communication_integration.py`
- **.subscribe_to_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **.unsubscribe_from_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/communication_integration.py`
- **Process a message to determine if the NPC should respond. Args: npc_id: ID of…** (1 connections) — `server/npc/communication_integration.py`
- **Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…** (1 connections) — `server/npc/communication_integration.py`
- **Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…** (1 connections) — `server/npc/communication_integration.py`
- **Integrates NPCs with the existing chat and whisper systems. This class provides…** (1 connections) — `server/npc/communication_integration.py`
- **Initialize the NPC communication integration. Args: event_bus: Optional…** (1 connections) — `server/npc/communication_integration.py`
- **Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the…** (1 connections) — `server/npc/communication_integration.py`
- **Send a whisper from an NPC to a specific player. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/communication_integration.py`

## Relationships

- [event_types.py](event_types.py.md) (4 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/npc/communication_integration.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*