# Player Death Service Tests

> 85 nodes · cohesion 0.02

## Key Concepts

- **test_player_death_service.py** (48 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_service_init()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test PlayerService initialization.** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test get_mortally_wounded_players() excludes healthy players.** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test process_mortally_wounded_tick() returns False when player not found.** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Test _clear_player_combat_state() clears combat state.** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_handles_error()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_no_service()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_clear_player_combat_state_success()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_already_lying()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_ensure_player_posture_lying_changes_posture()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_empty()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_excludes_alive()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_finds_dead()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_handles_error()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_dead()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_healthy()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (3 shared connections)
- [[Player Death Service]] (2 shared connections)
- [[Player Domain Model]] (2 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[Player Service Tests]] (1 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 182 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
