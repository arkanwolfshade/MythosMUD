# Services Combat Initialization

> 14 nodes · cohesion 0.21

## Key Concepts

- **combat_initialization.py** (10 connections) — `server/services/combat_initialization.py`
- **.create_combat_instance()** (7 connections) — `server/services/combat_initialization.py`
- **_build_participant()** (6 connections) — `server/services/combat_initialization.py`
- **_build_combat_instance()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **CombatParticipantData** (4 connections) — `server/services/combat_initialization.py`
- **CombatInstance** (3 connections) — `server/services/combat_initialization.py`
- **UUID** (3 connections) — `server/services/combat_initialization.py`
- **CombatParticipant** (2 connections) — `server/services/combat_initialization.py`
- **Combat initialization logic.  Handles creation and setup of combat instances.** (1 connections) — `server/services/combat_initialization.py`
- **Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds * 10** (1 connections) — `server/services/combat_initialization.py`
- **Build CombatParticipant from CombatParticipantData.** (1 connections) — `server/services/combat_initialization.py`
- **Return participant IDs sorted by dexterity (highest first).** (1 connections) — `server/services/combat_initialization.py`
- **Create and initialize a combat instance.** (1 connections) — `server/services/combat_initialization.py`

## Relationships

- [[Combat Service Bundle]] (7 shared connections)
- [[Combat Taunt Tests]] (4 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/combat_initialization.py`

## Audit Trail

- EXTRACTED: 46 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
