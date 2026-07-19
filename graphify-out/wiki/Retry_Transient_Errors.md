# Retry Transient Errors

> 36 nodes · cohesion 0.09

## Key Concepts

- **retry.py** (13 connections) — `server/utils/retry.py`
- **retry_with_backoff()** (10 connections) — `server/utils/retry.py`
- **is_transient_error()** (9 connections) — `server/utils/retry.py`
- **test_retry.py** (9 connections) — `server/tests/unit/utils/test_retry.py`
- **Exception** (8 connections) — `server/utils/retry.py`
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_is_asyncpg_transient()** (3 connections) — `server/utils/retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **Any** (2 connections) — `server/utils/retry.py`
- **_calculate_retry_delay()** (2 connections) — `server/utils/retry.py`
- **_log_retry_attempt()** (2 connections) — `server/utils/retry.py`
- **_log_retry_failure()** (2 connections) — `server/utils/retry.py`
- **Create async wrapper function with retry logic.** (2 connections) — `server/utils/retry.py`
- **F** (1 connections) — `server/utils/retry.py`
- **Retry utilities for transient database errors.  This module provides retry decor** (1 connections) — `server/utils/retry.py`
- **Decorator to retry a function with exponential backoff on transient errors.** (1 connections) — `server/utils/retry.py`
- **Return True if error is an asyncpg transient error.** (1 connections) — `server/utils/retry.py`
- *... and 11 more nodes in this community*

## Relationships

- [[NPC Admin API]] (3 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 111 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
