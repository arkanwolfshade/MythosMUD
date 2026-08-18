# log_and_raise_enhanced

> 85 nodes

## Key Concepts

- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **enhanced_error_logging.py** (39 connections) — `server/utils/enhanced_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **wrap_third_party_exception_enhanced()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (11 connections) — `server/utils/enhanced_error_logging.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **create_logged_http_exception_enhanced()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **log_and_raise_http_enhanced()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **log_performance_metric()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- *... and 60 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (17 shared connections)
- [PlayerService](PlayerService.md) (16 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (12 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (11 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (10 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (10 shared connections)
- [MythosMUDError](MythosMUDError.md) (9 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (9 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (6 shared connections)
- [log_with_context](log_with_context.md) (6 shared connections)

## Source Files

- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_parser.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 288 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*