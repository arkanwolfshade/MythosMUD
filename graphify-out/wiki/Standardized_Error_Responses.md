# Standardized Error Responses

> 714 nodes

## Key Concepts

- **exceptions.py** (196 connections) — `server/exceptions.py`
- **MythosMUDError** (79 connections) — `server/exceptions.py`
- **RateLimitError** (76 connections) — `server/exceptions.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **ErrorContext** (54 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (48 connections) — `server/legacy_error_handlers.py`
- **ErrorType** (47 connections) — `server/error_types.py`
- **ErrorMessages** (47 connections) — `server/error_types.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **test_legacy_error_handlers.py** (41 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **CircuitBreaker** (38 connections) — `server/legacy_error_handlers.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **error_types.py** (37 connections) — `server/error_types.py`
- **NetworkError** (37 connections) — `server/exceptions.py`
- **ErrorResponse** (37 connections) — `server/legacy_error_handlers.py`
- **StandardizedErrorResponse** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (35 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **ResourceNotFoundError** (34 connections) — `server/exceptions.py`
- **create_error_context()** (33 connections) — `server/exceptions.py`
- **standardized_responses.py** (32 connections) — `server/error_handlers/standardized_responses.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **ConfigurationError** (32 connections) — `server/exceptions.py`
- **GameLogicError** (31 connections) — `server/exceptions.py`
- **TestSanitization** (31 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- *... and 689 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (183 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (74 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (74 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (40 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (32 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (31 shared connections)
- [Container Open Events](Container_Open_Events.md) (20 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (14 shared connections)
- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (13 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (11 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (11 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (9 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/player_helpers.py`
- `server/error_handlers/__init__.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/mechanics.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/monitoring/exception_metrics.py`
- `server/realtime/message_handler_factory.py`
- `server/services/combat_messaging_service.py`
- `server/services/environmental_container_loader.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/error_handlers/test_standardized_responses_security.py`

## Audit Trail

- EXTRACTED: 3223 (84%)
- INFERRED: 630 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*