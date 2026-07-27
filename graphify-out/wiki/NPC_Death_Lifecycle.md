# NPC Death Lifecycle

> 32 nodes · cohesion 0.02

## Key Concepts

- **ErrorContext** (51 connections) — `server/exceptions.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **LoggedException** (21 connections) — `server/exceptions.py`
- **.__init__()** (16 connections) — `server/exceptions.py`
- **Any** (14 connections) — `server/exceptions.py`
- **handle_exception()** (13 connections) — `server/exceptions.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.mark_logged()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.to_dict()** (3 connections) — `server/exceptions.py`
- **.__init__()** (3 connections) — `server/exceptions.py`
- **._log_error()** (3 connections) — `server/exceptions.py`
- **.already_logged()** (2 connections) — `server/exceptions.py`
- **Unpack** (1 connections) — `server/exceptions.py`
- **Initialize MythosMUD error.          Args:             message: Technical error** (1 connections) — `server/exceptions.py`
- **Log validation errors at warning so expected user-input errors do not flood erro** (1 connections) — `server/exceptions.py`
- **Contextual information for error handling.      Provides structured context for** (1 connections) — `server/exceptions.py`
- **Create an error context with the given parameters.      Args:         **kwargs:** (1 connections) — `server/exceptions.py`
- *... and 7 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (26 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [API Type Guards](API_Type_Guards.md) (2 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)
- [Game Client Container](Game_Client_Container.md) (1 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/exceptions.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 195 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*