# subject validation services

> 103 nodes

## Key Concepts

- **SubjectValidationError** (29 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectValidator** (23 connections) — `server/services/nats_subject_manager/validation.py`
- **PatternNotFoundError** (21 connections) — `server/services/nats_subject_manager/exceptions.py`
- **manager.py** (20 connections) — `server/services/nats_subject_manager/manager.py`
- **MissingParameterError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **InvalidPatternError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_subscription_patterns.py** (14 connections) — `server/tests/unit/services/nats_subject_manager/test_subscription_patterns.py`
- **exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **__init__.py** (12 connections) — `server/services/nats_subject_manager/__init__.py`
- **get_subscription_pattern()** (12 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **subscription_patterns.py** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_chat_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **get_event_subscription_patterns()** (10 connections) — `server/services/nats_subject_manager/subscription_patterns.py`
- **register_pattern()** (9 connections) — `server/api/admin/subject_controller.py`
- **validation.py** (7 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exception_hierarchy()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.__init__()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **.validate_parameter_value()** (5 connections) — `server/services/nats_subject_manager/validation.py`
- **test_exceptions_can_be_caught_by_base()** (5 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **.validate_pattern_params()** (4 connections) — `server/services/nats_subject_manager/validation.py`
- *... and 78 more nodes in this community*

## Relationships

- [manager subject services](manager_subject_services.md) (32 shared connections)
- [zone npc config](zone_npc_config.md) (15 shared connections)
- [manager services nats](manager_services_nats.md) (6 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (5 shared connections)
- [pattern matcher services](pattern_matcher_services.md) (3 shared connections)
- [room rationale subzone](room_rationale_subzone.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (1 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
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

- EXTRACTED: 397 (91%)
- INFERRED: 39 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*