# test_chat_npc_system.py

> 99 nodes

## Key Concepts

- **test_chat_npc_system.py** (47 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (34 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
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
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 74 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (17 shared connections)
- [QuestService](QuestService.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [quest_commands.py](quest_commands.py.md) (9 shared connections)
- [NPCBase](NPCBase.md) (5 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [talk_command.py](talk_command.py.md) (3 shared connections)
- [.initialize](initialize.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 248 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*