# asyncio

> 35 nodes

## Key Concepts

- **asyncio** (26 connections)
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_no_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_changes_posture()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_excludes_alive()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_finds_dead()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_healthy()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_finds_mortally_wounded()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_success()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_caps_at_negative_10()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_changes_posture_to_lying()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() finds mortally wounded players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() excludes healthy players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() returns empty list when no dead players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() finds dead players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() excludes alive players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() returns False when player not found.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_player_death_service.py](test_player_death_service.py.md) (22 shared connections)
- [event_handler.py](event_handler.py.md) (1 shared connections)
- [test_clear_player_combat_state_success](test_clear_player_combat_state_success.md) (1 shared connections)
- [test_ensure_player_posture_lying_already_lying](test_ensure_player_posture_lying_already_lying.md) (1 shared connections)
- [test_get_mortally_wounded_players_handles_error](test_get_mortally_wounded_players_handles_error.md) (1 shared connections)
- [test_handle_player_death_with_killer_info](test_handle_player_death_with_killer_info.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 60 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*