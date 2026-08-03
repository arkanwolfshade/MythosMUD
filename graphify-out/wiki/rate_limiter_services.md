# rate limiter services

> 14 nodes

## Key Concepts

- **RateLimiter** (17 connections) — `server/services/rate_limiter.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **rate_limiter()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_initialization()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limiter_legacy_config()** (3 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **.set_limit()** (2 connections) — `server/services/rate_limiter.py`
- **.reset_player_limits()** (2 connections) — `server/services/rate_limiter.py`
- **Sliding window rate limiter for chat channels.      Implements per-user, per-cha** (1 connections) — `server/services/rate_limiter.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Set a custom rate limit for a channel.          Args:             channel: Chann** (1 connections) — `server/services/rate_limiter.py`
- **Reset rate limiting for a player.          Args:             player_id: Player I** (1 connections) — `server/services/rate_limiter.py`
- **Create a RateLimiter instance with mocked config.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test RateLimiter initializes with correct limits.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test RateLimiter handles legacy dict config format.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [schedule service services](schedule_service_services.md) (6 shared connections)
- [rate limiter services](rate_limiter_services.md) (4 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*