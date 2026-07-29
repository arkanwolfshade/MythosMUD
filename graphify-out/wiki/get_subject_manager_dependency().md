# get subject manager dependency()

> 83 nodes

## Key Concepts

- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (48 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test NATSSubjectManager initialization without metrics.** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_invalid_parameter_value()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_success()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_no_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_multiple_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_validate_subject_valid()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 58 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (17 shared connections)
- [Any](Any.md) (11 shared connections)
- [.build subject()](build_subject%28%29.md) (8 shared connections)
- [init](init.md) (6 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (4 shared connections)
- [nats config()](nats_config%28%29.md) (3 shared connections)
- [event publisher()](event_publisher%28%29.md) (2 shared connections)
- [NATS](NATS.md) (2 shared connections)
- [message broker](message_broker.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 237 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*