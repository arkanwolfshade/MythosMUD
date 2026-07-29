# AuthenticationBackend

> 16 nodes

## Key Concepts

- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **.parse_id()** (4 connections) — `server/auth/users.py`
- **Any** (4 connections)
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (3 connections) — `server/auth/users.py`
- **.login()** (3 connections) — `server/auth/users.py`
- **AuthenticationBackend** (2 connections)
- **Test UsernameAuthenticationBackend login method.** (2 connections) — `server/tests/unit/auth/test_users.py`
- **Parse a value into a UUID instance.** (1 connections) — `server/auth/users.py`
- **Custom authentication backend that uses username instead of email.** (1 connections) — `server/auth/users.py`
- **Custom login that uses username.** (1 connections) — `server/auth/users.py`
- **Get strategy for channel type.          Args:             channel_type: Type of** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test that get_username_auth_backend returns UsernameAuthenticationBackend.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [BaseUserManager](BaseUserManager.md) (6 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (5 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (3 shared connections)
- [get current user with logging()](get_current_user_with_logging%28%29.md) (1 shared connections)
- [get user db()](get_user_db%28%29.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 45 (87%)
- INFERRED: 7 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*