# NATSSubjectManager

> 299 nodes

## Key Concepts

- **NATSSubjectManager** (59 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validation.py** (36 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **SubjectValidationError** (22 connections) — `server/services/nats_subject_manager/exceptions.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 274 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (12 shared connections)
- [NATSService](NATSService.md) (8 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [NATSError](NATSError.md) (5 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [_EventPersistence](_EventPersistence.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 465 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*