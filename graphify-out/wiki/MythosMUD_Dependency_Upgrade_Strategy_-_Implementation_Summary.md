# MythosMUD Dependency Upgrade Strategy - Implementation Summary

> 22 nodes · cohesion 0.10

## Key Concepts

- **test_player_death_service.py** (57 connections) — `server/tests/unit/services/test_player_death_service.py`
- **_player()** (5 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **UUID** (2 connections)
- **test_get_room_name_for_death_empty_location()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_container()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_with_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init_no_dependencies()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_no_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_killer_info()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Unit tests for player death service. Tests the PlayerDeathService class for…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns room name when available.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() never leaks the room_id when room not found…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns 'Unknown Location' for empty location.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() never leaks the room_id when async_persistence…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _publish_death_event() publishes event when event bus available.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _publish_death_event() includes killer information.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _publish_death_event() does nothing when event bus unavailable.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test PlayerDeathService initialization.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test PlayerDeathService initialization without dependencies.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`

## Relationships

- [Test Suite Analyzer Subagent](Test_Suite_Analyzer_Subagent.md) (11 shared connections)
- [Quick Start: Running E2E Tests](Quick_Start-_Running_E2E_Tests.md) (7 shared connections)
- [test_check_codacy_yaml.py](test_check_codacy_yaml.py.md) (5 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_handle_spells_command_with_spells](test_handle_spells_command_with_spells.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*