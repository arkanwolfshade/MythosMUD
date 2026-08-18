# server services combat event publisher

> 100 nodes

## Key Concepts

- **NATSSubjectManager** (58 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (49 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_cache()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test NATSSubjectManager initialization without metrics.** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **fixture** (3 connections)
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_invalid_parameter_value()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_multiple_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 75 more nodes in this community*

## Relationships

- [server services nats subject manager](server_services_nats_subject_manager.md) (26 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (7 shared connections)
- [server events combat events](server_events_combat_events.md) (3 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (2 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [msg](msg.md) (1 shared connections)
- [server services nats exceptions natsrequesterror](server_services_nats_exceptions_natsrequesterror.md) (1 shared connections)
- [server realtime event publisher eventpersistence](server_realtime_event_publisher_eventpersistence.md) (1 shared connections)
- [server events combat events combatendedevent](server_events_combat_events_combatendedevent.md) (1 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 153 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*