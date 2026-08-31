# test_player_respawn_service.py

> 92 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **asyncio** (27 connections)
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (16 connections) — `server/events/event_types.py`
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
- **test_move_player_to_limbo_refused_when_not_dead()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_clears_combat_state()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_no_combat_service()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (12 shared connections)
- [Player](Player.md) (10 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (7 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (6 shared connections)
- [RespawnPlayerEventPayload](RespawnPlayerEventPayload.md) (6 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 165 (85%)
- INFERRED: 28 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*