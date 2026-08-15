# EventPublisher

> 82 nodes

## Key Concepts

- **EventPublisher** (29 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (25 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **asyncio** (13 connections)
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_handles_container_failure()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 57 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [HealthMonitor](HealthMonitor.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 117 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*