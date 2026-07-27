# Services Rate Limiter

> 3 nodes · cohesion 0.67

## Key Concepts

- **test_get_retry_stats()** (3 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **Test get_player_stats returns correct statistics.** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [[NATS Retry Handler]] (2 shared connections)
- [[Rate Limiter Service]] (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_retry_handler.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
