# asyncio

> 23 nodes

## Key Concepts

- **asyncio** (28 connections)
- **test_clear_player_combat_state_handles_error()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_success()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_changes_posture()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_healthy()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_handle_player_death_success()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_applies_decay()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_handles_error()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() excludes healthy players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_dead_players() returns empty list when no dead players.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() applies DP decay via Player.apply_dp_decay.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _ensure_player_posture_lying() changes posture to lying.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _clear_player_combat_state() clears combat state.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _clear_player_combat_state() handles errors gracefully.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test handle_player_death() successfully handles player death.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test handle_player_death() returns False when player not found.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() returns empty list when no mortally wounded…** (1 connections) — `server/tests/unit/services/test_player_death_service.py`

## Relationships

- [test_player_death_service.py](test_player_death_service.py.md) (11 shared connections)
- [test_get_dead_players_debug_only_when_found](test_get_dead_players_debug_only_when_found.md) (2 shared connections)
- [ValueError](ValueError.md) (1 shared connections)
- [test_clear_player_combat_state_no_service](test_clear_player_combat_state_no_service.md) (1 shared connections)
- [test_ensure_player_posture_lying_already_lying](test_ensure_player_posture_lying_already_lying.md) (1 shared connections)
- [test_get_dead_players_excludes_alive](test_get_dead_players_excludes_alive.md) (1 shared connections)
- [test_get_dead_players_finds_dead](test_get_dead_players_finds_dead.md) (1 shared connections)
- [test_get_dead_players_handles_error](test_get_dead_players_handles_error.md) (1 shared connections)
- [test_get_mortally_wounded_players_excludes_dead](test_get_mortally_wounded_players_excludes_dead.md) (1 shared connections)
- [test_get_mortally_wounded_players_finds_mortally_wounded](test_get_mortally_wounded_players_finds_mortally_wounded.md) (1 shared connections)
- [test_handle_player_death_clears_combat_state](test_handle_player_death_clears_combat_state.md) (1 shared connections)
- [test_handle_player_death_handles_error](test_handle_player_death_handles_error.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*