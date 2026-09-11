# should_notify_quest_progress

> 11 nodes

## Key Concepts

- **should_notify_quest_progress()** (10 connections) — `server/game/quest/quest_chat_notify.py`
- **_goal_is_met()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **_progress_has_any_value()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **Any** (4 connections)
- **_as_int()** (3 connections) — `server/game/quest/quest_chat_notify.py`
- **test_should_notify_quest_progress_milestones()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Coerce progress/config scalars to int; non-numeric becomes default.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Return True if one goal is satisfied given current progress.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **True if any goal slot has a non-zero / non-empty progress value.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Return True when a progress personal-system line should be sent. Notifies on…** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Progress chat only on first tick or newly met goal; never on completing tick.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`

## Relationships

- [test_chat_npc_system.py](test_chat_npc_system.py.md) (6 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [quest_commands.py](quest_commands.py.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*