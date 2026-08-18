# test_chat_npc_system.py

> 83 nodes

## Key Concepts

- **test_chat_npc_system.py** (47 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (34 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **asyncio** (8 connections)
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_personal_system_message_targets_player()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **npc_sender_id()** (5 connections) — `server/game/chat_npc_system.py`
- *... and 58 more nodes in this community*

## Relationships

- [quest_commands.py](quest_commands.py.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (10 shared connections)
- [chat_service.py](chat_service.py.md) (10 shared connections)
- [ChatMessage](ChatMessage.md) (7 shared connections)
- [QuestService](QuestService.md) (7 shared connections)
- [subscribe_npc_spoke_to_chat](subscribe_npc_spoke_to_chat.md) (6 shared connections)
- [quest_service.py](quest_service.py.md) (6 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 230 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*