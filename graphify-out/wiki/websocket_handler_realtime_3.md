# websocket handler realtime

> 78 nodes

## Key Concepts

- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_utc_now()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_success()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_refused_when_not_dead()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_combat_clear_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_database_error()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_clears_combat_state()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_no_combat_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_increments_existing_liabilities()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **mock_player_combat_service()** (2 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 53 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (10 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 178 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*