# Security Infrastructure

> 15 nodes · cohesion 0.14

## Key Concepts

- **is_safe_filename()** (10 connections) — `server/security_utils.py`
- **test_is_safe_filename_empty()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_unicode()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_valid()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_with_backslash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_with_dot_dot()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_with_forward_slash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_is_safe_filename_with_special_chars()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename rejects filenames with backslash.** (2 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename with valid filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename with empty string (considered safe).** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename rejects filenames with ..** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename rejects filenames with forward slash.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test is_safe_filename with Unicode characters.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Check if a filename is safe (no path traversal, no special characters).      Arg** (1 connections) — `server/security_utils.py`

## Relationships

- [[Security Infrastructure]] (8 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/security_utils.py`
- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
