# GameTerminalContext

> 20 nodes

## Key Concepts

- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (8 connections)
- **.detect_and_handle_error_state()** (8 connections) — `server/realtime/errors/error_handler.py`
- **Any** (7 connections)
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.__init__()** (4 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- **__init__.py** (3 connections) — `server/realtime/errors/__init__.py`
- **Error handling components for connection management.  This package provides spec** (1 connections) — `server/realtime/errors/__init__.py`
- **Handles error detection, logging, and recovery for connection management.      T** (1 connections) — `server/realtime/errors/error_handler.py`
- **Initialize the error handler.          Args:             force_disconnect_callba** (1 connections) — `server/realtime/errors/error_handler.py`
- **Detect when a client is in an error state and handle it appropriately.** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle WebSocket-specific errors.          Args:             player_id: The play** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle authentication-related errors.          Args:             player_id: The** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle security violations.          Args:             player_id: The player's I** (1 connections) — `server/realtime/errors/error_handler.py`
- **Attempt to recover from an error state for a player.          Args:** (1 connections) — `server/realtime/errors/error_handler.py`
- **Get error handling statistics.          Args:             online_players: Online** (1 connections) — `server/realtime/errors/error_handler.py`

## Relationships

- [world](world.md) (3 shared connections)
- [close db()](close_db%28%29.md) (2 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (1 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)

## Source Files

- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*