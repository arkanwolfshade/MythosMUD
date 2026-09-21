# NATSSubjectManager

> 270 nodes

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
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Any** (7 connections)
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 245 more nodes in this community*

## Relationships

- [subject_controller.py](subject_controller.py.md) (12 shared connections)
- [test_subscription_patterns.py](test_subscription_patterns.py.md) (11 shared connections)
- [NATSPublishError](NATSPublishError.md) (10 shared connections)
- [test_metrics.py](test_metrics.py.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)

## Source Files

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
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 423 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*