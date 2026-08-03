# realtime maintenance connection

> 5 nodes

## Key Concepts

- **.get_player_stats()** (5 connections) — `server/services/rate_limiter.py`
- **.get_system_stats()** (3 connections) — `server/services/rate_limiter.py`
- **Any** (2 connections)
- **Get rate limiting statistics for a player.          Args:             player_id:** (1 connections) — `server/services/rate_limiter.py`
- **Get system-wide rate limiting statistics.          Returns:             Dictiona** (1 connections) — `server/services/rate_limiter.py`

## Relationships

- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [schedule service services](schedule_service_services.md) (2 shared connections)

## Source Files

- `server/services/rate_limiter.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*