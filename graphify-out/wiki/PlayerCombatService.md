# PlayerCombatService

> 101 nodes

## Key Concepts

- **NPCStartupService** (54 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (38 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **asyncio** (26 connections)
- **Any** (17 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **_errors_len()** (7 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **test_spawn_npcs_on_startup_critical_exception()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_exception_in_session()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_exception()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_exception()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_no_spawn_room()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.spawn_npcs_on_startup()** (4 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 175 (85%)
- INFERRED: 31 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*