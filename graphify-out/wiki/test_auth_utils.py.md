# test_auth_utils.py

> 202 nodes

## Key Concepts

- **test_auth_utils.py** (53 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (43 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **AuthenticationError** (37 connections) — `server/exceptions.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **argon2_utils.py** (19 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 177 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [test_users.py](test_users.py.md) (5 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [error_logging.py](error_logging.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (1 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 370 (94%)
- INFERRED: 24 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*