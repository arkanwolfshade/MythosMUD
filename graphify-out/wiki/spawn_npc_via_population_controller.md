# spawn_npc_via_population_controller

> 6 nodes

## Key Concepts

- **spawn_npc_via_population_controller()** (11 connections) — `server/npc/npc_utils.py`
- **test_spawn_npc_via_population_controller_falls_back_without_controller()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_spawn_npc_via_population_controller_routes_through_controller()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **Spawn an NPC through `population_controller.spawn_npc` when one is configured…** (1 connections) — `server/npc/npc_utils.py`
- **#768: with a population_controller configured, spawn must go through it (not…** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **No population_controller configured (e.g. minimal test setups): fall back to…** (1 connections) — `server/tests/unit/npc/test_npc_utils.py`

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (2 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 14 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*