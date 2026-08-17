# is_transient_error

> 11 nodes

## Key Concepts

- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **_iter_exception_chain()** (4 connections) — `server/utils/retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **_is_asyncpg_transient()** (3 connections) — `server/utils/retry.py`
- **BaseException** (1 connections)
- **Test is_transient_error() identifies transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **DatabaseError wrapping asyncpg closed-connection must still retry (e2e…** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Return True if error is an asyncpg transient error.** (1 connections) — `server/utils/retry.py`
- **Walk __cause__/__context__ without looping.** (1 connections) — `server/utils/retry.py`
- **Check if an error is a transient database error that should be retried. Args:…** (1 connections) — `server/utils/retry.py`

## Relationships

- [test_retry.py](test_retry.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Exception](Exception.md) (4 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*