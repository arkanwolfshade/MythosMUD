# NPCCommunicationIntegration

> 8 nodes

## Key Concepts

- **NPCCommunicationIntegration** (10 connections) — `server/npc/communication_integration.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **.subscribe_to_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **.unsubscribe_from_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…** (1 connections) — `server/npc/communication_integration.py`
- **Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…** (1 connections) — `server/npc/communication_integration.py`
- **Integrates NPCs with the existing chat and whisper systems. This class provides…** (1 connections) — `server/npc/communication_integration.py`
- **Initialize the NPC communication integration. Args: event_bus: Optional…** (1 connections) — `server/npc/communication_integration.py`

## Relationships

- [.handle_player_message](handle_player_message.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/npc/communication_integration.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*