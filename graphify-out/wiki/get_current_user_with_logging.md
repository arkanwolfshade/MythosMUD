# get_current_user_with_logging

> 18 nodes

## Key Concepts

- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **asyncio** (7 connections)
- **test_get_current_user_with_logging_generic_exception()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_http_exception()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_long_auth_header()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_auth_header()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_request()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_user()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_success()** (5 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **DependsParam** (1 connections)
- **Enhanced get_current_user with detailed logging.** (1 connections) — `server/auth/users.py`
- **Test _get_current_user_with_logging when HTTPException is raised.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging with successful authentication.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when generic Exception is raised.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging with long Authorization header.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when Authorization header is missing.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when request is None.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when no user is returned.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [User](User.md) (7 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`

## Audit Trail

- EXTRACTED: 32 (82%)
- INFERRED: 7 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*