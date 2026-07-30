# .initialize()

> 71 nodes

## Key Concepts

- **test_chat_npc_system.py** (43 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **quest_chat_notify.py** (16 connections) — `server/game/quest/quest_chat_notify.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **schedule_personal_system()** (10 connections) — `server/game/chat_npc_system.py`
- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **schedule_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_on_npc_spoke()** (6 connections) — `server/game/chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (5 connections)
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **schedule_coro()** (4 connections) — `server/game/chat_npc_system.py`
- **UUID** (4 connections)
- *... and 46 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (29 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (11 shared connections)
- [QuestCompleted](QuestCompleted.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (9 shared connections)
- [test command parser](test_command_parser.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 294 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*