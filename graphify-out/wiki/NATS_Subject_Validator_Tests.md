# NATS Subject Validator Tests

> 27 nodes · cohesion 0.08

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **custom_length_validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **strict_validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_custom_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_strict()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **validator()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Any** (3 connections) — `server/services/nats_subject_manager/validation.py`
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **Create SubjectValidator instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Create SubjectValidator with strict validation.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Create SubjectValidator with custom max length.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test SubjectValidator initialization.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test SubjectValidator initialization with strict validation.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Test SubjectValidator initialization with custom max length.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Validate all parameters used in the pattern.          Args:             pattern:** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validate that a subscription pattern is not overly broad.          Prevents patt** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validator for NATS subjects and parameters.      Provides validation logic that** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Initialize validator.          Args:             max_subject_length: Maximum all** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Perform basic validation checks on subject.          Args:             subject:** (1 connections) — `server/services/nats_subject_manager/validation.py`
- *... and 2 more nodes in this community*

## Relationships

- [[NATS Subject Exceptions]] (8 shared connections)
- [[NATS Subject Validator]] (7 shared connections)
- [[Manager Services Nats]] (2 shared connections)
- [[NATS Subject Manager]] (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 68 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
