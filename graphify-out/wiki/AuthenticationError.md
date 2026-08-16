# AuthenticationError

> 98 nodes

## Key Concepts

- **AuthenticationError** (46 connections) — `server/exceptions.py`
- **test_argon2_utils.py** (43 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (19 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
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
- *... and 73 more nodes in this community*

## Relationships

- [test_auth_utils.py](test_auth_utils.py.md) (27 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (20 shared connections)
- [create_hasher_with_params](create_hasher_with_params.md) (9 shared connections)
- [log_and_raise](log_and_raise.md) (6 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [player_respawn_wrapper.py](player_respawn_wrapper.py.md) (1 shared connections)
- [client/package.json](client-package.json.md) (1 shared connections)
- [real_time.py](real_time.py.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 213 (88%)
- INFERRED: 29 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*