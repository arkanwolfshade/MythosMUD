# Test Endpoints Register

> 91 nodes

## Key Concepts

- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **UserCreate** (31 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **asyncio** (18 connections)
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **User** (9 connections)
- **Request** (8 connections)
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_unexpected_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **IntegrityError** (7 connections)
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (6 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (6 connections) — `server/auth/endpoints.py`
- **_get_user_characters()** (6 connections) — `server/auth/endpoints.py`
- **reserve_invite()** (6 connections) — `server/auth/invites.py`
- **test_register_user_duplicate_username()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- *... and 66 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (16 shared connections)
- [Invites](Invites.md) (9 shared connections)
- [Test Endpoints Invites](Test_Endpoints_Invites.md) (9 shared connections)
- [Players](Players.md) (7 shared connections)
- [Character Creation API](Character_Creation_API.md) (6 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (5 shared connections)
- [Endpoints](Endpoints.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 230 (88%)
- INFERRED: 30 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*