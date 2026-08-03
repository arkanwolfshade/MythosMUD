# player realtime event

> 24 nodes

## Key Concepts

- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **.npc_entered()** (4 connections) — `server/models/room.py`
- **.create_npc_instance()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._get_room_for_spawn()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_exception()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._generate_npc_id()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._start_npc_thread_async()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._cleanup_failed_spawn()** (3 connections) — `server/npc/lifecycle_manager.py`
- **Add an NPC to the room and trigger event.          Args:             npc_id: The** (1 connections) — `server/models/room.py`
- **Create an NPC instance or return None on failure.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Get room from persistence and handle errors.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Clean up lifecycle record and active NPCs on spawn failure.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Queue NPC thread start, handling async event loop if available.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Spawn an NPC instance.          Thin wrapper around _spawn_npc_impl to keep pu** (1 connections) — `server/npc/lifecycle_manager.py`
- **Internal implementation for spawning an NPC with full error handling.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Handle failure when the spawning service cannot create an NPC instance.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Notify room of NPC entry and queue thread start if needed.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Handle logging and lifecycle updates for a failed spawn.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Generate a unique NPC ID.          Args:             definition: NPC definiti** (1 connections) — `server/npc/lifecycle_manager.py`
- **Start NPC thread asynchronously for behavior execution.          Args:** (1 connections) — `server/npc/lifecycle_manager.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (14 shared connections)
- [models npc rationale](models_npc_rationale.md) (10 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/npc/lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 70 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*