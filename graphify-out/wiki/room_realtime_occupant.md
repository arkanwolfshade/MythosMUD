# room realtime occupant

> 4 nodes

## Key Concepts

- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [event events serialization](event_events_serialization.md) (1 shared connections)
- [game chat whisper](game_chat_whisper.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)
- [error websocket handler](error_websocket_handler.md) (1 shared connections)
- [chat logger services](chat_logger_services.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 8 (62%)
- INFERRED: 5 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*