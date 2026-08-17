# DatabaseError

> 472 nodes

## Key Concepts

- **DatabaseError** (264 connections) — `server/exceptions.py`
- **server/exceptions.py** (246 connections) — `server/exceptions.py`
- **MythosMUDError** (66 connections) — `server/exceptions.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **RateLimitError** (49 connections) — `server/exceptions.py`
- **AuthenticationError** (46 connections) — `server/exceptions.py`
- **legacy_error_handlers.py** (44 connections) — `server/legacy_error_handlers.py`
- **test_exceptions.py** (44 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (43 connections) — `server/exceptions.py`
- **test_legacy_error_handlers.py** (43 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **enhanced_error_logging.py** (39 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (35 connections) — `server/exceptions.py`
- **standardized_responses.py** (35 connections) — `server/error_handlers/standardized_responses.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **TestErrorMapping** (32 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **_map_error_type()** (23 connections) — `server/legacy_error_handlers.py`
- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **NetworkError** (22 connections) — `server/exceptions.py`
- **ResourceNotFoundError** (21 connections) — `server/exceptions.py`
- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **ErrorSeverity** (19 connections) — `server/error_types.py`
- *... and 447 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (58 shared connections)
- [get_logger](get_logger.md) (46 shared connections)
- [ErrorType](ErrorType.md) (39 shared connections)
- [get_session_maker](get_session_maker.md) (36 shared connections)
- [pytest.md](pytest.md.md) (34 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (26 shared connections)
- [JSONResponse](JSONResponse.md) (25 shared connections)
- [User](User.md) (24 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (23 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (20 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (18 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (17 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/exceptions.py`
- `server/game/player_state_service.py`
- `server/legacy_error_handlers.py`
- `server/legacy_error_sanitization.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 1467 (83%)
- INFERRED: 300 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*