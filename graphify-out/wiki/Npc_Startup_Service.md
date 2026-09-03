# Npc Startup Service

> 36 nodes

## Key Concepts

- **NPCStartupService** (54 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service.py** (18 connections) — `server/services/npc_startup_service.py`
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
- *... and 11 more nodes in this community*

## Relationships

- [Test Npc Startup Service](Test_Npc_Startup_Service.md) (34 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (4 shared connections)
- [Test Npc Database](Test_Npc_Database.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [NPC Models](NPC_Models.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 93 (75%)
- INFERRED: 31 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*