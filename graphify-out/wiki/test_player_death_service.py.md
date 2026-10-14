# test_player_death_service.py

> 22 nodes

## Key Concepts

- **test_player_death_service.py** (57 connections) — `server/tests/unit/services/test_player_death_service.py`
- **_player()** (5 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_empty_location()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_container()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_with_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init_no_dependencies()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_no_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_killer_info()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **UUID** (2 connections)
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

- [asyncio](asyncio.md) (11 shared connections)
- [fixture](fixture.md) (7 shared connections)
- [test_get_dead_players_debug_only_when_found](test_get_dead_players_debug_only_when_found.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [test_get_mortally_wounded_players_finds_mortally_wounded](test_get_mortally_wounded_players_finds_mortally_wounded.md) (1 shared connections)
- [test_get_mortally_wounded_players_excludes_dead](test_get_mortally_wounded_players_excludes_dead.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*