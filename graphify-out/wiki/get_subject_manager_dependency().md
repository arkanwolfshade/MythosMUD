# get subject manager dependency()

> 53 nodes

## Key Concepts

- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **subject_manager()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 28 more nodes in this community*

## Relationships

- [Any](Any.md) (13 shared connections)
- [test nats message handler](test_nats_message_handler.md) (10 shared connections)
- [test corpse lifecycle service](test_corpse_lifecycle_service.md) (10 shared connections)
- [test clear corrupted cache entry](test_clear_corrupted_cache_entry.md) (3 shared connections)
- [metrics](metrics.md) (2 shared connections)
- [test command parser](test_command_parser.md) (2 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [message broker](message_broker.md) (1 shared connections)
- [MapZoneContext](MapZoneContext.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 169 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*