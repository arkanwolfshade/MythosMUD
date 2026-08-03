# services admin auth

> 35 nodes

## Key Concepts

- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (12 connections) — `server/services/admin_auth_service.py`
- **AdminRole** (7 connections) — `server/services/admin_auth_service.py`
- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **Any** (6 connections)
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **.get_user_role()** (5 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **.get_username()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (4 connections) — `server/services/admin_auth_service.py`
- **Request** (4 connections)
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **test_admin_session_init()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **.cleanup_expired_sessions()** (2 connections) — `server/services/admin_auth_service.py`
- **Enumeration of admin roles.** (1 connections) — `server/services/admin_auth_service.py`
- **Represents an admin session.** (1 connections) — `server/services/admin_auth_service.py`
- **Service for admin authentication and authorization.** (1 connections) — `server/services/admin_auth_service.py`
- **Initialize the admin auth service.** (1 connections) — `server/services/admin_auth_service.py`
- **Determine the admin role for a user.          Args:             current_user: Th** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get username from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [admin auth service](admin_auth_service.md) (13 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 117 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*