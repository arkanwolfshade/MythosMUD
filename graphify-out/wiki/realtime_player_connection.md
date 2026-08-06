# realtime player connection

> 93 nodes

## Key Concepts

- **NPCStartupService** (44 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
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
- *... and 68 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (5 shared connections)
- [tick game processing](tick_game_processing.md) (4 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (4 shared connections)
- [services user manager](services_user_manager.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (2 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 335 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*