# EventPublisher

> 14 nodes

## Key Concepts

- **EventPublisher** (29 connections) — `server/realtime/event_publisher.py`
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_handles_container_failure()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Service for publishing real-time game events to NATS subjects. This service…** (1 connections) — `server/realtime/event_publisher.py`
- **Reset the sequence number to 0.** (1 connections) — `server/realtime/event_publisher.py`
- **Persistence lookup should replace Player_/Room_ fallbacks in event data.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Legacy subject strings when subject_manager is unset.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **tick_number from additional_metadata should win over sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **publish() returning False should surface as False from EventPublisher.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Container lookup failures should leave async_persistence unset.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [test_event_publisher.py](test_event_publisher.py.md) (9 shared connections)
- [._create_event_message](_create_event_message.md) (7 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [event_publisher](event_publisher.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 42 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*