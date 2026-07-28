# WebSocket Connection Setup

> 87 nodes · cohesion 0.03

## Key Concepts

- **RateLimiter** (55 connections) — `server/realtime/rate_limiter.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **Any** (3 connections)
- **.get_message_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_stats()** (3 connections) — `server/realtime/rate_limiter.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_rate_limiter_check_message_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_message_rate_limit_first()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_message_rate_limit_within_limit()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_first_attempt()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_old_attempts_removed()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_within_limit()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_removes_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_message_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_message_attempts_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_message_attempts_removes_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_message_rate_limit_info()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_message_rate_limit_info_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_rate_limit_info()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- *... and 62 more nodes in this community*

## Relationships

- [Realtime Event Delegation](Realtime_Event_Delegation.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)
- [Realtime Messaging Message](Realtime_Messaging_Message.md) (1 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 243 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*