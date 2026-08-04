# command exploration models

> 31 nodes

## Key Concepts

- **NPCCommunicationIntegration** (24 connections) — `server/npc/communication_integration.py`
- **test_communication_integration.py** (16 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **.__init__()** (4 connections) — `server/npc/communication_integration.py`
- **.send_message_to_room()** (4 connections) — `server/npc/communication_integration.py`
- **.handle_player_message()** (4 connections) — `server/npc/communication_integration.py`
- **._process_message_for_response()** (4 connections) — `server/npc/communication_integration.py`
- **.send_whisper_to_player()** (3 connections) — `server/npc/communication_integration.py`
- **.subscribe_to_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **.unsubscribe_from_room_messages()** (2 connections) — `server/npc/communication_integration.py`
- **test_send_message_to_room_publishes_event()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_send_whisper_to_player_publishes_event()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_handle_player_message_triggers_greeting_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_question_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_subscribe_and_unsubscribe_room_messages()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_send_message_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_help_and_thanks_responses()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_process_message_default_response()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_whisper_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_handle_player_message_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_subscribe_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_unsubscribe_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **test_init_without_event_bus_uses_default()** (2 connections) — `server/tests/unit/npc/test_communication_integration.py`
- **Integrates NPCs with the existing chat and whisper systems.      This class prov** (1 connections) — `server/npc/communication_integration.py`
- **Initialize the NPC communication integration.          Args:             event_b** (1 connections) — `server/npc/communication_integration.py`
- **Send a message from an NPC to a room.          Args:             npc_id: ID of t** (1 connections) — `server/npc/communication_integration.py`
- *... and 6 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [chat service game](chat_service_game.md) (1 shared connections)

## Source Files

- `server/npc/communication_integration.py`
- `server/tests/unit/npc/test_communication_integration.py`

## Audit Trail

- EXTRACTED: 98 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*