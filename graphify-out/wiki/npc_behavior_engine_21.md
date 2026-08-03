# npc behavior engine

> 10 nodes

## Key Concepts

- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **test_validate_security_comprehensive_message()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_security_comprehensive_action()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_security_comprehensive_player_name()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_security_comprehensive_default()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test comprehensive validation for message type.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test comprehensive validation for action type.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test comprehensive validation for player_name type.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test comprehensive validation with unknown field type defaults to message.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Comprehensive security validation for any text field.      This is the main vali** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (5 shared connections)
- [command communication models](command_communication_models.md) (1 shared connections)
- [subject nats manager](subject_nats_manager.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*