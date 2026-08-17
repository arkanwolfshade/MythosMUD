# server services nats subject manager

> 88 nodes

## Key Concepts

- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **SubjectValidationError** (20 connections) — `server/services/nats_subject_manager/exceptions.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (17 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_multiple()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 63 more nodes in this community*

## Relationships

- [server services combat event publisher](server_services_combat_event_publisher.md) (20 shared connections)
- [server tests unit services nats](server_tests_unit_services_nats.md) (10 shared connections)
- [server services nats subject manager](server_services_nats_subject_manager.md) (7 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (5 shared connections)
- [server game chat nats publisher](server_game_chat_nats_publisher.md) (2 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [server events combat events](server_events_combat_events.md) (1 shared connections)
- [baseexception](baseexception.md) (1 shared connections)
- [server config init create config](server_config_init_create_config.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/patterns.py`
- `server/services/nats_subject_manager/subscription_patterns.py`
- `server/services/nats_subject_manager/validation.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`

## Audit Trail

- EXTRACTED: 197 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*