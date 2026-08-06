# manager subject services

> 59 nodes

## Key Concepts

- **NATSSubjectManager** (56 connections) — `server/services/nats_subject_manager/manager.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **subject_manager()** (6 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
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
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 34 more nodes in this community*

## Relationships

- [subject validation services](subject_validation_services.md) (17 shared connections)
- [manager subject services](manager_subject_services.md) (10 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (1 shared connections)
- [holiday service services](holiday_service_services.md) (1 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (1 shared connections)
- [event publisher realtime](event_publisher_realtime.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/infrastructure/nats_broker.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 183 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*