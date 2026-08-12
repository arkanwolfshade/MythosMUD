# Middleware Command Rate

> 20 nodes

## Key Concepts

- **CommandRateLimiter** (10 connections) — `server/middleware/command_rate_limiter.py`
- **.get_stats()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **.__init__()** (3 connections) — `server/middleware/command_rate_limiter.py`
- **.cleanup_inactive_players()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_remaining_commands()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.get_wait_time()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.is_allowed()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_all()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **.reset_player()** (2 connections) — `server/middleware/command_rate_limiter.py`
- **datetime** (2 connections)
- **Any** (1 connections)
- **Get number of commands player can still execute. Args: player_name: Player to…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for a specific player. Useful for admin commands or when…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Reset rate limit for all players. Clears all accumulated timestamp data.…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Get system-wide rate limiting statistics. Returns: Dictionary containing rate…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Remove timestamp data for players who haven't been active recently. Prevents…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Per-player command rate limiting using sliding window algorithm. Tracks command…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Initialize command rate limiter. Args: max_commands: Maximum commands allowed…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Check if player can execute a command now. Implements sliding window rate…** (1 connections) — `server/middleware/command_rate_limiter.py`
- **Get seconds until rate limit resets for this player. Calculates when the oldest…** (1 connections) — `server/middleware/command_rate_limiter.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/middleware/command_rate_limiter.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*