# Community 169

> 80 nodes

## Key Concepts

- **RateLimiter** (58 connections) — `server/realtime/rate_limiter.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **.get_message_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_stats()** (3 connections) — `server/realtime/rate_limiter.py`
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
- **test_rate_limiter_get_rate_limit_info_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- *... and 55 more nodes in this community*

## Relationships

- [Community 127](Community_127.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 538](Community_538.md) (2 shared connections)
- [Connection Manager Broadcast](Connection_Manager_Broadcast.md) (2 shared connections)
- [Community 576](Community_576.md) (2 shared connections)
- [Community 594](Community_594.md) (2 shared connections)
- [Community 351](Community_351.md) (1 shared connections)
- [Community 1280](Community_1280.md) (1 shared connections)
- [Community 267](Community_267.md) (1 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 123 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*