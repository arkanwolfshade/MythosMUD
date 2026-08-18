# test_npc_startup_service.py

> 21 nodes

## Key Concepts

- **test_npc_startup_service.py** (40 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **npc_startup_service()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_case_insensitive()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_unknown()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_arena_room_ids()** (2 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **fixture** (1 connections)
- **Unit tests for NPC startup service. Tests the NPCStartupService class.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns correct room for known sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns None for unknown sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() is case insensitive.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test get_npc_startup_service() returns service instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Create an NPCStartupService instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() processes startup spawning.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [asyncio](asyncio.md) (12 shared connections)
- [mock_container](mock_container.md) (10 shared connections)
- [NPCStartupService](NPCStartupService.md) (9 shared connections)
- [_errors_len](_errors_len.md) (6 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 54 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*