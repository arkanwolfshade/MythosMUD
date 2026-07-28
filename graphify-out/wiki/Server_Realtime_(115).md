# Server Realtime (115)

> 7 nodes

## Key Concepts

- **.get_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **Any** (3 connections)
- **.get_stats()** (3 connections) — `server/realtime/rate_limiter.py`
- **.get_message_rate_limit_info()** (3 connections) — `server/realtime/rate_limiter.py`
- **Get rate limit information for a player.          Args:             player_id: T** (1 connections) — `server/realtime/rate_limiter.py`
- **Get rate limiter statistics.          Returns:             dict: Statistics abou** (1 connections) — `server/realtime/rate_limiter.py`
- **Get message rate limit information for a connection.          Args:** (1 connections) — `server/realtime/rate_limiter.py`

## Relationships

- [Server Realtime (30)](Server_Realtime_%2830%29.md) (3 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*