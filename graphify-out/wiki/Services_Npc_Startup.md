# Services Npc Startup

> 4 nodes · cohesion 0.50

## Key Concepts

- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (1 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (1 shared connections)
- [Health Endpoint Spec](Health_Endpoint_Spec.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 8 (62%)
- INFERRED: 5 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*