# Standardized Error Responses

> 65 nodes · cohesion 0.03

## Key Concepts

- **RateLimitError** (80 connections) — `server/exceptions.py`
- **MythosMUDError** (67 connections) — `server/exceptions.py`
- **ErrorMessages** (53 connections) — `server/error_types.py`
- **AuthenticationError** (50 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (45 connections) — `server/error_types.py`
- **NetworkError** (42 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (40 connections) — `server/exceptions.py`
- **ConfigurationError** (39 connections) — `server/exceptions.py`
- **CircuitBreaker** (39 connections) — `server/legacy_error_handlers.py`
- **GameLogicError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (36 connections) — `server/legacy_error_handlers.py`
- **ErrorSeverity** (34 connections) — `server/error_types.py`
- **HttpStandardErrorResponse** (21 connections) — `server/error_types.py`
- **Request** (21 connections) — `server/legacy_error_handlers.py`
- **ErrorResponseDetailsInput** (20 connections) — `server/error_types.py`
- **_AppStateWithLegacyConfig** (19 connections) — `server/legacy_error_handlers.py`
- **_AppWithLegacyConfigState** (19 connections) — `server/legacy_error_handlers.py`
- **FastAPI** (19 connections) — `server/legacy_error_handlers.py`
- **HTTPException** (19 connections) — `server/legacy_error_handlers.py`
- **ErrorResponseDetailsInput** (18 connections) — `server/legacy_error_handlers.py`
- **_CircuitBreakerResult** (17 connections) — `server/legacy_error_handlers.py`
- **create_error_response()** (17 connections) — `server/legacy_error_handlers.py`
- **Exception** (17 connections) — `server/legacy_error_handlers.py`
- **_map_error_type()** (15 connections) — `server/legacy_error_handlers.py`
- *... and 40 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (26 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (18 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (12 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (12 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (11 shared connections)
- [Game Client Container](Game_Client_Container.md) (11 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (8 shared connections)
- [Nats Code Review](Nats_Code_Review.md) (6 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Bench Cache](Bench_Cache.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Auth Set Secret](Auth_Set_Secret.md) (1 shared connections)

## Source Files

- `server/error_types.py`
- `server/exceptions.py`
- `server/legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 464 (48%)
- INFERRED: 493 (52%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*