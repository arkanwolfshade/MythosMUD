# NATSSubjectManager

> 49 nodes

## Key Concepts

- **NATSSubjectManager** (57 connections) — `server/services/nats_subject_manager/manager.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 24 more nodes in this community*

## Relationships

- [test_manager.py](test_manager.py.md) (10 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (9 shared connections)
- [subject_controller.py](subject_controller.py.md) (7 shared connections)
- [SubjectValidator](SubjectValidator.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (2 shared connections)
- [test_nats_service_init_with_subject_manager](test_nats_service_init_with_subject_manager.md) (1 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 101 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*