# Api Player

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

- [Admin Command Models](Admin_Command_Models.md) (10 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (8 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (8 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (5 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Nats Anti Patterns](Nats_Anti_Patterns.md) (4 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)

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