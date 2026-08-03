# event publisher realtime

> 69 nodes

## Key Concepts

- **EventPublisher** (23 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (19 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher.py** (10 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_success()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_not_connected()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_event_success()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_success()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_with_metadata()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 44 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 183 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*