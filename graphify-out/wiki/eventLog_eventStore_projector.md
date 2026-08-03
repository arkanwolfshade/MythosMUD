# eventLog eventStore projector

> 10 nodes

## Key Concepts

- **validate_help_topic()** (8 connections) — `server/validators/security_validator.py`
- **.validate_topic()** (3 connections) — `server/models/command_utility.py`
- **test_validate_help_topic_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_help_topic_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_help_topic_rejects_invalid_format()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate help topic format using centralized validation.** (1 connections) — `server/models/command_utility.py`
- **Test validating empty help topic.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid help topic.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_help_topic rejects invalid format.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Centralized validation for help topic fields.      This function provides consis** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (4 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)

## Source Files

- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*