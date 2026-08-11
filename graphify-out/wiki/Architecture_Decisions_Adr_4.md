# Architecture Decisions Adr

> 4 nodes

## Key Concepts

- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Cursor Plans Plan](Cursor_Plans_Plan.md) (1 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)
- [Commands Time](Commands_Time.md) (1 shared connections)
- [Admin Teleport FRD](Admin_Teleport_FRD.md) (1 shared connections)

## Source Files

- `server/services/rate_limiter.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 8 (62%)
- INFERRED: 5 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*