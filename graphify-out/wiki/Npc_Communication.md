# Npc Communication

> 18 nodes · cohesion 0.12

## Key Concepts

- **NPCCommunicationIntegration** (10 connections) — `server/npc/communication_integration.py`
- **.handle_player_message()** (4 connections) — `server/npc/communication_integration.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **._process_message_for_response()** (4 connections) — `server/npc/communication_integration.py`
- **.send_message_to_room()** (4 connections) — `server/npc/communication_integration.py`
- **.send_whisper_to_player()** (3 connections) — `server/npc/communication_integration.py`
- **.subscribe_to_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **.unsubscribe_from_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **Handle a message received by an NPC from a player.          Args:             np** (1 connections) — `server/npc/communication_integration.py`
- **Process a message to determine if the NPC should respond.          Args:** (1 connections) — `server/npc/communication_integration.py`
- **Subscribe an NPC to messages in a specific room.          Args:             npc_** (1 connections) — `server/npc/communication_integration.py`
- **Unsubscribe an NPC from messages in a specific room.          Args:** (1 connections) — `server/npc/communication_integration.py`
- **Integrates NPCs with the existing chat and whisper systems.      This class prov** (1 connections) — `server/npc/communication_integration.py`
- **Initialize the NPC communication integration.          Args:             event_b** (1 connections) — `server/npc/communication_integration.py`
- **Send a message from an NPC to a room.          Args:             npc_id: ID of t** (1 connections) — `server/npc/communication_integration.py`
- **Send a whisper from an NPC to a specific player.          Args:             npc_** (1 connections) — `server/npc/communication_integration.py`
- **ChatService** (1 connections) — `server/npc/communication_integration.py`
- **EventBus** (1 connections) — `server/npc/communication_integration.py`

## Relationships

- [[Distributed Event Bus]] (4 shared connections)
- [[Aggressive Mob NPC]] (1 shared connections)

## Source Files

- `server/npc/communication_integration.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
