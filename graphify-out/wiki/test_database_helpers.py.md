# test_database_helpers.py

> 110 nodes · cohesion 0.04

## Key Concepts

- **test_chat_npc_system.py** (50 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (43 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (15 connections) — `server/game/chat_npc_system.py`
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
- **npc_sender_id()** (7 connections) — `server/game/chat_npc_system.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 85 more nodes in this community*

## Relationships

- [PassiveMobNPC](PassiveMobNPC.md) (11 shared connections)
- [BaseEvent](BaseEvent.md) (10 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (10 shared connections)
- [deque](deque.md) (10 shared connections)
- [look_container.py](look_container.py.md) (9 shared connections)
- [test_skill_service_graded.py](test_skill_service_graded.py.md) (9 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (7 shared connections)
- [properties](properties.md) (6 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (5 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/realtime/test_chat_segments.py`

## Audit Trail

- EXTRACTED: 312 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*