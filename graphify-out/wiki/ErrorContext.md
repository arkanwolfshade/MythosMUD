# ErrorContext

> 108 nodes

## Key Concepts

- **ErrorContext** (40 connections) — `server/exceptions.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **create_error_context()** (30 connections) — `server/exceptions.py`
- **test_subject_controller.py** (24 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **Any** (13 connections)
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **._extract_context_from_request()** (8 connections) — `server/error_handlers/standardized_responses.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_invalid()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **asyncio** (6 connections)
- **RegisterPatternResponse** (5 connections) — `server/api/admin/subject_controller.py`
- **.mark_logged()** (5 connections) — `server/exceptions.py`
- **test_register_pattern_success()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_invalid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_valid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- *... and 83 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (54 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (20 shared connections)
- [ErrorType](ErrorType.md) (12 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (12 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (7 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/api/player_helpers.py`
- `server/error_handlers/pydantic_error_handler.py`
- `server/error_handlers/standardized_responses.py`
- `server/exceptions.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_error_logging.py`

## Audit Trail

- EXTRACTED: 281 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*