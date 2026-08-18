# MythosMUDError

> 51 nodes

## Key Concepts

- **MythosMUDError** (66 connections) — `server/exceptions.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **Any** (5 connections)
- **.to_dict()** (3 connections) — `server/exceptions.py`
- **test_create_error_context_with_user_sets_user_id_and_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_without_user_sets_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_mythos_mud_error_with_details()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_mythos_mud_error_with_user_friendly()** (3 connections) — `server/tests/unit/test_exceptions.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context_with_metadata()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_error_context_to_dict()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_and_raise_delegates_to_enhanced()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_wrap_third_party_exception_delegates()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **._log_error()** (2 connections) — `server/exceptions.py`
- **test_create_context_from_request_none()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_context_from_request_with_state()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_context_from_websocket()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_logged_http_exception_delegates()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- *... and 26 more nodes in this community*

## Relationships

- [test_exceptions.py](test_exceptions.py.md) (20 shared connections)
- [DatabaseError](DatabaseError.md) (20 shared connections)
- [AuthenticationError](AuthenticationError.md) (11 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (9 shared connections)
- [ErrorType](ErrorType.md) (9 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (4 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (2 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 146 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*