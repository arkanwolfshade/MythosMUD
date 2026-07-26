# enhanced_error_logging.py

> 43 nodes · cohesion 0.06

## Key Concepts

- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **wrap_third_party_exception_enhanced()** (10 connections) — `server/utils/enhanced_error_logging.py`
- **log_structured_error()** (9 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (9 connections)
- **_log_http_error()** (8 connections) — `server/utils/enhanced_error_logging.py`
- **create_logged_http_exception_enhanced()** (7 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (7 connections) — `server/utils/error_logging.py`
- **log_and_raise_http_enhanced()** (6 connections) — `server/utils/enhanced_error_logging.py`
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- **test_player_helpers.py** (5 connections) — `server/tests/unit/api/test_player_helpers.py`
- **log_performance_metric()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **log_security_event_enhanced()** (5 connections) — `server/utils/enhanced_error_logging.py`
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **test_create_error_context_with_user_sets_user_id_and_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_without_user_sets_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **Exception** (2 connections)
- **HTTPException** (2 connections)
- **Any** (1 connections)
- **Request** (1 connections)
- **Create error context from request and user.      Helper function to reduce dupli** (1 connections) — `server/api/player_helpers.py`
- **Any** (1 connections)
- **Exception metrics tracking for monitoring.  This module provides thread-safe exc** (1 connections) — `server/monitoring/exception_metrics.py`
- *... and 18 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (10 shared connections)
- [ErrorContext](ErrorContext.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [lifespan.py](lifespan.py.md) (8 shared connections)
- [exceptions.py](exceptions.py.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [wrap_third_party_exception](wrap_third_party_exception.md) (4 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [validate_room_data](validate_room_data.md) (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 171 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*