# SubjectValidator

> 44 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
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
- **Any** (3 connections)
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **Any** (2 connections)
- **Subscription pattern utilities for NATS Subject Manager. This module provides…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **Convert a pattern template into a subscription pattern with wildcards. Args:…** (1 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- *... and 19 more nodes in this community*

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (14 shared connections)
- [test_validation.py](test_validation.py.md) (7 shared connections)

## Source Files

- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 73 (86%)
- INFERRED: 12 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*