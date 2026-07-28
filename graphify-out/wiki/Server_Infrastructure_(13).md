# Server Infrastructure (13)

> 22 nodes

## Key Concepts

- **test_security_utils.py** (39 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **get_secure_file_path()** (13 connections) — `server/security_utils.py`
- **test_get_secure_file_path_valid()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_invalid_characters()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_slash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_creates_directory()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_underscores()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_dots()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_hyphens()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_numeric_filename()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_mixed_case()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_get_secure_file_path_with_spaces()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path rejects filenames with slashes.** (2 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path accepts filenames with dots.** (2 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Get a secure file path within a base directory.      Args:         filename: The** (1 connections) — `server/security_utils.py`
- **Unit tests for security utilities.  Tests path validation and file security func** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with valid filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path rejects invalid characters.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path creates base directory if it doesn't exist.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path accepts filenames with underscores.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with numeric filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test get_secure_file_path with mixed case filename.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`

## Relationships

- [Server Infrastructure (12)](Server_Infrastructure_%2812%29.md) (12 shared connections)
- [Server Infrastructure (18)](Server_Infrastructure_%2818%29.md) (8 shared connections)
- [Server Infrastructure (20)](Server_Infrastructure_%2820%29.md) (6 shared connections)
- [Server Infrastructure (31)](Server_Infrastructure_%2831%29.md) (2 shared connections)

## Source Files

- `server/security_utils.py`
- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 94 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*