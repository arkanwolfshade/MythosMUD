# test_player_death_service.py

> 30 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_dead()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_clears_combat_state()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_already_dead()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_applies_decay()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_empty_location()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_container()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_no_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_with_room()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init_no_dependencies()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_no_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_killer_info()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Unit tests for player death service. Tests the PlayerDeathService class for…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() excludes dead players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() returns False when player already dead.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() applies DP decay via Player.apply_dp_decay.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns room name when available.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns room_id when room not found.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns 'Unknown' for empty location.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns room_id when async_persistence…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _publish_death_event() publishes event when event bus available.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _publish_death_event() includes killer information.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (22 shared connections)
- [fixture](fixture.md) (7 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (2 shared connections)
- [event_handler.py](event_handler.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_get_mortally_wounded_players_handles_error](test_get_mortally_wounded_players_handles_error.md) (1 shared connections)
- [test_ensure_player_posture_lying_already_lying](test_ensure_player_posture_lying_already_lying.md) (1 shared connections)
- [test_clear_player_combat_state_success](test_clear_player_combat_state_success.md) (1 shared connections)
- [test_handle_player_death_with_killer_info](test_handle_player_death_with_killer_info.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*