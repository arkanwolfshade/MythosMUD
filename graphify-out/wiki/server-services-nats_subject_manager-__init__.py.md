# server/services/nats_subject_manager/__init__.py

> 55 nodes

## Key Concepts

- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **SubjectValidationError** (19 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (11 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (8 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_nats_subject_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_pattern_not_found_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subject_validation_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **patterns.py** (3 connections) — `server/services/nats_subject_manager/patterns.py`
- *... and 30 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (15 shared connections)
- [MessageBroker](MessageBroker.md) (14 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (5 shared connections)
- [test_websocket_handler_rate_limit.py](test_websocket_handler_rate_limit.py.md) (5 shared connections)
- [Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch](Uvicorn-ASGI_Code_Review_-_feature-sqlite-to-postgresql_Branch.md) (4 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (4 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (4 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (3 shared connections)
- [ChatModeration](ChatModeration.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (2 shared connections)

## Source Files

- `server/services/nats_service_pool.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 175 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*