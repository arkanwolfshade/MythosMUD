# test_player_death_service.py

> 88 nodes

## Key Concepts

- **test_player_death_service.py** (53 connections) — `server/tests/unit/services/test_player_death_service.py`
- **asyncio** (26 connections)
- **fixture** (7 connections)
- **mock_player()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_no_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_success()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_already_lying()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_changes_posture()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_excludes_alive()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_finds_dead()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_dead()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_healthy()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_finds_mortally_wounded()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 63 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (4 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 128 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*