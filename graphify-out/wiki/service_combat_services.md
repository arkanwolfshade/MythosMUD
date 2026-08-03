# service combat services

> 5 nodes

## Key Concepts

- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **UUID** (3 connections)
- **Grant experience points to a character and check for level-up.          Adds amo** (1 connections) — `server/game/level_service.py`
- **Recompute level from current total XP and persist if level increased.          U** (1 connections) — `server/game/level_service.py`

## Relationships

- [quests players rationale](quests_players_rationale.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*