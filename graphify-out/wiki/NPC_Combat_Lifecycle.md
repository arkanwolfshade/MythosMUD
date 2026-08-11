# NPC Combat Lifecycle

> 117 nodes

## Key Concepts

- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_generic_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- *... and 92 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (67 shared connections)
- [Who Command Helpers](Who_Command_Helpers.md) (19 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (8 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (4 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (3 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (3 shared connections)
- [Archive Combat Health](Archive_Combat_Health.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/character_creation.py`
- `server/auth/endpoints.py`
- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 539 (83%)
- INFERRED: 108 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*