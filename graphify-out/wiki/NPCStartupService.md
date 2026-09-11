# NPCStartupService

> 34 nodes

## Key Concepts

- **NPCStartupService** (54 connections) — `server/services/npc_startup_service.py`
- **Any** (17 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **_merge_phase_into_startup()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_persistence_for_spawn()** (3 connections) — `server/services/npc_startup_service.py`
- **._handle_required_no_room()** (3 connections) — `server/services/npc_startup_service.py`
- **.__init__()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_fallback_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_specific_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._warmup_room_cache_for_arena()** (3 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **fixture** (1 connections)
- **Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…** (1 connections) — `server/services/npc_startup_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_npc_startup_service.py](test_npc_startup_service.py.md) (33 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 79 (72%)
- INFERRED: 31 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*