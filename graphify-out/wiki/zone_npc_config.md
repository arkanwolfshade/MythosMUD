# zone npc config

> 85 nodes

## Key Concepts

- **test_validation.py** (36 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **SubjectValidationError** (29 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **strict_validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **custom_length_validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_strict()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_custom_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_empty()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_invalid_characters()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_strict_no_underscores()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_invalid()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_multiple_invalid()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **Any** (2 connections)
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **test_validate_subject_basic_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- *... and 60 more nodes in this community*

## Relationships

- [subject validation services](subject_validation_services.md) (14 shared connections)
- [commands communication support](commands_communication_support.md) (9 shared connections)
- [manager subject services](manager_subject_services.md) (8 shared connections)
- [alias command models](alias_command_models.md) (2 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (1 shared connections)
- [combat validator validators](combat_validator_validators.md) (1 shared connections)
- [pattern matcher services](pattern_matcher_services.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 225 (93%)
- INFERRED: 17 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*