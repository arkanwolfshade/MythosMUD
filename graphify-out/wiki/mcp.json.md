# mcp.json

> 13 nodes · cohesion 0.24

## Key Concepts

- **schemas/quest/__init__.py** (10 connections) — `server/schemas/quest/__init__.py`
- **quest/quest.py** (8 connections) — `server/schemas/quest/quest.py`
- **QuestLogEntryResponse** (7 connections) — `server/schemas/quest/quest.py`
- **QuestLogResponse** (7 connections) — `server/schemas/quest/quest.py`
- **BaseModel** (6 connections)
- **QuestGoalSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestTriggerSchema** (4 connections) — `server/schemas/quest/quest.py`
- **Quest subsystem schemas: definition, progress, API responses.** (1 connections) — `server/schemas/quest/__init__.py`
- **Quest subsystem Pydantic schemas for MythosMUD server. Defines schemas for…** (1 connections) — `server/schemas/quest/quest.py`
- **Single goal in a quest definition (complete_activity, kill_n, collect_n, etc.).** (1 connections) — `server/schemas/quest/quest.py`
- **Single trigger that can start a quest (room, npc, item).** (1 connections) — `server/schemas/quest/quest.py`
- **Single quest entry in GET /quests (quest log) response.** (1 connections) — `server/schemas/quest/quest.py`
- **Response model for GET /quests (quest log).** (1 connections) — `server/schemas/quest/quest.py`

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (3 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (3 shared connections)

## Source Files

- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*