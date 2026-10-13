# Community 451

> 39 nodes

## Key Concepts

- **NPCCommunicationIntegration** (24 connections) — `server/npc/communication_integration.py`
- **test_communication_integration.py** (16 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **communication_integration.py** (13 connections) — `server/npc/communication_integration.py`
- **NPCSpoke** (10 connections) — `server/events/event_types.py`
- **subscribe_npc_spoke_to_chat()** (6 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (5 connections) — `server/game/chat_npc_system.py`
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
- *... and 14 more nodes in this community*

## Relationships

- [Game Event Types](Game_Event_Types.md) (5 shared connections)
- [Community 301](Community_301.md) (4 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (4 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Chat Service](Chat_Service.md) (2 shared connections)
- [Community 318](Community_318.md) (1 shared connections)
- [Community 54](Community_54.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/chat_npc_system.py`
- `server/npc/communication_integration.py`
- `server/tests/unit/npc/test_communication_integration.py`

## Audit Trail

- EXTRACTED: 79 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*