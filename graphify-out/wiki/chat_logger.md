# chat_logger

> 9 nodes

## Key Concepts

- **chat_logger()** (8 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/services/test_chat_logger.py`
- **fixture** (2 connections)
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Initialize the user manager. Args: data_dir: Directory for player-specific mute…** (1 connections) — `server/services/user_manager.py`
- **Create a temporary directory for chat logs.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [ChatPoseManager](ChatPoseManager.md) (1 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 19 (76%)
- INFERRED: 6 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*