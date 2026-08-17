# CombatEndedEvent

> 8 nodes

## Key Concepts

- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **test_publish_combat_ended_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_not_connected()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Event fired when combat ends.** (1 connections) — `server/events/combat_events.py`
- **Test publish_combat_ended() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_ended() when NATS is not connected.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Test publish_combat_ended() when NATS service is None.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (2 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 16 (70%)
- INFERRED: 7 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*