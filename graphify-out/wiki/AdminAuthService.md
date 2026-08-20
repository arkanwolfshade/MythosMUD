# AdminAuthService

> 28 nodes

## Key Concepts

- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (11 connections) — `server/services/admin_auth_service.py`
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_role()** (4 connections) — `server/services/admin_auth_service.py`
- **Request** (4 connections)
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_username()** (3 connections) — `server/services/admin_auth_service.py`
- **.cleanup_expired_sessions()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **Any** (2 connections)
- **Service for admin authentication and authorization.** (1 connections) — `server/services/admin_auth_service.py`
- **Initialize the admin auth service.** (1 connections) — `server/services/admin_auth_service.py`
- **Determine the admin role for a user. Args: current_user: The current user…** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get username from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get user ID from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- **Validate that the current user has permission to perform the action. Args:…** (1 connections) — `server/services/admin_auth_service.py`
- **Check if a role has permission for an action. Args: role: The user's role…** (1 connections) — `server/services/admin_auth_service.py`
- **Check if user has exceeded rate limits. Args: user_id: The user ID request: The…** (1 connections) — `server/services/admin_auth_service.py`
- **Update or create admin session. Args: user_id: The user ID username: The…** (1 connections) — `server/services/admin_auth_service.py`
- **Log an audit event. Args: user_id: The user ID username: The username action:…** (1 connections) — `server/services/admin_auth_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_admin_auth_service.py](test_admin_auth_service.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [admin_auth_service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*