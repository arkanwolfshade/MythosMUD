# 🔴 CRITICAL ISSUES

> 5 nodes · cohesion 0.40

## Key Concepts

- **rate_limiter()** (5 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **mock_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **fixture** (2 connections)
- **Create a mock config with chat rate limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Create a RateLimiter instance with mocked config.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [debugLogger](debugLogger.md) (2 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*