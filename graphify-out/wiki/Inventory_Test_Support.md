# Inventory Test Support

> 64 nodes

## Key Concepts

- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_subject_too_long()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
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
- *... and 39 more nodes in this community*

## Relationships

- [Services Rescue Service](Services_Rescue_Service.md) (12 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (8 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (5 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*