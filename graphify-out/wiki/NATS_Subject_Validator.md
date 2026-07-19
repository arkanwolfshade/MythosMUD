# NATS Subject Validator

> 46 nodes · cohesion 0.05

## Key Concepts

- **test_validation.py** (34 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test validate_subject() returns False for empty subject.** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test validate_subject_components() returns True for valid components.** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test validate_subject() returns True for valid subject.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_empty()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test validate_parameter_value() raises error for empty parameter.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test validate_pattern_params() validates all used parameters.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test validate_subject_components() allows underscores in non-strict mode.** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
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
- *... and 21 more nodes in this community*

## Relationships

- [[NATS Subject Validator Tests]] (7 shared connections)
- [[NATS Subject Manager]] (2 shared connections)
- [[NATS Subject Exceptions]] (1 shared connections)

## Source Files

- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
