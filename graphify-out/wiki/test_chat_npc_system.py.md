# test_chat_npc_system.py

> 69 nodes

## Key Concepts

- **test_chat_npc_system.py** (47 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (34 connections) — `server/game/chat_npc_system.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **asyncio** (8 connections)
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_personal_system_message_targets_player()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- **_on_npc_spoke()** (5 connections) — `server/game/chat_npc_system.py`
- **_reset_chat_npc_wiring()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_when_chat_service_unwired()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_publish_failure()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_rejects_empty_message_and_room()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_rejects_empty()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 44 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (14 shared connections)
- [quest_commands.py](quest_commands.py.md) (13 shared connections)
- [event_types.py](event_types.py.md) (10 shared connections)
- [QuestService](QuestService.md) (9 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)
- [chat_service.py](chat_service.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [NPCEventReaction](NPCEventReaction.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 189 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*