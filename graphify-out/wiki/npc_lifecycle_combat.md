# npc lifecycle combat

> 187 nodes

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
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 162 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (28 shared connections)
- [player requests schemas](player_requests_schemas.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [Spell Validation](Spell_Validation.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [package argon2 engines](package_argon2_engines.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 658 (91%)
- INFERRED: 65 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*