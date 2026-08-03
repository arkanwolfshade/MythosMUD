# auth users rationale

> 6 nodes

## Key Concepts

- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **Get strategy for channel type.          Args:             channel_type: Type of** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test UsernameAuthenticationBackend login method.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend initialization.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 13 (76%)
- INFERRED: 4 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*