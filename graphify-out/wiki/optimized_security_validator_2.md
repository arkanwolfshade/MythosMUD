# optimized security validator

> 10 nodes

## Key Concepts

- **optimized_sanitize_unicode_input()** (8 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_normal_text()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_unicode()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **_cached_ftfy_fix()** (3 connections) — `server/validators/optimized_security_validator.py`
- **Test sanitizing empty string.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test sanitizing normal text (no changes expected).** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test sanitizing text with Unicode issues.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Cached version of ftfy.fix_text for repeated inputs.** (1 connections) — `server/validators/optimized_security_validator.py`
- **Optimized Unicode sanitization with caching.      Args:         text: Raw input** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [optimized security validator](optimized_security_validator.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [realtime message handler](realtime_message_handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*