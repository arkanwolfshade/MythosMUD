# NATS Subject Exceptions

> 69 nodes · cohesion 0.06

## Key Concepts

- **SubjectValidationError** (25 connections) — `server/services/nats_subject_manager/exceptions.py`
- **manager.py** (19 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (18 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (15 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (14 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_subscription_patterns.py** (13 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **exceptions.py** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (9 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **validation.py** (6 connections) — `server/services/nats_subject_manager/validation.py`
- **Any** (5 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **SubjectValidator** (5 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **metrics.py** (4 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
- **test_invalid_pattern_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 44 more nodes in this community*

## Relationships

- [[NATS Subject Manager]] (15 shared connections)
- [[Manager Services Nats]] (12 shared connections)
- [[NATS Subject Validator Tests]] (8 shared connections)
- [[NATS Subject Admin API]] (2 shared connections)
- [[Combat Domain Events]] (2 shared connections)
- [[NATS Pattern Matcher]] (2 shared connections)
- [[Chat NATS Publisher]] (1 shared connections)
- [[Message Broker Errors]] (1 shared connections)
- [[NATS Subject Validator]] (1 shared connections)

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

- EXTRACTED: 298 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
