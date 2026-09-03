# Lifecycle Manager

> 48 nodes

## Key Concepts

- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCDefinition** (11 connections)
- **.__init__()** (8 connections) — `server/npc/lifecycle_manager.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._generate_npc_id()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._get_room_for_spawn()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_exception()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._set_npc_room_tracking()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._start_npc_thread_async()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._validate_npc_room_tracking()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._cleanup_failed_spawn()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_npc_lifecycle_record()** (3 connections) — `server/npc/lifecycle_manager.py`
- **._subscribe_to_events()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.create_npc_instance()** (3 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (3 connections)
- **Protocol** (2 connections)
- **NPCPopulationController** (1 connections)
- **NPCThreadManager** (1 connections)
- *... and 23 more nodes in this community*

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (17 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*