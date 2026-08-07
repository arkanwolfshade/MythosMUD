# command handler processing

> 19 nodes

## Key Concepts

- **test_users_current_user_logging.py** (12 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **test_get_current_user_with_logging_success()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_request()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_long_auth_header()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_auth_header()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_user()** (3 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_http_exception()** (3 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_generic_exception()** (3 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **DependsParam** (1 connections)
- **Enhanced get_current_user with detailed logging.** (1 connections) — `server/auth/users.py`
- **Unit tests for get_current_user_with_logging wrapper.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging with successful authentication.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when request is None.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when no user is returned.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when HTTPException is raised.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when generic Exception is raised.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging with long Authorization header.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **Test _get_current_user_with_logging when Authorization header is missing.** (1 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`

## Relationships

- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*