# Security Infrastructure

> 24 nodes

## Key Concepts

- **validate_secure_path()** (16 connections) — `server/security_utils.py`
- **test_validate_secure_path_absolute_base()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_commonpath_mismatch()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_commonpath_mismatch_with_mock()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_different_drives_windows()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_empty_user_path()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_nested_path()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_valid()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_with_dot_dot()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_with_leading_slash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_with_spaces()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_with_tilde()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Validate and sanitize a user-provided path to prevent path traversal attacks.…** (1 connections) — `server/security_utils.py`
- **Test validate_secure_path detects when common_path != base_path (lines 59-66).** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path with valid path.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path handles different drives on Windows.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path rejects path traversal with ..** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path rejects path traversal with ~** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path with nested valid path.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path with empty user path.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path handles leading slashes.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path normalizes base path to absolute.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path with path containing spaces.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path detects when common_path != base_path (lines 59-66)…** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`

## Relationships

- [Security Infrastructure](Security_Infrastructure.md) (12 shared connections)
- [test_validate_secure_path_path_traversal_commonpath](test_validate_secure_path_path_traversal_commonpath.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/security_utils.py`
- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*