# test_connection_session_management.py

> 104 nodes · cohesion 0.03

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (21 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (13 connections) — `server/auth/argon2_utils.py`
- **seed_e2e_users.py** (11 connections) — `scripts/seed_e2e_users.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **_ensure_player_for_user()** (6 connections) — `scripts/seed_e2e_users.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **_seed_e2e_users()** (5 connections) — `scripts/seed_e2e_users.py`
- **test_needs_rehash_error_handling()** (5 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **e2e_player_id()** (4 connections) — `scripts/seed_e2e_users.py`
- **e2e_user_id()** (4 connections) — `scripts/seed_e2e_users.py`
- **UUID** (4 connections)
- **_validate_hasher_params()** (4 connections) — `server/auth/argon2_utils.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 79 more nodes in this community*

## Relationships

- [test_look_container.py](test_look_container.py.md) (14 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [._create_grid_map](_create_grid_map.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [bonus_tags](bonus_tags.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 187 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*