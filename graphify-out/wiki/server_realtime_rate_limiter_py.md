# server realtime rate limiter py

> 7 nodes

## Key Concepts

- **.get_message_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_stats()** (3 connections) — `server/realtime/rate_limiter.py`
- **Any** (3 connections)
- **Get rate limiter statistics. Returns: dict: Statistics about current rate…** (1 connections) — `server/realtime/rate_limiter.py`
- **Get message rate limit information for a connection. Args: connection_id: The…** (1 connections) — `server/realtime/rate_limiter.py`
- **Get rate limit information for a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/rate_limiter.py`

## Relationships

- [server realtime rate limiter ratelimiter](server_realtime_rate_limiter_ratelimiter.md) (3 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*