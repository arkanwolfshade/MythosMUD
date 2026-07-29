# get current user with logging()

> 14 nodes

## Key Concepts

- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **test_get_current_user_with_logging_success()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_long_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_user()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_http_exception()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_generic_exception()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **Test _get_current_user_with_logging when HTTPException is raised.** (2 connections) — `server/tests/unit/auth/test_users.py`
- **Test _get_current_user_with_logging with long Authorization header.** (2 connections) — `server/tests/unit/auth/test_users.py`
- **Enhanced get_current_user with detailed logging.** (1 connections) — `server/auth/users.py`
- **Test _get_current_user_with_logging with successful authentication.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test _get_current_user_with_logging when request is None.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test _get_current_user_with_logging when no user is returned.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (8 shared connections)
- [APIRouter](APIRouter.md) (4 shared connections)
- [BaseUserManager](BaseUserManager.md) (1 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*