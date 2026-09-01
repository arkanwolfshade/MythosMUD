# event_publisher.py

> 28 nodes

## Key Concepts

- **event_publisher.py** (14 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher_helpers.py** (10 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **_EventPersistence** (6 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (5 connections) — `server/realtime/event_publisher.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Protocol** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/event_publisher.py`
- **test_create_event_message()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **UUID** (2 connections)
- **fixture** (2 connections)
- **.is_connected()** (1 connections) — `server/realtime/event_publisher.py`
- **.publish()** (1 connections) — `server/realtime/event_publisher.py`
- **EventPublisher service for MythosMUD real-time events. This module provides a…** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`
- **Unit tests for event publisher helper functions. Tests the helper functions in…** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Create a mock NATS service.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Create an EventPublisher instance.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test _create_event_message() creates event message.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- *... and 3 more nodes in this community*

## Relationships

- [EventPublisher](EventPublisher.md) (6 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 47 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*