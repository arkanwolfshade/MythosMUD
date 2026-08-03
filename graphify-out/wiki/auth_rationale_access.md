# auth rationale access

> 100 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 75 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (19 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [room websocket updates](room_websocket_updates.md) (3 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 334 (95%)
- INFERRED: 19 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*