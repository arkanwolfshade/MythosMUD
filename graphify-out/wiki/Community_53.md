# Community 53

> 126 nodes

## Key Concepts

- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **test_lifecycle_periodic.py** (42 connections) — `server/tests/unit/npc/test_lifecycle_periodic.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (22 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_periodic.py** (21 connections) — `server/npc/lifecycle_periodic.py`
- **test_lifecycle_despawn.py** (21 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **NPCDied** (19 connections) — `server/events/event_types.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **check_optional_npc_spawns_impl()** (13 connections) — `server/npc/lifecycle_periodic.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **_make_manager()** (12 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_attempt_optional_npc_spawn()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **run_periodic_maintenance_impl()** (11 connections) — `server/npc/lifecycle_periodic.py`
- **NPCMaintenanceConfig** (10 connections) — `server/config/npc_config.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **cleanup_old_records_impl()** (10 connections) — `server/npc/lifecycle_periodic.py`
- **_check_spawn_conditions_for_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **get_zone_key_for_definition()** (9 connections) — `server/npc/lifecycle_periodic.py`
- **_should_skip_optional_npc()** (9 connections) — `server/npc/lifecycle_periodic.py`
- *... and 101 more nodes in this community*

## Relationships

- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (26 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (21 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (20 shared connections)
- [Community 40](Community_40.md) (12 shared connections)
- [Game Event Types](Game_Event_Types.md) (6 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (6 shared connections)
- [Community 318](Community_318.md) (4 shared connections)
- [Community 550](Community_550.md) (2 shared connections)
- [Community 536](Community_536.md) (2 shared connections)
- [Community 893](Community_893.md) (1 shared connections)
- [Community 114](Community_114.md) (1 shared connections)
- [Community 231](Community_231.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_periodic.py`

## Audit Trail

- EXTRACTED: 356 (92%)
- INFERRED: 30 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*