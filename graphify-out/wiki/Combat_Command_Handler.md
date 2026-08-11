# Combat Command Handler

> 110 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **get_user_db()** (7 connections) — `server/auth/users.py`
- **.__init__()** (4 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_user_manager()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_success()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_long_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **SQLAlchemyUserDatabase** (3 connections)
- **._hash_password()** (3 connections) — `server/auth/users.py`
- **._verify_password()** (3 connections) — `server/auth/users.py`
- **Request** (3 connections)
- *... and 85 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (30 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (11 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (2 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 342 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*