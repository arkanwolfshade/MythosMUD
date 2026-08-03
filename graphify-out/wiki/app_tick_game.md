# app tick game

> 10 nodes

## Key Concepts

- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **test_get_injection_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_injection_patterns_no_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_injection_patterns_has_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test getting injection patterns list.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test checking for injection patterns when none present.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test checking for injection patterns when present.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Get the list of injection patterns used in validation.      Returns:         Lis** (1 connections) — `server/validators/security_validator.py`
- **Check if text matches injection patterns.      Args:         text: The text to c** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (5 shared connections)
- [command communication models](command_communication_models.md) (2 shared connections)

## Source Files

- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*