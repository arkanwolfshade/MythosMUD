# Server Services (10)

> 125 nodes

## Key Concepts

- **test_admin_auth_service.py** (54 connections) — `server/tests/unit/services/test_admin_auth_service.py`
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
- **admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **mock_user()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **superuser()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_session_init()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **.cleanup_expired_sessions()** (2 connections) — `server/services/admin_auth_service.py`
- **test_admin_role_enum()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- *... and 100 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (16 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 308 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*