# Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch

> 28 nodes

## Key Concepts

- **SubjectValidator** (19 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **custom_length_validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **strict_validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **validator()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_custom_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **test_subject_validator_init_strict()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **fixture** (3 connections)
- **.__init__()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_basic()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subject_components()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **.validate_subscription_pattern()** (2 connections) — `server/services/nats_subject_manager/validation.py`
- **Any** (2 connections)
- **Validate all parameters used in the pattern. Args: pattern: Pattern template…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validate that a subscription pattern is not overly broad. Prevents patterns…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validator for NATS subjects and parameters. Provides validation logic that can…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Initialize validator. Args: max_subject_length: Maximum allowed subject length…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Perform basic validation checks on subject. Args: subject: Subject string to…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validate each component of the subject. Args: subject: Subject string to…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Validate a parameter value. Args: param_name: Name of the parameter…** (1 connections) — `server/services/nats_subject_manager/validation.py`
- **Create SubjectValidator instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Create SubjectValidator with strict validation.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- **Create SubjectValidator with custom max length.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_validation.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (7 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (4 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_validation.py`

## Audit Trail

- EXTRACTED: 39 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*