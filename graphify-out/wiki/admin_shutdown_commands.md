# admin shutdown commands

> 10 nodes

## Key Concepts

- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **.get_participants_by_initiative()** (4 connections) — `server/models/combat.py`
- **.apply_damage()** (3 connections) — `server/models/combat.py`
- **.is_combat_over()** (3 connections) — `server/models/combat.py`
- **Check if participant is dead.          For players: dead if DP <= -10         Fo** (1 connections) — `server/models/combat.py`
- **Apply damage to this participant and determine resulting death states.** (1 connections) — `server/models/combat.py`
- **Check if combat should end.          CRITICAL: Combat should NOT end when a play** (1 connections) — `server/models/combat.py`
- **Get all participants that are not dead (includes mortally wounded players at 0 D** (1 connections) — `server/models/combat.py`
- **Get all alive participants sorted by dexterity (highest first) for initiative or** (1 connections) — `server/models/combat.py`

## Relationships

- [Item Instances](Item_Instances.md) (4 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)

## Source Files

- `server/models/combat.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*