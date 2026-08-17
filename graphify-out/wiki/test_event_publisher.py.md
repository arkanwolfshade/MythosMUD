# test_event_publisher.py

> 20 nodes

## Key Concepts

- **test_event_publisher.py** (26 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_handles_container_failure()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_nats_error()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Unit tests for event publisher. Tests the EventPublisher class.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test get_next_sequence_number() returns and increments sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test reset_sequence_number() resets sequence to 0.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization without subject manager.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization with initial sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **tick_number from additional_metadata should win over sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Container lookup failures should leave async_persistence unset.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test EventPublisher initialization.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_game_tick_event() successfully publishes.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_entered_event() handles NATS errors.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [EventPublisher](EventPublisher.md) (5 shared connections)
- [event_publisher](event_publisher.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 38 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*