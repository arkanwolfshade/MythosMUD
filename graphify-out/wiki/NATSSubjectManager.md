# NATSSubjectManager

> 73 nodes

## Key Concepts

- **NATSSubjectManager** (59 connections) — `server/services/nats_subject_manager/manager.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **.build_subject()** (7 connections) — `server/services/nats_subject_manager/manager.py`
- **Any** (7 connections)
- **_EventPersistence** (6 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (5 connections) — `server/realtime/event_publisher.py`
- **._ensure_pattern_exists()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._ensure_required_params()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **._format_subject()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_pattern_info()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **.__init__()** (5 connections) — `server/services/nats_subject_manager/manager.py`
- **nats_subject_manager/metrics.py** (5 connections) — `server/services/nats_subject_manager/metrics.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **._ensure_subject_length()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_all_patterns()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **.matches_any_pattern()** (4 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_performance_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- *... and 48 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (9 shared connections)
- [SubjectValidator](SubjectValidator.md) (8 shared connections)
- [test_manager.py](test_manager.py.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (7 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [test_nats_service_pool.py](test_nats_service_pool.py.md) (3 shared connections)
- [EventPublisher](EventPublisher.md) (2 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)
- [subject_manager_no_cache](subject_manager_no_cache.md) (2 shared connections)
- [test_metrics.py](test_metrics.py.md) (2 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/realtime/event_publisher.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`

## Audit Trail

- EXTRACTED: 148 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*