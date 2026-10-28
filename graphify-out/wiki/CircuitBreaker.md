# CircuitBreaker

> 154 nodes · cohesion 0.02

## Key Concepts

- **NATSSubjectManager** (60 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **SubjectValidationError** (22 connections) — `server/services/nats_subject_manager/exceptions.py`
- **server/services/nats_subject_manager/__init__.py** (20 connections) — `server/services/nats_subject_manager/__init__.py`
- **PatternNotFoundError** (17 connections) — `server/services/nats_subject_manager/exceptions.py`
- **MissingParameterError** (16 connections) — `server/services/nats_subject_manager/exceptions.py`
- **test_nats_subject_exceptions.py** (16 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **InvalidPatternError** (15 connections) — `server/services/nats_subject_manager/exceptions.py`
- **nats_subject_manager/exceptions.py** (13 connections) — `server/services/nats_subject_manager/exceptions.py`
- **NATSSubjectError** (10 connections) — `server/services/nats_subject_manager/exceptions.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_exception_hierarchy()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **test_exceptions_can_be_raised()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_cache()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_exceptions_can_be_caught_by_base()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`
- *... and 129 more nodes in this community*

## Relationships

- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (17 shared connections)
- [test_look_item.py](test_look_item.py.md) (12 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (10 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (4 shared connections)
- [Room](Room.md) (4 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (3 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (2 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (2 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (2 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/exceptions.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/services/nats_subject_manager/test_nats_subject_exceptions.py`

## Audit Trail

- EXTRACTED: 279 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*