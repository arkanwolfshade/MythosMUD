# NATSSubjectManager

> 188 nodes

## Key Concepts

- **NATSSubjectManager** (58 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (49 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **SubjectValidationError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.__init__()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 163 more nodes in this community*

## Relationships

- [SubjectValidator](SubjectValidator.md) (14 shared connections)
- [subject_controller.py](subject_controller.py.md) (12 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [NATSMetrics](NATSMetrics.md) (5 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (3 shared connections)
- [test_validation.py](test_validation.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [chat_nats_publisher.py](chat_nats_publisher.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 324 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*