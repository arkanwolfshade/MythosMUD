# hash password()

> 31 nodes

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
- **Test hash_password raises AuthenticationError on ValueError.** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verify_password handles AttributeError and returns False.** (2 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Hash a plaintext password using Argon2id.      This function provides superior** (1 connections) — `server/auth_utils.py`
- **Verify a plaintext password against a hash.      This function safely handles** (1 connections) — `server/auth_utils.py`
- **Test successful password hashing.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test that hash_password raises AuthenticationError on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 6 more nodes in this community*

## Relationships

- [create access token()](create_access_token%28%29.md) (17 shared connections)
- [. init ()](_init_%28%29.md) (10 shared connections)
- [PasswordHasher](PasswordHasher.md) (4 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 91 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*