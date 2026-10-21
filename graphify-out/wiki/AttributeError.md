# AttributeError

> 264 nodes · cohesion 0.01

## Key Concepts

- **server/exceptions.py** (271 connections) — `server/exceptions.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **MythosMUDError** (55 connections) — `server/exceptions.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **ErrorContext** (40 connections) — `server/exceptions.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **create_error_context()** (30 connections) — `server/exceptions.py`
- **test_enhanced_error_logging.py** (27 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **skill_use_log_repository.py** (14 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **spell_repository.py** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (13 connections)
- **ResourceNotFoundError** (13 connections) — `server/exceptions.py`
- **player_state_service.py** (13 connections) — `server/game/player_state_service.py`
- **NetworkError** (12 connections) — `server/exceptions.py`
- **movement_room_occupancy.py** (12 connections) — `server/game/movement_room_occupancy.py`
- *... and 239 more nodes in this community*

## Relationships

- [Room](Room.md) (42 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (35 shared connections)
- [endpoints.py](endpoints.py.md) (31 shared connections)
- [EventBus](EventBus.md) (26 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (25 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (23 shared connections)
- [test_look_player.py](test_look_player.py.md) (20 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (19 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (15 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (15 shared connections)
- [test_look_container.py](test_look_container.py.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (9 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/async_persistence_direct_queries.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/game/movement_room_occupancy.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/services/combat_messaging_service.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/services/test_combat_messaging_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 997 (96%)
- INFERRED: 40 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*