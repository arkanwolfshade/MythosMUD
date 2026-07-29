# Custom user manager for MythosMUD.

> 74 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_user_manager()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_hash_password()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_verify_password()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_uuid()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_string()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_invalid()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_non_string_non_uuid()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_non_string_convertible()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_none()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_empty_string()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_valid_uuid_string()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_value_error()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_type_error()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_parse_id_attribute_error()** (3 connections) — `server/tests/unit/auth/test_users.py`
- *... and 49 more nodes in this community*

## Relationships

- [BaseUserManager](BaseUserManager.md) (20 shared connections)
- [APIRouter](APIRouter.md) (10 shared connections)
- [get current user with logging()](get_current_user_with_logging%28%29.md) (8 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (5 shared connections)
- [get user db()](get_user_db%28%29.md) (3 shared connections)
- [Request](Request.md) (2 shared connections)
- [Test getting authentication backend.](Test_getting_authentication_backend.md) (2 shared connections)
- [Hash password using Argon2 instead](Hash_password_using_Argon2_instead.md) (1 shared connections)
- [Verify password using Argon2 instead](Verify_password_using_Argon2_instead.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 252 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*