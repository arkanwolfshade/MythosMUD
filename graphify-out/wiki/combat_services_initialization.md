# combat services initialization

> 14 nodes

## Key Concepts

- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **test_validate_alias_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_invalid_format()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_hyphens()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate alias name format using centralized validation.** (1 connections) — `server/models/command_alias.py`
- **Validate alias name format using centralized validation.** (1 connections) — `server/models/command_alias.py`
- **Test validating empty alias name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid alias name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_alias_name rejects invalid format.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_alias_name rejects hyphens.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Centralized validation for alias name fields.      This function provides consis** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (5 shared connections)
- [feature services flag](feature_services_flag.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*