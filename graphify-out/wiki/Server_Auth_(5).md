# Server Auth (5)

> 5 nodes

## Key Concepts

- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend login method.** (2 connections) — `server/tests/unit/auth/test_users.py`
- **Get strategy for channel type.          Args:             channel_type: Type of** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`

## Relationships

- [Server Auth](Server_Auth.md) (4 shared connections)
- [Server Realtime (87)](Server_Realtime_%2887%29.md) (2 shared connections)
- [Server Realtime (96)](Server_Realtime_%2896%29.md) (1 shared connections)

## Source Files

- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 13 (76%)
- INFERRED: 4 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*