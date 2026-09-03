# Test Event Publisher Helpers

> 15 nodes

## Key Concepts

- **test_event_publisher_helpers.py** (10 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_create_event_message()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **fixture** (2 connections)
- **Unit tests for event publisher helper functions. Tests the helper functions in…** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Create a mock NATS service.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Create an EventPublisher instance.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test _create_event_message() creates event message.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test get_next_sequence_number() increments sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test reset_sequence_number() resets to 0.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test _get_async_persistence() returns the injected persistence layer (#679:…** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Relationships

- [Event Publisher](Event_Publisher.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 18 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*