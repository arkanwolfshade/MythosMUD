# Integer Coercion Utils

> 34 nodes

## Key Concepts

- **hash_password()** (18 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_with_very_long_password()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_with_very_long_password()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_returns_false_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_runtime_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Hash a plaintext password using Argon2id.      This function provides superior** (1 connections) — `server/auth_utils.py`
- **Verify a plaintext password against a hash.      This function safely handles** (1 connections) — `server/auth_utils.py`
- **Test successful password hashing.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test that hash_password raises AuthenticationError on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test that verify_password returns False on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on AuthenticationError from argon2** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 9 more nodes in this community*

## Relationships

- [Auth Token Utilities](Auth_Token_Utilities.md) (17 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (10 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (1 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 91 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*