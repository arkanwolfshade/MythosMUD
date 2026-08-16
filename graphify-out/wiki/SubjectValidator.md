# SubjectValidator

> 54 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **SubjectValidationError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **test_get_chat_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_chat_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_event_subscription_patterns_missing_pattern()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_multiple_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_no_params()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **test_get_subscription_pattern_single_param()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
- **Any** (3 connections)
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- *... and 29 more nodes in this community*

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (12 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (11 shared connections)
- [test_validation.py](test_validation.py.md) (10 shared connections)
- [test_manager.py](test_manager.py.md) (3 shared connections)
- [subject_controller.py](subject_controller.py.md) (2 shared connections)
- [.build_subject](build_subject.md) (1 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 117 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*