# NPCStartupService

> 27 nodes

## Key Concepts

- **NPCStartupService** (52 connections) — `server/services/npc_startup_service.py`
- **Any** (16 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **._get_persistence_for_spawn()** (4 connections) — `server/services/npc_startup_service.py`
- **._handle_required_no_room()** (4 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **._warmup_room_cache_for_arena()** (4 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **_merge_phase_into_startup()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_fallback_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_specific_room()** (3 connections) — `server/services/npc_startup_service.py`
- **Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…** (1 connections) — `server/services/npc_startup_service.py`
- **Second pass: spawn one instance per definition (that was spawned in…** (1 connections) — `server/services/npc_startup_service.py`
- **Determine the appropriate room for spawning an NPC. Args: npc_def: NPC…** (1 connections) — `server/services/npc_startup_service.py`
- **Get a default room for a given sub-zone. Args: sub_zone_id: Sub-zone identifier…** (1 connections) — `server/services/npc_startup_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [mock_container](mock_container.md) (9 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (8 shared connections)
- [_errors_len](_errors_len.md) (5 shared connections)
- [npc_startup_service](npc_startup_service.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`

## Audit Trail

- EXTRACTED: 103 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*