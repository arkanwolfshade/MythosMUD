# headers middleware security

> 4 nodes

## Key Concepts

- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **Patrol the NPC's territory.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle patrolling territory action.** (1 connections) — `server/npc/aggressive_mob_npc.py`

## Relationships

- [error logging rationale](error_logging_rationale.md) (2 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*