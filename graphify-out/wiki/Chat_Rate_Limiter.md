# Chat Rate Limiter

> 30 nodes · cohesion 0.09

## Key Concepts

- **RateLimiter** (17 connections) — `server/services/rate_limiter.py`
- **._cleanup_old_entries()** (6 connections) — `server/services/rate_limiter.py`
- **.get_limit()** (6 connections) — `server/services/rate_limiter.py`
- **.check_rate_limit()** (5 connections) — `server/services/rate_limiter.py`
- **.get_player_stats()** (5 connections) — `server/services/rate_limiter.py`
- **.get_remaining_messages()** (4 connections) — `server/services/rate_limiter.py`
- **.record_message()** (4 connections) — `server/services/rate_limiter.py`
- **.get_system_stats()** (3 connections) — `server/services/rate_limiter.py`
- **.__init__()** (3 connections) — `server/services/rate_limiter.py`
- **.is_player_rate_limited()** (3 connections) — `server/services/rate_limiter.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_legacy_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.__init__()** (2 connections) — `server/realtime/rate_limiter.py`
- **Initialize the rate limiter with configurable settings.          Args:** (2 connections) — `server/realtime/rate_limiter.py`
- **Any** (2 connections) — `server/services/rate_limiter.py`
- **.reset_player_limits()** (2 connections) — `server/services/rate_limiter.py`
- **.set_limit()** (2 connections) — `server/services/rate_limiter.py`
- **Remove timestamps older than the window size.          Args:             player_** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is within rate limits for a channel.          Args:** (1 connections) — `server/services/rate_limiter.py`
- **Record a message for rate limiting.          Args:             player_id: Player** (1 connections) — `server/services/rate_limiter.py`
- **Sliding window rate limiter for chat channels.      Implements per-user, per-cha** (1 connections) — `server/services/rate_limiter.py`
- **Get rate limiting statistics for a player.          Args:             player_id:** (1 connections) — `server/services/rate_limiter.py`
- **Reset rate limiting for a player.          Args:             player_id: Player I** (1 connections) — `server/services/rate_limiter.py`
- **Get system-wide rate limiting statistics.          Returns:             Dictiona** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is currently rate limited on a channel.          Args:** (1 connections) — `server/services/rate_limiter.py`
- *... and 5 more nodes in this community*

## Relationships

- [[Rate Limiter Service]] (4 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Rate Limiter Utilities]] (1 shared connections)

## Source Files

- `server/realtime/rate_limiter.py`
- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 85 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
