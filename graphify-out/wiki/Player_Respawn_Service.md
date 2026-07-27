# Player Respawn Service

> 68 nodes · cohesion 0.03

## Key Concepts

- **test_player_respawn_service.py** (43 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **datetime** (3 connections) — `server/services/player_respawn_service.py`
- **respawn_service_no_deps()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_utc_now()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_player_combat_service()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **Test respawning player from delirium clears combat state.** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_refused_when_not_dead()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_sqlalchemy_error()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_clears_combat_state()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[Player Respawn Service]] (5 shared connections)
- [[Player Respawn Events]] (2 shared connections)
- [[Player Domain Model]] (2 shared connections)
- [[Lucidity State Models]] (1 shared connections)
- [[Lucidity Database Models]] (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 158 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
