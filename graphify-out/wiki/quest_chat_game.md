# quest chat game

> 72 nodes

## Key Concepts

- **test_chat_npc_system.py** (45 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **send_personal_system_message()** (11 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **deliver_npc_room_speech()** (8 connections) — `server/game/chat_npc_system.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **deliver_personal_system()** (7 connections) — `server/game/chat_npc_system.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **_mock_chat_service()** (7 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **resolve_npc_display_name()** (6 connections) — `server/npc/npc_display_names.py`
- **test_deliver_npc_room_speech_uses_registered_name()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (5 connections)
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **UUID** (4 connections)
- **Any** (4 connections)
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 47 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (24 shared connections)
- [quest game service](quest_game_service.md) (13 shared connections)
- [NATS Messaging](NATS_Messaging.md) (11 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (10 shared connections)
- [chat service game](chat_service_game.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [dialogue service game](dialogue_service_game.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/npc/npc_display_names.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 305 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*