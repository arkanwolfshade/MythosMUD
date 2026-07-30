# .initialize()

> 85 nodes

## Key Concepts

- **test_chat_npc_system.py** (43 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **chat_npc_system.py** (31 connections) — `server/game/chat_npc_system.py`
- **quest_chat_notify.py** (16 connections) — `server/game/quest/quest_chat_notify.py`
- **send_npc_say_to_room()** (13 connections) — `server/game/chat_npc_system.py`
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
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **_ChatDeliveryService** (7 connections) — `server/game/chat_npc_system.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_on_npc_spoke()** (6 connections) — `server/game/chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_send_npc_say_to_room_publishes_say_with_npc_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 60 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (19 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (16 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (11 shared connections)
- [QuestCompleted](QuestCompleted.md) (10 shared connections)
- [test command parser](test_command_parser.md) (4 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 373 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*