# EventPublisher

> 70 nodes

## Key Concepts

- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (19 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **asyncio** (8 connections)
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_nats_error()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_with_metadata()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 45 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 196 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*