# npc lifecycle combat

> 26 nodes

## Key Concepts

- **hash_password()** (18 connections) — `server/auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_with_very_long_password()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_with_very_long_password()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Hash a plaintext password using Argon2id.      This function provides superior** (1 connections) — `server/auth_utils.py`
- **Test successful password hashing.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test that hash_password raises AuthenticationError on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on AuthenticationError from argon2** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on ValueError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on TypeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on RuntimeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hashing empty string password raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verifying empty string password - cannot hash empty password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hashing a very long password raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 1 more nodes in this community*

## Relationships

- [auth rationale access](auth_rationale_access.md) (13 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 69 (88%)
- INFERRED: 9 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*