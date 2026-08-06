# websocket handler realtime

> 189 nodes

## Key Concepts

- **AuthenticationError** (63 connections) — `server/exceptions.py`
- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 164 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (19 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (13 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (7 shared connections)
- [auth users rationale](auth_users_rationale.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [nats services metrics](nats_services_metrics.md) (4 shared connections)
- [package argon2 engines](package_argon2_engines.md) (3 shared connections)
- [room sync service](room_sync_service.md) (3 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (2 shared connections)
- [player death service](player_death_service.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 663 (91%)
- INFERRED: 66 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*