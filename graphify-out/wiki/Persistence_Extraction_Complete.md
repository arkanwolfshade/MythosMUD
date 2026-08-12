# Persistence Extraction Complete

> 5 nodes

## Key Concepts

- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **UUID** (3 connections)
- **Grant experience points to a character and check for level-up.          Adds amo** (1 connections) — `server/game/level_service.py`
- **Recompute level from current total XP and persist if level increased.          U** (1 connections) — `server/game/level_service.py`

## Relationships

- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (2 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*