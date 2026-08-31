# test_event_publisher.py

> 20 nodes

## Key Concepts

- **test_event_publisher.py** (26 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_returns_none_when_unset()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_with_metadata()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Unit tests for event publisher. Tests the EventPublisher class.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test get_next_sequence_number() returns and increments sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test reset_sequence_number() resets sequence to 0.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization without subject manager.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization with initial sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Same persistence name resolution path for player_left.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **#679: async_persistence is injected at construction (no container lookup at all…** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_entered_event() with additional metadata.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_left_event() when NATS is not connected.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [EventPublisher](EventPublisher.md) (5 shared connections)
- [event_publisher](event_publisher.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*