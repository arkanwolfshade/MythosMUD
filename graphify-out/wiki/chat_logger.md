# chat_logger

> 4 nodes · cohesion 0.50

## Key Concepts

- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [CombatService](CombatService.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [ChatWhisperTracker](ChatWhisperTracker.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [._get_player_mute_file](_get_player_mute_file.md) (1 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 8 (62%)
- INFERRED: 5 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*