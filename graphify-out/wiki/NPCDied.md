# NPCDied

> 121 nodes

## Key Concepts

- **NPCDied** (29 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleState** (24 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_mark_despawned_logs_failure()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- *... and 96 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (83 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (7 shared connections)
- [.__post_init__](__post_init__.md) (5 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [EventHandler](EventHandler.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (1 shared connections)
- [quest_service](quest_service.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 289 (84%)
- INFERRED: 54 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*