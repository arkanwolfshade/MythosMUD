# manager subject services

> 80 nodes

## Key Concepts

- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [commands communication support](commands_communication_support.md) (23 shared connections)
- [subject validation services](subject_validation_services.md) (1 shared connections)
- [player death service](player_death_service.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 174 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*