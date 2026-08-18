# server tests unit services test

> 5 nodes

## Key Concepts

- **rate_limiter()** (5 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **mock_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **fixture** (2 connections)
- **Create a mock config with chat rate limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Create a RateLimiter instance with mocked config.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (2 shared connections)
- [server services rate limiter py](server_services_rate_limiter_py.md) (1 shared connections)
- [server realtime rate limiter py](server_realtime_rate_limiter_py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*