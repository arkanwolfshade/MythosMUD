# Combat Disconnect Bug

> 22 nodes

## Key Concepts

- **hash_password()** (18 connections) — `server/auth_utils.py`
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
- **Test that hash_password raises AuthenticationError on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on AuthenticationError from argon2** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on ValueError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on TypeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on RuntimeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hashing empty string password raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verifying empty string password - cannot hash empty password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hashing a very long password raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verifying a very long password - cannot hash password exceeding limit.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`

## Relationships

- [Auth Token Utilities](Auth_Token_Utilities.md) (11 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (10 shared connections)
- [Services Rescue Service](Services_Rescue_Service.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 59 (87%)
- INFERRED: 9 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*