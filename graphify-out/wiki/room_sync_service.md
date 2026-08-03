# room sync service

> 15 nodes

## Key Concepts

- **__init__.py** (9 connections) — `server/schemas/quest/__init__.py`
- **quest.py** (8 connections) — `server/schemas/quest/quest.py`
- **QuestLogEntryResponse** (7 connections) — `server/schemas/quest/quest.py`
- **QuestLogResponse** (7 connections) — `server/schemas/quest/quest.py`
- **BaseModel** (6 connections)
- **QuestGoalSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestRewardSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestTriggerSchema** (4 connections) — `server/schemas/quest/quest.py`
- **Quest subsystem schemas: definition, progress, API responses.** (1 connections) — `server/schemas/quest/__init__.py`
- **Quest subsystem Pydantic schemas for MythosMUD server.  Defines schemas for ques** (1 connections) — `server/schemas/quest/quest.py`
- **Single goal in a quest definition (complete_activity, kill_n, collect_n, etc.).** (1 connections) — `server/schemas/quest/quest.py`
- **Single reward in a quest definition (xp, item, spell).** (1 connections) — `server/schemas/quest/quest.py`
- **Single trigger that can start a quest (room, npc, item).** (1 connections) — `server/schemas/quest/quest.py`
- **Single quest entry in GET /quests (quest log) response.** (1 connections) — `server/schemas/quest/quest.py`
- **Response model for GET /quests (quest log).** (1 connections) — `server/schemas/quest/quest.py`

## Relationships

- [admin auth service](admin_auth_service.md) (3 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)

## Source Files

- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*