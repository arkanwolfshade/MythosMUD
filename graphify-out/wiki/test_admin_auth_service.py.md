# test_admin_auth_service.py

> 128 nodes

## Key Concepts

- **test_admin_auth_service.py** (56 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **AdminAction** (32 connections) — `server/services/admin_auth_service.py`
- **AdminRole** (24 connections) — `server/services/admin_auth_service.py`
- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (11 connections) — `server/services/admin_auth_service.py`
- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **admin_auth_service()** (5 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_role()** (4 connections) — `server/services/admin_auth_service.py`
- **mock_user()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **superuser()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_session_init()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_moderator()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_superuser()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_viewer()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Request** (4 connections)
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_username()** (3 connections) — `server/services/admin_auth_service.py`
- *... and 103 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (23 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 171 (81%)
- INFERRED: 39 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*