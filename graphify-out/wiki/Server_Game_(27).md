# Server Game (27)

> 28 nodes

## Key Concepts

- **quest_chat_notify.py** (16 connections) — `server/game/quest/quest_chat_notify.py`
- **schedule_personal_system()** (10 connections) — `server/game/chat_npc_system.py`
- **notify_quest_started()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_progress()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_completed()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **notify_quest_abandoned()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **test_notify_quest_lifecycle_schedules_personal_system()** (6 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **UUID** (5 connections)
- **emit_quest_npc_say()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **title_from_quest_result()** (5 connections) — `server/game/quest/quest_chat_notify.py`
- **test_emit_quest_npc_say_and_templates()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **quest_ask_npc_line()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (4 connections) — `server/game/quest/quest_chat_notify.py`
- **test_title_from_quest_result_prefers_title_field()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Schedule personal system chat from sync or async callers.** (1 connections) — `server/game/chat_npc_system.py`
- **Any** (1 connections)
- **Quest lifecycle and NPC quest-line chat helpers (issue #146 MVP).  # ponytail:** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest becomes active.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat on every progress tick (debug volume).** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest completes.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Personal system chat when a quest is abandoned.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Room say-shaped NPC line for quest ask/turnin.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Template NPC speech when offering/starting a quest.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Template NPC speech when accepting a turn-in.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- **Extract quest title from a QuestService result message, if successful.** (1 connections) — `server/game/quest/quest_chat_notify.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Game (16)](Server_Game_%2816%29.md) (19 shared connections)
- [Server Commands (18)](Server_Commands_%2818%29.md) (1 shared connections)
- [Server Game (44)](Server_Game_%2844%29.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*