# Server Realtime (30)

> 56 nodes

## Key Concepts

- **RateLimiter** (50 connections) — `server/realtime/rate_limiter.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **Test RateLimiter.cleanup_old_attempts() removes old attempts.** (4 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_init_custom()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_first_attempt()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_within_limit()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_rate_limit_old_attempts_removed()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_rate_limit_info()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_rate_limit_info_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_removes_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_old_attempts_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_remove_player_data_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_stats()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_stats_empty()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_get_stats_error()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_message_rate_limit_first()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_message_rate_limit_within_limit()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_rate_limiter_check_message_rate_limit_exceeded()** (3 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- *... and 31 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Realtime (115)](Server_Realtime_%28115%29.md) (3 shared connections)
- [Server Realtime (85)](Server_Realtime_%2885%29.md) (2 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (1 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (1 shared connections)
- [Server Realtime (124)](Server_Realtime_%28124%29.md) (1 shared connections)
- [Server Realtime (125)](Server_Realtime_%28125%29.md) (1 shared connections)
- [Server Realtime (126)](Server_Realtime_%28126%29.md) (1 shared connections)
- [Server Realtime (127)](Server_Realtime_%28127%29.md) (1 shared connections)
- [Server Realtime (128)](Server_Realtime_%28128%29.md) (1 shared connections)
- [Server Realtime (129)](Server_Realtime_%28129%29.md) (1 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 199 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*