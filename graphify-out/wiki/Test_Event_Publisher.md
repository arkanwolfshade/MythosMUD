# Test Event Publisher

> 7 nodes

## Key Concepts

- **event_publisher()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **fixture** (3 connections)
- **Create a mock NATS service.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Create a mock subject manager.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Create an EventPublisher instance.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [Test Event Publisher](Test_Event_Publisher.md) (3 shared connections)
- [Event Publisher](Event_Publisher.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*