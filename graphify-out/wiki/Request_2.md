# Request

> 34 nodes

## Key Concepts

- **test_admin_auth_service.py** (54 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **mock_user()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_auth_service_init()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_from_dict()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_none()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_missing_attribute()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_from_dict()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_none()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_none_user()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_rate_limit_exceeded()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_moderator()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_check_rate_limit_cleanup_old_entries()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_update_session_updates_existing()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_active_sessions()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_audit_log()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_audit_log_no_limit()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_logs_permission_denied()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Unit tests for admin authentication service.  Tests the AdminAuthService class f** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Create a mock user object.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test AdminAuthService initialization.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username from dict.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username returns 'unknown' for None.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username returns 'unknown' when username missing.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id from dict.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id returns 'unknown' for None.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)
- [init](init.md) (2 shared connections)
- [Test set mechanical effects stores](Test_set_mechanical_effects_stores.md) (2 shared connections)
- [admin_auth_service](admin_auth_service.md) (1 shared connections)
- [superuser](superuser.md) (1 shared connections)
- [test_admin_action_enum](test_admin_action_enum.md) (1 shared connections)
- [test_admin_role_enum](test_admin_role_enum.md) (1 shared connections)
- [test_check_rate_limit_adds_request](test_check_rate_limit_adds_request.md) (1 shared connections)
- [test_cleanup_expired_sessions](test_cleanup_expired_sessions.md) (1 shared connections)
- [test_cleanup_expired_sessions_no_expired](test_cleanup_expired_sessions_no_expired.md) (1 shared connections)
- [test_get_active_sessions_filters_expired](test_get_active_sessions_filters_expired.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*