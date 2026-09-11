# .__init__

> 13 nodes

## Key Concepts

- **_PopulationLifecycleManager** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- **.clear_population_stats()** (3 connections) — `server/npc/population_control.py`
- **._subscribe_to_events()** (3 connections) — `server/npc/population_control.py`
- **.spawn_npc()** (3 connections) — `server/npc/population_control.py`
- **Protocol** (1 connections)
- **Initialize the NPC population controller. Args: event_bus: Event bus for…** (1 connections) — `server/npc/population_control.py`
- **Load zone and sub-zone configurations from PostgreSQL database.** (1 connections) — `server/npc/population_control.py`
- **Subscribe to relevant game events.** (1 connections) — `server/npc/population_control.py`
- **Lifecycle manager surface used by NPCPopulationController (avoids import cycle…** (1 connections) — `server/npc/population_control.py`
- **Clear all population statistics. This ensures a clean state when the server…** (1 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance; returns (npc_id, None) or (None, failure_reason).** (1 connections) — `server/npc/population_control.py`

## Relationships

- [event_types.py](event_types.py.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*