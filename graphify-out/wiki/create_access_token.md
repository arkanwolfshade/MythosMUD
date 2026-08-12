# create_access_token

> 57 nodes

## Key Concepts

- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
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
- **test_create_access_token_jwt_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_algorithm()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_expires_delta_zero()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_empty_data()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_invalid()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 32 more nodes in this community*

## Relationships

- [test_auth_utils.py](test_auth_utils.py.md) (31 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*