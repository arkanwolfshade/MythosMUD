# seed_e2e_users.py

> 17 nodes

## Key Concepts

- **optimized_comprehensive_sanitize_input()** (14 connections) — `server/validators/optimized_security_validator.py`
- **optimized_validate_security_comprehensive()** (8 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_normal()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_normalizes_newlines()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_security_comprehensive_dangerous_chars()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_security_comprehensive_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_security_comprehensive_injection()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_validate_security_comprehensive_valid()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive sanitization of empty string.** (2 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive security validation of valid text.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive security validation with dangerous characters.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive security validation with injection pattern.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive sanitization of normal text.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test that optimized comprehensive sanitization normalizes newlines to spaces.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Optimized comprehensive input sanitization. Args: text: Raw input text to…** (1 connections) — `server/validators/optimized_security_validator.py`
- **Optimized comprehensive security validation entry point. Args: value: The value…** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [map/types.ts](map-types.ts.md) (10 shared connections)
- [DecodeLiabilitiesFn](DecodeLiabilitiesFn.md) (3 shared connections)
- [TestValidateCommandBasics](TestValidateCommandBasics.md) (1 shared connections)
- [validate.mjs](validate.mjs.md) (1 shared connections)
- [intersection_schema.json](intersection_schema.json.md) (1 shared connections)
- [room_schema.json](room_schema.json.md) (1 shared connections)
- [CORSConfigDict](CORSConfigDict.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*