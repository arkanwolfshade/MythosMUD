# game chat moderation

> 28 nodes

## Key Concepts

- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (5 connections)
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_coro()** (4 connections) — `server/game/chat_npc_system.py`
- **Any** (4 connections)
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **_as_int()** (3 connections) — `server/game/quest/quest_chat_notify.py`
- **test_should_notify_quest_progress_milestones()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Fire-and-forget a coroutine on the running loop when available.** (1 connections) — `server/game/chat_npc_system.py`
- **Schedule personal system chat from sync or async callers.** (1 connections) — `server/game/chat_npc_system.py`
- **Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP).  # group: ques** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest becomes active.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat for milestone progress (first tick or goal newly met).** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest completes.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest is abandoned.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Coerce progress/config scalars to int; non-numeric becomes default.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Return True if one goal is satisfied given current progress.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **True if any goal slot has a non-zero / non-empty progress value.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 3 more nodes in this community*

## Relationships

- [quest chat game](quest_chat_game.md) (13 shared connections)
- [quest game service](quest_game_service.md) (13 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [dialogue service game](dialogue_service_game.md) (2 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 122 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*