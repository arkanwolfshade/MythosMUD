# Level and XP Curve

> 5 nodes · cohesion 0.40

## Key Concepts

- **.check_level_up()** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **UUID** (3 connections)
- **Grant experience points to a character and check for level-up.          Adds amo** (1 connections) — `server/game/level_service.py`
- **Recompute level from current total XP and persist if level increased.          U** (1 connections) — `server/game/level_service.py`

## Relationships

- [Commands Npc Admin](Commands_Npc_Admin.md) (2 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*