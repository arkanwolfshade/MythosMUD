# test_admin_auth_service.py

> 89 nodes

## Key Concepts

- **test_admin_auth_service.py** (56 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **AdminRole** (24 connections) — `server/services/admin_auth_service.py`
- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **test_admin_session_init()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_moderator()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_superuser()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_viewer()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_action_enum()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_role_enum()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_cleanup_expired_sessions()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_cleanup_expired_sessions_no_expired()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_active_sessions()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_active_sessions_filters_expired()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_audit_log()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_audit_log_no_limit()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_superuser()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_viewer()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_with_dict_is_admin()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_with_is_admin_attribute()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event_limits_size()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event_no_request()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_update_session_creates_new()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_update_session_no_request()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- *... and 64 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [AdminAuthService](AdminAuthService.md) (5 shared connections)
- [admin_auth_service](admin_auth_service.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 108 (77%)
- INFERRED: 33 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*