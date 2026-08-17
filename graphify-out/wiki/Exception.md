# Exception

> 14 nodes

## Key Concepts

- **Exception** (9 connections)
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_is_wrapped_transient_message()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_log_retry_attempt()** (2 connections) — `server/utils/retry.py`
- **_log_retry_failure()** (2 connections) — `server/utils/retry.py`
- **Any** (2 connections)
- **Determine if an error should be retried.** (1 connections) — `server/utils/retry.py`
- **Create async wrapper function with retry logic.** (1 connections) — `server/utils/retry.py`
- **Create sync wrapper function with retry logic.** (1 connections) — `server/utils/retry.py`
- **Return True if error is a psycopg2 transient error…** (1 connections) — `server/utils/retry.py`
- **True when a domain wrapper (DatabaseError) embeds a transient DB failure in its…** (1 connections) — `server/utils/retry.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [is_transient_error](is_transient_error.md) (4 shared connections)
- [get_session_maker](get_session_maker.md) (1 shared connections)

## Source Files

- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*