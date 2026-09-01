# NATSSubjectManager

> 74 nodes

## Key Concepts

- **NATSSubjectManager** (59 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **create_error_context()** (29 connections) — `server/exceptions.py`
- **test_subject_controller.py** (22 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **_admin_user()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_register_pattern_invalid()** (7 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **BaseModel** (6 connections)
- **asyncio** (6 connections)
- **RegisterPatternResponse** (5 connections) — `server/api/admin/subject_controller.py`
- **test_register_pattern_success()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_invalid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_validate_subject_valid()** (5 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **PatternsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **SubjectStatisticsResponse** (4 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectResponse** (4 connections) — `server/api/admin/subject_controller.py`
- *... and 49 more nodes in this community*

## Relationships

- [PatternNotFoundError](PatternNotFoundError.md) (20 shared connections)
- [test_manager.py](test_manager.py.md) (11 shared connections)
- [SubjectValidator](SubjectValidator.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [NATSService](NATSService.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (5 shared connections)
- [pydantic_error_handler.py](pydantic_error_handler.py.md) (4 shared connections)
- [User](User.md) (4 shared connections)
- [NATSPublishError](NATSPublishError.md) (3 shared connections)
- [event_publisher.py](event_publisher.py.md) (3 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/exceptions.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_error_logging.py`

## Audit Trail

- EXTRACTED: 231 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*