# combat_event_publisher

> 7 nodes

## Key Concepts

- **combat_event_publisher()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **fixture** (3 connections)
- **Create a mock NATS service.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Create a mock subject manager.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Create a CombatEventPublisher instance.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [event_types.py](event_types.py.md) (3 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*