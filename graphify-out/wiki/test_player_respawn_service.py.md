# test_player_respawn_service.py

> 204 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **server/models/game.py** (33 connections) — `server/models/game.py`
- **asyncio** (27 connections)
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **PositionState** (17 connections) — `server/models/game.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **fixture** (7 connections)
- **test_respawn_player_from_delirium_combat_clear_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 179 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (65 shared connections)
- [LucidityService](LucidityService.md) (17 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (12 shared connections)
- [PlayerService](PlayerService.md) (11 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [coerce_int](coerce_int.md) (7 shared connections)
- [Stats](Stats.md) (6 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (4 shared connections)
- [run_flee_effect](run_flee_effect.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/game.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 349 (83%)
- INFERRED: 71 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*