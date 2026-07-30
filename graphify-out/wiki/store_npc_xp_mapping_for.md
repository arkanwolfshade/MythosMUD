# .store npc xp mapping for

> 21 nodes

## Key Concepts

- **validate_token_impl()** (15 connections) — `server/realtime/connection_delegates.py`
- **_PlayerIdCarrier** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (6 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (6 connections) — `server/realtime/connection_delegates.py`
- **Protocol** (4 connections)
- **.get_player_by_user_id()** (4 connections) — `server/realtime/connection_delegates.py`
- **test_validate_token_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_invalid_payload()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_player_mismatch()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Minimal player shape for token validation.** (1 connections) — `server/realtime/connection_delegates.py`
- **Persistence surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Look up a player by auth user id.** (1 connections) — `server/realtime/connection_delegates.py`
- **ConnectionManager surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Validate a JWT token for a connection.      Args:         token: JWT token to va** (1 connections) — `server/realtime/connection_delegates.py`
- **Test validate_token_impl() successfully validates token.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() returns False for invalid payload.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() returns False when persistence not available.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() returns False for player mismatch.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`

## Relationships

- [connection delegates](connection_delegates.md) (11 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [command processor()](command_processor%28%29.md) (1 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 60 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*