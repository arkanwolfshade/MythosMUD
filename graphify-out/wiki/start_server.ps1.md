# start_server.ps1

> 5 nodes

## Key Concepts

- **rate_limiter()** (5 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **mock_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **fixture** (2 connections)
- **Create a mock config with chat rate limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Create a RateLimiter instance with mocked config.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [dependencies](dependencies.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*