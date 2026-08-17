# server npc communication integration npccommunicationintegration

> 31 nodes

## Key Concepts

- **NPCCommunicationIntegration** (24 connections) — `server/npc/communication_integration.py`
- **test_communication_integration.py** (16 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **.handle_player_message()** (4 connections) — `server/npc/communication_integration.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **._process_message_for_response()** (4 connections) — `server/npc/communication_integration.py`
- **.send_message_to_room()** (4 connections) — `server/npc/communication_integration.py`
- **.send_whisper_to_player()** (3 connections) — `server/npc/communication_integration.py`
- **.subscribe_to_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **.unsubscribe_from_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **test_handle_player_message_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_handle_player_message_triggers_greeting_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_init_without_event_bus_uses_default()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_default_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_help_and_thanks_responses()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_question_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_send_message_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_send_message_to_room_publishes_event()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_send_whisper_to_player_publishes_event()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_subscribe_and_unsubscribe_room_messages()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_subscribe_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_unsubscribe_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_whisper_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/communication_integration.py`
- **Process a message to determine if the NPC should respond. Args: npc_id: ID of…** (1 connections) — `server/npc/communication_integration.py`
- **Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…** (1 connections) — `server/npc/communication_integration.py`
- *... and 6 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (5 shared connections)
- [server npc init](server_npc_init.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (1 shared connections)

## Source Files

- `server/npc/communication_integration.py`
- `server/tests/unit/npc/test_communication_integration.py`

## Audit Trail

- EXTRACTED: 40 (75%)
- INFERRED: 13 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*