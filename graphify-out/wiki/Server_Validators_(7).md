# Server Validators (7)

> 16 nodes

## Key Concepts

- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **optimized_sanitize_unicode_input()** (8 connections) — `server/validators/optimized_security_validator.py`
- **benchmark_validation_performance()** (5 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_normal_text()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_sanitize_unicode_input_unicode()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_benchmark_validation_performance()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **_cached_ftfy_fix()** (3 connections) — `server/validators/optimized_security_validator.py`
- **Test sanitizing empty string.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test sanitizing normal text (no changes expected).** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test sanitizing text with Unicode issues.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test benchmark function runs without errors.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Optimized security validation functions for MythosMUD.  This module provides per** (1 connections) — `server/validators/optimized_security_validator.py`
- **Cached version of ftfy.fix_text for repeated inputs.** (1 connections) — `server/validators/optimized_security_validator.py`
- **Optimized Unicode sanitization with caching.      Args:         text: Raw input** (1 connections) — `server/validators/optimized_security_validator.py`
- **Benchmark the performance of optimized vs original validation functions.** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [Server Validators (3)](Server_Validators_%283%29.md) (9 shared connections)
- [Server Validators (6)](Server_Validators_%286%29.md) (3 shared connections)
- [Server Validators (5)](Server_Validators_%285%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Validators (15)](Server_Validators_%2815%29.md) (2 shared connections)
- [Server Validators (14)](Server_Validators_%2814%29.md) (1 shared connections)
- [Server Validators (11)](Server_Validators_%2811%29.md) (1 shared connections)
- [Server Validators (22)](Server_Validators_%2822%29.md) (1 shared connections)
- [Server Validators (20)](Server_Validators_%2820%29.md) (1 shared connections)
- [Server Validators (8)](Server_Validators_%288%29.md) (1 shared connections)
- [Server Validators (19)](Server_Validators_%2819%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*