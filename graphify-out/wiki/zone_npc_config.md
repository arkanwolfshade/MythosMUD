# zone npc config

> 64 nodes

## Key Concepts

- **test_validation.py** (36 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
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
- **test_validate_subject_basic_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_too_long()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_double_dots()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_starts_with_dot()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_ends_with_dot()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_custom_length()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_with_underscores()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_strict_no_underscores()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_invalid_characters()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_empty_component()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_components_numbers()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- *... and 39 more nodes in this community*

## Relationships

- [subject validation services](subject_validation_services.md) (8 shared connections)
- [commands communication support](commands_communication_support.md) (7 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 136 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*