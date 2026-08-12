# _PopulationLifecycleManager

> 13 nodes

## Key Concepts

- **_PopulationLifecycleManager** (13 connections) — `server/npc/population_control.py`
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

- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)
- [test_population_control.py](test_population_control.py.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 20 (71%)
- INFERRED: 8 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*