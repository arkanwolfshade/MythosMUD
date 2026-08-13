# test_player_respawn_service.py

> 73 nodes

## Key Concepts

- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **asyncio** (23 connections)
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **fixture** (7 connections)
- **respawn_service()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_refused_when_not_dead()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_sqlalchemy_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_clears_combat_state()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 48 more nodes in this community*

## Relationships

- [Player](Player.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (5 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 126 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*