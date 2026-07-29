# .get instance()

> 95 nodes

## Key Concepts

- **NPCStartupService** (44 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.get_instance()** (29 connections) — `server/container/main.py`
- **mock_container()** (12 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.spawn_npcs_on_startup()** (8 connections) — `server/services/npc_startup_service.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_errors_len()** (7 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **._spawn_required_npcs()** (6 connections) — `server/services/npc_startup_service.py`
- **._determine_spawn_room()** (6 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Any** (4 connections)
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_no_spawn_room()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- *... and 70 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (7 shared connections)
- [.shutdown()](shutdown%28%29.md) (6 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [lifespan](lifespan.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (1 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)
- [event publisher()](event_publisher%28%29.md) (1 shared connections)
- [combat](combat.md) (1 shared connections)
- [CombatDPSync](CombatDPSync.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 338 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*