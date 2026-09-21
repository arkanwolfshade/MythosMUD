# .detect_and_handle_error_state

> 18 nodes

## Key Concepts

- **.detect_and_handle_error_state()** (9 connections) — `server/realtime/errors/error_handler.py`
- **UUID** (9 connections)
- **Any** (7 connections)
- **.get_error_statistics()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_authentication_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_security_violation()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.handle_websocket_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._terminate_connections_for_error()** (5 connections) — `server/realtime/errors/error_handler.py`
- **._write_error_log_entry()** (5 connections) — `server/realtime/errors/error_handler.py`
- **.recover_from_error()** (4 connections) — `server/realtime/errors/error_handler.py`
- **Append one JSON error record to the dedicated connection_errors.log file.** (1 connections) — `server/realtime/errors/error_handler.py`
- **Fatal errors disconnect the whole player; connection-specific errors drop just…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Detect when a client is in an error state and handle it appropriately. Args:…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle WebSocket-specific errors. Args: player_id: The player's ID…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle authentication-related errors. Args: player_id: The player's ID…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Handle security violations. Args: player_id: The player's ID violation_type:…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Attempt to recover from an error state for a player. Args: player_id: The…** (1 connections) — `server/realtime/errors/error_handler.py`
- **Get error handling statistics. Args: online_players: Online players dictionary…** (1 connections) — `server/realtime/errors/error_handler.py`

## Relationships

- [connection_manager.py](connection_manager.py.md) (9 shared connections)
- [get_config](get_config.md) (2 shared connections)

## Source Files

- `server/realtime/errors/error_handler.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*