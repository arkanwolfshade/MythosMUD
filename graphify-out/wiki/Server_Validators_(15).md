# Server Validators (15)

> 9 nodes

## Key Concepts

- **optimized_strip_ansi_codes()** (8 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_no_ansi()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_with_ansi()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **_cached_strip_ansi()** (3 connections) — `server/validators/optimized_security_validator.py`
- **Test stripping ANSI codes from text without ANSI.** (2 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test stripping ANSI codes from empty string.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Cached version of strip_ansi for repeated inputs.** (1 connections) — `server/validators/optimized_security_validator.py`
- **Optimized ANSI code removal with caching.      Args:         text: Input text th** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [Server Validators (3)](Server_Validators_%283%29.md) (4 shared connections)
- [Server Validators (7)](Server_Validators_%287%29.md) (2 shared connections)
- [Server Validators (6)](Server_Validators_%286%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*