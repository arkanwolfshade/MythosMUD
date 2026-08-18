# server container main applicationcontainer get

> 33 nodes

## Key Concepts

- **NPCStartupService** (52 connections) — `server/services/npc_startup_service.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **Any** (16 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
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
- **.__init__()** (2 connections) — `server/services/npc_startup_service.py`
- **fixture** (1 connections)
- **Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…** (1 connections) — `server/services/npc_startup_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (33 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (6 shared connections)
- [server events combat events](server_events_combat_events.md) (5 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (5 shared connections)
- [server services user manager py](server_services_user_manager_py.md) (3 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (2 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (2 shared connections)
- [healthstatus](healthstatus.md) (2 shared connections)
- [server game mechanics](server_game_mechanics.md) (2 shared connections)
- [server app lifespan](server_app_lifespan.md) (1 shared connections)
- [server container main get container](server_container_main_get_container.md) (1 shared connections)
- [server game magic magic healing](server_game_magic_magic_healing.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 108 (77%)
- INFERRED: 32 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*