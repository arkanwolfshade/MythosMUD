# player game schema

> 45 nodes

## Key Concepts

- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **player_helpers.py** (9 connections) — `server/api/player_helpers.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **log_error_with_context()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http()** (6 connections) — `server/utils/error_logging.py`
- **test_player_helpers.py** (5 connections) — `server/tests/unit/api/test_player_helpers.py`
- **Any** (5 connections)
- **test_create_error_context_without_user_sets_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_with_user_sets_user_id_and_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_error_context_with_metadata()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_error_context_to_dict()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_and_raise_delegates_to_enhanced()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_wrap_third_party_exception_delegates()** (3 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_and_raise_http_delegates()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_context_from_request_with_state()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_context_from_request_none()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_context_from_websocket()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_log_error_with_context_delegates()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_create_logged_http_exception_delegates()** (2 connections) — `server/tests/unit/utils/test_error_logging.py`
- **Exception** (2 connections)
- *... and 20 more nodes in this community*

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (12 shared connections)
- [add used user](add_used_user.md) (11 shared connections)
- [spell game magic](spell_game_magic.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 151 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*