# Api Player Respawn

> 5 nodes · cohesion 0.01

## Key Concepts

- **ValidationError** (189 connections) — `server/exceptions.py`
- **MythosValidationError** (8 connections) — `server/error_handlers/pydantic_error_handler.py`
- **Request** (4 connections) — `server/api/player_respawn.py`
- **ValidationError** (2 connections) — `server/api/player_respawn.py`
- **Data validation errors (e.g. empty local/whisper message). Log at warning, not e** (1 connections) — `server/exceptions.py`

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (12 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (11 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (3 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 128 (63%)
- INFERRED: 76 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*