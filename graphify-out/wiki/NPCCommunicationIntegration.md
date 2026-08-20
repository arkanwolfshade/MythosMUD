# NPCCommunicationIntegration

> 33 nodes

## Key Concepts

- **NPCCommunicationIntegration** (24 connections) — `server/npc/communication_integration.py`
- **server/npc/__init__.py** (19 connections) — `server/npc/__init__.py`
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
- *... and 8 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [population_control.py](population_control.py.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)

## Source Files

- `server/npc/__init__.py`
- `server/npc/communication_integration.py`
- `server/tests/unit/npc/test_communication_integration.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*