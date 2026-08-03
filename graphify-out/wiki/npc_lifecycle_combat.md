# npc lifecycle combat

> 10 nodes

## Key Concepts

- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **test_get_dangerous_characters()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_dangerous_characters_no_dangerous()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_dangerous_characters_has_dangerous()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test getting dangerous characters list.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test checking for dangerous characters when none present.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test checking for dangerous characters when present.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Get the list of dangerous characters used in validation.      Returns:         L** (1 connections) — `server/validators/security_validator.py`
- **Check if text contains dangerous characters.      Args:         text: The text t** (1 connections) — `server/validators/security_validator.py`

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