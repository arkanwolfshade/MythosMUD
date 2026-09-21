# test_auth_utils.py

> 209 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **AttributeError** (47 connections)
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **AuthenticationError** (37 connections) — `server/exceptions.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **argon2_utils.py** (21 connections) — `server/auth/argon2_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (13 connections) — `server/auth/argon2_utils.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- *... and 184 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [endpoints.py](endpoints.py.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [MythosMUDError](MythosMUDError.md) (6 shared connections)
- [real_time.py](real_time.py.md) (5 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (3 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (2 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (2 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 377 (85%)
- INFERRED: 67 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*