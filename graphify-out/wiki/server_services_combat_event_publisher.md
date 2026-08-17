# server services combat event publisher

> 117 nodes

## Key Concepts

- **NATSSubjectManager** (51 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (49 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Any** (7 connections)
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_cache()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test NATSSubjectManager initialization without metrics.** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 92 more nodes in this community*

## Relationships

- [server services nats subject manager](server_services_nats_subject_manager.md) (23 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (7 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (2 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 165 (90%)
- INFERRED: 19 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*