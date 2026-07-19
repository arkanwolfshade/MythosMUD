# Admin Auth Service

> 30 nodes · cohesion 0.11

## Key Concepts

- **AdminAuthService** (18 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (12 connections) — `server/services/admin_auth_service.py`
- **AdminRole** (7 connections) — `server/services/admin_auth_service.py`
- **Any** (6 connections) — `server/services/admin_auth_service.py`
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **.get_user_role()** (5 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **Request** (4 connections) — `server/services/admin_auth_service.py`
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_username()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **.cleanup_expired_sessions()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **Determine the admin role for a user.          Args:             current_user: Th** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get username from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get user ID from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- **Validate that the current user has permission to perform the action.          Ar** (1 connections) — `server/services/admin_auth_service.py`
- **Check if a role has permission for an action.          Args:             role: T** (1 connections) — `server/services/admin_auth_service.py`
- **Check if user has exceeded rate limits.          Args:             user_id: The** (1 connections) — `server/services/admin_auth_service.py`
- **Enumeration of admin roles.** (1 connections) — `server/services/admin_auth_service.py`
- **Update or create admin session.          Args:             user_id: The user ID** (1 connections) — `server/services/admin_auth_service.py`
- **Log an audit event.          Args:             user_id: The user ID** (1 connections) — `server/services/admin_auth_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [[NPC Admin API]] (5 shared connections)
- [[Services Admin Auth]] (3 shared connections)
- [[Admin Auth Service Tests]] (2 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)
- [[NPC Definition Admin API]] (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
