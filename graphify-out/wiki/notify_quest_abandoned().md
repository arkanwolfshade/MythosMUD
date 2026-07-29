# notify quest abandoned()

> 11 nodes

## Key Concepts

- **notify_quest_progress()** (8 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_started()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (5 connections)
- **Quest notify helpers schedule personal system chat with expected text.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Personal system chat when a quest becomes active.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat on every progress tick (debug volume).** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest completes.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest is abandoned.** (1 connections) — `server/game/quest/quest_chat_notify.py`

## Relationships

- [ExitStack](ExitStack.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [QuestCompleted](QuestCompleted.md) (5 shared connections)
- [collect inventory](collect_inventory.md) (4 shared connections)

## Source Files

- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*