# Quest

> 15 nodes

## Key Concepts

- **schemas/quest/__init__.py** (10 connections) — `server/schemas/quest/__init__.py`
- **quest/quest.py** (9 connections) — `server/schemas/quest/quest.py`
- **BaseModel** (6 connections)
- **QuestLogEntryResponse** (5 connections) — `server/schemas/quest/quest.py`
- **QuestLogResponse** (5 connections) — `server/schemas/quest/quest.py`
- **QuestGoalSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestRewardSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestTriggerSchema** (4 connections) — `server/schemas/quest/quest.py`
- **Quest subsystem schemas: definition, progress, API responses.** (1 connections) — `server/schemas/quest/__init__.py`
- **Quest subsystem Pydantic schemas for MythosMUD server. Defines schemas for…** (1 connections) — `server/schemas/quest/quest.py`
- **Single goal in a quest definition (complete_activity, kill_n, collect_n, etc.).** (1 connections) — `server/schemas/quest/quest.py`
- **Single reward in a quest definition (xp, item, spell).** (1 connections) — `server/schemas/quest/quest.py`
- **Single trigger that can start a quest (room, npc, item).** (1 connections) — `server/schemas/quest/quest.py`
- **Single quest entry in GET /quests (quest log) response.** (1 connections) — `server/schemas/quest/quest.py`
- **Response model for GET /quests (quest log).** (1 connections) — `server/schemas/quest/quest.py`

## Relationships

- [Npc Admin](Npc_Admin.md) (3 shared connections)
- [Quest Service](Quest_Service.md) (3 shared connections)
- [Players](Players.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)

## Source Files

- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*