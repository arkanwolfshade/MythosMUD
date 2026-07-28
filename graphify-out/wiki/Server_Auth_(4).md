# Server Auth (4)

> 82 nodes

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_error_handling()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **._hash_password()** (3 connections) — `server/auth/users.py`
- **._verify_password()** (3 connections) — `server/auth/users.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_valid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 57 more nodes in this community*

## Relationships

- [Server Error Handlers](Server_Error_Handlers.md) (9 shared connections)
- [Server Admin](Server_Admin.md) (7 shared connections)
- [Server Auth (3)](Server_Auth_%283%29.md) (5 shared connections)
- [Scripts (51)](Scripts_%2851%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Auth](Server_Auth.md) (2 shared connections)
- [Client (13)](Client_%2813%29.md) (1 shared connections)
- [Server Auth (2)](Server_Auth_%282%29.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 288 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*