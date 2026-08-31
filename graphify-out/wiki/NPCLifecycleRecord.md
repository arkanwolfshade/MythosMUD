# NPCLifecycleRecord

> 27 nodes

## Key Concepts

- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **._spawn_npc_impl()** (12 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- **._generate_npc_id()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._get_room_for_spawn()** (4 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_exception()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.change_state()** (4 connections) — `server/npc/lifecycle_types.py`
- **._cleanup_failed_spawn()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_npc_lifecycle_record()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.get_statistics()** (3 connections) — `server/npc/lifecycle_types.py`
- **.__init__()** (3 connections) — `server/npc/lifecycle_types.py`
- **Any** (2 connections)
- **Get room from persistence and handle errors.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Clean up lifecycle record and active NPCs on spawn failure.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Spawn an NPC instance. Thin wrapper around _spawn_npc_impl to keep public…** (1 connections) — `server/npc/lifecycle_manager.py`
- **Internal implementation for spawning an NPC with full error handling.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Handle failure when the spawning service cannot create an NPC instance.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Handle logging and lifecycle updates for a failed spawn.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Generate a unique NPC ID. Args: definition: NPC definition room_id: Room where…** (1 connections) — `server/npc/lifecycle_manager.py`
- **Get lifecycle record for an NPC. Args: npc_id: ID of the NPC Returns: Lifecycle…** (1 connections) — `server/npc/lifecycle_manager.py`
- **Return a snapshot of this record's stats (counts, times, state, age). Returns:…** (1 connections) — `server/npc/lifecycle_types.py`
- **Record of an NPC's lifecycle events and state changes.** (1 connections) — `server/npc/lifecycle_types.py`
- **Initialize lifecycle record for an NPC. Args: npc_id: Unique identifier for the…** (1 connections) — `server/npc/lifecycle_types.py`
- *... and 2 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (18 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*