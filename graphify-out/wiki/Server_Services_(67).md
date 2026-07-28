# Server Services (67)

> 24 nodes

## Key Concepts

- **test_rate_limiter.py** (35 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_existing()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_limit_default()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_disabled()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_error_handling()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_get_player_stats()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_specific_channel()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_reset_player_limits_all_channels()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_sliding_window()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_rate_limit_different_players()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **test_check_rate_limit_logs_violation()** (2 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Unit tests for rate limiter service.  Tests the RateLimiter class which provides** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_limit returns configured limit.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_limit returns default for unknown channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit returns False when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit always returns True when disabled.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit handles errors gracefully (fails open).** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test get_player_stats returns correct statistics.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits resets specific channel.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test reset_player_limits resets all channels when channel is None.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting uses sliding window correctly.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test rate limiting is per-player.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`
- **Test check_rate_limit logs violation when limit exceeded.** (1 connections) — `server/tests/unit/services/test_rate_limiter.py`

## Relationships

- [Server Services (65)](Server_Services_%2865%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Services (261)](Server_Services_%28261%29.md) (1 shared connections)
- [Server Services (262)](Server_Services_%28262%29.md) (1 shared connections)
- [Server Services (277)](Server_Services_%28277%29.md) (1 shared connections)
- [Server Services (266)](Server_Services_%28266%29.md) (1 shared connections)
- [Server Services (272)](Server_Services_%28272%29.md) (1 shared connections)
- [Server Services (274)](Server_Services_%28274%29.md) (1 shared connections)
- [Server Services (273)](Server_Services_%28273%29.md) (1 shared connections)
- [Server Services (268)](Server_Services_%28268%29.md) (1 shared connections)
- [Server Services (269)](Server_Services_%28269%29.md) (1 shared connections)
- [Server Services (271)](Server_Services_%28271%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rate_limiter.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*