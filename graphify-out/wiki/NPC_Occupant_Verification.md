# NPC Occupant Verification

> 127 nodes · cohesion 0.02

## Key Concepts

- **get_npc_instance_service()** (80 connections) — `server/services/npc_instance_service.py`
- **test_npc_instance_service.py** (47 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCInstanceService** (25 connections) — `server/services/npc_instance_service.py`
- **npc_startup_service.py** (14 connections) — `server/services/npc_startup_service.py`
- **NPCStartupService** (13 connections) — `server/services/npc_startup_service.py`
- **Any** (12 connections) — `server/services/npc_instance_service.py`
- **.spawn_npcs_on_startup()** (8 connections) — `server/services/npc_startup_service.py`
- **verify_npc_occupants.py** (7 connections) — `server/scripts/verify_npc_occupants.py`
- **verify_npcs_in_lifecycle_manager()** (6 connections) — `server/scripts/verify_npc_occupants.py`
- **_check_service_availability()** (5 connections) — `server/scripts/verify_npc_occupants.py`
- **Any** (5 connections) — `server/services/npc_startup_service.py`
- **.spawn_npc_instance()** (5 connections) — `server/services/npc_instance_service.py`
- **._determine_spawn_room()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **_collect_npcs_by_room()** (4 connections) — `server/scripts/verify_npc_occupants.py`
- **_test_query_for_room()** (4 connections) — `server/scripts/verify_npc_occupants.py`
- **.despawn_npc_instance()** (4 connections) — `server/services/npc_instance_service.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **._spawn_arena_npcs()** (4 connections) — `server/services/npc_startup_service.py`
- **test_initialize_npc_instance_service()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **_print_summary()** (3 connections) — `server/scripts/verify_npc_occupants.py`
- **Any** (3 connections) — `server/scripts/verify_npc_occupants.py`
- *... and 102 more nodes in this community*

## Relationships

- [[NPC Services Bundle]] (11 shared connections)
- [[NPC Definition Admin API]] (8 shared connections)
- [[NPC Database Sessions]] (8 shared connections)
- [[Aggressive Mob NPC]] (7 shared connections)
- [[NPC Admin Commands]] (6 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Distributed Event Bus]] (4 shared connections)
- [[NPC Death Lifecycle]] (4 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[NPC Combat Lifecycle]] (4 shared connections)
- [[Look NPC Command]] (4 shared connections)
- [[Commands Npc Admin]] (4 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/scripts/verify_npc_occupants.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 422 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
