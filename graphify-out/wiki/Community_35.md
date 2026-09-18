# Community 35

> 154 nodes

## Key Concepts

- **NPCLifecycleManager** (64 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCLeftRoom** (32 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (29 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCDied** (27 connections) — `server/events/event_types.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (22 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (21 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (19 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **_make_manager()** (12 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- *... and 129 more nodes in this community*

## Relationships

- [NPC Event Types](NPC_Event_Types.md) (20 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (19 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (15 shared connections)
- [Community 131](Community_131.md) (15 shared connections)
- [Community 258](Community_258.md) (13 shared connections)
- [Event Bus](Event_Bus.md) (9 shared connections)
- [Community 91](Community_91.md) (8 shared connections)
- [Community 165](Community_165.md) (6 shared connections)
- [Community 149](Community_149.md) (5 shared connections)
- [Community 452](Community_452.md) (5 shared connections)
- [Community 624](Community_624.md) (5 shared connections)
- [NPC Follow System](NPC_Follow_System.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 410 (89%)
- INFERRED: 53 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*