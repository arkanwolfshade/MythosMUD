# create access token()

> 189 nodes

## Key Concepts

- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **auth_utils.py** (16 connections) — `server/auth_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 164 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (25 shared connections)
- [real time](real_time.md) (12 shared connections)
- [fetch schedule entries()](fetch_schedule_entries%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [follow commands](follow_commands.md) (4 shared connections)
- [seed e2e users](seed_e2e_users.md) (3 shared connections)
- [metrics](metrics.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [equipment helpers](equipment_helpers.md) (2 shared connections)
- [argon2](argon2.md) (1 shared connections)
- [connection delegates](connection_delegates.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 660 (91%)
- INFERRED: 66 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*