# test_real_time_helpers.py

> 15 nodes

## Key Concepts

- **test_real_time_helpers.py** (32 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (6 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_empty()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_last_part()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_with_marker()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_subprotocol_token()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Parse token from WebSocket subprotocol header. Example formats: "bearer,…** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).…** (1 connections) — `server/api/real_time.py`
- **Extract bearer token from parsed subprotocol parts. If 'bearer' marker is…** (1 connections) — `server/api/real_time.py`
- **Unit tests for real_time API helper functions.** (1 connections) — `server/tests/unit/api/test_real_time_helpers.py`

## Relationships

- [asyncio](asyncio.md) (18 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [realtime/realtime.py](realtime-realtime.py.md) (4 shared connections)
- [_ensure_connection_manager](_ensure_connection_manager.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*