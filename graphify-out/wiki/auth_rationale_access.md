# auth rationale access

> 57 nodes

## Key Concepts

- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
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
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_wrong_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_invalid()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_token()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_empty_data()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_algorithm()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 32 more nodes in this community*

## Relationships

- [npc lifecycle combat](npc_lifecycle_combat.md) (28 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 176 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*