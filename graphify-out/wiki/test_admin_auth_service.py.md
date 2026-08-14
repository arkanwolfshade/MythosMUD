# test_admin_auth_service.py

> 34 nodes

## Key Concepts

- **test_admin_auth_service.py** (54 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_cleanup_expired_sessions_no_expired()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_active_sessions_filters_expired()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_from_dict()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_none()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_with_dict_is_admin()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_from_user_object()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_moderator()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_superuser()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event_limits_size()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_update_session_no_request()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_logs_audit()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_logs_permission_denied()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_none_user()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_viewer_limited()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Unit tests for admin authentication service. Tests the AdminAuthService class…** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_role returns ADMIN for dict user with is_admin.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username from User object.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id from dict.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id returns 'unknown' for None.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test validate_permission limits viewer role.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test validate_permission raises for None user.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test _has_permission for superuser.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [admin_auth_service](admin_auth_service.md) (3 shared connections)
- [AdminAuthService](AdminAuthService.md) (2 shared connections)
- [AdminSession](AdminSession.md) (2 shared connections)
- [User](User.md) (1 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (1 shared connections)
- [test_get_user_role_viewer](test_get_user_role_viewer.md) (1 shared connections)
- [test_get_user_role_none](test_get_user_role_none.md) (1 shared connections)
- [test_get_user_role_with_is_admin_attribute](test_get_user_role_with_is_admin_attribute.md) (1 shared connections)
- [test_get_username_from_dict](test_get_username_from_dict.md) (1 shared connections)
- [test_get_username_none](test_get_username_none.md) (1 shared connections)
- [test_get_username_missing_attribute](test_get_username_missing_attribute.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*