# websocket_handler_validation.py

> 17 nodes

## Key Concepts

- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **extract_csrf_token_from_raw()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **restore_csrf_on_connection_metadata()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket message validation, CSRF/JWT resolution, and rate limiting. Extracted…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Persist a validated message JWT on connection metadata after reconnect edge…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Validate csrfToken from the message body and optionally heal connection…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Resolve the CSRF/JWT token used for message validation. Prefer connection…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Validate message and send error response if validation fails. Returns:…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Check rate limit and send error response if exceeded. Returns: True if rate…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Parse outer JSON once to read csrfToken/csrf_token when metadata lacks a stored…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Return stored JWT, connection_id, and metadata from the active WebSocket…** (1 connections) — `server/realtime/websocket_handler_validation.py`

## Relationships

- [ErrorType](ErrorType.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_validation.py`

## Audit Trail

- EXTRACTED: 40 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*