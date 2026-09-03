# Test Admin Auth Service

> 130 nodes

## Key Concepts

- **test_admin_auth_service.py** (57 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **AdminAction** (36 connections) — `server/services/admin_auth_service.py`
- **AdminRole** (25 connections) — `server/services/admin_auth_service.py`
- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (11 connections) — `server/services/admin_auth_service.py`
- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_role()** (4 connections) — `server/services/admin_auth_service.py`
- **admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **mock_user()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **superuser()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_admin_session_init()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_get_admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_admin_room_management()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_moderator()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_superuser()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **test_has_permission_viewer()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **Request** (4 connections)
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (3 connections) — `server/services/admin_auth_service.py`
- *... and 105 more nodes in this community*

## Relationships

- [Npc Admin](Npc_Admin.md) (15 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (6 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (1 shared connections)
- [Maps](Maps.md) (1 shared connections)
- [Test Player Requests](Test_Player_Requests.md) (1 shared connections)
- [Players](Players.md) (1 shared connections)
- [Rooms](Rooms.md) (1 shared connections)
- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (1 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 177 (82%)
- INFERRED: 39 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*