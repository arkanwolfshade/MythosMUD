# Combat Command Models

> 67 nodes

## Key Concepts

- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_error_handling()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **._verify_password()** (3 connections) — `server/auth/users.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_valid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_time_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_memory_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_parallelism()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_hash_len()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_invalid_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_invalid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_none()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 42 more nodes in this community*

## Relationships

- [Command Testing Guide](Command_Testing_Guide.md) (22 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Integer Coercion Utils](Integer_Coercion_Utils.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 213 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*