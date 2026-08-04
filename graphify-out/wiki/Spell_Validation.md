# Spell Validation

> 154 nodes

## Key Concepts

- **ErrorContext** (54 connections) — `server/exceptions.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **create_error_context()** (36 connections) — `server/exceptions.py`
- **LoggedException** (23 connections) — `server/exceptions.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **.__init__()** (16 connections) — `server/exceptions.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Any** (14 connections)
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **player_helpers.py** (9 connections) — `server/api/player_helpers.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Any** (9 connections)
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **.__init__()** (8 connections) — `server/exceptions.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- *... and 129 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (59 shared connections)
- [Loot Generation](Loot_Generation.md) (32 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (24 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [manager subject services](manager_subject_services.md) (6 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (5 shared connections)
- [nats services service](nats_services_service.md) (5 shared connections)
- [world loader room](world_loader_room.md) (5 shared connections)
- [game weapon player](game_weapon_player.md) (4 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 643 (94%)
- INFERRED: 38 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*