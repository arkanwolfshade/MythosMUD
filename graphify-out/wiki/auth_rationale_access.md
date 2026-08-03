# auth rationale access

> 70 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
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
- **setup_jwt_secret()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_returns_false_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_expires_delta()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 45 more nodes in this community*

## Relationships

- [npc lifecycle combat](npc_lifecycle_combat.md) (13 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 251 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*