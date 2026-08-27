# retry.py

> 20 nodes

## Key Concepts

- **retry.py** (19 connections) — `server/utils/retry.py`
- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **Exception** (9 connections)
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_is_wrapped_transient_message()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_is_asyncpg_transient()** (3 connections) — `server/utils/retry.py`
- **_log_retry_attempt()** (2 connections) — `server/utils/retry.py`
- **_log_retry_failure()** (2 connections) — `server/utils/retry.py`
- **Any** (2 connections)
- **Retry utilities for transient database errors. This module provides retry…** (1 connections) — `server/utils/retry.py`
- **Determine if an error should be retried.** (1 connections) — `server/utils/retry.py`
- **Create async wrapper function with retry logic.** (1 connections) — `server/utils/retry.py`
- **Create sync wrapper function with retry logic.** (1 connections) — `server/utils/retry.py`
- **Return True if error is an asyncpg transient error.** (1 connections) — `server/utils/retry.py`
- **Return True if error is a psycopg2 transient error…** (1 connections) — `server/utils/retry.py`
- **True when a domain wrapper (DatabaseError) embeds a transient DB failure in its…** (1 connections) — `server/utils/retry.py`
- **Check if an error is a transient database error that should be retried. Args:…** (1 connections) — `server/utils/retry.py`

## Relationships

- [test_retry.py](test_retry.py.md) (6 shared connections)
- [_iter_exception_chain](_iter_exception_chain.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [retry_with_backoff](retry_with_backoff.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [_calculate_retry_delay](_calculate_retry_delay.md) (1 shared connections)

## Source Files

- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*