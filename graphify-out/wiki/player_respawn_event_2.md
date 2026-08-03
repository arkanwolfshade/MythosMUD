# player respawn event

> 20 nodes

## Key Concepts

- **NPCStartupService** (44 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_required_npcs()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_spawn_failure()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_unknown()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.__init__()** (2 connections) — `server/services/npc_startup_service.py`
- **Service for automatic NPC spawning during server startup.      This service coor** (1 connections) — `server/services/npc_startup_service.py`
- **Initialize the NPC startup service.** (1 connections) — `server/services/npc_startup_service.py`
- **Create an NPCStartupService instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() processes startup spawning.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() handles spawn failures.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns correct room for known sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns None for unknown sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test get_npc_startup_service() returns service instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [startup npc service](startup_npc_service.md) (18 shared connections)
- [services npc startup](services_npc_startup.md) (16 shared connections)
- [startup services npc](startup_services_npc.md) (5 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 78 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*