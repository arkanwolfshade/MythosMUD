# NATSSubjectManager

> 232 nodes

## Key Concepts

- **NATSSubjectManager** (57 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **create_error_context()** (35 connections) — `server/exceptions.py`
- **subject_controller.py** (29 connections) — `server/api/admin/subject_controller.py`
- **SubjectValidationError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_subject_controller.py** (21 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 207 more nodes in this community*

## Relationships

- [test_validation.py](test_validation.py.md) (17 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [MythosMUDError](MythosMUDError.md) (8 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [ErrorContext](ErrorContext.md) (5 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (5 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (4 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/exceptions.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 452 (94%)
- INFERRED: 29 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*