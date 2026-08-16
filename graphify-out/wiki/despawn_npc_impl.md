# despawn_npc_impl

> 26 nodes

## Key Concepts

- **despawn_npc_impl()** (20 connections) — `server/npc/lifecycle_despawn.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **NPCLifecycleEvent** (13 connections) — `server/npc/lifecycle_types.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_resolve_despawn_room_id()** (6 connections) — `server/npc/lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **test_despawn_exception_sets_error_state()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_success_with_persistence_and_room()** (5 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_despawn_prefers_current_room_over_room_id()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_publishes_event_without_persistence()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_record_only_when_not_active()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_skips_left_event_when_room_unknown()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_uses_lifecycle_spawn_room_when_attrs_missing()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_without_population_controller()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (3 connections)
- **test_despawn_nonexistent_npc_returns_false()** (2 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **NPC despawn logic for lifecycle. Extracted from lifecycle_manager to keep file…** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Prefer live NPC room attrs, then lifecycle SPAWNED/left event room_id.** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Mutate room occupants or publish NPCLeftRoom; skip unknown rooms.** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Despawn an NPC instance. Args: manager: NPCLifecycleManager instance. npc_id:…** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Despawn an NPC instance (delegates to lifecycle_despawn).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Enumeration of NPC lifecycle events.** (1 connections) — `server/npc/lifecycle_types.py`
- *... and 1 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (6 shared connections)
- [NPCDied](NPCDied.md) (5 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [.add_event](add_event.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`

## Audit Trail

- EXTRACTED: 73 (88%)
- INFERRED: 10 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*