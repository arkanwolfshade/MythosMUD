# PlayerIdCarrier

> 22 nodes

## Key Concepts

- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **Protocol** (4 connections)
- **test_validate_token_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **_PlayerIdCarrier** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (4 connections) — `server/realtime/connection_delegates.py`
- **.get_player_by_user_id()** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (4 connections) — `server/realtime/connection_delegates.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **test_validate_token_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_invalid_payload()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_validate_token_impl_player_mismatch()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() returns False for invalid payload.** (2 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() successfully validates token.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() returns False when persistence not available.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Test validate_token_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Minimal player shape for token validation.** (1 connections) — `server/realtime/connection_delegates.py`
- **Persistence surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Look up a player by auth user id.** (1 connections) — `server/realtime/connection_delegates.py`
- **ConnectionManager surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Validate a JWT token for a connection.      Args:         token: JWT token to va** (1 connections) — `server/realtime/connection_delegates.py`
- **Validate a JWT token for a connection.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [connection delegates](connection_delegates.md) (12 shared connections)
- [Player](Player.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*