# NPC Room Lifecycle

> 182 nodes

## Key Concepts

- **NPCLifecycleManager** (58 connections) — `server/npc/lifecycle_manager.py`
- **test_npc_event_handlers.py** (45 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **NPCEnteredRoom** (34 connections) — `server/events/event_types.py`
- **NPCLeftRoom** (33 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (29 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **_make_manager()** (19 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **asyncio** (16 connections)
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **.get_lifecycle_statistics()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._generate_npc_id()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._get_room_for_spawn()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._handle_npc_entered_room()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_exception()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._set_npc_room_tracking()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._start_npc_thread_async()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._validate_npc_room_tracking()** (4 connections) — `server/npc/lifecycle_manager.py`
- *... and 157 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (31 shared connections)
- [Community 53](Community_53.md) (26 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (9 shared connections)
- [Community 40](Community_40.md) (8 shared connections)
- [Game Event Types](Game_Event_Types.md) (6 shared connections)
- [NPC Population Stats](NPC_Population_Stats.md) (4 shared connections)
- [Community 318](Community_318.md) (4 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (3 shared connections)
- [Community 395](Community_395.md) (2 shared connections)
- [Community 244](Community_244.md) (2 shared connections)
- [Community 77](Community_77.md) (2 shared connections)
- [Community 247](Community_247.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 329 (90%)
- INFERRED: 36 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*