# test corpse lifecycle service

> 64 nodes

## Key Concepts

- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_invalid_parameter_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_duplicate_name()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_invalid_format()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_register_pattern_missing_placeholder()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_pattern_info_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_get_subscription_pattern_not_found()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
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
- *... and 39 more nodes in this community*

## Relationships

- [Any](Any.md) (14 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*