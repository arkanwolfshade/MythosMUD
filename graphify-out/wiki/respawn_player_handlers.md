# respawn player handlers

> 16 nodes

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_invalid_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_verification_error()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_invalid_hash_exception()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_type_error()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Unit tests for Argon2 password hashing utilities.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verifying password with invalid hash format.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verifying password with non-string hash returns False.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verifying password with empty hash returns False.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test hash_password handles HashingError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verify_password handles VerificationError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verify_password handles InvalidHash exception.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verify_password handles TypeError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [auth users rationale](auth_users_rationale.md) (11 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [countdown rest task](countdown_rest_task.md) (8 shared connections)
- [persistence constants rationale](persistence_constants_rationale.md) (5 shared connections)
- [security headers middleware](security_headers_middleware.md) (4 shared connections)
- [archive QUALITY AUDIT](archive_QUALITY_AUDIT.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*