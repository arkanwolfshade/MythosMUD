# metadata rationale npc

> 8 nodes

## Key Concepts

- **optimized_validate_reason_content()** (7 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_validate_reason_content_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_reason_content_valid()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_reason_content_injection()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating empty reason content.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating valid reason content.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test validating reason content with injection pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Optimized validation for reason content fields.      Args:         value: The re** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [optimized security validator](optimized_security_validator.md) (4 shared connections)
- [optimized validators security](optimized_validators_security.md) (1 shared connections)
- [realtime message handler](realtime_message_handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*