# Who Command Helpers

> 35 nodes

## Key Concepts

- **InviteManager** (24 connections) — `server/auth/invites.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **get_invite_manager()** (6 connections) — `server/auth/invites.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **test_list_invites()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_create_invite()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_list_invites_empty_list()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_list_invites_with_used_invite()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_list_invites_with_expired_invite()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_create_invite_success()** (4 connections) — `server/tests/unit/auth/test_endpoints.py`
- **UUID** (3 connections)
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.cleanup_expired_invites()** (3 connections) — `server/auth/invites.py`
- **.__init__()** (2 connections) — `server/auth/invites.py`
- **AsyncSession** (2 connections)
- **.list_invites()** (2 connections) — `server/auth/invites.py`
- **List all invite codes.      This endpoint returns all invite codes in the system** (1 connections) — `server/auth/endpoints.py`
- **Create a new invite code.      This endpoint creates a new invite code for user** (1 connections) — `server/auth/endpoints.py`
- **Request** (1 connections)
- **Manages invite creation, validation, and tracking.      Handles the invite-only** (1 connections) — `server/auth/invites.py`
- **Validate an invite code.** (1 connections) — `server/auth/invites.py`
- **Mark an invite as used by a specific user.** (1 connections) — `server/auth/invites.py`
- *... and 10 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (19 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (16 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (7 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (2 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/tests/unit/auth/test_endpoints.py`

## Audit Trail

- EXTRACTED: 113 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*