# Admin Auth Service Tests

> 41 nodes · cohesion 0.08

## Key Concepts

- **admin_auth_service.py** (19 connections) — `server/services/admin_auth_service.py`
- **AdminAuthService** (19 connections) — `server/services/admin_auth_service.py`
- **AdminAction** (15 connections) — `server/services/admin_auth_service.py`
- **.validate_permission()** (12 connections) — `server/services/admin_auth_service.py`
- **AdminRole** (7 connections) — `server/services/admin_auth_service.py`
- **._update_session()** (6 connections) — `server/services/admin_auth_service.py`
- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **Any** (6 connections)
- **.get_user_role()** (5 connections) — `server/services/admin_auth_service.py`
- **._has_permission()** (5 connections) — `server/services/admin_auth_service.py`
- **._log_audit_event()** (5 connections) — `server/services/admin_auth_service.py`
- **._check_rate_limit()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_user_id()** (4 connections) — `server/services/admin_auth_service.py`
- **.get_username()** (4 connections) — `server/services/admin_auth_service.py`
- **Request** (4 connections)
- **test_get_admin_auth_service()** (4 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.get_active_sessions()** (3 connections) — `server/services/admin_auth_service.py`
- **.get_audit_log()** (3 connections) — `server/services/admin_auth_service.py`
- **test_admin_session_init()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.cleanup_expired_sessions()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **Admin Authentication and Authorization Service for MythosMUD.  This module provi** (1 connections) — `server/services/admin_auth_service.py`
- **Determine the admin role for a user.          Args:             current_user: Th** (1 connections) — `server/services/admin_auth_service.py`
- **Safely get username from current user object.** (1 connections) — `server/services/admin_auth_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (13 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Api Admin Npc](Api_Admin_Npc.md) (2 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (2 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (2 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (2 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 157 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*