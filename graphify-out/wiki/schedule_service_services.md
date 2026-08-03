# schedule service services

> 12 nodes

## Key Concepts

- **.get_limit()** (6 connections) — `server/services/rate_limiter.py`
- **._cleanup_old_entries()** (6 connections) — `server/services/rate_limiter.py`
- **.check_rate_limit()** (5 connections) — `server/services/rate_limiter.py`
- **.record_message()** (4 connections) — `server/services/rate_limiter.py`
- **.get_remaining_messages()** (4 connections) — `server/services/rate_limiter.py`
- **.is_player_rate_limited()** (3 connections) — `server/services/rate_limiter.py`
- **Get the current rate limit for a channel.          Args:             channel: Ch** (1 connections) — `server/services/rate_limiter.py`
- **Remove timestamps older than the window size.          Args:             player_** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is within rate limits for a channel.          Args:** (1 connections) — `server/services/rate_limiter.py`
- **Record a message for rate limiting.          Args:             player_id: Player** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is currently rate limited on a channel.          Args:** (1 connections) — `server/services/rate_limiter.py`
- **Get the number of remaining messages a player can send on a channel.          Ar** (1 connections) — `server/services/rate_limiter.py`

## Relationships

- [rate limiter services](rate_limiter_services.md) (6 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)

## Source Files

- `server/services/rate_limiter.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*