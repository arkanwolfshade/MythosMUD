# test_security_utils.py

> 24 nodes

## Key Concepts

- **test_security_utils.py** (39 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **get_secure_file_path()** (13 connections) — `server/security_utils.py`
- **test_get_secure_file_path_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_invalid_characters()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_mixed_case()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_numeric_filename()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_valid()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_dots()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_hyphens()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_slash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_spaces()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_underscores()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Get a secure file path within a base directory. Args: filename: The filename…** (1 connections) — `server/security_utils.py`
- **Unit tests for security utilities. Tests path validation and file security…** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with valid filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path rejects invalid characters.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path rejects filenames with slashes.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path creates base directory if it doesn't exist.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path accepts filenames with underscores.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path accepts filenames with dots.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path accepts filenames with hyphens.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with numeric filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with mixed case filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path rejects filenames with spaces.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`

## Relationships

- [validate_secure_path](validate_secure_path.md) (12 shared connections)
- [is_safe_filename](is_safe_filename.md) (8 shared connections)
- [ensure_directory_exists](ensure_directory_exists.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_validate_secure_path_path_traversal_commonpath](test_validate_secure_path_path_traversal_commonpath.md) (2 shared connections)

## Source Files

- `server/security_utils.py`
- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*