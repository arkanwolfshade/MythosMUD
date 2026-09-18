# Community 755

> 22 nodes

## Key Concepts

- **quest_chat_notify.py** (20 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (12 connections) — `server/game/chat_npc_system.py`
- **should_notify_quest_progress()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **UUID** (5 connections)
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **Any** (4 connections)
- **_as_int()** (3 connections) — `server/game/quest/quest_chat_notify.py`
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

## Relationships

- [Community 122](Community_122.md) (13 shared connections)
- [Community 160](Community_160.md) (7 shared connections)
- [Community 135](Community_135.md) (6 shared connections)
- [Community 506](Community_506.md) (2 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*