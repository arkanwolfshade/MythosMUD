# test_look_container.py

> 101 nodes · cohesion 0.04

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **AuthenticationError** (37 connections) — `server/exceptions.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_value_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 76 more nodes in this community*

## Relationships

- [test_connection_session_management.py](test_connection_session_management.py.md) (14 shared connections)
- [AttributeError](AttributeError.md) (11 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (5 shared connections)
- [endpoints.py](endpoints.py.md) (3 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (3 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (3 shared connections)
- [security.ts](security.ts.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [S. Petersen's Field Guide to Lovecraftian Horrors (source summary)](S._Petersen's_Field_Guide_to_Lovecraftian_Horrors_source_summary.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 204 (88%)
- INFERRED: 28 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*