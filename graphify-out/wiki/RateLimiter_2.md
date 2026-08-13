# RateLimiter

> 27 nodes

## Key Concepts

- **RateLimiter** (17 connections) — `server/services/rate_limiter.py`
- **._cleanup_old_entries()** (6 connections) — `server/services/rate_limiter.py`
- **.get_limit()** (6 connections) — `server/services/rate_limiter.py`
- **.check_rate_limit()** (5 connections) — `server/services/rate_limiter.py`
- **.get_player_stats()** (5 connections) — `server/services/rate_limiter.py`
- **.get_remaining_messages()** (4 connections) — `server/services/rate_limiter.py`
- **.record_message()** (4 connections) — `server/services/rate_limiter.py`
- **.get_system_stats()** (3 connections) — `server/services/rate_limiter.py`
- **.is_player_rate_limited()** (3 connections) — `server/services/rate_limiter.py`
- **test_rate_limiter_initialization()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_legacy_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.reset_player_limits()** (2 connections) — `server/services/rate_limiter.py`
- **.set_limit()** (2 connections) — `server/services/rate_limiter.py`
- **Any** (2 connections)
- **Remove timestamps older than the window size. Args: player_id: Player ID…** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is within rate limits for a channel. Args: player_id: Player…** (1 connections) — `server/services/rate_limiter.py`
- **Record a message for rate limiting. Args: player_id: Player ID channel: Channel…** (1 connections) — `server/services/rate_limiter.py`
- **Sliding window rate limiter for chat channels. Implements per-user, per-channel…** (1 connections) — `server/services/rate_limiter.py`
- **Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…** (1 connections) — `server/services/rate_limiter.py`
- **Reset rate limiting for a player. Args: player_id: Player ID channel: Specific…** (1 connections) — `server/services/rate_limiter.py`
- **Get system-wide rate limiting statistics. Returns: Dictionary with system…** (1 connections) — `server/services/rate_limiter.py`
- **Check if a player is currently rate limited on a channel. Args: player_id:…** (1 connections) — `server/services/rate_limiter.py`
- **Get the number of remaining messages a player can send on a channel. Args:…** (1 connections) — `server/services/rate_limiter.py`
- **Set a custom rate limit for a channel. Args: channel: Channel name limit:…** (1 connections) — `server/services/rate_limiter.py`
- **Get the current rate limit for a channel. Args: channel: Channel name Returns:…** (1 connections) — `server/services/rate_limiter.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_rate_limiter.py](test_rate_limiter.py.md) (3 shared connections)
- [rate_limiter](rate_limiter.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*