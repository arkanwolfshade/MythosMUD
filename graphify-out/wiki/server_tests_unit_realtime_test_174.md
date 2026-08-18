# server tests unit realtime test

> 14 nodes

## Key Concepts

- **test_websocket_handler_rate_limit.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **test_check_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **test_check_rate_limit_no_connection_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **test_check_rate_limit_passed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **asyncio** (3 connections)
- **fixture** (2 connections)
- **Unit tests for websocket handler rate limiting. Tests the rate limiting…** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **Create a mock WebSocket.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **Test _check_rate_limit() returns True when no connection_id.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **Test _check_rate_limit() returns True when rate limit check passes.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`
- **Test _check_rate_limit() returns False when rate limit exceeded.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`

## Relationships

- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_handler_rate_limit.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*