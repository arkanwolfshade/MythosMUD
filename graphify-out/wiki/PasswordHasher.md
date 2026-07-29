# PasswordHasher

> 80 nodes

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **auth_utils.py** (16 connections) — `server/auth_utils.py`
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
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_valid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_time_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 55 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (10 shared connections)
- [BaseUserManager](BaseUserManager.md) (5 shared connections)
- [hash password()](hash_password%28%29.md) (4 shared connections)
- [seed e2e users](seed_e2e_users.md) (3 shared connections)
- [create access token()](create_access_token%28%29.md) (3 shared connections)
- [argon2](argon2.md) (1 shared connections)
- [Hash password using Argon2 instead](Hash_password_using_Argon2_instead.md) (1 shared connections)
- [Verify password using Argon2 instead](Verify_password_using_Argon2_instead.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 297 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*