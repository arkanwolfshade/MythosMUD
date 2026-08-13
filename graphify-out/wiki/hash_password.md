# hash_password

> 34 nodes

## Key Concepts

- **hash_password()** (17 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_empty_string()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_runtime_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_type_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_value_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_with_very_long_password()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_empty_string()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_returns_false_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_runtime_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_with_very_long_password()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Hash a plaintext password using Argon2id. This function provides superior…** (1 connections) — `server/auth_utils.py`
- **Verify a plaintext password against a hash. This function safely handles both…** (1 connections) — `server/auth_utils.py`
- **Test hash_password raises AuthenticationError on AuthenticationError from…** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on ValueError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on TypeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on RuntimeError.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verify_password handles AttributeError and returns False.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verify_password handles RuntimeError and returns False.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_auth_utils.py](test_auth_utils.py.md) (17 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 57 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*