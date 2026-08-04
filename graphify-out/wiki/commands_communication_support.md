# commands communication support

> 76 nodes

## Key Concepts

- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **SubjectValidationError** (29 connections) — `server/services/nats_subject_manager/exceptions.py`
- **PatternNotFoundError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (19 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **test_exception_hierarchy()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **test_exceptions_can_be_caught_by_base()** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_pattern_not_found_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_missing_parameter_error_single()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_invalid_pattern_error()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 51 more nodes in this community*

## Relationships

- [manager subject services](manager_subject_services.md) (35 shared connections)
- [subject validation services](subject_validation_services.md) (16 shared connections)
- [zone npc config](zone_npc_config.md) (7 shared connections)
- [combat validator validators](combat_validator_validators.md) (5 shared connections)
- [manager services nats](manager_services_nats.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (2 shared connections)
- [event publisher realtime](event_publisher_realtime.md) (2 shared connections)
- [pattern matcher services](pattern_matcher_services.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [alias command models](alias_command_models.md) (1 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 312 (88%)
- INFERRED: 42 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*