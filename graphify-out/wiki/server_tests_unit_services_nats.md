# server tests unit services nats

> 61 nodes

## Key Concepts

- **test_validation.py** (37 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **custom_length_validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **strict_validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_custom_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_strict()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **fixture** (3 connections)
- **Test validate_subject_basic() returns False for empty subject.** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_invalid_characters()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_none()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_numbers()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_strict_allows_hyphens()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_strict_no_underscores()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_parameter_value_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_invalid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_multiple_invalid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_unused_ignored()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_pattern_params_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_custom_length()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_double_dots()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_ends_with_dot()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_validate_subject_basic_starts_with_dot()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- *... and 36 more nodes in this community*

## Relationships

- [server services nats subject manager](server_services_nats_subject_manager.md) (10 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 71 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*