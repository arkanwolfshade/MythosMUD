# create_access_token

> 61 nodes

## Key Concepts

- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_wrong_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_algorithm()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_expires_delta_zero()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_empty_data()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 36 more nodes in this community*

## Relationships

- [test_auth_utils.py](test_auth_utils.py.md) (38 shared connections)
- [User](User.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 113 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*