# Spell Validation

> 144 nodes

## Key Concepts

- **ErrorContext** (54 connections) — `server/exceptions.py`
- **test_exceptions.py** (43 connections) — `server/tests/unit/test_exceptions.py`
- **create_error_context()** (36 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **LoggedException** (23 connections) — `server/exceptions.py`
- **.__init__()** (16 connections) — `server/exceptions.py`
- **Any** (14 connections)
- **handle_exception()** (13 connections) — `server/exceptions.py`
- **.__init__()** (8 connections) — `server/exceptions.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **test_logged_http_exception_initialization()** (5 connections) — `server/tests/unit/test_exceptions.py`
- **test_handle_exception_standard_exception()** (5 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **.test_mythos_exception_handler_sets_request_id()** (5 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.__init__()** (4 connections) — `server/error_handlers/pydantic_error_handler.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.to_dict()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **.__init__()** (4 connections) — `server/exceptions.py`
- **test_mythos_mud_error_initialization()** (4 connections) — `server/tests/unit/test_exceptions.py`
- *... and 119 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (66 shared connections)
- [Loot Generation](Loot_Generation.md) (22 shared connections)
- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (10 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [manager subject services](manager_subject_services.md) (6 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (5 shared connections)
- [game weapon player](game_weapon_player.md) (4 shared connections)
- [conftest mock rationale](conftest_mock_rationale.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (2 shared connections)
- [countdown rest task](countdown_rest_task.md) (1 shared connections)
- [player death service](player_death_service.md) (1 shared connections)

## Source Files

- `server/error_handlers/pydantic_error_handler.py`
- `server/exceptions.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/tests/unit/utils/test_error_logging.py`

## Audit Trail

- EXTRACTED: 516 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*