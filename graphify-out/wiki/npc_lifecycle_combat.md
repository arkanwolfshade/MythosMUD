# npc lifecycle combat

> 115 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
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
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 90 more nodes in this community*

## Relationships

- [auth rationale access](auth_rationale_access.md) (28 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (19 shared connections)
- [Loot Generation](Loot_Generation.md) (14 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [service combat services](service_combat_services.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 405 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*