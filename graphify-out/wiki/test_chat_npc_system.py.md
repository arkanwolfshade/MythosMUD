# test_chat_npc_system.py

> 122 nodes

## Key Concepts

- **test_chat_npc_system.py** (50 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (43 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (15 connections) — `server/game/chat_npc_system.py`
- **NPCSpoke** (14 connections) — `server/events/event_types.py`
- **deliver_personal_system()** (14 connections) — `server/game/chat_npc_system.py`
- **send_fake_npc_whisper()** (14 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (14 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **deliver_fake_npc_whisper()** (11 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (10 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **asyncio** (10 connections)
- **deliver_npc_room_speech()** (9 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **_mock_chat_service()** (9 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_ChatDeliveryService** (8 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **npc_sender_id()** (7 connections) — `server/game/chat_npc_system.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 97 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (23 shared connections)
- [EventBus](EventBus.md) (14 shared connections)
- [get_username_from_user](get_username_from_user.md) (11 shared connections)
- [NpcDisposition](NpcDisposition.md) (9 shared connections)
- [QuestService](QuestService.md) (7 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (6 shared connections)
- [quest_service.py](quest_service.py.md) (6 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (6 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/events/event_types.py`
- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_base.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/realtime/test_chat_segments.py`

## Audit Trail

- EXTRACTED: 336 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*