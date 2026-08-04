# command parser rationale

> 20 nodes

## Key Concepts

- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **despawn_npc_impl()** (18 connections) — `server/npc/lifecycle_despawn.py`
- **_make_manager()** (10 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **_remove_npc_from_room_on_despawn()** (5 connections) — `server/npc/lifecycle_despawn.py`
- **test_despawn_publishes_event_when_room_missing()** (4 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Any** (3 connections)
- **.despawn_npc()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_despawn_success_with_persistence_and_room()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_publishes_event_without_persistence()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_record_only_when_not_active()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_exception_sets_error_state()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_without_population_controller()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_skips_left_event_when_room_unknown()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_prefers_current_room_over_room_id()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_uses_lifecycle_spawn_room_when_attrs_missing()** (3 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **test_despawn_nonexistent_npc_returns_false()** (2 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **Mutate room occupants or publish NPCLeftRoom; skip unknown rooms.** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Despawn an NPC instance.      Args:         manager: NPCLifecycleManager instanc** (1 connections) — `server/npc/lifecycle_despawn.py`
- **Despawn an NPC instance (delegates to lifecycle_despawn).** (1 connections) — `server/npc/lifecycle_manager.py`
- **Unit tests for NPC lifecycle despawn helpers.** (1 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [combat services rationale](combat_services_rationale.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`

## Audit Trail

- EXTRACTED: 91 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*