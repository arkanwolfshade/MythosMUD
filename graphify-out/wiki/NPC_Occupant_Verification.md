# NPC Occupant Verification

> 105 nodes

## Key Concepts

- **NPCStartupService** (53 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **Any** (16 connections)
- **mock_container()** (12 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **_errors_len()** (7 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- *... and 80 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (8 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)
- [Party Service Management](Party_Service_Management.md) (2 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Character Creation API](Character_Creation_API.md) (1 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 411 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*