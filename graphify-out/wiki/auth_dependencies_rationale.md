# auth dependencies rationale

> 10 nodes

## Key Concepts

- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **.validate_filter_name_field()** (3 connections) — `server/models/command_utility.py`
- **test_validate_filter_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_filter_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_filter_name_rejects_invalid_format()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate filter name format using centralized validation.** (1 connections) — `server/models/command_utility.py`
- **Test validating empty filter name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid filter name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_filter_name rejects invalid format.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Centralized validation for filter name fields.      This function provides consi** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (4 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)

## Source Files

- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*