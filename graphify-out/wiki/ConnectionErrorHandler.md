# ConnectionErrorHandler

> 20 nodes

## Key Concepts

- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **.detect_and_handle_error_state()** (8 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (8 connections)
- **Any** (7 connections)
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.__init__()** (4 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- **errors/__init__.py** (3 connections) — `server/realtime/errors/__init__.py`
- **Handle WebSocket-specific errors. Args: player_id: The player's ID…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle authentication-related errors. Args: player_id: The player's ID…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle security violations. Args: player_id: The player's ID violation_type:…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Attempt to recover from an error state for a player. Args: player_id: The…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Get error handling statistics. Args: online_players: Online players dictionary…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handles error detection, logging, and recovery for connection management. This…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Initialize the error handler. Args: force_disconnect_callback: Callback to…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Detect when a client is in an error state and handle it appropriately. Args:…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Error handling components for connection management. This package provides…** (1 connections) — `server/realtime/errors/__init__.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*