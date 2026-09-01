# EventPublisher

> 68 nodes

## Key Concepts

- **EventPublisher** (32 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (26 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **asyncio** (13 connections)
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (7 connections) — `server/realtime/event_publisher.py`
- **._publish_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (5 connections) — `server/realtime/event_publisher.py`
- **JsonMap** (5 connections)
- **._get_async_persistence()** (4 connections) — `server/realtime/event_publisher.py`
- **._resolve_player_and_room_names()** (4 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **._player_event_subject()** (3 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_returns_none_when_unset()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 43 more nodes in this community*

## Relationships

- [event_publisher.py](event_publisher.py.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 111 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*