# Community 1127

> 11 nodes

## Key Concepts

- **LevelService** (8 connections) — `server/game/level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.__init__()** (4 connections) — `server/game/level_service.py`
- **UUID** (3 connections)
- **LevelUpHook** (1 connections)
- **Any** (1 connections)
- **Service for character level and XP: grant XP, recompute level from curve, run…** (1 connections) — `server/game/level_service.py`
- **Initialize the level service. Args: async_persistence: Async persistence for…** (1 connections) — `server/game/level_service.py`
- **Grant experience points to a character and check for level-up. Adds amount to…** (1 connections) — `server/game/level_service.py`
- **Recompute level from current total XP and persist if level increased. Use when…** (1 connections) — `server/game/level_service.py`

## Relationships

- [Community 841](Community_841.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 1416](Community_1416.md) (2 shared connections)
- [Community 1360](Community_1360.md) (1 shared connections)

## Source Files

- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 16 (89%)
- INFERRED: 2 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*