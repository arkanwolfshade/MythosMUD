# test_auth_utils.py

> 125 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (17 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_error_handling()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **setup_jwt_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 100 more nodes in this community*

## Relationships

- [create_access_token](create_access_token.md) (31 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (17 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [seed_e2e_users.py](seed_e2e_users.py.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 426 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*