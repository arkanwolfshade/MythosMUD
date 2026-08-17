# validate_websocket_message

> 13 nodes

## Key Concepts

- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **extract_csrf_token_from_raw()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **restore_csrf_on_connection_metadata()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **Persist a validated message JWT on connection metadata after reconnect edge…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Validate csrfToken from the message body and optionally heal connection…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Resolve the CSRF/JWT token used for message validation. Prefer connection…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Validate message and send error response if validation fails. Returns:…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Parse outer JSON once to read csrfToken/csrf_token when metadata lacks a stored…** (1 connections) — `server/realtime/websocket_handler_validation.py`
- **Return stored JWT, connection_id, and metadata from the active WebSocket…** (1 connections) — `server/realtime/websocket_handler_validation.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_validation.py`

## Audit Trail

- EXTRACTED: 22 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*