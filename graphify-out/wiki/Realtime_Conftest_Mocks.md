# Realtime Conftest Mocks

> 93 nodes

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **hash_password()** (28 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (19 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
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
- *... and 68 more nodes in this community*

## Relationships

- [Auth Token Utilities](Auth_Token_Utilities.md) (15 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (5 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Package Engines Node](Package_Engines_Node.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 314 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*