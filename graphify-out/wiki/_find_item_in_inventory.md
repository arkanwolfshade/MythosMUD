# _find_item_in_inventory

> 78 nodes · cohesion 0.05

## Key Concepts

- **ConnectionErrorHandler** (28 connections) — `server/realtime/errors/error_handler.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_connection_error_handler.py** (15 connections) — `server/tests/unit/realtime/test_connection_error_handler.py`
- **error_handler.py** (13 connections) — `server/realtime/errors/error_handler.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **.detect_and_handle_error_state()** (9 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (9 connections)
- **asyncio** (9 connections)
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **ConnectionErrorHandlerCallbacks** (7 connections) — `server/realtime/errors/error_handler.py`
- **Any** (7 connections)
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._terminate_connections_for_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._write_error_log_entry()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- *... and 53 more nodes in this community*

## Relationships

- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (15 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (9 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (3 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (1 shared connections)
- [Domain Model Anemic Anti-Pattern Audit](Domain_Model_Anemic_Anti-Pattern_Audit.md) (1 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [authenticated.ts](authenticated.ts.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/tests/unit/realtime/test_connection_error_handler.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 169 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*