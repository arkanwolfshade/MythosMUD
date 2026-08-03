# services npc startup

> 91 nodes

## Key Concepts

- **NPCStartupService** (44 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **mock_container()** (12 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.spawn_npcs_on_startup()** (8 connections) — `server/services/npc_startup_service.py`
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
- **test_spawn_required_npcs_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 299 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*