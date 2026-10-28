# Test Suite Analyzer Subagent

> 23 nodes · cohesion 0.09

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

- [MythosMUD Dependency Upgrade Strategy - Implementation Summary](MythosMUD_Dependency_Upgrade_Strategy_-_Implementation_Summary.md) (11 shared connections)
- [test_check_codacy_yaml.py](test_check_codacy_yaml.py.md) (2 shared connections)
- [test_restore_mp_from_meditation_higher_than_rest](test_restore_mp_from_meditation_higher_than_rest.md) (1 shared connections)
- [test_restore_mp_from_rest_calculates_max_from_power](test_restore_mp_from_rest_calculates_max_from_power.md) (1 shared connections)
- [test_handle_learn_command_wrapper_success](test_handle_learn_command_wrapper_success.md) (1 shared connections)
- [test_handle_learn_command_with_corruption](test_handle_learn_command_with_corruption.md) (1 shared connections)
- [test_handle_stop_command_wrapper_success](test_handle_stop_command_wrapper_success.md) (1 shared connections)
- [test_handle_spell_command_spell_not_found](test_handle_spell_command_spell_not_found.md) (1 shared connections)
- [test_handle_spells_command_with_spells](test_handle_spells_command_with_spells.md) (1 shared connections)
- [test_restore_mp_from_item_restores_mp](test_restore_mp_from_item_restores_mp.md) (1 shared connections)
- [test_restore_mp_from_item_calculates_max_from_power](test_restore_mp_from_item_calculates_max_from_power.md) (1 shared connections)
- [test_restore_mp_from_item_player_not_found](test_restore_mp_from_item_player_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*