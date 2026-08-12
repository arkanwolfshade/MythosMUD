# Combat Persistence Events

> 29 nodes

## Key Concepts

- **NPCStartupService** (53 connections) — `server/services/npc_startup_service.py`
- **Any** (16 connections)
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._handle_required_no_room()** (4 connections) — `server/services/npc_startup_service.py`
- **._warmup_room_cache_for_arena()** (4 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._get_persistence_for_spawn()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **_merge_phase_into_startup()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_specific_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_fallback_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **.__init__()** (2 connections) — `server/services/npc_startup_service.py`
- **Service for automatic NPC spawning during server startup.      This service coor** (1 connections) — `server/services/npc_startup_service.py`
- **Initialize the NPC startup service.** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn NPCs during server startup.          This method handles the automatic spa** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn all required NPCs.          Args:             required_npcs: List of requi** (1 connections) — `server/services/npc_startup_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [NPC Occupant Verification](NPC_Occupant_Verification.md) (23 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`

## Audit Trail

- EXTRACTED: 166 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*