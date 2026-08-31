# test_argon2_utils.py

> 79 nodes

## Key Concepts

- **test_argon2_utils.py** (43 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_error_handling()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_hash_len()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_memory_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_parallelism()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_time_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_low_memory_cost_warning()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 54 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [seed_e2e_users.py](seed_e2e_users.py.md) (2 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 143 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*