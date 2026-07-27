# Admin Auth Service Tests

> 34 nodes · cohesion 0.06

## Key Concepts

- **test_admin_auth_service.py** (52 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_admin_auth_service()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_role_enum()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_check_rate_limit_adds_request()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_audit_log_no_limit()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_from_dict()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_id_from_user_object()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_user_role_superuser()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_dict_without_username()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_username_none()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_superuser()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_log_audit_event_limits_size()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_logs_audit()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_rate_limit_exceeded()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_validate_permission_superuser_all_actions()** (2 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Unit tests for admin authentication service.  Tests the AdminAuthService class f** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_role returns SUPERUSER for superuser.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username returns 'unknown' for None.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_username returns 'unknown' when dict doesn't have username.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id from User object.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test get_user_id from dict.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test validate_permission allows superuser all actions.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Test validate_permission enforces rate limiting.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [[Services Admin Auth]] (30 shared connections)
- [[Admin Auth Service]] (2 shared connections)
- [[NPC Definition Admin API]] (2 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 102 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
