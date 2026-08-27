# NATSSubjectManager

> 252 nodes

## Key Concepts

- **NATSSubjectManager** (61 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (49 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **SubjectValidationError** (23 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **test_subject_controller.py** (22 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **register_pattern()** (11 connections) — `server/api/admin/subject_controller.py`
- **validate_subject()** (11 connections) — `server/api/admin/subject_controller.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_patterns()** (9 connections) — `server/api/admin/subject_controller.py`
- **get_subject_statistics()** (9 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (8 connections) — `server/api/admin/subject_controller.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **_register_pattern_try()** (7 connections) — `server/api/admin/subject_controller.py`
- *... and 227 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (12 shared connections)
- [test_subscription_patterns.py](test_subscription_patterns.py.md) (11 shared connections)
- [NATSService](NATSService.md) (11 shared connections)
- [test_validation.py](test_validation.py.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [NATSError](NATSError.md) (5 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (4 shared connections)
- [nats_broker.py](nats_broker.py.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_service_pool.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 491 (94%)
- INFERRED: 29 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*