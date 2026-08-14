# quest_chat_notify.py

> 26 nodes

## Key Concepts

- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (9 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **UUID** (5 connections)
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **Any** (4 connections)
- **_as_int()** (3 connections) — `server/game/quest/quest_chat_notify.py`
- **test_should_notify_quest_progress_milestones()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Schedule personal system chat from sync or async callers.** (1 connections) — `server/game/chat_npc_system.py`
- **Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP). # group:…** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest becomes active.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat for milestone progress (first tick or goal newly met).** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest completes.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest is abandoned.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Coerce progress/config scalars to int; non-numeric becomes default.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Return True if one goal is satisfied given current progress.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **True if any goal slot has a non-zero / non-empty progress value.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Return True when a progress personal-system line should be sent. Notifies on…** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Quest notify helpers schedule personal system chat with expected text.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 1 more nodes in this community*

## Relationships

- [chat_service.py](chat_service.py.md) (14 shared connections)
- [QuestService](QuestService.md) (13 shared connections)
- [quest_commands.py](quest_commands.py.md) (6 shared connections)
- [talk_command.py](talk_command.py.md) (2 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*