# Quest Schemas

> 12 nodes · cohesion 0.23

## Key Concepts

- **quest.py** (8 connections) — `server/schemas/quest/quest.py`
- **__init__.py** (8 connections) — `server/schemas/quest/__init__.py`
- **QuestDefinitionSchema** (5 connections) — `server/schemas/quest/quest.py`
- **QuestGoalSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestRewardSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestTriggerSchema** (4 connections) — `server/schemas/quest/quest.py`
- **Quest subsystem Pydantic schemas for MythosMUD server.  Defines schemas for ques** (1 connections) — `server/schemas/quest/quest.py`
- **Single goal in a quest definition (complete_activity, kill_n, etc.).** (1 connections) — `server/schemas/quest/quest.py`
- **Single reward in a quest definition (xp, item, spell).** (1 connections) — `server/schemas/quest/quest.py`
- **Single trigger that can start a quest (room, npc, item).** (1 connections) — `server/schemas/quest/quest.py`
- **Parsed quest definition (stored as JSONB in quest_definitions.definition).** (1 connections) — `server/schemas/quest/quest.py`
- **Quest subsystem schemas: definition, progress, API responses.** (1 connections) — `server/schemas/quest/__init__.py`

## Relationships

- [[Admin NPC Schemas]] (8 shared connections)
- [[Quest Service Core]] (1 shared connections)

## Source Files

- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
