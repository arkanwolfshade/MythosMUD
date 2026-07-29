# test player death service

> 12 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_excludes_alive()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_caps_at_negative_10()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_room_name_for_death_empty_location()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Unit tests for player death service.  Tests the PlayerDeathService class for man** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a mock player.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() returns empty list when no mortally wounded** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() excludes alive players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() caps DP at -10 via Player.apply_dp_decay.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _get_room_name_for_death() returns 'Unknown' for empty location.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`

## Relationships

- [. init ()](_init_%28%29.md) (7 shared connections)
- [Test process mortally wounded tick()](Test_process_mortally_wounded_tick%28%29.md) (6 shared connections)
- [Test get mortally wounded players()](Test_get_mortally_wounded_players%28%29.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [Test clear player combat state()](Test_clear_player_combat_state%28%29.md) (3 shared connections)
- [Test get room name for](Test_get_room_name_for.md) (3 shared connections)
- [Test ensure player posture lying()](Test_ensure_player_posture_lying%28%29.md) (2 shared connections)
- [Test handle player death() handles](Test_handle_player_death%28%29_handles.md) (2 shared connections)
- [mock event bus()](mock_event_bus%28%29.md) (1 shared connections)
- [mock player combat service()](mock_player_combat_service%28%29.md) (1 shared connections)
- [mock session()](mock_session%28%29.md) (1 shared connections)
- [player death service()](player_death_service%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 68 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*