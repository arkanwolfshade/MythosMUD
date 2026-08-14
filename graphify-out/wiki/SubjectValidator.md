# SubjectValidator

> 84 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **SubjectValidationError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **server/services/nats_subject_manager/__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_nats_subject_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_pattern_not_found_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 59 more nodes in this community*

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (13 shared connections)
- [test_validation.py](test_validation.py.md) (10 shared connections)
- [test_manager.py](test_manager.py.md) (6 shared connections)
- [.build_subject](build_subject.md) (5 shared connections)
- [test_metrics.py](test_metrics.py.md) (4 shared connections)
- [.validate_parameter_value](validate_parameter_value.md) (3 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (3 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 193 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*