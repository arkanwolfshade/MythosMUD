# test corpse lifecycle service

> 50 nodes

## Key Concepts

- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_invalid_parameter_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_no_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_multiple_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_invalid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_event_domain()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_uses_cache()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_no_cache()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_clears_cache()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_pattern_info_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_all_patterns()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_subscription_pattern_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_chat_subscription_patterns()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_event_subscription_patterns()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_clear_cache()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_performance_metrics_with_metrics()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_performance_metrics_without_metrics()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_records_metrics()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_records_error_metrics()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_records_metrics()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_records_cache_hit()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 25 more nodes in this community*

## Relationships

- [test nats message handler](test_nats_message_handler.md) (10 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (10 shared connections)
- [Any](Any.md) (4 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 121 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*